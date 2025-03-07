# Spanish Vocabulary Teaching Program

## Overview
The **Spanish Vocabulary Teaching Program** is a Python-based interactive tool designed to help users learn Spanish vocabulary. The program prompts users to translate English sentences into Spanish, reinforcing vocabulary retention and translation skills.

## Features
- Accepts a list of Spanish words and generates translations with example sentences.
- Uses the **Groq API** to generate translations and verify user responses.
- Provides feedback on user translations and offers the correct answer if needed.
- Interactive and engaging way to practice Spanish vocabulary.

## Prerequisites
- Python 3.x installed on your system
- A Groq API key (stored in the environment variable `GROQ_API_KEY`)

## Installation
1. Clone this repository or download the script.
   ```sh
   git clone https://github.com/your-repository/spanish-vocabulary-teacher.git
   cd spanish-vocabulary-teacher
   ```
2. Install dependencies (if any additional libraries are required, update this step accordingly).
   ```sh
   pip install groq
   ```
3. Set your Groq API key as an environment variable:
   ```sh
   export GROQ_API_KEY=your_api_key_here  # For macOS/Linux
   set GROQ_API_KEY=your_api_key_here    # For Windows (Command Prompt)
   ```

## Usage
Run the program using:
```sh
python spanish_vocab.py
```

### How It Works
1. Enter a list of Spanish words (comma-separated) when prompted.
2. The program will generate:
   - The English translation of each word.
   - An English sentence containing that word.
   - The Spanish translation of the sentence.
3. You will be asked to translate the given English sentence into Spanish.
4. The program checks your translation and provides feedback.
5. If incorrect, you can try again or type `answer` to see the correct translation.
6. Continue until all words are processed.

## Error Handling
- If the API fails or an unexpected response is received, the program will skip to the next word.
- Incorrect translations prompt users to retry.

## License
This project is licensed under the MIT License.

---
Feel free to contribute, suggest improvements, or report issues!
