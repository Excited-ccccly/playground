var mysql = require('mysql');

const option = {
    host: process.env.HOST || 'localhost',
    user: process.env.USER || 'root',
    password: process.env.PASSWORD || 'admin' 
}
const connection = mysql.createConnection(option);

function initSql() {
    query(createSchema);
    query(createTable);
}

function getData(callback) {
    query(`select * from ruff_wechat.qrcode_statistics`, results => {
        callback(results);
    });
}

function isSceneExist(scene, callback) {
    query(`select count from ruff_wechat.qrcode_statistics where scene=\'${scene}\'`, results => {
         if (results.length > 0) callback(true, results[0].count);
         else callback(false, 0);
    });
}

function insert(scene, count, ticket) {
    query(`insert into ruff_wechat.qrcode_statistics (scene, count, ticket) values (\'${scene}\', ${count}, \'${ticket}\')`,results => {
        console.log(`insert scene ${scene} count successfully`);
    });
}

function update(count, scene) {
    query(`update ruff_wechat.qrcode_statistics set count=${count} where scene=\'${scene}\'`, results => {
        console.log(`Update scene ${scene} count successfully`);
    });
}

function query(sql, callback) {
    connection.query(sql, (err, result, fields) => {
        if (err) console.log(err);
        if (callback) {
            callback(result);
        }
    });
}

const createSchema = 'CREATE SCHEMA IF NOT EXISTS ruff_wechat DEFAULT CHARACTER SET utf8';

const createTable = `CREATE TABLE IF NOT EXISTS ruff_wechat.qrcode_statistics (
    id BIGINT(10) NOT NULL AUTO_INCREMENT,
    scene VARCHAR(100),
    count BIGINT(10),
    ticket VARCHAR(200),
    createTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE(scene)
)`;

const dropTable = `DROP TABLE IF EXISTS ruff_wechat.qrcode_statistics`;

module.exports = {
    initSql,
    query,
    update,
    insert,
    isSceneExist,
    getData
}


