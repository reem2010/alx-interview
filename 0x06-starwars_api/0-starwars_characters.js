#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
    if (error) {
      throw error;
    } else {
      body = JSON.parse(body);
      const peoples = body.characters;
      peoples.map((url) => {
        request(url, (error, response, body) => {
          if (error) {
            throw error;
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
