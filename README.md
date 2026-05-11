# 🧵 Threads 監控儀表板系統

> Google Apps Script 後端 + GitHub Pages 前端儀表板

---

## 📂 檔案結構

```
FYapi/
├── README.md
├── index.html          # 完整前端儀表板
└── Code-FINAL-v14.gs   # GAS 完整後端
```

---

## 🚀 快速開始

### Step 1：部署 GAS 後端
1. Code-FINAL-v14.gs 全選替換 GAS 的 Code.gs → 儲存 → 部署新版本
2. GAS 指令碼屬性新增 `GEMINI_API_KEY`

### Step 2：部署前端
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
| 文案產生器 | iframe 嵌入 copywriting-nu.vercel.app |
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
| v14（2026-05） | 文案產生器改為 iframe 嵌入、排程錯誤訊息優化、RangeError 修復 |
| v13（2026-04） | Phase 2 分析、排程/CTA CORS 修復、AI 顧問 Gemini 中繼 |
| v10-v12 | 儀表板 API 整合、追蹤數快照 |

---

**Built with ❤️ for TKB 放洋留遊學團隊**
