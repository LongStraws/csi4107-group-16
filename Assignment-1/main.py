from indexing import build_inverted_index
from preprocessing import load_stopwords
from query import queryData
from typing import List, Tuple


def prompt_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def main():
    stop_words = load_stopwords()
    inverted_index = build_inverted_index("corpus.jsonl", stop_words)
    query_text = prompt_non_empty("Enter a query: ")
    ranked_results: List[Tuple[str, float]] = queryData(
        inverted_index, query_text, stop_words
    )

    # Temporary output for quick inspection (top 10).
    for doc_id, score in ranked_results[:10]:
        print(doc_id, score)


if __name__ == "__main__":
    main()
