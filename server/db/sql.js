var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : '127.0.0.1',
  user     : 'root',
  password : 'hzy.lucas18.com',
  database : 'demo'
});
module.exports=connection