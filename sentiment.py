#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_3_Dictionaries/sentiment.py
import string

def clean_txt(filename='sentiment.txt'):
    """
    :param filename: local .txt file, default to sentiment.txt
    :return: list
    """
    with open(filename) as txt_file:
        temp_list = []
        # Run through each line of the file
        for line in txt_file:
            # lines with a # will be skipped
            if '#' not in line:
                # blank lines will be skipped
                if line != '\n':
                    # Split each line in .txt file into ['word', 'value']
                    split_line = line.split()
                    # Store each iteration in a new list
                    temp_list.append(split_line)

    return temp_list


def load_score_dict(filename='sentiment.txt'):
    """
    :param filename: local .txt file, default to sentiment.txt
    :return: dictionary of form word [value]
    """
    # Clean any blank lines or '#' from indicated .txt file with clean_txt function
    clean_list = clean_txt(filename)
    # Making a dictionary to store in
    clean_dict = {}
    # Go through each pair in clean_list and separate into 'word': value format
    for pair in clean_list:
        name, value = pair[0], float(pair[1])
        clean_dict[name] = value
    return clean_dict


def get_words(sentence):
    """
    :param sentence: Complete sentence with at least one alphanumeric character
    :return: list of strings containing individual lowercase words from sentence
    """
    case_words = sentence.lower()
    print(case_words)
    internal_punctuation = case_words.strip('-:')
    print(internal_punctuation)
    raw_words = internal_punctuation.split()
    print(raw_words)
    return

if __name__ == "__main__":
    print('testing')
    # print(load_score_dict())
    get_words("Grocery list: 3 boxes Land-o-Lakes butter, Aunt Jemima's butter pancake mix")
