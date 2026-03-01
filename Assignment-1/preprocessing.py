# STEP 1

import re
from typing import List, Set
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def getStopwords(filePath = "List of Stopwords.html"):
    with open(filePath, encoding="utf-8") as file:
        stopWords = file.read()
    stopWords = re.sub(r"<[^>]+>", "", stopWords) #Removes html.
    return set(word.strip() for word in stopWords.splitlines() if word.strip())

def preprocess(text, stopWords, stem = False):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = word_tokenize(text.lower())
    cleanedTokens = []

    #Removes all stopwords from the tokens.
    for word in tokens:
        if word not in stopWords:
            cleanedTokens.append(word)

    #Stems the index words if stem is set to true.
    if stem:
        stemmer = PorterStemmer()
        return [stemmer.stem(word) for word in cleanedTokens]

    return cleanedTokens