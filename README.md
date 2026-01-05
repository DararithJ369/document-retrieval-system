# Document Retrieval System (Simple Search Engine)

A modular, object-oriented search engine built in Python to demonstrate core software engineering principles and information retrieval fundamentals.

## Features
- **Inverted index** for fast document lookup
- **Cosine similarity ranking** using custom vector implementation
- Support for multiple document types (`TextDocument`, `PDFDocument`)
- Clean, extensible architecture using **Composition**, **Factory Method**, and **Custom Data Structures**
- TF (Term Frequency) based vector representation *(extendable to TF-IDF)*


## How to Run

### Prerequisites
- Python 3.8+
- (Optional) Virtual environment

### Steps
1. Clone or navigate to the project directory:
   ```bash
   cd Document Retrieval System
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .env
   source .env/bin/activate  # On macOS/Linux
   ```
3. Run the search engine:
   ```bash
   python main.py
   ```
4. Try queries like:
- brown fox
- machine learning
- Type quit to exit.