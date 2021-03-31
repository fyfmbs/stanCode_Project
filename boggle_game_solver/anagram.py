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

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
sum_count = 0


def main():

    while True:
        new_word_lst = []
        count = 0
        print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
        word = input('Find anagram for: ')
        word = word.lower()
        word_dic = read_dictionary(len(word))
        if word == EXIT:
            break
        print('Searching....')
        word_lst = find_anagrams(word)
        for new_word in word_lst:
            if new_word in word_dic:
                new_word_lst.append(new_word)
                count += 1
                print('Found', new_word)
                print('Searching....')
        print(count, 'anagrams: ', new_word_lst)


def read_dictionary(num):
    """
    Create a list for saving the whole dictionary
    :return: list of dictionary
    """
    word_dic = []
    with open('dictionary.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == num:
                word_dic.append(word)
    return word_dic


def find_anagrams(s):
    """
    :param s: the word for search the anagram
    :return: the word list including all the anagram of searching word
    """
    alphabet_dic = create_alphabet_dic(s, {})
    # list for counting how many times for using find_anagrams_helper
    cnt_lst = []
    word_dic = read_dictionary(len(s))
    word_lst = find_anagrams_helper(alphabet_dic, '', [], [], cnt_lst, word_dic)
    return word_lst


def find_anagrams_helper(alphabet_dic, c_s, c_n, word_lst, cnt_lst, word_dic):
    """
    a helper for the find_anagrams that can input more info
    :param word_dic:
    :param alphabet_dic: the dictionary include every alphabet in the searching word
    :param c_s: a string for saving the word that we search
    :param c_n: a list for saving the index of the dictionary
    :param word_lst: a list for saving the word that I searched
    :param cnt_lst: the list that saving the using times
    :return: the word list that we searched
    """
    cnt_lst.append(1)
    if len(c_s) == len(alphabet_dic):
        if c_s not in word_lst:
            word_lst.append(c_s)

    else:
        for ele in alphabet_dic:
            if ele not in c_n:
                c_n.append(ele)
                c_s += alphabet_dic[ele]
                if has_prefix(c_s, word_dic) is True:
                    find_anagrams_helper(alphabet_dic, c_s, c_n, word_lst, cnt_lst, word_dic)
                    c_n.pop()
                    c_s = c_s[:len(c_s)-1]
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


def has_prefix(sub_s, word_dic):
    """
    :param word_dic:
    :param sub_s: the sub_string with the staring word
    :return: True of False
    """
    for word in word_dic:
        if word.startswith(sub_s) is True:
            return True
    return False

if __name__ == '__main__':
    main()
