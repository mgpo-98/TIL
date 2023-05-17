const express = require('express');

const app = express();

app.get('/hello',(req,res)=>{
  res.send('<h1> Hello Express </h1>');
});

app.listen(3000);
