from translate import Translator
import streamlit
translator= Translator(to_lang="es")
streamlit.title("Python Language Translator")
input = streamlit.text_input("Enter text to translate from English to Spanish")
translation = translator.translate(input)
streamlit.write(translation)