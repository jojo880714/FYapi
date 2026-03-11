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

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
