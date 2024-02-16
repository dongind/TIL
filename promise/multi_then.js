const testPromise = new Promise((resolve) => {
  console.log("In promise executor");
  setTimeout(() => {
    resolve("Promise!");
  }, 0);
});

testPromise
  .then((result) => {
    console.log(result, "1");
    setTimeout(() => {
      console.log("it's in setTimeout of first then method");
      return result;
    }, 0);
  })
  .then((result) => {
    console.log(result, "2");
    return result;
  });

testPromise
  .then((result) => {
    console.log(result, "3");
    return result;
  })
  .then((result) => {
    console.log(result, "4");
    return result;
  });
