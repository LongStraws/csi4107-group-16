#Need to pip install sentence-transformers

from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def rerank(query, docTexts, docIDs):

    docs = [docTexts(id) for id in docIDs]

    docEmbeddings = model.encode(docs)
    queryEmbeddings = model.encode(query)
    scores = util.cos_sim(queryEmbeddings, docEmbeddings)[0].numpy()

    ranked = [docIDs[i] for i in np.argsort(-scores)]        
    
    return ranked