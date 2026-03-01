#Need to pip install sentence-transformers

from sentence_transformers import CrossEncoder
import numpy as np

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docTexts, docIDs):

    #Gets query-document pairs for the cross encoder BERT and sorts the results by descending score
    inputs = [(query, docTexts[docID]) for docID in docIDs]
    scores = model.predict(inputs)
    ranked = [docIDs[i] for i in np.argsort(-scores)]

    return ranked