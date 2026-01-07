from .document import TextDocument, PDFDocument

class DocumentFactory:
    """
    Factory class that creates document instances based on type.
    Implements the Factory Method design pattern.
    """
    
    @staticmethod
    def create_document(doc_type: str, doc_id, content: str):
        """
        Creates a document of the specified type.
        
        Args:
            doc_type (str): Type of document ('text' or 'pdf')
            doc_id: Unique identifier (int or str)
            content (str): 
                - For 'text': raw text string
                - For 'pdf': either raw text (for simulation) OR a path to a .pdf file
                
        Returns:
            Document: Instance of TextDocument or PDFDocument
            
        Raises:
            ValueError: If doc_type is unsupported or PDF file is invalid
        """
        doc_type = doc_type.lower().strip()
        if doc_type == 'text':
            return TextDocument(doc_id, content)
        elif doc_type == 'pdf':
            return PDFDocument(doc_id, content)
        else:
            raise ValueError(f"Unsupported document type: '{doc_type}'. Use 'text' or 'pdf'.")