import argparse
from transformers import MarianMTModel, MarianTokenizer
import os

# Function to load the model and tokenizer for the specified language pair
def load_model_and_tokenizer(language_pair):
    model_name = f"Helsinki-NLP/opus-mt-{language_pair}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Function to translate text
def translate_text(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Main translation function
def translate_file(input_file, output_dir, language_pairs):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Translate the content into each target language
    for lang_pair in language_pairs:
        print(f"Translating to {lang_pair.split('-')[1]}...")
        tokenizer, model = load_model_and_tokenizer(lang_pair)
        translated_content = translate_text(content, tokenizer, model)

        # Save the translated content
        lang_code = lang_pair.split('-')[1]
        output_file = os.path.join(output_dir, f"{os.path.basename(input_file).split('.')[0]}_{lang_code}.md")
        with open(output_file, "w", encoding="utf-8") as out_file:
            out_file.write(translated_content)

        print(f"Saved translation: {output_file}")

# Command-line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate documentation into multiple languages.")
    
    # Command-line arguments
    parser.add_argument(
        "--input", 
        required=True, 
        help="Path to the input markdown file to translate."
    )
    parser.add_argument(
        "--languages", 
        required=True, 
        help="Comma-separated list of target language codes (e.g., 'es,fr,de,zh')."
    )
    parser.add_argument(
        "--output", 
        default="./translations", 
        help="Directory to save the translated files (default: './translations')."
    )

    args = parser.parse_args()

    # Parse arguments
    input_file = args.input
    target_languages = args.languages.split(",")
    output_dir = args.output

    # Construct language pairs (assuming source language is English)
    language_pairs = [f"en-{lang}" for lang in target_languages]

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
    else:
        # Perform translation
        translate_file(input_file, output_dir, language_pairs)

