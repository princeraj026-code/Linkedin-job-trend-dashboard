#!/bin/bash

# Streamlit Cloud Setup Script
# Installs spaCy language model for NLP processing

echo "Installing spaCy English language model..."
python -m spacy download en_core_web_sm

echo "✅ Setup complete!"
