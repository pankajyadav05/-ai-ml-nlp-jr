<div align="center">
	<a target="_blank" href="https://gitforcetalent.com">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://gitforcetalent.com/_next/image?url=%2Fimages%2Flogo-light.png&w=1920&q=75">
            <source media="(prefers-color-scheme: light)" srcset="https://gitforcetalent.com/_next/image?url=%2Fimages%2Flogo.png&w=1920&q=75">
            <img alt="https://gitforcetalent.com" src="https://gitforcetalent.com/_next/image?url=%2Fimages%2Flogo.png">
        </picture>
	</a>
    <br />
    <br />
</div>

---

---

# Assignment: AI ML Engineer Tech Evaluation Gitforce

This task involves creating a word chain game that incorporates basic NLP concepts. Here's a breakdown of the challenge:

## Game Rules

1. The game is turn-based between the user and the computer.
2. Each computer's word must start with the last letter of the previous word.
3. Words must be valid English words (validated using NLTK's words corpus).
4. No word should be repeated during the game.
5. The game continues until the player types "quit" to end the game or the computer is not able to come up with a word that start's with the last letter of the previous word.

## Features

1. Word Validation: The game uses NLTK's words corpus to validate user input.
2. Game Logic: It implements a simple turn-based game where the computer responds with a word starting with the last letter of the user's word.
3. Word Selection: The computer selects a random valid word that hasn't been used before.

