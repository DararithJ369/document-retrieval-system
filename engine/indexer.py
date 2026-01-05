from collections import defaultdict

class Indexer:
    def __init__(self):
        self.inverted_index = defaultdict(set)  # word -> {doc_id1, doc_id2, ...}
        self.documents = {}                     # doc_id -> Documents
        
    def add_document(self, doc):
        self.documents[doc.id] = doc
        tokens = doc.tokenize()
        for token in set(tokens):               # use set to avoid duplicate entires per doc
            self.inverted_index[token].add(doc.id)
            
    def remove_document(self, doc_id):
        if doc_id not in self.documents:
            return 
        doc = self.documents.pop(doc_id)
        tokens = doc.tokenize()
        for token in set(tokens):
            self.inverted_index[token].discard(doc_id)
            if not self.inverted_index[token]:
                del self.inverted_index[token]
                
    def get_documents(self, word):
        return list(self.inverted_index.get(word, []))