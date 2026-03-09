# Assignment 2: CSI4107

## Team Members

- Name: Yahya Osman  | Student Number: 30024009
- Name: Kevin Govier | Student Number: 300282040
- Name: Emily Cheng | Student Number: 300299745

## Task Division

- Yanya Osamn: [Task]
- Kevin Govier: [Task]
- Emily Cheng: Results and Evaluation

## Program Functionality

### Neural Model 1 (Sentence Transformer (SBERT): all-MiniLM-L6-v2)

[Details]

### Neural Model 2 (Cross-Encoder BERT: ms-marco-MiniLM-L-6-v2)

[Details]

### Results Generation

[Details]

## How to Run

- Environment setup:
  - Python 3.11+ recommended
  - If you cannot install `sentence-transformers` system-wide, use a virtual environment:
    - `python3 -m venv Assignment-2/.venv`
    - `source Assignment-2/.venv/bin/activate`
    - `python -m pip install --upgrade pip`
    - `python -m pip install sentence-transformers`
- Run commands:
  - `python Assignment-2/main.py > Assignment-2/RESULTS.txt`
- Output:
  - Results file path: `Assignment-2/RESULTS.txt`
  - Note: each run overwrites `Assignment-2/RESULTS.txt`
  - Note: only queries listed in `Assignment-2/qrels/test.tsv` are processed

## Algorithms, Data Structures, and Optimizations

[Details]

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
