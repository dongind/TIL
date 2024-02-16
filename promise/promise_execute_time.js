const testPromise = new Promise((resolve) => {
  console.log("In Promise Execution Function");
  setTimeout(() => {
    console.log("In setTimeout");
    resolve();
  }, 3);
});

console.log("before promise");

testPromise
  .then((result) => {
    console.log("In Then Method 1.1", result);
  })
  .then(() => {
    console.log("In Then Method 1.2");
  });

testPromise
  .then((result) => {
    console.log("In Then Method 2.1", result);
  })
  .then(() => {
    console.log("In Then Method 2.2");
  });

console.log("after promise");
