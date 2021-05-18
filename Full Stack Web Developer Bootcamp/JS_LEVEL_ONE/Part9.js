var name = prompt("What is your name?");
var lastname = prompt("What is your lastname?");
var age = prompt("How old are you?");
var height = prompt("How tall are you?");
var petname= prompt("What is your pet name?");

var flag = true;

if (name[0] !== lastname[0]){
  flag = false;
  if (20 >== age && age >== 30){
    flag = false;
    if (height < 170){
      flag = false;
      if (petname[petname.length - 1] !== 'y'){
        flag = false;
      }
    }
  }
}


if (flag){
  console.log("Secret message.");
} else {
  console.log("Normal message.")
}
