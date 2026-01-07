from abc import ABC, abstractmethod
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
import os
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
    def __init__(self, doc_id, content_or_path: str):
        """
        Initialize PDFDocument.
        - If `content_or_path` is a string ending with '.pdf' and points to an existing file,
          it will be treated as a file path and text will be extracted.
        - Otherwise, it's treated as raw text (for testing/demo).
        """
        if (isinstance(content_or_path, str) and 
            content_or_path.lower().endswith('.pdf') and 
            os.path.isfile(content_or_path)):
            # Real PDF file → extract text
            self.file_path = content_or_path
            extracted_text = self._extract_text_from_pdf(content_or_path)
            super().__init__(doc_id, extracted_text)
        else:
            # Simulated PDF (raw string)
            super().__init__(doc_id, content_or_path)

    def _extract_text_from_pdf(self, file_path: str) -> str:
        """Extract text from a real PDF file."""
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
            return text.strip()
        except PdfReadError as e:
            raise ValueError(f"Invalid or encrypted PDF: {file_path} ({e})")
        except Exception as e:
            raise ValueError(f"Failed to read PDF '{file_path}': {e}")

    def tokenize(self):
        return re.findall(r'\b\w+\b', self.text.lower())