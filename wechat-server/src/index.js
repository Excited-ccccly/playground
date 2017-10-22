var express = require('express');
var bodyParser = require('body-parser');
var webot = require('weixin-robot');
var sql = require('./sql');
var consts = require('./const');
var initSql = sql.initSql;
var query = sql.query;
var update = sql.update;
var insert = sql.insert;
var isSceneExist = sql.isSceneExist;
var getData = sql.getData;
var app = express();

initSql();

webot.set('subscribe', {
  pattern: function(info) {
    return info.is('event') && info.param.event === 'subscribe'
  },
  handler: function(info) {
    if (/^qrscene_/.test(info.param.eventKey)) {
      const scene = info.param.eventKey.split('_')[1];
      isSceneExist(scene, (isExist, count) => {
        if (isExist) {
          count = count + 1;
          update(count, scene);
        } else {
          let count = 1;
          const ticket = info.param.ticket;
          insert(scene, count, ticket);
        }
      });
    }
    return consts.reply.subscribe;
  }
});

app.use(bodyParser.json());
app.get('/statistics', (req, res) => {
  getData(results => {
    res.json(results);
    res.end();
  });
});

app.post('/createQRcode', (req, res) => {
  const count = 0;
  const scene = req.body.scene;
  const ticket = req.body.ticket;
  isSceneExist(scene, (isExist) => {
    if (isExist) {
      res.json({ code: -1, data: '该场景已存在，不允许重复创建'});
    } else {
      insert(scene, count, ticket);
      res.json({ code: 0 });
    }
    res.end();
});
});





webot.watch(app, { token: process.env.TOKEN || 'keyboardcat123', path: '/' });
app.listen(3000);
