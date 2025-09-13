# Gemini API Interface

A simple Streamlit-based interface to interact with Google's Gemini AI model. This application provides an easy way to test and experiment with the Gemini API.

## Features

- 🤖 **Multiple Models**: Support for different Gemini models (gemini-pro, gemini-pro-vision)
- 🔍 **Raw Payload Inspection**: Option to view the raw API response for debugging
- 🔐 **Secure API Key Handling**: Environment variable support and password input
- 📱 **Responsive Design**: Clean, modern interface built with Streamlit
- 🚀 **Easy Setup**: Simple installation and configuration

## Prerequisites

- Python 3.7 or higher
- A Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Installation

1. **Clone or download this project**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key** (choose one method):
   
   **Method 1: Environment file (Recommended)**
   - Create a `.env` file in the Task_2 directory
   - Add your API key: `GEMINI_API_KEY=your_actual_api_key_here`
   
   **Method 2: Direct input**
   - Run the app and enter your API key in the sidebar

## Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Configure the API**:
   - Enter your Gemini API key in the sidebar
   - Select your preferred model
   - Click "Initialize API"

3. **Start chatting**:
   - Type your prompt in the text area
   - Click "Generate Response"
   - View the AI-generated response

4. **Debug (Optional)**:
   - Enable "Show Raw Payload" to inspect the full API response
   - Useful for understanding the response structure

## Configuration Options

- **Model Selection**: Choose between different Gemini models
- **Raw Payload**: Toggle to see the complete API response object
- **API Key**: Secure input with environment variable support

## Example Prompts

- "Explain quantum computing in simple terms"
- "Write a Python function to sort a list"
- "What are the benefits of renewable energy?"
- "Create a recipe for chocolate chip cookies"

## File Structure

```
Task_2/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── env_example.txt     # Example environment file
└── README.md          # This file
```

## Troubleshooting

- **API Key Issues**: Ensure your API key is valid and has proper permissions
- **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
- **Connection Issues**: Check your internet connection and API key validity

## Security Notes

- Never commit your actual API key to version control
- Use environment variables for production deployments
- The `.env` file is typically ignored by git (add it to `.gitignore`)

## License

This project is for educational and development purposes. Please ensure you comply with Google's Gemini API terms of service.