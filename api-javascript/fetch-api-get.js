const getPost = (num) => {
    fetch(`https://jsonplaceholder.typicode.com/posts/${num}`)
      .then(response => response.json())
      .then(data => console.log(data));
  };
  
  getPost(1);
  