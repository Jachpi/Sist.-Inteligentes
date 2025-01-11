import separar_columna

# Example usage
if __name__ == "__main__":
    input_file = "../src/Dataset/peliculas_procesado.csv"  # Path to the input CSV file
    target_column = "consensus"  # Column to analyze for unique words
    output_file = "../src/Dataset/peliculas_consensus_separado.json"  # Path to save the updated CSV
    separar_columna.create_word_dict(input_file, target_column, output_file)
