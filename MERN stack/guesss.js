// // Generate a random number between 1 and 100
// const randomNumber = Math.floor(Math.random() * 100) + 1;

// // Initialize the number of attempts and a flag for game completion
// let attempts = 0;
// let gameOver = false;

// // Function to start and manage the game
// function startGame() {
//   while (!gameOver) {
//     // Prompt the player for a guess
//     const playerGuess = parseInt(prompt("Guess a number between 1 and 100:"));

//     // Validate the input
//     if (isNaN(playerGuess)) {
//       alert("Invalid input. Please enter a number.");
//       continue;
//     }

//     // Increment the number of attempts
//     attempts++;

//     // Check the guess against the random number
//     if (playerGuess === randomNumber) {
//       alert(`Congratulations! You guessed the number in ${attempts} attempts.`);
//       gameOver = true;
//     } else if (playerGuess < randomNumber) {
//       alert("Too low. Try again!");
//     } else {
//       alert("Too high. Try again!");
//     }
//   }
// }

// // Start the game
// startGame();
