# -*- coding: utf-8 -*-
"""
Created on Sat May 27 00:53:57 2023

@author: YUVRAJ
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer


document = "This is a sample document. It contains multiple sentences."
tokens = word_tokenize(document)
pos_tags = pos_tag(tokens)

stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

documents = [document]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names()
tfidf_representation = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
