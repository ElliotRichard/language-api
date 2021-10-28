import express from 'express';
const fs = require('fs');
const path = require('path');
const app = express();

app.get('/code/:code', (req, res) => {
  try {
    const data = fs.readFileSync(path.join(__dirname, './languages.json'));
    const languageCodes = JSON.parse(data);
    const languageResult = languageCodes.find((languages) => languages.code === req.params.code);
    if (!languageResult) {
      const err = new Error(`Language code ${req.params.code} stats not found`);
      err.status = 404;
      throw err;
    }
    return res.json(languageResult);
  } catch (e) {
    console.log(e);
  }
});
app.get('/', (req, res) => {
  return res.send('Received a GET HTTP method');
});

app.post('/', (req, res) => {
  return res.send('Received a POST HTTP method');
});

app.put('/', (req, res) => {
  return res.send('Received a PUT HTTP method');
});

app.delete('/', (req, res) => {
  return res.send('Received a DELETE HTTP method');
});

app.listen(3000, () => console.log(`Example app listening on port ${3000}!`));
