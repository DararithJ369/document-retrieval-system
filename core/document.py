from abc import ABC, abstractmethod
import re

class Document(ABC):
    """
    Abstract base class for all document types.
    Encapsulates common document attributes and behavior.
    """
    def __init__(self, doc_id, text):
        if not isinstance(doc_id, (int, str)):
            raise ValueError("Document ID must be integer or string.")
        self.id = doc_id
        self.text = str(text)
        self.vector_representation = None       # will be set by indexer later
        
    @abstractmethod
    def tokenize(self):
        """
        Tokenize the document text into a list of normalized words.
        Must be implemented by subclasses (though logic is usually shared).
        """
        pass
    

class TextDocument(Document):
    """
    Represents a plain text document.
    """
    def tokenize(self):
        # simple tokenization: lowercases + alphanumerical words
        return re.findall(r'\b\w+\b', self.text.lower())
    

class PDFDocument(Document):
    """
    Simulated PDF document.
    In real system, this would parse PDF content (e.g., with PyPDF2).
    For now, treat input text as extracted content.
    """
    def tokenize(self):
        # same as TextDocument for simulation
        return re.findall(r'\b\w+\b', self.text.lower())