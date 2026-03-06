from json import loads
from indexing import buildInvertedIndex
from preprocessing import getStopwords
from query import queryData
from typing import List, Tuple
import sbert
import cbert


def load_test_query_ids(path: str) -> set[str]:
    query_ids = set()
    with open(path, "r", encoding="utf-8") as file:
        next(file, None)
        for line in file:
            parts = line.strip().split("\t")
            if parts:
                query_ids.add(parts[0])
    return query_ids


def prompt_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def getRerankDocs(corpus):
    docs = {}
    with open(corpus, "r", encoding="utf-8") as file:
        for line in file:
            obj = loads(line)
            docs[obj["_id"]] = obj["title"] + " " + obj["text"]
    return docs


def main():
    stop_words = getStopwords()
    inverted_index = buildInvertedIndex("corpus.jsonl", stop_words)
    run_name = prompt_non_empty("Enter run name: ")
    test_query_ids = load_test_query_ids("qrels/test.tsv")
    
    #RESULTS.txt to get ranking with CrossEncoder
    with open("RESULTS.txt", "w", encoding="utf-8") as results_file:
        with open("queries.jsonl", "r", encoding="utf-8") as file:
            for line in file:
                data = loads(line)
                query_id = data["_id"]
                if query_id not in test_query_ids:
                    continue

                query_text = data["text"]
                ranked_results: List[Tuple[str, float]] = queryData(
                    inverted_index, query_text, stop_words
                )

                #RERANK
                docTexts = getRerankDocs("corpus.jsonl")
                docIDs = [docID for docID, _ in ranked_results[:100]]
                #rerankedResults = sbert.rerank(query_text, docTexts, docIDs)
                rerankedResults = cbert.rerank(query_text, docTexts, docIDs) #better option

                # Output in TREC format for top-100 results.
                for rank, doc_id in enumerate(rerankedResults[:100], start=1):
                    results_file.write(
                        f"{query_id} Q0 {doc_id} {rank} {100-rank} {run_name}\n"
                    )
    
    #Results2.txt to get ranking with SentenceTransformer
    """with open("RESULTS2.txt", "w", encoding="utf-8") as results_file:
        with open("queries.jsonl", "r", encoding="utf-8") as file:
            for line in file:
                data = loads(line)
                query_id = data["_id"]
                if query_id not in test_query_ids:
                    continue

                query_text = data["text"]
                ranked_results: List[Tuple[str, float]] = queryData(
                    inverted_index, query_text, stop_words
                )

                #RERANK
                docTexts = getRerankDocs("corpus.jsonl")
                docIDs = [docID for docID, _ in ranked_results[:100]]
                rerankedResults = sbert.rerank(query_text, docTexts, docIDs)
                #rerankedResults = cbert.rerank(query_text, docTexts, docIDs)

                # Output in TREC format for top-100 results.
                for rank, doc_id in enumerate(rerankedResults[:100], start=1):
                    results_file.write(
                        f"{query_id} Q0 {doc_id} {rank} {100-rank} {run_name}\n"
                    )"""


if __name__ == "__main__":
    main()
