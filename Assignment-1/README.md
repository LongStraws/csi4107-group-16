# Assignment 1: CSI4107

## Team Members

- Name: Yahya Osman  | Student Number: 30024009
- Name: Kevin Govier | Student Number: [STUDENT NUMBER]
- Name: Emily Cheng | Student Number: [STUDENT NUMBER]

## Task Division

- [NAME]: [STEP(S) OR TASKS]
- [NAME]: [STEP(S) OR TASKS]

## Program Functionality

- [DESCRIBE PREPROCESSING MODULE]
- [DESCRIBE INDEXING MODULE]
- [DESCRIBE RETRIEVAL/RANKING MODULE]
- [DESCRIBE OUTPUT FORMAT AND RESULTS GENERATION]

## How to Run

- Environment setup:
  - Python 3.11+ recommended
  - If you cannot install `nltk` system-wide, use a virtual environment:
    - `python3 -m venv Assignment-1/.venv`
    - `source Assignment-1/.venv/bin/activate`
    - `python -m pip install --upgrade pip`
    - `python -m pip install nltk`
  - NLTK data downloads:
    - `python -c "import nltk; nltk.download('punkt')"`
    - `python -c "import nltk; nltk.download('punkt_tab')"`
- Run commands:
  - `python Assignment-1/main.py > Assignment-1/RESULTS.txt`
- Output:
  - Results file path: `Assignment-1/RESULTS.txt`
  - Note: each run overwrites `Assignment-1/RESULTS.txt`
  - Note: only queries listed in `Assignment-1/qrels/test.tsv` are processed

## Algorithms, Data Structures, and Optimizations

### Step 1: Preprocessing

- [TOKENIZATION DETAILS]
- [STOPWORD REMOVAL DETAILS]
- [STEMMING OPTIONAL DETAILS]
- [REGEX / NORMALIZATION DETAILS]

### Step 2: Indexing

- [INVERTED INDEX STRUCTURE]
- [TERM FREQUENCY STORAGE]
- [ANY OPTIMIZATIONS]

### Step 3: Retrieval and Ranking

- [CANDIDATE DOCUMENT SELECTION]
- [TF-IDF WEIGHTING]
- [COSINE SIMILARITY]
- [ANY OPTIMIZATIONS]

## Vocabulary Statistics

- Vocabulary size: [NUMBER]
- Sample 100 tokens: [PASTE 100 TOKENS HERE]

## Results (Qualitative)

- First 10 answers for Query 1:
  - [DOC_ID 1] [SCORE]
  - [DOC_ID 2] [SCORE]
  - [DOC_ID 3] [SCORE]
  - [DOC_ID 4] [SCORE]
  - [DOC_ID 5] [SCORE]
  - [DOC_ID 6] [SCORE]
  - [DOC_ID 7] [SCORE]
  - [DOC_ID 8] [SCORE]
  - [DOC_ID 9] [SCORE]
  - [DOC_ID 10] [SCORE]

- First 10 answers for Query 2:
  - [DOC_ID 1] [SCORE]
  - [DOC_ID 2] [SCORE]
  - [DOC_ID 3] [SCORE]
  - [DOC_ID 4] [SCORE]
  - [DOC_ID 5] [SCORE]
  - [DOC_ID 6] [SCORE]
  - [DOC_ID 7] [SCORE]
  - [DOC_ID 8] [SCORE]
  - [DOC_ID 9] [SCORE]
  - [DOC_ID 10] [SCORE]

## Evaluation

- trec_eval command used: [COMMAND]
- MAP score: [VALUE]

## Discussion

- [DISCUSS PERFORMANCE, ERROR CASES, AND OBSERVATIONS]
