from core.document_factory import DocumentFactory
from core.vector import Vector
from engine.indexer import Indexer
from engine.query_processor import QueryProcessor
from engine.search_engine import SearchEngine
from collections import Counter

def main():
    indexer = Indexer()
    qp = QueryProcessor()
    engine = SearchEngine(indexer, qp)

    # sample documents
    sample_docs = [
        ("text", 1, "The quick brown fox jumps over the lazy dog"),
        ("text", 2, "A fast brown fox leaps over a sleepy dog"),
        ("text", 3, "Machine learning is amazing for search engines"),
        ("pdf", 4, "I2-Unit 3.pdf")
    ]

    # add documents AND assign TF vectors
    for doc_type, doc_id, text in sample_docs:
        doc = DocumentFactory.create_document(doc_type, doc_id, text)
        indexer.add_document(doc)
        # assign raw term frequency vector
        tf = Counter(doc.tokenize())
        doc.vector_representation = Vector(tf) 
    
    print("Simple Search Engine (Type 'quit' to exit)")
    while True:
        query = input("\nEnter search query: ").strip()
        if query.lower() == 'quit':
            break
        if not query:
            print("Empty query.")
            continue

        results = engine.search(query, top_k=3)
        if results:
            print(f"Top results: {results}")
        else:
            print("No matching documents found.")

if __name__ == "__main__":
    main()