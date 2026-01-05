from .document import TextDocument, PDFDocument

class DocumentFactory:
    """
    Factory class that creates document instances based on type.
    Implements the Factory Method design pattern.
    """
    
    @staticmethod
    def create_document(doc_type: str, doc_id, text: str):
        """
        Creates a document of the specified type.
        
        Args:
            doc_type (str): Type of document ('text' or 'pdf')
            doc_id: Unique identifier (int or str)
            text (str): Raw content of the document
            
        Returns:
            Document: Instance of TextDocument or PDFDocument
            
        Raises:
            ValueError: If doc_type is unsupported
        """
        doc_type = doc_type.lower().strip()
        if doc_type == 'text':
            return TextDocument(doc_id, text)
        elif doc_type == 'pdf':
            return PDFDocument(doc_id, text)
        else:
            raise ValueError(f"Unsupported document type: '{doc_type}'. Use 'text' or 'pdf'.")