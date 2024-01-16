#!/user/bin/node
// prints number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonData = JSON.parse(body).results;

    for (const i in jsonData) {
      const characterID = jsonData[i].characters;

      for (const j in characterID) {
        if (characterID[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
