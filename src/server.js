var express = require('express');
var app = express();
var http = require('http').Server(app);

const serverPort = 3249;

function server(port) {
    app.use(express.static(__dirname + '/public'));

    http.listen(port, function() {
        console.log('└──────────────────────────────────────────┘')
    });
}

server(serverPort)