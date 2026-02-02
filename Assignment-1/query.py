import math
from collections import Counter, defaultdict
from typing import Dict, DefaultDict, List, Optional, Set, Tuple

from preprocessing import preprocess

InvertedIndex = Dict[str, Dict[str, int]]
DocNorms = Dict[str, float]


def _collect_doc_ids(inverted_index: InvertedIndex) -> Set[str]:
    doc_ids: Set[str] = set()
    for postings in inverted_index.values():
        doc_ids.update(postings.keys())
    return doc_ids


def _compute_idf(doc_count: int, doc_freq: int) -> float:
    return math.log((doc_count + 1) / (doc_freq + 1)) + 1


def _compute_doc_norms(inverted_index: InvertedIndex, doc_count: int) -> DocNorms:
    doc_norms: DefaultDict[str, float] = defaultdict(float)

    # Build full document vector norms using tf-idf weights.
    for term, postings in inverted_index.items():
        doc_freq = len(postings)
        idf = _compute_idf(doc_count, doc_freq)

        for doc_id, tf in postings.items():
            weight = tf * idf
            doc_norms[doc_id] += weight * weight

    for doc_id in list(doc_norms.keys()):
        doc_norms[doc_id] = math.sqrt(doc_norms[doc_id])

    return dict(doc_norms)




def queryData(
    inverted_index: InvertedIndex,
    query: str,
    stop_words: Set[str],
    stem: bool = False,
    doc_norms: Optional[DocNorms] = None,
) -> List[Tuple[str, float]]:
    # Preprocess the raw query text using the same pipeline as the documents.
    tokens = preprocess(query, stop_words, stem=stem)
    if not tokens:
        return []

    query_tf = Counter(tokens)

    # Compute corpus size and document norms if not provided.
    if doc_norms is None:
        doc_ids = _collect_doc_ids(inverted_index)
        doc_count = len(doc_ids)
        doc_norms = _compute_doc_norms(inverted_index, doc_count)
    else:
        doc_count = len(doc_norms)

    # Compute cosine similarity between the query and candidate documents.
    scores: DefaultDict[str, float] = defaultdict(float)
    query_norm_sq = 0.0

    for term, tfq in query_tf.items():
        if term not in inverted_index:
            continue

        postings = inverted_index[term]
        doc_freq = len(postings)
        idf = _compute_idf(doc_count, doc_freq)
        wq = tfq * idf
        query_norm_sq += wq * wq

        # Accumulate dot product for documents containing this term.
        for doc_id, tf in postings.items():
            wd = tf * idf
            scores[doc_id] += wq * wd

    query_norm = math.sqrt(query_norm_sq)
    if query_norm == 0.0:
        return []

    # Normalize by the document norms to get cosine similarity.
    ranked: List[Tuple[str, float]] = []
    for doc_id, dot in scores.items():
        denom = query_norm * doc_norms.get(doc_id, 0.0)
        if denom:
            ranked.append((doc_id, dot / denom))

    ranked.sort(key=lambda item: item[1], reverse=True)
    return ranked
