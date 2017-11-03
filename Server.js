const express = require('express')
const fs = require('fs')
// const cors = require('cors')

app = express();
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "http://localhost:8080");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});


app.get('/', function(req, res) {
    res.send('Hey welcome to port 3000 homepage');

});

app.get('/tests', function(req, res) {
    fs.readdir(__dirname+'/static/data/', function(err, files) {
        res.send(files);
    });
});



app.get('/fetch_cosbench_summary', function(req, res) {
    data = []
    fs.readdir(__dirname+'/static/data/cosbench/', function(err, files) {
        files.forEach(function(f) {
            var path = __dirname + '/static//data/cosbench/'+f+'/data.json';
            data.push(JSON.parse(fs.readFileSync(path)));
        });
        res.send(JSON.stringify(data));
    });
});
/*
app.get('/fetch_workload', function(req, res) {
    res.sendFile(__dirname+'/static/data/'+req.query.id+'/data.json');
 
});
*/


app.get('fetch_dd_read_summary', function(req, res) {
    data = []
    /* Read CSV in line by line
    / Create an object with
        {
            block_size: [{metric:value}]
        }     
    for every block size
    */
});

app.listen(3000, function listening() {
   console.log('listening to port localhost 3000'); 
});
