# Made by chatGPT with human modifications

# Define the input and output file paths
input_file_path = "words_alpha.txt"
output_file_path = "filtered_words.txt"

MIN_LEN = 3
MAX_LEN = 7

# Read the input file, filter words with length between 3 and 7 letters, and save to output file
with open(input_file_path, "r") as infile, open(output_file_path, "w") as outfile:
    for word in infile:
        word = word.strip()  # Remove any leading/trailing whitespace
        if MIN_LEN <= len(word) <= MAX_LEN:
            outfile.write(word + "\n")

# Return the output file path
output_file_path
