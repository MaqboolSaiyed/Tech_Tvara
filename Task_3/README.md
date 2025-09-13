# E5 Model Similarity Test

A Streamlit application that uses the **intfloat/e5-small-v2** Hugging Face model with sentence transformers to perform semantic similarity testing on PDF documents.

## 🚀 Features

- **PDF Text Extraction**: Upload and extract text from PDF documents
- **Semantic Similarity**: Use E5 model to find semantically similar text chunks
- **Interactive Interface**: User-friendly Streamlit interface with real-time results
- **Visualization**: Interactive charts and graphs showing similarity distributions
- **Configurable Parameters**: Adjustable chunk size, overlap, and top-k results
- **Export Results**: Download similarity results as CSV files

## 🤖 Model Information

- **Model**: intfloat/e5-small-v2
- **Type**: Sentence Transformer
- **Purpose**: Semantic similarity and embedding generation
- **Max Sequence Length**: 512 tokens
- **Performance**: Optimized for both accuracy and speed

## 📋 Requirements

- Python 3.8+
- Streamlit
- Sentence Transformers
- PyTorch
- PyPDF2
- Pandas
- NumPy
- Scikit-learn
- Plotly

## 🛠️ Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Local Development

Run the Streamlit app locally:
```bash
streamlit run streamlit_app.py
```

## 📖 How to Use

1. **Upload PDF**: Use the file uploader in the sidebar to upload a PDF document
2. **Enter Query**: Type your search query in the text area
3. **Adjust Parameters**: Modify chunk size, overlap, and top-k results as needed
4. **View Results**: Explore similarity results with interactive visualizations
5. **Export Data**: Download results as CSV for further analysis

## 🔧 Parameters

- **Chunk Size**: Size of text chunks for similarity analysis (100-1000 words)
- **Overlap**: Overlap between consecutive chunks (10-200 words)
- **Top K**: Number of top similarity results to display (1-20)

## 📊 Output

The application provides:

- **Similarity Scores**: Cosine similarity scores for each text chunk
- **Ranked Results**: Top-k most similar chunks with full text
- **Visualizations**: Histograms and bar charts of similarity distributions
- **Statistics**: Mean, max, min, and standard deviation of similarities
- **Export**: CSV download of all results

## 🎯 Use Cases

- **Document Search**: Find relevant sections in large documents
- **Content Analysis**: Analyze semantic relationships in text
- **Research**: Identify similar concepts across documents
- **QA Systems**: Build question-answering systems
- **Information Retrieval**: Improve search and retrieval systems

## 🔍 Technical Details

- **Embedding Model**: E5-small-v2 (384-dimensional embeddings)
- **Similarity Metric**: Cosine similarity
- **Text Processing**: Automatic chunking with configurable overlap
- **Visualization**: Interactive Plotly charts
- **Caching**: Model loading is cached for better performance

## 📝 Example Queries

Try these example queries to test the system:

- "What are the main findings?"
- "How does the methodology work?"
- "What are the key recommendations?"
- "Explain the results section"
- "What is the conclusion?"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the E5 model
- [Sentence Transformers](https://www.sbert.net/) for the embedding framework
- [Streamlit](https://streamlit.io/) for the web interface
- [Plotly](https://plotly.com/) for interactive visualizations

---

**Note**: This application is designed for local development and testing with the E5 model for semantic similarity analysis.