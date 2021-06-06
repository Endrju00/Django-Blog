// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
function add(name){
  roster.push(name);
}
// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT
function remove(name){
  var index = roster.indexOf(name);
  if (index > -1){
    roster.splice(index, 1);
  }
}
// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(){
  console.log(roster);
}

// Start by asking if they want to use the web app
var start = prompt("Do you want to use the web app? Type \'y\' for yes and \'n\' for no.");
if (start == 'y'){
  while (true){
    var action = prompt("Type add to add a student, remove 0to remove the student, display to display all of the students or quit to exit the web app.");
    if (action == "add"){
      var name = prompt("Type the name of a student.");
      add(name);
    } else if (action == "remove"){
      var name = prompt("Type the name of a student.");
      remove(name);
    } else if (action == "display"){
      display();
    } else if (action == "quit"){
      break;
    }
  }
}
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
