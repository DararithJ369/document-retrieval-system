from core.vector import Vector
from collections import Counter

class SearchEngine:
    def __init__(self, indexer, query_processor):
        self.indexer = indexer
        self.query_processor = query_processor
        
    def search(self, query, top_k=5):
        if not query or not query.strip():
            return []
        
        tokens = self.query_processor.process(query)
        if not tokens:
            return []
        
        # get candidate docs (union of all terms)
        candidate_ids = set()
        for token in tokens:
            candidate_ids.update(self.indexer.inverted_index.get(token, []))
            
        if not candidate_ids:
            return []
        
        # build query vector (TF-style; extend to TF-IDF if available)
        query_tf = Counter(tokens)
        query_vec = Vector(query_tf)
        
        # retrieve and rank: rank by cosine similarity
        scored = []
        for doc_id in candidate_ids:
            doc = self.indexer.documents[doc_id]
            if doc.vector_representation is None:
                print(f"Warning: doc {doc_id} has no vector!")
                continue
            sim = doc.vector_representation.cosine_similarity(query_vec)
            scored.append((sim, doc_id))
            
        scored.sort(reverse=True, key=lambda x: x[0])
        return [doc_id for _, doc_id in scored[:top_k]]
            