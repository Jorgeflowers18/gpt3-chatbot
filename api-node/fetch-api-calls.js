const getPost = (num) => {
  fetch(`https://jsonplaceholder.typicode.com/posts/${num}`)
    .then((response) => response.json())
    .then((data) => console.log(data));
};

getPost(1);

const postData = () => {
  fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    body: JSON.stringify({
      title: "foo",
      body: "bar",
      userId: 1,
    }),
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
};

postData()
