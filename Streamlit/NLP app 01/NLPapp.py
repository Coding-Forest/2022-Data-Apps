# Adopted from code authored by - https://github.com/Jcharis/Streamlit_DataScience_Apps/blob/master/NLP_App_with_Streamlit_Python/app.py
# followed the tutorial by - JCharisTech (2019) Building a NLP App with Streamlit,Spacy and Python (NER,Sentiment Analyser,Summarizer) https://www.youtube.com/watch?v=6acv9LL6gHg&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU&index=4

import streamlit as st

# NLP packages
import spacy
from textblob import TextBlob
import gensim
#from gensim.summarization import summarize      # requires roll-back to gensim==3.8.3

# Sumy packages
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
#from sumy.parsers.plaintext import PlaintextParser      # ImportError: cannot import name 'Sequence' from 'collections'

#in _run_script exec(code, module.__dict__)
# in <module> from sumy.parsers.plaintext import PlaintextParser
# in <module> from ..models.dom import ObjectDocumentModel, Paragraph, Sentence
# in <module> from .tf import TfDocumentModel
# in <module> from collections import Sequence


def lemmatise(input_text):
    # Create an nlp object and load the user input text into it.
    nlp = spacy.load('en_core_web_sm')
    docs = nlp(input_text)
    # tokens = [token.text for token in docs]
    lemma = [('Tokens: {}, \nLemma: {}'.format(token.text, token.lemma_)) for token in docs]
    return lemma


def identify_entity(input_text):
    nlp = spacy.load('en_core_web_sm')
    docs = nlp(input_text)

    tokens = [token.text for token in docs]
    entities = [(entity.text, entity.label_) for entity in docs.ents]
    data = ['Tokens: {},\nEntities:{}'.format(tokens, entities)]
    return data

# Summary Function
def sumy_summarise(text):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    ls = LexRankSummarizer()
    summary = ls(parser.document, 3)
    summary_list = [str(sent) for sent in summary]
    result = ' '.join(summary_list)
    return result



def main():
    """NLP App with Streamlit"""
    st.title("""Simple NLP APP""")
    st.subheader('Natural Language Processing on the go')

    # Tokenisation
    if st.checkbox('Show tokens and lemma'):
        st.subheader('Tokenise text')
        text_input = st.text_area('Enter text', 'Type here')
        if st.button('Analyse'):
            result = lemmatise(text_input)
            st.json(result)

    # Named entity
    if st.checkbox('Show named entities'):
        st.subheader('Exstract entities from input text')
        text_input = st.text_area('Enter text', 'Type here')
        if st.button('Extract'):
            result = identify_entity(text_input)
            st.json(result)


    # Sentiment Analsysis
    if st.checkbox('Analyse sentiment'):
        st.subheader('See how your text feels')
        text_input = st.text_area('Enter text', 'Type here')
        if st.button('Analyse'):
            blob = TextBlob(text_input)
            result = blob.sentiment
            st.success(result)


if __name__ == '__main__':
    main()


"""
    # Text Summarisation
    if st.checkbox('Summarise text'):
        st.subheader('See what your text is trying to say')
        text_input = st.text_area('Enter text', 'Type here')

        if st.button('Summarise'):
            st.text('Using Summy')
            summary = sumy_summarise(text_input)
            st.success(summary)

        summary_options = st.selectbox('Choose a summary engine', ('gensim', 'sumy'))

        if st.button('Summarise'):
            if summary_options == 'gensim':
                st.text('Using Gensim')
                summary = summarise(text_input)

            else:
                st.warning('Using Default Summarizer')
                summary = summarise(text_input)
"""
