# 🧵 Threads 監控儀表板系統

> **完整的 Threads 社群數據監控與分析系統**  
> Google Apps Script 後端 + GitHub Pages 前端儀表板

---

## 🎯 專案概述

這是一個完整的 Threads 社群監控系統，包含：

- ✅ **Google Apps Script 後端 API** — RESTful API 提供資料存取
- ✅ **獨立前端儀表板** — 部署於 GitHub Pages
- ✅ **Meta Threads API 整合** — 自動抓取貼文數據與互動指標
- ✅ **數據洞察分析** — 主題平均瀏覽、月度趨勢、發文時間熱圖、5 大指標卡片
- ✅ **AI 功能** — Gemini 驅動的文案產生器 + AI 數據顧問（透過 GAS 中繼，無 CORS 問題）
- ✅ **自動化 CTA** — 根據指標觸發自動回覆
- ✅ **排程發文** — 支援新增、編輯、刪除、立即發文與預約排程

---

## 📂 檔案結構

```
FYapi/
├── README.md           # 本檔案
├── index.html          # 完整前端儀表板（單一檔案，所有功能）
└── Code-FINAL-v14.gs   # GAS 完整後端程式碼
```

---

## 🚀 快速開始

### 步驟 1：部署後端（5-10 分鐘）

1. 開啟你的 Google Apps Script 專案
2. 複製 `Code-FINAL-v14.gs` 的完整內容，全選替換現有 `Code.gs`
3. 儲存
4. 部署 → 管理部署 → 選現有部署 → 編輯 → 版本選「新版本」→ 部署
5. 複製 Web App URL

### 步驟 2：設定 GAS 指令碼屬性

前往 GAS 左側齒輪「專案設定」→「指令碼屬性」，新增：

| 屬性名稱 | 值 |
|---------|---|
| `GEMINI_API_KEY` | 你的 Gemini API Key |

### 步驟 3：部署前端

1. 將 `index.html` 推上 GitHub Repository
2. 啟用 GitHub Pages（Settings → Pages → Deploy from main branch）
3. 開啟儀表板 → 系統設定 → 貼上 GAS Web App URL → 儲存

---

## 📊 功能清單

### 數據分析

| 功能 | 說明 |
|------|------|
| 總覽 Dashboard | 統計卡片、追蹤數歷史、30天趨勢圖、主題分布圓餅圖、Top 3 貼文 |
| 貼文管理 | 完整貼文列表，支援帳號/主題/月份/關鍵字篩選，快速編輯主題與 CTA 狀態 |
| AI 數據分析 | 貼文成效熱力圖（1H/24H/3D/7D）、AI 數據顧問（Gemini 驅動） |
| 數據洞察 | 5 大指標卡片（互動率/留言率/轉發率/平均互動/爆款率）、主題平均瀏覽柱狀圖、月度發文折線圖、發文時間熱圖（7×24） |

### 內容操作

| 功能 | 說明 |
|------|------|
| 文案產生器 | 去 AI 化文案翻譯、雙版本輸出（版本 A/B）、語氣檢測、AI 局部改寫、學習帳號爆款風格 |
| 排程發文 | 新增/編輯/刪除排程，立即發文或預約時間，回文延遲設定 |

### 系統

| 功能 | 說明 |
|------|------|
| CTA 資料庫 | 新增/編輯/刪除 CTA 規則，依帳號/主題/指標/數值觸發自動回文 |
| 系統設定 | GAS API URL 設定、Gemini Key 設定、外觀切換（深/淺色模式） |

---

## 🔧 後端 API 路由一覽

| action | 說明 |
|--------|------|
| `getDashboardData` | 貼文列表（支援 account/topic/region/month/keyword 篩選） |
| `getStats` | 整體統計 |
| `getTop3` | Top 3 貼文（metric 參數：views/likes/replies/engagement） |
| `getTrend` | 30 天發文趨勢 |
| `getTopicDist` | 主題分布圓餅圖 |
| `getFilterOptions` | 篩選下拉選項 |
| `getFollowersData` | 各帳號月度追蹤數歷史 |
| `getTopicAvgViews` | 各主題平均瀏覽（數據洞察用） |
| `getMonthlyTrend` | 月度發文趨勢（數據洞察用） |
| `getHeatmapData` | 熱力圖資料 |
| `getScheduleList` | 排程清單 |
| `getCTARules` | CTA 規則列表 |
| `askGemini` | Gemini AI 中繼（文案產生器 + AI 顧問共用） |
| `getTopPostsForCopy` | 各帳號 Top 4 高瀏覽貼文（文案產生器風格學習用） |
| `createPost` | 立即發文（GET 版） |
| `addSchedule` | 新增排程 |
| `updateScheduleRow` | 更新排程 |
| `deleteScheduleRow` | 刪除排程 |
| `saveCTARule` | 儲存 CTA 規則 |
| `deleteCTARule` | 刪除 CTA 規則 |
| `updatePostTopic` | 更新貼文主題 |
| `updateCTAStatus` | 更新 CTA 狀態 |
| `executeAction` | 執行後台函式 |
| `submitFeedback` | 回報問題 |

---

## 🔧 技術架構

```
前端 (GitHub Pages)
  index.html — HTML + CSS + Vanilla JS + Chart.js (CDN)

        ↕ HTTPS GET

後端 (Google Apps Script)
  Code-FINAL-v14.gs — doGet RESTful API
  → Meta Threads API（抓貼文、發文、回文）
  → Gemini API（文案生成、AI 顧問、語氣檢測）

        ↕

資料庫 (Google Sheets — Threads監管小工具)
  · 數據成效監控（主表，808+ 筆）
  · 帳號金鑰管理
  · CTA 資料庫
  · 排程發文清單
  · 追蹤數歷史
  · 貼文分類
```

---

## ⚙️ 帳號設定

系統目前監控三個帳號：

| 帳號 | 標籤 | 顏色 |
|------|------|------|
| `tkbletsplay_` | 遊學 | 紫 `#9A7ED0` |
| `tkbletsgo.usca` | 美加 | 綠 `#76C8A7` |
| `tkbletsgo.ukau` | 英澳 | 橙 `#FFA534` |

---

## 📝 版本記錄

| 版本 | 更新重點 |
|------|---------|
| v14（2026-05） | 新增 `getTopPostsForCopy`、`getTopPostsForCopy` doGet 路由、`askGemini` maxOutputTokens 提升至 2000 |
| v13（2026-04） | Phase 2 分析 API、排程 CORS 修復、CTA CORS 修復、AI 顧問 Gemini 中繼、`getScheduleList` |
| v10-v12 | 儀表板 API 整合、函式名稱衝突修正、追蹤數快照 |

---

## 🛡️ 安全性提醒

- **不要**公開分享包含 API Token 的設定檔
- 定期更新 Meta API Token（建議每月）
- Gemini API Key 存放於 GAS 指令碼屬性，不會出現在前端程式碼
- 使用 GitHub Private Repository 儲存程式碼

---

## 📞 常見問題

**Q：API 回傳錯誤？**  
確認 GAS 部署設定：執行身分「我」、存取權「任何人」，並確認已部署新版本。

**Q：前端顯示空白？**  
F12 → Console 查看錯誤。最常見原因：GAS URL 未設定，或 GAS 未重新部署。

**Q：Token 失效？**  
至 Meta for Developers 重新產生 Long-lived Token，更新到「帳號金鑰管理」工作表，執行 `testToken()` 驗證。

**Q：文案產生器生成失敗？**  
確認 GAS 指令碼屬性已設定 `GEMINI_API_KEY`，並已部署新版本。

---

**Built with ❤️ for TKB 放洋留遊學團隊**
