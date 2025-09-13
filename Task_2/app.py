import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="Gemini API Interface",
    page_icon="🤖",
    layout="wide"
)

# Initialize Gemini API
def initialize_gemini(api_key):
    """Initialize Gemini API with the provided key"""
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"Error initializing Gemini API: {str(e)}")
        return False

# Generate response using Gemini
def generate_response(prompt, model_name="gemini-2.0-flash", show_raw_payload=False):
    """Generate response from Gemini API"""
    try:
        model = genai.GenerativeModel(model_name)
        
        if show_raw_payload:
            # Get raw response for debugging
            response = model.generate_content(prompt)
            return response.text, response
        else:
            # Get just the text response
            response = model.generate_content(prompt)
            return response.text, None
            
    except Exception as e:
        return f"Error generating response: {str(e)}", None

# Main app
def main():
    st.title("🤖 Gemini API Interface")
    st.markdown("A simple interface to interact with Google's Gemini AI model")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            value=os.getenv("GEMINI_API_KEY", ""),
            help="Enter your Gemini API key. You can also set it in a .env file as GEMINI_API_KEY"
        )
        
        
        # Raw payload flag
        show_raw_payload = st.checkbox(
            "Show Raw Payload",
            help="Display the raw response object for debugging purposes"
        )
        
        # Initialize button
        if st.button("Initialize API", type="primary"):
            if api_key:
                if initialize_gemini(api_key):
                    st.success("✅ Gemini API initialized successfully!")
                else:
                    st.error("❌ Failed to initialize Gemini API")
            else:
                st.error("Please enter your API key")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Chat with Gemini")
        
        # Text input for prompt
        prompt = st.text_area(
            "Enter your prompt:",
            height=200,
            placeholder="Ask Gemini anything...",
            help="Type your question or prompt here"
        )
        
        # Generate button
        if st.button("Generate Response", type="primary", disabled=not api_key):
            if prompt.strip():
                with st.spinner("Generating response..."):
                    response_text, raw_response = generate_response(
                        prompt, 
                        "gemini-2.0-flash", 
                        show_raw_payload
                    )
                
                # Display response
                st.subheader("Response:")
                st.write(response_text)
                
                # Show raw payload if requested
                if show_raw_payload and raw_response:
                    with st.expander("Raw Payload"):
                        st.json({
                            "text": raw_response.text,
                            "candidates": [
                                {
                                    "content": {
                                        "parts": [{"text": part.text} for part in raw_response.candidates[0].content.parts],
                                        "role": raw_response.candidates[0].content.role
                                    },
                                    "finish_reason": raw_response.candidates[0].finish_reason
                                }
                            ]
                        })
            else:
                st.warning("Please enter a prompt")
    
    with col2:
        st.header("Instructions")
        st.markdown("""
        ### How to use:
        1. **Get API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to get your Gemini API key
        2. **Enter API Key**: Paste your API key in the sidebar
        3. **Initialize**: Click "Initialize API" to set up the connection
        4. **Ask Questions**: Type your prompt and click "Generate Response"
        
        ### Features:
        - 🤖 Gemini 2.0 Flash model
        - 🔍 Raw payload inspection
        - 🔐 Secure API key handling
        - 📱 Responsive design
        
        ### Tips:
        - You can set your API key in a `.env` file as `GEMINI_API_KEY=your_key`
        - Use "Show Raw Payload" to debug responses
        - Gemini 2.0 Flash provides fast and accurate responses
        """)
        
        # Example prompts
        st.subheader("Example Prompts:")
        example_prompts = [
            "Explain quantum computing in simple terms",
            "Write a Python function to sort a list",
            "What are the benefits of renewable energy?",
            "Create a recipe for chocolate chip cookies"
        ]
        
        for i, example in enumerate(example_prompts):
            if st.button(f"Example {i+1}", key=f"example_{i}"):
                st.session_state.example_prompt = example
        
        # Auto-fill example prompt
        if hasattr(st.session_state, 'example_prompt'):
            st.text_area("Selected Example:", value=st.session_state.example_prompt, height=100)

if __name__ == "__main__":
    main()