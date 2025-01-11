import separar_columna

if __name__ == "__main__":
    input_file = "../Dataset/peliculas_procesado.csv"  # Path to the input CSV file
    target_column = "synopsis"  # Column to analyze for unique words
    output_file = "../Dataset/peliculas_separado.json"  # Path to save the updated CSV

    separar_columna.create_word_dict(input_file, target_column, output_file)