"""
File: boggle.py
Name: Shawn Chan
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: find all the words from boggle that can be found in dictionary
	"""
	all_row = []
	for i in range(1, 5):
		row = input(str(i) + ' row of letters: ')
		row.strip()
		if len(row.split(' ')) < 4:
			print('Illegal form')
			break
		else:
			all_row.append(row.split(' '))
	word_lst = find_word(all_row, '', [])
	print('There are ', len(word_lst), ' words in total.')


def find_word(all_row, word, word_lst):
	"""
	A function to find the words in boggle
	:param all_row: the list stored 4 input string row
	:param word: the word that be found in boggle
	:param word_lst: the list stored the words found in boggle
	:return: the list of the finding words
	"""
	word_dic = read_dictionary()
	for y in range(4):
		for x in range(4):
			start_x = x
			start_y = y
			cor_lst = [(start_x, start_y)]
			word += all_row[start_x][start_y]
			find_word_helper(all_row, word, word_lst, start_x, start_y, cor_lst, word_dic)
			cor_lst.pop()
			word = word[:len(word) - 1]
	return word_lst


def find_word_helper(all_row, word, word_lst, start_x, start_y, cor_lst, word_dic):
	"""
	A helper for helping the function find_word to add letters next to the fist letter.
	:param all_row: the list stored 4 input string row
	:param word: the word that be found in boggle
	:param word_lst: the list stored the words found in boggle
	:param start_x: the order of the row
	:param start_y: the order of the letter in the chosen row
	:param cor_lst: the list stored the chosen coordinate
	:param word_dic: the word list of the dictionary

	"""
	if len(word) >= 4:
		if word in word_dic:
			if word not in word_lst:
				print('Found', word)
				word_lst.append(word)

	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			now_x = start_x + i
			now_y = start_y + j
			if 0 <= start_x + i < 4:
				if 0 <= start_y + j < 4:
					if (now_x, now_y) not in cor_lst:
						cor_lst.append((now_x, now_y))
						letter = all_row[now_x][now_y]
						word += letter
						if has_prefix(word, word_dic) is True:
							find_word_helper(all_row, word, word_lst, now_x, now_y, cor_lst, word_dic)
							word = word[:len(word) - 1]
							now_x -= i
							now_y -= j
							cor_lst.pop()
						else:
							word = word[:len(word) - 1]
							now_x -= i
							now_y -= j
							cor_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list

	:return: list of dictionary
	"""
	word_dic = []
	with open('dictionary.txt', 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				word_dic.append(word)
	return word_dic


def has_prefix(sub_s, word_dic):
	"""
	:param word_dic: the word list of the dictionary
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_dic:
		if word.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
