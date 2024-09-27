

# Shyam Lal College FAQ Chatbot

This project is a simple FAQ chatbot built using **Streamlit** and **spaCy** to answer frequently asked questions related to **Shyam Lal College**. The chatbot interface allows users to input questions, and it attempts to find the closest matching question from a predefined FAQ list, providing a relevant answer.

## Features

- **Natural Language Processing (NLP)**: Uses `spaCy` to preprocess user queries (tokenization, stopword removal, etc.).
- **Closest Match Retrieval**: Finds the most relevant question from the FAQ list using `difflib`.
- **User Interface**: Built with **Streamlit**, providing a simple interface to ask questions and receive answers.

## Prerequisites

To run this project, you need the following Python packages installed:

- `streamlit`
- `spacy`
- `difflib` (this is a built-in Python module)
  
You will also need to download the `spaCy` English language model:

```bash
pip install spacy streamlit
python -m spacy download en_core_web_sm
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/faq-chatbot.git
   cd faq-chatbot
   ```

2. **Install dependencies**:

   Run the following command to install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the `spaCy` language model**:

   ```bash
   python -m spacy download en_core_web_sm
   ```

## How to Run the Chatbot

1. Navigate to the project directory.
2. Run the following command to launch the Streamlit application:

   ```bash
   streamlit run chatbot.py
   ```

3. This will open up the chatbot interface in your browser where you can start asking questions about Shyam Lal College.

## FAQ List

Here are some sample questions the chatbot can answer:

- What courses are offered at Shyam Lal College?
- What are the admission criteria?
- Where is Shyam Lal College located?
- What is the fee structure?
- Is there a hostel facility?
- What extracurricular activities are available?
- Who is the principal of Shyam Lal College?
- What are the library timings?

## Code Overview

- **chatbot.py**: This is the main file that contains the Streamlit interface, NLP preprocessing, and matching logic.
  
  - `preprocess_input(query)`: Preprocesses the user query by removing stopwords and punctuation using `spaCy`.
  
  - `find_closest_match(query, faq_dict)`: Matches the processed query to the most relevant FAQ using the `difflib` library.
  
  - `chatbot_interface()`: Creates the Streamlit interface where users can input their questions and see the chatbot's response.

## Future Improvements

- Adding more FAQs to make the chatbot more informative.
- Enhancing the NLP pipeline to handle more complex queries.
- Storing FAQs in a database or external file for easier updates.

## License

This project is licensed under the MIT Licence.
