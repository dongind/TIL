const testPromise = new Promise((resolve) => {
  console.log("In promise executor");
  resolve("Promise!");
});

testPromise.then((result) => {
  console.log(result, "1");
});

testPromise.then((result) => {
  console.log(result, "2");
});
