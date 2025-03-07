import os
from groq import Groq

# Initialize the Groq client with the API key from environment variables
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def main():
    # Welcome message and instructions
    print("Welcome to the Spanish Vocabulary Teaching Program!")
    print("This program helps you learn Spanish vocabulary by translating English sentences into Spanish.")
    print("You'll see an English sentence containing the translation of a Spanish word, and your task is to translate the entire sentence into Spanish.")
    print("If your translation is incorrect, you can try again or type 'answer' to see the correct translation.\n")

    # Get the list of Spanish words from the user
    words_input = input("Enter Spanish words separated by commas (e.g., perro, gato, amigo): ")
    words = [word.strip() for word in words_input.split(",")]

    # Process each word
    for word in words:
        # Prompt to get English translation, English sentence, and Spanish translation
        prompt = (
            f"Given the Spanish word '{word}', provide its English translation, "
            "an English sentence that uses that translation, and the Spanish translation of that English sentence. "
            "Format your response as:\n"
            "Translation: [English translation]\n"
            "English sentence: [sentence]\n"
            "Spanish translation: [translation]"
        )

        try:
            # Call the API to generate the response
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides translations and sentences."},
                    {"role": "user", "content": prompt}
                ],
                model="llama3-8b-8192",
            )
            response_text = response.choices[0].message.content

            # Parse the response
            lines = response_text.split("\n")
            translation = ""
            english_sentence = ""
            spanish_translation = ""

            for line in lines:
                if line.startswith("Translation:"):
                    translation = line[len("Translation:"):].strip()
                elif line.startswith("English sentence:"):
                    english_sentence = line[len("English sentence:"):].strip()
                elif line.startswith("Spanish translation:"):
                    spanish_translation = line[len("Spanish translation:"):].strip()

            # Verify all parts are present
            if not translation or not english_sentence or not spanish_translation:
                print(f"Error: Could not parse the response for word '{word}'. Skipping to the next word.")
                continue

            # Display the English sentence and prompt for translation
            print(f"\nTranslate this sentence into Spanish: {english_sentence}")

            while True:
                user_input = input("Your translation: ").strip()

                # Option to see the answer
                if user_input.lower() == "answer":
                    print(f"The correct translation is: {spanish_translation}")
                    break
                else:
                    # Prompt to check the user's translation
                    check_prompt = (
                        f"Is '{user_input}' a correct Spanish translation of the English sentence '{english_sentence}'? "
                        "Answer 'yes' if it is correct, 'no' if it is not."
                    )

                    # Call the API to verify the translation
                    check_response = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant that checks translations."},
                            {"role": "user", "content": check_prompt}
                        ],
                        model="llama3-8b-8192",
                    )
                    check_text = check_response.choices[0].message.content.lower()

                    # Handle the API's response
                    if check_text.startswith("yes"):
                        print("Correct!")
                        break
                    elif check_text.startswith("no"):
                        print("Incorrect. Try again or type 'answer' to see the correct translation.")
                    else:
                        print("Unexpected response from API. Please try again.")

        except Exception as e:
            print(f"API error for word '{word}': {e}. Skipping to the next word.")
            continue

    print("\nCongratulations! You have completed the vocabulary practice.")

if __name__ == "__main__":
    main()
