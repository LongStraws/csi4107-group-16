# Assignment 2: CSI4107

## Team Members

- Name: Yahya Osman  | Student Number: 30024009
- Name: Kevin Govier | Student Number: 300282040
- Name: Emily Cheng | Student Number: 300299745

## Task Division

- Yahya Osman: README/report writing and submission preparation.
- Kevin Govier: neural model setup and integration (SBERT + Cross-Encoder).
- Emily Cheng: Results and Evaluation

## Program Functionality

### Neural Model 1 (Sentence Transformer (SBERT): all-MiniLM-L6-v2)

We use a bi-encoder SBERT model to generate dense embeddings for the query and each candidate document. Cosine similarity is computed between the query embedding and each document embedding, and the candidates are re-ranked by descending similarity.

### Neural Model 2 (Cross-Encoder BERT: ms-marco-MiniLM-L-6-v2)

We use a Cross-Encoder BERT model that scores each (query, document) pair directly. The model outputs a relevance score for each candidate, and the documents are re-ranked by descending score.

### Results Generation

We first retrieve candidate documents using TF-IDF cosine similarity over an inverted index. For each test query, we take the top-100 candidates and apply a neural re-ranker (SBERT or Cross-Encoder). The final ranking is written in TREC format.

## How to Run

- Environment setup:
  - Python 3.11+ recommended
  - If you cannot install `sentence-transformers` system-wide, use a virtual environment:
    - `python3 -m venv Assignment-2/.venv`
    - `source Assignment-2/.venv/bin/activate`
    - `python -m pip install --upgrade pip`
    - `python -m pip install sentence-transformers`
- Run commands:
  - `python3 main.py`
  - Enter a run name when prompted (used in the output file)
- Output:
  - Results file path: `RESULTS.txt`
  - Note: each run overwrites `RESULTS.txt`
  - Note: only queries listed in `qrels/test.tsv` are processed
  - Note: for submission, rename `RESULTS.txt` to `Results` if required

## Algorithms, Data Structures, and Optimizations

Preprocessing and Indexing
- Lowercase, remove non-alphabetic characters, tokenize with NLTK, remove stopwords from `List of Stopwords.html`.
- Build an inverted index mapping term -> {doc_id: tf}.

Retrieval (TF-IDF)
- Weighting: tf-idf with `IDF = log((N+1)/(df+1)) + 1`.
- Similarity: cosine similarity between query vector and document vectors.
- Candidate set: documents containing at least one query term.

Neural Re-ranking
- SBERT bi-encoder: cosine similarity between query and document embeddings.
- Cross-Encoder: direct relevance scoring for each (query, document) pair.

## Results
### SBERT
First 10 answers for Query 1:
    [doc_id] [score]
-   17388232    1
-   803312      2
-   8891333     3
-   25404036    4
-   10628767    5
-   6863070     6
-   40212412    7
-   43385013    8
-   10607877    9
-   16939583    10

First 10 answers for Query 3:
    [doc_id] [score]
-   2739854     1
-   23389795    2
-   14717500    3
-   19058822    4
-   13914198    5
-   4632921     6
-   32181055    7
-   13519661    8
-   1388704     9
-   4378885     10

### Cross-Encoder BERT
First 10 answers for Query 1:
    [doc_id] [score]
-   43385013    1
-   37437064    2
-   121581019   3
-   6863070     4
-   4459491     5
-   36637129    6
-   10906636    7
-   10608397    8
-   17518195    9
-   27049238    10

First 10 answers for Query 3:
    [doc_id] [score]
-   14717500    1
-   4414547     2
-   2739854     3
-   4632921     4
-   19058822    5
-   23389795    6
-   4378885     7
-   1388704     8
-   13519661    9
-   2107238     10

## Evaluation

### SBERT

MAP score for SBERT is 0.6093

P@10 score for SBERT is 0.0893

### Cross-Encoder BERT

MAP score for Cross-Encoder BERT is 0.6492

P@10 score for Cross-Encoder BERT is 0.0900

The best method is Cross-Encoder BERT with a 0.6492 MAP score and a P@10 score of 0.0900. 

The MAP score for the TF-IDF method was 0.5300. Both SBERT and Cross-Encoder BERT have improvement over the TF-IDF system.

## Discussion
The Cross-Encoder BERT re-ranking achieved the best MAP and P@10, improving on both SBERT and the TF-IDF baseline. SBERT provides a faster re-rank due to independent embeddings, while the Cross-Encoder is slower but more accurate because it models query-document interactions directly. Overall, the neural re-rankers provided meaningful gains over the classical TF-IDF system.
