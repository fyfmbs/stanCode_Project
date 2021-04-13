"""
File: anagram.py
Name: Shawn Chan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable

prefix_dict = {}


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagram for: ')
        if word == EXIT:
            break
        start_time = time.time()
        word = word.lower()
        print('Searching....')
        word_lst = find_anagrams(sorted(word))
        print(len(word_lst), 'anagrams: ', word_lst)
        print("--- %s seconds ---" % (time.time() - start_time))


def read_dictionary(num):
    """
    Create a list for saving the whole dictionary
    :return: list of dictionary
    """
    global prefix_dict
    prefix_dict = {}
    with open('dictionary.txt', 'r') as f:
        # remove the line breaker '\n'
        words = f.read().splitlines()
        for word in words:
            if len(word) == num:
                for i in range(len(word)-1):
                    # store all prefix of word (including it self) in prefix_dict
                    prefix = word[:i+1]
                    if prefix not in prefix_dict:
                        prefix_dict[prefix] = prefix
                prefix_dict[word] = word
    return prefix_dict


def find_anagrams(s):
    """
    :param s: the word for search the anagram
    :return: the word list including all the anagram of searching word
    """
    alphabet_dic = create_alphabet_dic(s, {})
    # list for counting how many times for using find_anagrams_helper
    read_dictionary(len(s))
    word_lst = find_anagrams_helper(alphabet_dic, '', [], [])
    return word_lst


def find_anagrams_helper(alphabet_dic, c_s, c_n, word_lst):
    """
    a helper for the find_anagrams that can input more info
    :param alphabet_dic: the dictionary include every alphabet in the searching word
    :param c_s: a string for saving the word that we search
    :param c_n: a list for saving the index of the dictionary
    :param word_lst: a list for saving the word that I searched
    :return: the word list that we searched
    """

    if len(c_s) == len(alphabet_dic):
        if c_s not in word_lst:
            word_lst.append(c_s)
            print('Found', c_s)
            print('Searching....')

    else:
        for ele in alphabet_dic:
            if ele not in c_n:
                c_n.append(ele)
                c_s += alphabet_dic[ele]
                if has_prefix(c_s) is True:
                    find_anagrams_helper(alphabet_dic, c_s, c_n, word_lst)
                    c_n.pop()
                    c_s = c_s[:len(c_s) - 1]
                else:
                    c_n.pop()
                    c_s = c_s[:len(c_s) - 1]
    return word_lst


def create_alphabet_dic(word, alphabet_dic):
    """
    Created a dictionary for saving each alphabet
    in the word that we want to searching
    :param word: the input word
    :param alphabet_dic: a empty dictionary for saving the alphabet
    :return: the dictionary with every alphabet in the word
    """
    for i in range(len(word)):
        alphabet_dic[i] = word[i]
    return alphabet_dic


def has_prefix(sub_s):
    """
    :param sub_s: the sub_string with the staring word
    :return: True of False
    """
    if sub_s in prefix_dict:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
