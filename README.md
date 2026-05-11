# 🧵 Threads 監控儀表板系統

> **完整的 Threads 社群數據監控與分析系統**  
> Google Apps Script 後端 + GitHub Pages 前端儀表板

---

## 🎯 專案概述

- ✅ Google Apps Script 後端 API — RESTful API 提供資料存取
- ✅ 獨立前端儀表板 — 部署於 GitHub Pages
- ✅ Meta Threads API 整合 — 自動抓取貼文數據與互動指標
- ✅ 數據洞察分析 — 主題平均瀏覽、月度趨勢、發文時間熱圖、5 大指標卡片
- ✅ AI 數據顧問 — Gemini 驅動（透過 GAS 中繼，無 CORS 問題）
- ✅ 文案產生器 — 嵌入外部已訓練模型（copywriting-nu.vercel.app）
- ✅ 自動化 CTA — 根據指標觸發自動回覆
- ✅ 排程發文 — 支援新增、編輯、刪除、立即發文與預約排程

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

### 步驟 1：部署後端

1. 複製 Code-FINAL-v14.gs 全選替換 GAS 的 Code.gs
2. 儲存 → 部署新版本
3. 複製 Web App URL

### 步驟 2：GAS 指令碼屬性

| 屬性名稱 | 值 |
|---------|---|
| `GEMINI_API_KEY` | 你的 Gemini API Key |

### 步驟 3：部署前端

1. index.html 推上 GitHub → 啟用 GitHub Pages
2. 系統設定 → 貼上 GAS Web App URL → 儲存

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
| `getDashboardData` | 貼文列表 |
| `getStats` | 整體統計 |
| `getTop3` | Top 3 貼文 |
| `getTrend` | 30 天趨勢 |
| `getTopicDist` | 主題分布 |
| `getFilterOptions` | 篩選選項 |
| `getFollowersData` | 追蹤數歷史 |
| `getTopicAvgViews` | 主題平均瀏覽 |
| `getMonthlyTrend` | 月度趨勢 |
| `getHeatmapData` | 熱力圖 |
| `getScheduleList` | 排程清單 |
| `getCTARules` | CTA 規則 |
| `askGemini` | Gemini AI 中繼 |
| `createPost` | 立即發文 |
| `addSchedule` | 新增排程 |
| `updateScheduleRow` | 更新排程 |
| `deleteScheduleRow` | 刪除排程 |
| `saveCTARule` | 儲存 CTA |
| `deleteCTARule` | 刪除 CTA |
| `updatePostTopic` | 更新主題 |
| `updateCTAStatus` | 更新 CTA 狀態 |
| `executeAction` | 執行後台函式 |
| `submitFeedback` | 回報問題 |

---

## ⚙️ 帳號設定

| 帳號 | 標籤 | 顏色 |
|------|------|------|
| `tkbletsplay_` | 遊學 | 紫 `#9A7ED0` |
| `tkbletsgo.usca` | 美加 | 綠 `#76C8A7` |
| `tkbletsgo.ukau` | 英澳 | 橙 `#FFA534` |

---

## 📝 版本記錄

| 版本 | 更新重點 |
|------|---------|
| v14（2026-05） | 文案產生器改為 iframe 嵌入、RangeError 修復、getTopPostsForCopy 新增 |
| v13（2026-04） | Phase 2 分析、排程/CTA CORS 修復、AI 顧問 Gemini 中繼 |
| v10-v12 | 儀表板 API 整合、追蹤數快照 |

---

## 🛡️ 安全性提醒

- 不要公開分享含 API Token 的設定檔
- 定期更新 Meta API Token（建議每月）
- Gemini Key 存於 GAS 指令碼屬性，不出現在前端

---

**Built with ❤️ for TKB 放洋留遊學團隊**
