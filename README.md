
```markdown
# Shyam Lal College FAQ Chatbot

This project is a chatbot application built with Streamlit, spaCy, difflib, and Google's Generative AI API. The chatbot provides answers to frequently asked questions (FAQs) related to Shyam Lal College, University of Delhi. If the user's question is not among the predefined FAQs, the chatbot leverages Google Generative AI to provide a response.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [FAQs](#faqs)
- [Future Improvements](#future-improvements)

## Features

- **FAQ Matching**: The chatbot has a predefined set of FAQs for quick responses.
- **Natural Language Processing**: Uses spaCy for preprocessing user queries to enhance accuracy.
- **Fallback to AI**: If no FAQ match is found, the bot generates a response using Google Gemini's Generative AI.
- **User-Friendly Interface**: Built with Streamlit for an easy-to-use chatbot UI.

## Technologies Used

- **Python**: Programming language for developing the application.
- **Streamlit**: Web app framework to create the chatbot interface.
- **spaCy**: Natural Language Processing (NLP) library for query preprocessing.
- **difflib**: Python library for matching user questions to available FAQ entries.
- **Google Generative AI (Gemini)**: Used for generating responses when no FAQ match is found.

## Setup

### Prerequisites

- Python 3.7 or above
- pip (Python package installer)
- A valid Google Gemini API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shyam-lal-chatbot.git
   cd shyam-lal-chatbot
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file or use the provided `config.env` to store your Gemini API key:
   ```env
   Gemini_Api_Key=YOUR_API_KEY_HERE
   ```

4. Ensure the Spacy language model `en_core_web_sm` is installed:
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Running the Application

To run the Streamlit chatbot:

```bash
streamlit run chatbot.py
```

## Usage

- The chatbot allows you to ask questions related to **Shyam Lal College**.
- Enter your query in the text input field and get either an FAQ-based answer or an AI-generated response.

## FAQs

- **What is Shyam Lal College FAQ Chatbot?**  
  A chatbot built to answer questions related to Shyam Lal College, such as admission criteria, courses offered, and more.

- **What if the bot can't answer my question?**  
  If the bot does not find a matching FAQ, it will generate an answer using Google's Generative AI model.

## Future Improvements

- **Improve Accuracy**: Use more sophisticated deep learning models like BERT for FAQ matching.
- **Visual Enhancements**: Make the UI more engaging using advanced Streamlit components.
- **Add More FAQs**: Expand the FAQ database to cover more common queries.
- **Analytics Dashboard**: Add data visualization using libraries like Matplotlib, Seaborn, or Pandas to understand user questions better.
- **Multilingual Support**: Include more languages using translation APIs to enhance user experience.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

Chaitanya Lohani

Feel free to contribute, report issues, or make suggestions to improve the chatbot!
```
