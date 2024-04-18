#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  request('https://swapi-api.alx-tools.com/api/films', (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      body = JSON.parse(body);
      const peoples = body.results[[process.argv[2]]].characters;
      peoples.map((url) => {
        request(url, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            body = JSON.parse(body);
            console.log(body.name);
          }
        });
        return url;
      });
    }
  });
}
