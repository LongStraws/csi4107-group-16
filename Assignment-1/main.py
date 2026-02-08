from json import loads
from indexing import build_inverted_index
from preprocessing import load_stopwords
from query import queryData
from typing import List, Tuple


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


def main():
    stop_words = load_stopwords()
    inverted_index = build_inverted_index("corpus.jsonl", stop_words)
    """print("Vocab Size:", len(inverted_index)) #To get vocab count and 100 token
    sample_tokens = list(inverted_index.keys())[:100]
    print(sample_tokens)"""
    run_name = prompt_non_empty("Enter run name: ")
    test_query_ids = load_test_query_ids("qrels/test.tsv")
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

                # Output in TREC format for top-100 results.
                for rank, (doc_id, score) in enumerate(
                    ranked_results[:100], start=1
                ):
                    results_file.write(
                        f"{query_id} Q0 {doc_id} {rank} {score:.6f} {run_name}\n"
                    )


if __name__ == "__main__":
    main()
