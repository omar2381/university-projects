var express = require('express');
var app = express();
var pokemon = require("./pokemon.json")

app.get('/poke', function (request, response) {
    const key = request.query.name
    for( let i = 0; i <pokemon.length; i++)
        if (pokemon[i].name == key)
            response.send("Pokemon name is " + key + "from generation number" + pokemon[i].generation)
    response.send('404 Error, Pokemon not Found')
});

app.listen(8080)