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
    var data = []
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


app.get('/fetch_dd_summary', function(req, res) {
    var data = {}

    const path = __dirname+'/static/data/dd/summaries/' + req.query.summary + '.csv';
    fs.readFile(path, {encoding:'utf8'}, (err, contents) => {
        if (err) throw err;

        var csv_split = contents.split('\n');
        var headers = csv_split.shift();
        headers = headers.split(',');


        for (let line of csv_split) {
            if(line == '') {
                continue;
            }

            var split_line = line.split(',');
            var block_size = split_line[0];

            if( (block_size in data) == false) {
                data[block_size] = []
            }

            let metrics = {};
            for(let i=1; i<split_line.length; i++) {
                let field = headers[i];
                metrics[field] = split_line[i];
            }
            data[block_size].push(metrics);
        }

        res.send(JSON.stringify(data));
    });
});

app.listen(3000, function listening() {
   console.log('listening to port localhost 3000'); 
});
