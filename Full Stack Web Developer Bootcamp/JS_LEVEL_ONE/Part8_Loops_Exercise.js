/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
for(var i=1; i<=5; i++){
  console.log("Hello from for!");
}
// Do this with a While Loop and a For Loop
i = 0;
while(i<5){
  console.log("Hello from while!");
  i++;
}

/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop

i = 0;
while (i<=25){
  if (i%2 !== 0){
    console.log(i);
  }
  i++;
}

// METHOD TWO
// For Loop

for(i=1; i<=25; i+=2){
  console.log(i);
}
