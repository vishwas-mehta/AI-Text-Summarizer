# 🤖 AI Text Summarizer

An AI-powered text summarization tool that uses Large Language Models to generate concise summaries from any text input.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- **Simple Interface**: Clean, user-friendly web interface
- **AI-Powered**: Uses Facebook's BART model for accurate summarization
- **Fast Processing**: Get summaries in seconds
- **Input Validation**: Handles edge cases gracefully
- **Error Handling**: Comprehensive error messages

## 🛠️ Tech Stack

- **Python 3.8+** - Programming language
- **Streamlit** - Web framework
- **Hugging Face Inference API** - AI/ML backend
- **BART-large-CNN** - Summarization model

## 📖 How It Works

```
User Input → Validation → API Request → AI Processing → Summary Output
```

1. User enters text in the input area
2. Backend validates and sends the text to Hugging Face API
3. BART model processes and summarizes the content
4. Summary is displayed with a clean UI

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Hugging Face API key (free)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishwas-mehta/AI-Text-Summarizer.git
   cd AI-Text-Summarizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your Hugging Face API key.

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:8501`

## 🔑 Getting Your API Key

1. Go to [Hugging Face](https://huggingface.co/settings/tokens)
2. Sign up or log in
3. Create a new token (read access is sufficient)
4. Copy the token to your `.env` file

## 📁 Project Structure

```
AI-Text-Summarizer/
├── app.py              # Main Streamlit application
├── summarizer.py       # Summarization logic
├── utils.py            # Utility functions
├── config.py           # Configuration management
├── constants.py        # Application constants
├── validators.py       # Input validation
├── exceptions.py       # Custom exceptions
├── logger.py           # Logging configuration
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── .gitignore          # Git ignore rules
├── CONTRIBUTING.md     # Contribution guidelines
├── SECURITY.md         # Security policy
├── LICENSE             # MIT License
└── README.md           # Documentation
```

## 🎯 Use Cases

- Summarize articles and blog posts
- Condense research papers
- Quick overview of long documents
- Meeting notes summary
- Email digest creation

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📝 License

This project is licensed under the MIT License.

---

*Built with ❤️ using Python and Streamlit | Powered by Hugging Face 🤗*
