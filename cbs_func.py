from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import patsy
import string
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize, TreebankWordTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer 



def make_ep_list (url):
	'''
	Takes in html of TV series season directory and returns the text from URL for each episode
	title. 
	'''
	ep_list = []

	url1 = url 
	respond = requests.get(url1)
	titles = respond.text
	soup = BeautifulSoup(titles, "html.parser")
	titles_list = soup.find('div',class_='series_seasons').find_all('a')
	for link in soup.find_all('a'):
		ep_list.append(link.get('href'))

	for i, num in enumerate(ep_list):
		ep_list[i] = num.replace(url,'')

	ep_list = ep_list [5:]
	return ep_list


def ncis_data(ncis_list):
	'''
	Function takes in list of NCIS epsidoe titles and appends that to base URL to access each page of script.
	Returns the page text complete with html tags. They will be cleaned later.
	'''
	ncis_df = []
	url = 'https://subslikescript.com/series/NCIS-364845/{}'
	
	for ep in ncis_list:
		ep_title = ep
		response = requests.get(url.format(ep))
		page = response.text
		soup = BeautifulSoup(page, 'lxml')
		
		scripts = [{
					'ep_id': 'ncis_' + ep_title,
					'dialogue':soup.find(class_='full-script')
				   }]
			
				
		ncis_df.extend(scripts)
	 
	df =  pd.DataFrame(ncis_df)
	df = df[['ep_id', 'dialogue']]
	df = df[:-1]
	
	return df



def shield_data(shield_list):
	'''
	Function takes in list of The Shield episode titles and appends that to base URL to access each page of script.
	Returns the page text complete with html tags that need to be cleaned later.
	'''
	shield_df = []
	url = 'https://subslikescript.com/series/The_Shield-286486/{}'
	
	for ep in shield_list:
		ep_title = ep
		response = requests.get(url.format(ep))
		page = response.text
		soup = BeautifulSoup(page, 'lxml')
		
		scripts = [{
					'ep_id': 'the_shield_' + ep_title,
					'dialogue':soup.find(class_='full-script')
				   }]
			
				
		shield_df.extend(scripts)
	 
	df =  pd.DataFrame(shield_df)
	df = df[['ep_id', 'dialogue']]
	df = df[:-1]
	
	return df


def clean_tv_scripts (text):
	'''Make text lowercase, remove text in square brackets, remove punctuation
	and remove words containing numbers.'''

	text = re.sub('([A-Z]{2,})', ' ', text)
	text = text.lower()
	text = re.sub('\[.*?\]', ' ', text)
	text = re.sub('\<.*?>', ' ', text)
	text = re.sub('\(.*?\)', ' ', text)
	text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
	text = re.sub('\w*\d\w*', '', text)
	text = re.sub('\n', ' ', text)
	text = re.sub('   ', ' ', text)
	text = re.sub('  ', ' ', text)
	text = re.sub('♪', '', text)
	return text


def clean_sentiment(text):
	'''Remove text in square brackets, html tag brackets, parentheses, musical emojis, new line
	indicators and words containing numbers.'''

	text = re.sub('([A-Z]{2,})', ' ', text)
	text = re.sub('\[.*?\]', ' ', text)
	text = re.sub('\<.*?>', ' ', text)
	text = re.sub('\(.*?\)', ' ', text)
	text = re.sub('\w*\d\w*', '', text)
	text = re.sub('\n', ' ', text)
	text = re.sub('♪', '', text)
	return text


class NLPProcessor:
	
	def __init__(self, vectorizer_class, tokenizer_function, cleaning_function, lemmer_function):
		self.vectorizer = vectorizer_class
		self.tokenizer = tokenizer_function
		self.cleaning_function = cleaning_function
		self.lemmer = lemmer_function
	
	def fit(self, corpus_list_to_fit):
		cleaned_corpus = list(map(self.cleaning_function, corpus_list_to_fit))
#         print(cleaned_corpus)
		tokenized_list = list(map(self.tokenizer, cleaned_corpus))
#         print(tokenized_list)
		lemmed_list = [' '.join(list(map(self.lemmer, item))) for item in tokenized_list]
#         print(lemmed_list)
		return self.vectorizer.fit(lemmed_list)
	
	def transform(self, corpus_list_to_clean):
		cleaned_corpus = list(map(self.cleaning_function, corpus_list_to_clean))
		tokenized_list = list(map(self.tokenizer, cleaned_corpus))
		lemmed_list = [' '.join(list(map(self.lemmer, item))) for item in tokenized_list]
		return pd.DataFrame(self.vectorizer.transform(lemmed_list).toarray(), 
							columns=self.vectorizer.get_feature_names())

