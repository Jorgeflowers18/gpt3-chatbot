const http = require('http');

const options = {
  hostname: 'jsonplaceholder.typicode.com',
  path: '/posts',
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
  },
};

const getPosts = () => {
  let data = '';

  const request = http.request(options, (response) => {
    // Set the encoding, so we don't get log to the console a bunch of gibberish binary data
    response.setEncoding('utf8');
    // As data starts streaming in, add each chunk to "data"
    response.on('data', (chunk) => {data += chunk;});
    // The whole response has been received. Print out the result.
    response.on('end', () => {console.log(data);});
  });
  // Log errors if any occur
  request.on('error', (error) => {
    console.error(error);
  });
  // End the request
  request.end();
};

getPosts();

const http = require('http');

// Create the request body
const postData = JSON.stringify({
  title: 'foo',
  body: 'bar',
  userId: 1,
});

const options2 = {
  hostname: 'jsonplaceholder.typicode.com',
  path: '/posts',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(postData),
  },
};

const makePost = () => {
  let data = '';

  const request = http.request(options2, (response) => {
    response.setEncoding('utf8');

    response.on('data', (chunk) => {
      data += chunk;
    });

    response.on('end', () => {
      console.log(data);
    });
  });

  request.on('error', (error) => {
    console.error(error);
  });

  // Write data to the request body
  request.write(postData);

  request.end();
};

makePost();
