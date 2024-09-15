import os
from gtts import gTTS
import streamlit as st

# Function to generate and save speech from text using gTTS
def text_to_speech(text, lang='hi', tld='com'):
    tts = gTTS(text=text, lang=lang, tld=tld)
    tts.save('text_to_speech_gtts.wav')
    return 'text_to_speech_gtts.wav'

# Streamlit app
def main():
    st.title("Naresh Technology Data Science Program")
    st.write("Welcome to the Data Science program under Prakash Senapati's guidance!")

    # Input text
    text = st.text_area("Enter the text you want to convert to speech", 
                        '''Welcome to Naresh Technology Data Science programme under Prakash Senapati guidance. 
                           Classes will help practical exposure to boost up technical skills 
                           and increase learning for coding skills. We conduct this programme for 
                           both non-technical and technical learners. Thank you.''')

    # Language selection
    lang = st.selectbox("Select the language for speech", ('hi', 'en', 'fr', 'es'))

    # Generate speech
    if st.button("Convert to Speech"):
        output_file = text_to_speech(text, lang=lang)
        st.audio(output_file, format='audio/wav')

if __name__ == "__main__":
    main()
