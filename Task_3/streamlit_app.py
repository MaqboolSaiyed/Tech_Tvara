import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import PyPDF2
import io
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="E5 Model Similarity Test",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the E5 model
@st.cache_resource
def load_model():
    """Load the E5-small-v2 model"""
    try:
        model = SentenceTransformer('intfloat/e5-small-v2')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    """Extract text content from uploaded PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return ""

# Function to split text into chunks
def split_text_into_chunks(text, chunk_size=512, overlap=50):
    """Split text into overlapping chunks for better similarity analysis"""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk.strip())
    
    return chunks

# Function to compute similarities
def compute_similarities(model, query_text, document_chunks):
    """Compute cosine similarities between query and document chunks"""
    try:
        # Encode query and document chunks
        query_embedding = model.encode([query_text])
        doc_embeddings = model.encode(document_chunks)
        
        # Compute cosine similarities
        similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
        
        return similarities
    except Exception as e:
        st.error(f"Error computing similarities: {e}")
        return None

# Main app
def main():
    st.title("🔍 E5 Model Similarity Test")
    st.markdown("Test semantic similarity using the **intfloat/e5-small-v2** model with your PDF documents")
    
    # Load model
    with st.spinner("Loading E5 model..."):
        model = load_model()
    
    if model is None:
        st.stop()
    
    st.success("✅ E5 model loaded successfully!")
    
    # Sidebar for input
    st.sidebar.header("📄 Document Upload")
    
    # File upload
    uploaded_file = st.sidebar.file_uploader(
        "Upload a PDF file",
        type=['pdf'],
        help="Upload a PDF file to test similarity against"
    )
    
    # Query input
    st.sidebar.header("🔍 Query Input")
    query_text = st.sidebar.text_area(
        "Enter your query text:",
        placeholder="Enter the text you want to find similarities for...",
        height=100
    )
    
    # Parameters
    st.sidebar.header("⚙️ Parameters")
    chunk_size = st.sidebar.slider("Chunk Size", 100, 1000, 512, 50)
    overlap = st.sidebar.slider("Overlap", 10, 200, 50, 10)
    top_k = st.sidebar.slider("Top K Results", 1, 20, 5, 1)
    
    # Main content area
    if uploaded_file is not None and query_text.strip():
        
        # Extract text from PDF
        with st.spinner("Extracting text from PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
        
        if pdf_text:
            st.success(f"✅ Extracted {len(pdf_text)} characters from PDF")
            
            # Split into chunks
            with st.spinner("Processing document chunks..."):
                chunks = split_text_into_chunks(pdf_text, chunk_size, overlap)
            
            st.info(f"📊 Document split into {len(chunks)} chunks")
            
            # Compute similarities
            with st.spinner("Computing similarities..."):
                similarities = compute_similarities(model, query_text, chunks)
            
            if similarities is not None:
                # Create results dataframe
                results_df = pd.DataFrame({
                    'Chunk': range(len(chunks)),
                    'Similarity': similarities,
                    'Text': [chunk[:200] + "..." if len(chunk) > 200 else chunk for chunk in chunks]
                })
                
                # Sort by similarity
                results_df = results_df.sort_values('Similarity', ascending=False)
                
                # Display top results
                st.header("🎯 Top Similarity Results")
                
                # Create two columns for results and visualization
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    # Display top results
                    for i, (_, row) in enumerate(results_df.head(top_k).iterrows()):
                        with st.expander(f"Rank {i+1} - Similarity: {row['Similarity']:.4f}"):
                            st.write(f"**Chunk {row['Chunk']}:**")
                            st.write(chunks[row['Chunk']])
                
                with col2:
                    # Similarity distribution plot
                    fig = px.histogram(
                        results_df, 
                        x='Similarity', 
                        nbins=20,
                        title="Similarity Distribution",
                        labels={'Similarity': 'Cosine Similarity', 'count': 'Number of Chunks'}
                    )
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                
                # Top similarities bar chart
                st.header("📊 Top Similarities")
                top_results = results_df.head(10)
                
                fig = px.bar(
                    top_results,
                    x='Similarity',
                    y='Chunk',
                    orientation='h',
                    title="Top 10 Most Similar Chunks",
                    labels={'Similarity': 'Cosine Similarity', 'Chunk': 'Chunk Index'}
                )
                fig.update_layout(height=500)
                st.plotly_chart(fig, use_container_width=True)
                
                # Statistics
                st.header("📈 Statistics")
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Max Similarity", f"{similarities.max():.4f}")
                
                with col2:
                    st.metric("Mean Similarity", f"{similarities.mean():.4f}")
                
                with col3:
                    st.metric("Min Similarity", f"{similarities.min():.4f}")
                
                with col4:
                    st.metric("Std Deviation", f"{similarities.std():.4f}")
                
                # Download results
                st.header("💾 Download Results")
                csv = results_df.to_csv(index=False)
                st.download_button(
                    label="Download Results as CSV",
                    data=csv,
                    file_name="similarity_results.csv",
                    mime="text/csv"
                )
        
        else:
            st.error("❌ Could not extract text from PDF. Please check the file format.")
    
    elif uploaded_file is None:
        st.info("👆 Please upload a PDF file to get started")
    
    elif not query_text.strip():
        st.info("👆 Please enter a query text to search for similarities")
    
    # Instructions
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📖 Instructions")
    st.sidebar.markdown("""
    1. Upload a PDF file using the file uploader
    2. Enter your query text in the text area
    3. Adjust parameters if needed
    4. View similarity results and visualizations
    5. Download results as CSV if needed
    """)
    
    # Model info
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🤖 Model Information")
    st.sidebar.markdown("""
    **Model:** intfloat/e5-small-v2
    **Type:** Sentence Transformer
    **Purpose:** Semantic similarity and embedding generation
    **Max Sequence Length:** 512 tokens
    """)

if __name__ == "__main__":
    main()