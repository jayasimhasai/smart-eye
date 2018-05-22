// Boilerplate setup

express = require('express');
bodyParser = require('body-parser');
app = express();
var net = require('net');

var client = new net.Socket();

var fs = require('fs');

app.set('port', (process.env.PORT || 8080));
app.use(bodyParser.json({type: 'application/json'}));
server = app.listen(app.get('port'), function () {
  console.log('App listening on port %s', server.address().port);
  console.log('Press Ctrl+C to quit.');
});




// Create an instance of ApiAiAssistant
app.post('/', function (req, res) {

  var requestBody = "";

  req.on('data', function(data){
    requestBody+=data;
  });

  req.on('end', function(){
    var responseBody = {};
    console.log(requestBody);
    fs.writeFile("file2.txt", requestBody, function(err) {
        if(err) {
            return console.log(err);
        }
    });




    res.statusCode = 200;
    res.contentType('application/json');
    res.send(responseBody);
  });

})

// Start the server
