import json
from collections import defaultdict
from typing import DefaultDict, Dict, Set

from preprocessing import preprocess

InvertedIndex = Dict[str, Dict[str, int]]


def build_inverted_index(
    corpus_path: str,
    stop_words: Set[str],
    stem: bool = False,
) -> InvertedIndex:
    inverted_index: DefaultDict[str, DefaultDict[str, int]] = defaultdict(
        lambda: defaultdict(int)
    )

    with open(corpus_path, "r", encoding="utf-8") as file:
        for line in file:
            data = json.loads(line)
            text = data["title"] + " " + data["text"]
            tokens = preprocess(text, stop_words, stem=stem)
            document_id = data["_id"]

            for word in tokens:
                inverted_index[word][document_id] += 1

    return dict(inverted_index)
