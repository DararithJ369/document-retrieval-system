import re

class QueryProcessor:
    # optional: define stop words
    STOPWORDS = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for"}
    
    @staticmethod
    def process(query):
        tokens = re.findall(r'\b\w+\b', query.lower())
        # uncomment below to enable stop words removal
        # tokens = [t for t in tokens if t not in QsueryProcessor.STOPWORDS]
        return tokens