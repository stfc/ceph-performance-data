const express = require('express')
const fs = require('fs')
// const cors = require('cors')

app = express();
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "http://vm236.nubes.stfc.ac.uk:8080");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});


app.get('/', function(req, res) {
    res.send('Hey welcome to port 3000 homepage');

});

app.get('/fetchall', function(req, res) {
    data = []
    fs.readdir(__dirname+'/static/data/', function(err, files) {
        files.forEach(function(f) {
            var path = __dirname + '/static/data/'+f+'/data.json';
            data.push(JSON.parse(fs.readFileSync(path)));
        });
        res.send(JSON.stringify(data));
    });


});


app.get('/fetch_workload', function(req, res) {
    res.sendFile(__dirname+'/static/data/'+req.query.id+'/data.json');
 
});


app.listen(3000, function listening() {
   console.log('listening to port localhost 3000'); 
});
