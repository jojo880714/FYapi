# 🧵 Threads 監控儀表板系統

> Google Apps Script 後端 + GitHub Pages 前端儀表板

---

## 📂 檔案結構

```
FYapi/
├── README.md
├── index.html          # 完整前端儀表板
└── Code-FINAL-v16.gs   # GAS 完整後端（部署在 Google Apps Script，不在此 repo）
```

---

## 🚀 快速開始

### Step 1：部署 GAS 後端
1. Code-FINAL-v16.gs 全選替換 GAS 的 Code.gs → 儲存 → 部署新版本
2. GAS 指令碼屬性新增 GEMINI_API_KEY

### Step 2：設定觸發器
- `safeKeepAlive` → 每 5 分鐘（防冷啟動）
- `safeProcessScheduledPosts` → 每分鐘（排程回文）
- `safeDailySnapshot` → 每天 09:00-10:00（每日數據快照）
- `safeDailyDiagnostics` → 每天 23:00-00:00（健檢，寫入「執行紀錄」）
- `safeMonthlyAIAnalysis` → 每月 28 號 23:00（月度 AI 分析）

所有觸發器走 `_safe` wrapper，失敗自動寫進「執行紀錄」工作表，不會靜默掛掉。

### Step 3：部署前端
1. index.html 推上 GitHub → 啟用 GitHub Pages
2. 系統設定 → 填入 GAS Web App URL → 儲存

---

## 📊 功能清單

| 功能 | 說明 |
|------|------|
| 總覽 Dashboard | 統計卡片、追蹤數、趨勢圖、Top 3 |
| 貼文管理 | 篩選、快速編輯主題與 CTA 狀態 |
| AI 數據分析 | 熱力圖、AI 數據顧問 |
| 數據洞察 | 5 大指標、主題柱狀圖、月度折線圖、發文時間熱圖 |
| **週報（v16 新增）** | **3 帳號本週 vs 上週對比、Top 3 高互動貼文、一鍵下載 PNG 分享** |
| 文案產生器 | iframe 嵌入外部已訓練系統 |
| 排程發文 | 新增/編輯/刪除，立即或預約發文 |
| CTA 資料庫 | 規則管理，自動觸發回文 |

---

## 🔧 後端 API 路由

| action | 說明 |
|--------|------|
| getDashboardData | 貼文列表 |
| getStats | 整體統計 |
| getTop3 | Top 3 貼文 |
| getTrend | 30 天趨勢 |
| getTopicDist | 主題分布 |
| getFilterOptions | 篩選選項 |
| getFollowersData | 追蹤數歷史 |
| getTopicAvgViews | 主題平均瀏覽 |
| getMonthlyTrend | 月度趨勢 |
| getHeatmapData | 熱力圖 |
| getScheduleList | 排程清單 |
| getCTARules | CTA 規則 |
| askGemini | Gemini AI 中繼 |
| createPost | 立即發文 |
| addSchedule | 新增排程 |
| updateScheduleRow | 更新排程 |
| deleteScheduleRow | 刪除排程 |
| saveCTARule | 儲存 CTA |
| deleteCTARule | 刪除 CTA |
| updatePostTopic | 更新主題 |
| updateCTAStatus | 更新 CTA 狀態 |
| executeAction | 執行後台函式 |
| submitFeedback | 回報問題 |
| getTopPostsForCopy | 各帳號 Top 4 高瀏覽貼文 |
| **getDailySnapshot** (v16) | **每日數據快照（追蹤數 / 新增貼文 / 7天總互動）** |
| **getWeeklyReport** (v16) | **週報資料（本週 vs 上週對比 + Top 3）** |
| **getMonthlyReports** (v16) | **歷史月度 AI 分析報告** |

---

## ⚙️ 帳號設定

| 帳號 | 標籤 | 顏色 |
|------|------|------|
| tkbletsplay_ | 遊學 | 紫 #9A7ED0 |
| tkbletsgo.usca | 美加 | 綠 #76C8A7 |
| tkbletsgo.ukau | 英澳 | 橙 #FFA534 |

---

## 📝 版本記錄

| 版本 | 更新重點 |
|------|---------|
| **v16（2026-06）** | **每日數據快照、週報視覺化分頁（一鍵下載 PNG）、月度 Gemini AI 貼文成效分析、`_safe` 排程錯誤捕捉 + 執行紀錄、`doGet` ROUTES map 重構、`executeDashboardAction` dispatch table（移除 eval）** |
| v15（2026-05） | 排程清單/編輯/刪除、keepAlive 防冷啟動、localStorage 快取、追蹤數顯示修復 |
| v14（2026-05） | 文案產生器 iframe 嵌入、排程/CTA CORS 修復 |
| v10-v13 | 儀表板 API 整合、Phase 2 分析、追蹤數快照 |

---

## 🛡️ 監控與自我健檢

v16 起所有排程函式都包進 `_safe` wrapper，行為：

- ✅ 成功執行 → 寫一列 `成功` 到「執行紀錄」工作表
- ❌ 失敗 → 寫一列 `失敗` + 完整 stack trace
- 只保留最近 500 列，自動 truncate

加上每天 23:00 的 `safeDailyDiagnostics` 跑一次 `runDiagnostics()`，任何工作表被誤刪 / Token 失效 / API quota 超標 隔天可見。

---

**Built with ❤️ for TKB 放洋留遊學團隊**
