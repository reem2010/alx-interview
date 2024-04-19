#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');
const promisifiedRequest = promisify(request);
// if (process.argv.length === 3) {
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, async (error, response, body) => {
  if (error) {
    // throw error;
  } else {
    body = JSON.parse(body);
    let peoples = body.characters;
    peoples = await Promise.all(peoples.map(async (url) => {
      const body = await promisifiedRequest(url);
      const data = JSON.parse(body.body);
      //   console.log(body)
      return data.name;
    //   .then(({ body }) => {
    //     const data = JSON.parse(body);
    //     })
    //   })(url, (error, response, body) => {
    //     if (error) {
    //       throw error;
    //     } else {
    //       body = JSON.parse(body);
    //       name = body.name;
    //       console.log(name)
    //       console.log(ind)
    //     }
    //   });
    }));
    peoples.forEach((data) => console.log(data));
  }
});
// }
