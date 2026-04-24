
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python that uses strings, loops, conditionals, and user input to let a player guess a secret word.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a Python program that randomly selects a hidden word from a list and lets the player guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list.
- Prompt the user to guess one letter at a time.
- Display the current word progress with blanks and correctly guessed letters (e.g. `h _ n g m a n`).
- Track and display remaining incorrect guesses.
- Prevent duplicate letter guesses from counting against the player.
- End the game with a win message when the word is fully guessed.
- End the game with a lose message when the player runs out of attempts.
- Optionally show the correct word after a loss.

#### Example interaction

```text
Word: _ _ n g m a n
Guess a letter: a
Correct! Word: _ _ n g m a n
Guess a letter: h
Correct! Word: h _ n g m a n
...
```