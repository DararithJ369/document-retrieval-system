from core.document_factory import DocumentFactory

def test_document_creation():
    # test TextDocument
    text_doc = DocumentFactory.create_document("text", 1, "Hello world!")
    assert text_doc.id == 1
    assert text_doc.text == "Hello world!"
    assert text_doc.tokenize() == ["hello", "world"]
    print("TextDocument test passed")

    # test PDFDocument
    pdf_doc = DocumentFactory.create_document("pdf", "doc_2", "PDF content here.")
    assert pdf_doc.id == "doc_2"
    assert pdf_doc.tokenize() == ["pdf", "content", "here"]
    print("PDFDocument test passed")

    # test invalid type
    try:
        DocumentFactory.create_document("docx", 3, "Invalid")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print("Error handling test passed:", str(e))

if __name__ == "__main__":
    test_document_creation()