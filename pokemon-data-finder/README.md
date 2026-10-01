# Pokemon Data Finder

An early web programming exercise: a small Express API for looking up Pokemon by name, a Bootstrap search page, and a D3 visualisation of the Pokemon dataset.

University coursework on web development.

## Contents

| File | Purpose |
|---|---|
| `server.js` | Express server exposing `GET /poke?name=<name>`, which looks the Pokemon up in `pokemon.json` and returns its generation |
| `index.html`, `index.js` | Bootstrap search page that calls the API with `fetch` |
| `initial.html` | D3 chart built from the full Pokemon dataset, loaded from [omar2381/pokemon.csv](https://github.com/omar2381/pokemon.csv) |

## Running it

```bash
npm install
npm start          # serves the API on port 8080
```

Then open `index.html` in a browser. `index.js` calls port 8090, so change it to 8080 to match the server.

## Tech

Node.js, Express, Bootstrap, D3.js
