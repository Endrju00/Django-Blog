function hello(name){
  console.log("Hello " + name + "!");
}

function addNum(num1, num2){
  console.log(num1 + num2);
}

function helloSomeone(name="Default"){
  console.log("Hello " + name);
}

function fibonacci(num){
  if (num === 0){
    return 0;
  } else if (num == 1) {
    return 1;
  } else {
    return fibonacci(num - 1) + fibonacci(num - 2);
  }
}
