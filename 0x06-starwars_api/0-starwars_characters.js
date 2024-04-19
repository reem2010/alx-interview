#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');

const promisifiedRequest = promisify(request);

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, async (error, response, body) => {
  if (error) {
    throw error;
  } else {
    body = JSON.parse(body);
    let peoples = body.characters;
    peoples = await Promise.all(peoples.map(async (url) => {
      const body = await promisifiedRequest(url);
      const data = JSON.parse(body.body);
      return data.name;
    }));
    peoples.forEach((data) => console.log(data));
  }
});
