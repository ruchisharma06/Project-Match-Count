import re

def load_predefined_words(file_path):
    """Reading predefined keywords from a file"""
    with open(file_path, 'r') as file:
        predefined_keywords = set(word.strip().lower() for word in file)
    return predefined_keywords

def count_word_matches(text_file_path, predefined_keywords):
    """Counting word of predefined keywords in a input text file."""
    match_counts = {word: 0 for word in predefined_keywords}
    
    with open(text_file_path, 'r') as file:
        for line in file:
            # Converting each line to lowercase
            line_lowercase = line.strip().lower()
            # Using regex to find word to word match 
            words_in_line = re.findall(r'\b\w+\b', line_lowercase)
            for word in words_in_line:
                if word in predefined_keywords:
                    match_counts[word] += 1

    return match_counts

def print_match_counts(match_counts):
    """Printing matched words as given"""
    print(f"{'Predefined word':<20} {'Match count':<10}")
    for word, count in match_counts.items():
        print(f"{word:<20} {count:<10}")

def main():
    predefined_keywords_file = '/Users/mac/Desktop/wordmatch/predefined_words.txt'  
    input_file = '/Users/mac/Desktop/wordmatch/input_file.txt'  
    
    
    predefined_words = load_predefined_words(predefined_keywords_file)
    
    
    match_word_counts = count_word_matches(input_file, predefined_words)
    
    
    print_match_counts(match_word_counts)

if __name__ == "__main__":
    main()
