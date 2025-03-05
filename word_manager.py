WORDS_FILE = 'filtered_words.txt'

def getWords():
    WORDS = []
    
    with open(WORDS_FILE, 'r') as file:
        WORDS = file.readlines()
    
    WORDS = [line.strip() for line in WORDS]

    return WORDS