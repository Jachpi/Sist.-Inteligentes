import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string


'''
Código generado por IA
'''


# Ensure you have downloaded the NLTK stopwords and wordnet packages
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to clean text by removing stop words, punctuation, lemmatizing, and converting to lowercase
def clean_text(text):
    if not isinstance(text, str):
        return text

    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)  # Translator to remove punctuation
    text = text.translate(translator)  # Remove punctuation
    words = text.split()
    filtered_words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Function to clean specified columns in a DataFrame
def clean_columns(file_path, columns_to_clean, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Clean the specified columns
    for column in columns_to_clean:
        if column in df.columns:
            df[column] = df[column].apply(clean_text)
        else:
            print(f"Warning: Column '{column}' not found in the CSV file.")

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Cleaned CSV saved as '{output_file}'")

# Example usage
if __name__ == "__main__":
    input_file = "../Dataset/peliculas.csv"  # Path to the input CSV file
    columns_to_clean = ["title", "synopsis","consensus","type","rating","genre","original_language","director","producer",
                        "writer", "release_date_(theaters)", "production_co", "sound_mix", "view_the_collection"]  # List of columns to clean
    output_file = "../Dataset/peliculas_procesado.csv"  # Path to save the cleaned CSV

    clean_columns(input_file, columns_to_clean, output_file)
