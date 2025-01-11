import pandas as pd
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize



'''
Código generado por IA
'''

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


# Function to create a Python dictionary storing nouns for each row
def create_word_dict(file_path, target_column, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    if target_column not in df.columns:
        print(f"Error: Column '{target_column}' not found in the CSV file.")
        return

    # Create a dictionary to store arrays of nouns for each row
    noun_dict = {}

    for row in df.itertuples():
        text = getattr(row, target_column)
        index = getattr(row, "id")
        if isinstance(text, str):
            tokens = word_tokenize(text)
            tagged_words = pos_tag(tokens)
            nouns = [word for word, tag in tagged_words if tag.startswith('NN')]
            noun_dict[index] = nouns
        else:
            noun_dict[index] = []

    # Save the dictionary as a JSON file
    with open(output_file, 'w') as f:
        import json
        json.dump(noun_dict, f)

    print(f"Noun dictionary saved as '{output_file}'")