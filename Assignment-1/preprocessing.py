import re
from typing import List, Set
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def load_stopwords(file_path: str = "List of Stopwords.html") -> Set[str]:
    with open(file_path, encoding="utf-8") as file:
        content = file.read()
    content = re.sub(r"<[^>]+>", "", content)
    return set(word.strip() for word in content.splitlines() if word.strip())


def preprocess(text: str, stop_words: Set[str], stem: bool = False) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)

    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]

    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(word) for word in tokens]

    return tokens
