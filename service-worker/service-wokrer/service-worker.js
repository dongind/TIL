self.addEventListener("fetch", function (event) {
  const { url } = event.request;
  if (url === "https://jsonplaceholder.typicode.com/users/1") {
    event.respondWith(
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          console.log("[SW] Original Data : ", data);
          return new Response(
            JSON.stringify({
              ...data,
              id: 12345678,
              name: "Service Worker",
              username: "Service Worker",
              email: "Service_Worker@service.com",
            })
          );
        })
    );
  }
});

self.addEventListener("message", function (event) {
  console.log(event.data);
  this.self.clients.matchAll().then(function (clients) {
    clients.forEach(function (client) {
      client.postMessage("[SW] : Hello, Client. Your Client id is :" + client.id);
    });
  });
});
