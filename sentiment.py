#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_3_Dictionaries/sentiment.py
import string
import sys


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
    # Making everything lowercase
    word_list = str(sentence.lower())

    # Possible punctuation from python
    possible_punc = string.punctuation

    # Getting rid of possible internal punctuation
    for punc in word_list:
        if punc in possible_punc:
            word_list = word_list.replace(punc, '')

    # Breaking sentence into individual words
    word_list = word_list.split()
    return word_list


def score_sentence(sentence, score_dict):
    """
    :param sentence: any sentence in a string
    :param score_dict: dictionary containing scores of words
    :return: score of sentence
    """
    # Make sentence into a list of strings w/o punctuation
    mywords = get_words(sentence)

    # Convert word_list to a dictionary all equal to zero (score is a float)
    myscores = score_dict.fromkeys(mywords, 0.0)

    # Open dictionary with scores
    # score_dict = load_score_dict(filename)

    # Assign scores to words form sentence
    for word in myscores.keys():  # Loop for each word in sentence
        if word in score_dict.keys():  # Is the current word in the scoring dictionary
            myscores[word] = score_dict[word]

    # Sentence score
    return sum(myscores.values())


# if __name__ == "__main__":
#     print(load_score_dict())