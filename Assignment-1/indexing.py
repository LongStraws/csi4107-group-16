# STEP 2

import json
from collections import defaultdict
from typing import DefaultDict, Dict, Set
from preprocessing import preprocess

def buildInvertedIndex(corpusPath, stopWords, stem = False):
    invertedIndex = {}

    with open(corpusPath, "r", encoding="utf-8") as file:
        for line in file:
            content = json.loads(line)
            text = content["title"] + " " + content["text"]
            tokens = preprocess(text, stopWords, stem=stem)
            documentID = content["_id"]

            #Calculates the term frequency of the word in the document.
            for word in tokens:
                if word not in invertedIndex:
                    invertedIndex[word] = {}
                if documentID not in invertedIndex[word]:
                    invertedIndex[word][documentID] = 0
                invertedIndex[word][documentID] += 1

    return dict(invertedIndex)