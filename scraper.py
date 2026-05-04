"""
threads_followers_scraper.py
每天晚上自動抓取 Threads 三個帳號的追蹤數，寫入 Google Sheets「追蹤數快照」工作表。
"""

import os
import re
import json
from datetime import datetime, timezone, timedelta
from playwright.sync_api import sync_playwright
import gspread
from google.oauth2.service_account import Credentials

# ── 設定區 ──────────────────────────────────────────────
ACCOUNTS = ["tkbletsplay_", "tkbletsus", "tkbletsau"]  # 遊學、美加、英澳
ACCOUNT_LABELS = ["遊學", "美加", "英澳"]

SHEET_ID = "1wxc1BV4P8c4_6kpyB-WbK2uFJdNAsG6EMn-wFNhmiQE"
SHEET_NAME = "追蹤數快照"

# Google 憑證從環境變數讀取（Render 上設定）
GOOGLE_CREDS_JSON = os.environ.get("GOOGLE_CREDS_JSON")

# 台灣時區
TZ_TAIPEI = timezone(timedelta(hours=8))
# ────────────────────────────────────────────────────────


def get_sheets_client():
    """建立 Google Sheets 連線"""
    creds_dict = json.loads(GOOGLE_CREDS_JSON)
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)


def ensure_sheet_exists(spreadsheet):
    """確保「追蹤數快照」工作表存在，沒有就建立"""
    try:
        sheet = spreadsheet.worksheet(SHEET_NAME)
        print(f"✅ 工作表「{SHEET_NAME}」已存在")
    except gspread.exceptions.WorksheetNotFound:
        sheet = spreadsheet.add_worksheet(title=SHEET_NAME, rows=1000, cols=10)
        # 寫入標題列
        headers = ["日期"] + ACCOUNT_LABELS + ["總計"]
        sheet.append_row(headers)
        print(f"✅ 已建立工作表「{SHEET_NAME}」並設定標題")
    return sheet


def scrape_followers(username: str) -> int | None:
    """用 Playwright 開啟 Threads 頁面，抓取追蹤數"""
    url = f"https://www.threads.net/@{username}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            page.wait_for_timeout(3000)  # 等 JS 渲染完
            
            html = page.content()
            
            # 方法一：從頁面 JSON 抓（最穩）
            # Threads 通常在 <script> 裡有 "__bbox" JSON
            json_matches = re.findall(r'"followers_count"\s*:\s*(\d+)', html)
            if json_matches:
                count = int(json_matches[0])
                print(f"  ✅ @{username} 追蹤數：{count:,}（從 JSON）")
                return count
            
            # 方法二：從頁面文字抓「X followers」
            text = page.inner_text("body")
            follower_match = re.search(r'([\d,]+)\s*followers', text, re.IGNORECASE)
            if follower_match:
                count = int(follower_match.group(1).replace(",", ""))
                print(f"  ✅ @{username} 追蹤數：{count:,}（從文字）")
                return count
            
            # 方法三：找 meta 標籤
            meta_content = page.get_attribute('meta[name="description"]', "content") or ""
            meta_match = re.search(r'([\d,]+)\s*Followers', meta_content, re.IGNORECASE)
            if meta_match:
                count = int(meta_match.group(1).replace(",", ""))
                print(f"  ✅ @{username} 追蹤數：{count:,}（從 meta）")
                return count
            
            print(f"  ⚠️ @{username} 找不到追蹤數，回傳 None")
            return None
            
        except Exception as e:
            print(f"  ❌ @{username} 發生錯誤：{e}")
            return None
        finally:
            browser.close()


def write_to_sheet(sheet, date_str: str, counts: list):
    """寫入一列資料到 Google Sheets"""
    total = sum(c for c in counts if c is not None)
    row = [date_str] + [c if c is not None else "抓取失敗" for c in counts] + [total]
    sheet.append_row(row)
    print(f"✅ 已寫入 Sheets：{row}")


def main():
    print("=" * 50)
    print("Threads 追蹤數快照爬蟲啟動")
    now_taipei = datetime.now(TZ_TAIPEI)
    date_str = now_taipei.strftime("%Y-%m-%d")
    print(f"執行時間（台北）：{now_taipei.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    # 建立 Sheets 連線
    gc = get_sheets_client()
    spreadsheet = gc.open_by_key(SHEET_ID)
    sheet = ensure_sheet_exists(spreadsheet)

    # 抓取三個帳號
    counts = []
    for username in ACCOUNTS:
        print(f"\n抓取 @{username}...")
        count = scrape_followers(username)
        counts.append(count)

    # 寫入 Sheets
    print("\n寫入 Google Sheets...")
    write_to_sheet(sheet, date_str, counts)

    print("\n✅ 全部完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
