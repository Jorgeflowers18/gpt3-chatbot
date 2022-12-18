var XMLHttpRequest = require('xhr2');
var xhr = new XMLHttpRequest();

const getPosts = () => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts');
    xhr.responseType = 'json';
    xhr.onload = () => {
      console.log(xhr.response[1]['id']);
    }
    xhr.send();
};

getPosts();