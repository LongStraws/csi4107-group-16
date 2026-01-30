import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
from collections import defaultdict

# STEP 1
def preprocess(text, stem=False):
    text = text.lower() #Set to lowercase
    text = re.sub(r"[^a-z\s]", ' ', text) #Remove numbers and punctuation tokens
    
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopWords]

    #Stem the index words
    if stem:
        tokens = [PorterStemmer().stem(word) for word in tokens]
    
    return tokens


#Remove stop words
with open("List of Stopwords.html", encoding="utf-8") as file:
    stopWords = file.read()
stopWords = re.sub(r"<[^>]+>", "", stopWords) #Get rid of html tags
stopWords = set(word.strip() for word in stopWords.splitlines() if word.strip())


# STEP 2
invertedIndex = defaultdict(lambda: defaultdict(int)) #2D dictionary for storing the term frequency of words in each document
with open("corpus.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)
        text = data["title"] + " " + data["text"] #Get the contents of the document
        tokens = preprocess(text) #Call the preprocessing function with the document contents
        documentID = data["_id"] #Get the current document's ID

        #Calculate the term frequency of the word in the document
        for word in tokens:
            invertedIndex[word][documentID] += 1
        
print(invertedIndex["study"]) #Temporary test print