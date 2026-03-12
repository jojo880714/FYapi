/**
 * Threads API 中控台 - 轉寄站 (Render 端)
 * 功能：接收 Meta Webhook 通知並轉寄至 Google Sheets
 */

const express = require('express');
const axios = require('axios');
const app = express();

// 這裡設定 Render 的預設連接埠，或是 10000
const PORT = process.env.PORT || 10000;

// 你的 Google Apps Script 部署網址
const GAS_URL = "https://script.google.com/macros/s/AKfycbzS7BWNkS9uVAlNmLb9UpNy_qRJqux-2LCAUfZ44X-P0KDEp7sHpOK62pc1Izpn4MIN/exec";

// 你的 Webhook 驗證權杖 (與 Meta 後台填寫的一致)
const VERIFY_TOKEN = "my_secret_token_123";

app.use(express.json());

// --- 1. 基礎健康檢查 ---
app.get('/', (req, res) => {
  res.send('<h1>Threads API 轉寄站運行中！</h1><p>狀態：等待 Meta 訊號...</p>');
});

// --- 2. Meta Webhook 驗證路徑 (GET) ---
app.get('/webhook', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode === 'subscribe' && token === VERIFY_TOKEN) {
    console.log('✅ Webhook 驗證成功！');
    res.status(200).send(challenge);
  } else {
    console.error('❌ Webhook 驗證失敗：權杖不符');
    res.sendStatus(403);
  }
});

// --- 3. 接收通知並轉寄至 Google Sheets (POST) ---
app.post('/webhook', async (req, res) => {
  const body = req.body;

  // 在 Logs 中印出收到的原始資料，方便除錯
  console.log('--- 收到新事件 ---');
  console.log(JSON.stringify(body, null, 2));

  try {
    // 將整份 JSON 資料轉發給你的 Google Apps Script
    const response = await axios.post(GAS_URL, body, {
      headers: { 'Content-Type': 'application/json' }
    });

    console.log('🚀 已成功轉寄至 Google Sheets:', response.data);
    res.status(200).send('EVENT_RECEIVED');
  } catch (error) {
    console.error('⚠️ 轉寄失敗:', error.message);
    
    // 即使轉寄失敗，也回傳 200 給 Meta，避免 Meta 因為重試機制狂噴請求
    res.status(200).send('FORWARD_FAILED_BUT_ACKNOWLEDGED');
  }
});

// --- 啟動伺服器 ---
app.listen(PORT, () => {
  console.log(`
  --------------------------------------------------
  ✅ Threads API 伺服器已啟動！
  📍 監聽連接埠：${PORT}
  🔗 Webhook 路徑：https://你的網址.onrender.com/webhook
  --------------------------------------------------
  `);
});
