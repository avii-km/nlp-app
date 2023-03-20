import streamlit as st 
from time import sleep
from stqdm import stqdm
import pandas as pd
from transformers import pipeline
import json
import spacy
import spacy_streamlit


def draw_all( key, plot=False,):
    
    st.write(
        """
        # this is NLP basedWeb App
        
        This Natural Language Processing Based Web App can do anything u can imagine with Text. 😱 
        
        This App is built using pretrained transformers which are capable of doing wonders with the Textual data.
        
        ```python
        # Key Features of this App.
        1. Advanced Text Summarizer
        2. Named Entity Recognition
        3. Sentiment Analysis
        4. Question Answering
        5. Text Completion
       
        ```
        """
    )

    

with st.sidebar:
    draw_all("sidebar")



def main():
    st.title("NLP Web App")
    
  

if __name__ == '__main__':
	main()
