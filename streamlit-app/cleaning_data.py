def clean_data(a_string):
		import pandas as pd
		import numpy as np
		import re 
		import nltk
		from nltk.stem import WordNetLemmatizer
		nltk.download('stopwords')
		nltk.download('punkt')
		from nltk.corpus import stopwords
		from nltk import word_tokenize
		stopwords = stopwords.words('english')

		# 1. function that makes all text lowercase.
		def make_lowercase(test_string):
			return test_string.lower()

		# 2. function that removes all punctuation. 
		def remove_punc(test_string):
			test_string = re.sub(r'[^\w\s]', '', test_string)
			return test_string

		# 3. function that removes all stopwords.
		def remove_stopwords(test_string):
			# Break the sentence down into a list of words
			words = word_tokenize(test_string)
			
			# Make a list to append valid words into
			valid_words = []
			
			# Loop through all the words
			for word in words:
				
				# Check if word is not in stopwords. Stopwords was imported from nltk.corpus
				if word not in stopwords:
					
					# If word not in stopwords, append to our valid_words
					valid_words.append(word)

			# Join the list of words together into a string
			a_string = ' '.join(valid_words)

			return a_string

		# 4. function to break words into their lemm words
		def lem_words(a_string):
			# Initalize our Stemmer
			lemmatizer = WordNetLemmatizer()
			
			# Break the sentence down into a list of words
			words = word_tokenize(a_string)
			
			# Make a list to append valid words into
			valid_words = []

			# Loop through all the words
			for word in words:
				# Stem the word
				lemmed_word = lemmatizer.lemmatize(word) #from nltk.stem import PorterStemmer
				
				# Append stemmed word to our valid_words
				valid_words.append(lemmed_word)
				
			# Join the list of words together into a string
			a_string = ' '.join(valid_words)

			return a_string 
		

		a_string = make_lowercase(a_string)
		a_string = remove_punc(a_string)
		a_string = remove_stopwords(a_string)
		a_string = lem_words(a_string)

		return a_string
