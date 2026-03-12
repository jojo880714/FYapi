const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// 這是 Meta 驗證 Webhook 的邏輯
app.get('/webhook', (req, res) => {
  const VERIFY_TOKEN = "my_secret_token_123"; // 你可以自己改這串暗號

  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode && token) {
    if (mode === 'subscribe' && token === VERIFY_TOKEN) {
      console.log('WEBHOOK_VERIFIED');
      res.status(200).send(challenge);
    } else {
      res.sendStatus(403);
    }
  }
});

app.get('/', (req, res) => {
  res.send('Server is running!');
});

// 處理來自 Meta 的 POST 請求（真正的通知內容）
app.use(express.json()); // 讓伺服器看得懂 JSON 資料

app.post('/webhook', (req, res) => {
  const body = req.body;

  if (body.topic) {
    // 這行會在 Render 的 Logs 裡印出整串 Threads 的資料內容
    console.log('收到 Threads 通知:', JSON.stringify(body, null, 2));
    res.status(200).send('EVENT_RECEIVED');
  } else {
    res.sendStatus(404);
  }
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
