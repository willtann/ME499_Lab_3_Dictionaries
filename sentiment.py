#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_3_Dictionaries/sentiment.py


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


if __name__ == "__main__":
    print('testing')
    print(load_score_dict())
