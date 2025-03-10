import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2
from docx import Document
import speech_recognition as sr
import pyttsx3

load_dotenv()

# Configure the Gemini API
genai.configure(api_key="AIzaSyAHAfSBZv-Pk4zbfr95OdxNhVJfiDvA6bs")

# Language configuration with flags
LANGUAGE_FLAGS = {
    "Auto Detect": "",
    "Arabic": "",
    "Bengali": "",
    "Chinese": "",
    "Dutch": "",
    "English": "",
    "French": "",
    "German": "",
    "Gujarati": "",
    "Hebrew": "",
    "Hindi": "",
    "Indonesian": "",
    "Italian": "",
    "Japanese": "",
    "Kannada": "",
    "Korean": "",
    "Malayalam": "",
    "Marathi": "",
    "Portuguese": "",
    "Punjabi": "",
    "Russian": "",
    "Spanish": "",
    "Tamil": "",
    "Telugu": "",
    "Thai": "",
    "Turkish": "",
    "Urdu": "",
    "Vietnamese": ""
}

# Function to detect language
def detect_language(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Detect the language of the following text: '\n{text}'"
    response = model.generate_content(prompt)
    return response.text.strip()

# Function to translate text using Gemini
def translate_text(text, source_language, target_language):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = (
        f"Translate the following {source_language} text to {target_language} and provide a brief explanation: '\n{text}'"
    )
    response = model.generate_content(prompt)
    return response.text

# Function to extract text from PDF file
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from Word (DOCX) file
def extract_text_from_docx(uploaded_file):
    doc = Document(uploaded_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Function to recognize speech and return transcribed text
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        st.info("Listening... Please speak into the microphone.")
        audio = recognizer.listen(source)
        
    try:
        st.info("Recognizing...")
        text = recognizer.recognize_google(audio)
        st.success(f"Transcription: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Could not understand the audio.")
    except sr.RequestError:
        st.error("There was an issue with the speech recognition service.")
    return ""

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

# Streamlit UI
st.set_page_config(page_title="TranslateX", page_icon="", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    /* General Styling */
    .main {
        margin-top:20px;
        background-color: #f8f9fa;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #black;
    }
    
    /* Remove empty div under tabs */
    div.block-container {
        padding-top: 0rem;
    }
    
    /* Animated Heading with Color Transition Border */
    @keyframes borderColorChange {
        0% { border-image: linear-gradient(45deg, #3a7bd5, #00d2ff) 1; }
        25% { border-image: linear-gradient(45deg, #00d2ff, #6a11cb) 1; }
        50% { border-image: linear-gradient(45deg, #6a11cb, #fc466b) 1; }
        75% { border-image: linear-gradient(45deg, #fc466b, #3a7bd5) 1; }
        100% { border-image: linear-gradient(45deg, #3a7bd5, #00d2ff) 1; }
    }
    
    .animated-heading {
        text-align: center;
        padding: 20px;
        font-size: 2.5rem;
        font-weight: 700;
        font-family: 'Helvetica Neue'
        color: #2c3e50;
        border: 6px solid;
        border-image: linear-gradient(45deg, #3a7bd5, #00d2ff) 1;
        animation: borderColorChange 10s linear infinite;
        margin-top: 50px;
        margin-bottom: 30px;
        background-color: white;
        border-radius: 5px;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: white;
        border-radius: 8px;
        padding: 5px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f5;
        border-radius: 6px;
        border-color: #black;
        padding: 10px 16px;
        font-weight: 600;
        color: #495057;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #3a7bd5 !important;
        color: white !important;
    }
    
    /* Content Container */
    .content-container {
        background-color: white;
        padding: 25px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    
    /* Input Fields Styling */
    .stTextInput>div>div>input>div>div>div {
        background-color: #grey;
        border-radius: 6px;
        border: 1px solid #e9ecef;
        padding: 8px 12px;
        color: #white; /* Ensuring text color is dark in inputs */
    }
    
    /* Remove the blank space to the right of selectboxes */
    .stSelectbox {
        width: 100%;
    }
    .stSelectbox > div {
        width: 100%;
    }
    
    .stTextArea>div>div>textarea {
        background-color: #f8f9fa;
        border-radius: 6px;
        border: 1px solid #e9ecef;
        padding: 12px;
        font-size: 1rem;
        min-height: 120px;
        color: #black; /* Ensuring text color is dark in text areas */
    }
    
    /* Download Button Styling - White with orange hover */
    .stDownloadButton>button, button[data-testid="baseButton-secondary"] {
        background-color: white !important;
        color: #3a7bd5 !important;
        border: 1px solid #3a7bd5 !important;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stDownloadButton>button:hover, button[data-testid="baseButton-secondary"]:hover {
        background-color: #FF8C00 !important; /* Orange color on hover */
        color: white !important;
        border-color: #FF8C00 !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Regular Button Styling */
    .stButton>button {
        background-color: #3a7bd5;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #2a5db0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* File Uploader Styling */
    .stFileUploader>div {
        background-color: #f8f9fa;
        border-radius: 6px;
        border: 1px dashed #adb5bd;
        padding: 15px;
        color: #white; /* Ensuring text color is dark in file uploader */
    }
    
    /* Translation Result Styling */
    .translation-result {
        background-color: #black;
        border-left: 5px solid #3a7bd5;
        padding: 15px;
        border-radius: 6px;
        margin: 15px;
        color: #black; /* Ensuring text color is dark in translation results */
    }
    
    /* Status Message Styling */
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 10px 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    .info-message {
        background-color: #d1ecf1;
        color: #0c5460;
        padding: 10px 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    .warning-message {
        background-color: #fff3cd;
        color: #856404;
        padding: 10px 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 10px 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    
    /* Section Headers */
    .section-header {
        font-weight: 600;
        color: #3a7bd5;
        margin: 15px;
        padding-bottom: 8px;
        border-bottom: 2px solid #e9ecef;
    }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 20px 0;
        margin-top: 30px;
        color: #6c757d;
        font-size: 0.9rem;
        border-top: 1px solid #e9ecef;
    }
    
    /* Fix for disabled text areas */
    .stTextArea>div>div>textarea:disabled {
        color: #black; /* Darker text color for better visibility */
        background-color: #e9ecef; /* Slightly darker background for disabled areas */
        opacity: 0.9; /* Increased opacity for better contrast */
    }
    
    /* Ensuring label texts are visible */
    .stSelectbox > label, .stTextArea > label, .stTextInput > label, .stSlider > label {
        color: #black !important; /* Force darker color for labels */
        font-weight: 500 !important; /* Make labels slightly bolder */
    }
    
    /* Making sure text in info/warning boxes is visible */
    .stAlert {
        color: black !important; /* Ensuring text in alert boxes is visible */
    }
    
    .element-container {
        color: #black; /* Default text color for all streamlit elements */
    }
</style>
""", unsafe_allow_html=True)

# Animated heading
st.markdown('<div class="animated-heading">TranslateX</div>', unsafe_allow_html=True)

# Create tabs for different functionalities (removed Settings tab)
tabs = st.tabs(["Text Translation", "File Translation", "Voice Translation"])

# Global variables for translation
languages = ["Auto Detect"] + sorted([
    "Arabic", "Bengali", "Chinese", "Dutch", "English", "French", "German", "Gujarati",
    "Hebrew", "Hindi", "Indonesian", "Italian", "Japanese", "Kannada", "Korean",
    "Malayalam", "Marathi", "Portuguese", "Punjabi", "Russian", "Spanish", "Tamil",
    "Telugu", "Thai", "Turkish", "Urdu", "Vietnamese"
])

# Text Translation Tab
with tabs[0]:
#    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Language Selection</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        source_language_text = st.selectbox(
            "From Language:",
            options=languages,
            index=languages.index("Auto Detect"),
            key="source_lang_text"
        )
    
    with col2:
        target_language_text = st.selectbox(
            "To Language:",
            options=[lang for lang in languages if lang != "Auto Detect"],
            index=languages.index("English") - 1 if "Auto Detect" in languages else languages.index("English"),
            key="target_lang_text"
        )
    
    st.markdown('<div class="section-header">Enter Text</div>', unsafe_allow_html=True)
    source_text = st.text_area("Type or paste text to translate:", height=150, key="text_input")
    
    if st.button("Translate Text", key="translate_text_button"):
        if source_text:
            try:
                with st.spinner("Translating..."):
                    # Detect language if set to Auto Detect
                    if source_language_text == "Auto Detect":
                        detected_lang = detect_language(source_text)
                        st.info(f"Detected Language: {detected_lang}")
                        source_language_text = detected_lang
                    
                    # Translate text
                    translated_text = translate_text(source_text, source_language_text, target_language_text)
                    
                    # Display results
                    st.success("Translation Completed!")
                    st.markdown(f"<div class='section-header'>{target_language_text} Translation:</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='translation-result'>{translated_text}</div>", unsafe_allow_html=True)
                    
                    # Actions for translated text
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="Download Translation",
                            data=translated_text.encode(),
                            file_name=f"translated_{target_language_text}.txt",
                            mime="text/plain"
                        )
                    with col2:
                        st.button("Listen to Translation", 
                                on_click=text_to_speech, 
                                args=(translated_text,))
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter text to translate.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# File Translation Tab
with tabs[1]:
#    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Language Selection</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        source_language_file = st.selectbox(
            "From Language:",
            options=languages,
            index=languages.index("Auto Detect"),
            key="source_lang_file"
        )
    
    with col2:
        target_language_file = st.selectbox(
            "To Language:",
            options=[lang for lang in languages if lang != "Auto Detect"],
            index=languages.index("English") - 1 if "Auto Detect" in languages else languages.index("English"),
            key="target_lang_file"
        )
    
    st.markdown('<div class="section-header">Upload File</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a text file, PDF, or Word file:", type=["txt", "pdf", "docx"])
    
    file_content = ""
    if uploaded_file is not None:
        try:
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension == "txt":
                file_content = uploaded_file.read().decode("utf-8")
            elif file_extension == "pdf":
                file_content = extract_text_from_pdf(uploaded_file)
            elif file_extension == "docx":
                file_content = extract_text_from_docx(uploaded_file)
            
            st.success(f"File uploaded: {uploaded_file.name}")
            st.markdown('<div class="section-header">File Content</div>', unsafe_allow_html=True)
            st.text_area("Extracted text:", value=file_content, height=150, key="file_content_display", disabled=True)
        except Exception as e:
            st.error(f"Error processing file: {e}")
    
    if st.button("Translate File", key="translate_file_button"):
        if file_content:
            try:
                with st.spinner("Translating..."):
                    # Detect language if set to Auto Detect
                    if source_language_file == "Auto Detect":
                        detected_lang = detect_language(file_content)
                        st.info(f"Detected Language: {detected_lang}")
                        source_language_file = detected_lang
                    
                    # Translate text
                    translated_text = translate_text(file_content, source_language_file, target_language_file)
                    
                    # Display results
                    st.success("Translation Completed!")
                    st.markdown(f"<div class='section-header'>{target_language_file} Translation:</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='translation-result'>{translated_text}</div>", unsafe_allow_html=True)
                    
                    # Actions for translated text
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="Download Translation",
                            data=translated_text.encode(),
                            file_name=f"translated_{target_language_file}.txt",
                            mime="text/plain"
                        )
                    with col2:
                        st.button("Listen to Translation", 
                                on_click=text_to_speech, 
                                args=(translated_text,),
                                key="listen_file_translation")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload a file to translate.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Voice Translation Tab
with tabs[2]:
#    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Language Selection</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        source_language_voice = st.selectbox(
            "From Language:",
            options=languages,
            index=languages.index("Auto Detect"),
            key="source_lang_voice"
        )
    
    with col2:
        target_language_voice = st.selectbox(
            "To Language:",
            options=[lang for lang in languages if lang != "Auto Detect"],
            index=languages.index("English") - 1 if "Auto Detect" in languages else languages.index("English"),
            key="target_lang_voice"
        )
    
    st.markdown('<div class="section-header">Voice Input</div>', unsafe_allow_html=True)
    st.write("Click the button below and speak into your microphone.")
    
    if st.button("Record Voice", key="record_voice_button"):
        voice_text = recognize_speech_from_mic()
        
        if voice_text:
            try:
                with st.spinner("Translating..."):
                    # Detect language if set to Auto Detect
                    if source_language_voice == "Auto Detect":
                        detected_lang = detect_language(voice_text)
                        st.info(f"Detected Language: {detected_lang}")
                        source_language_voice = detected_lang
                    
                    # Translate text
                    translated_text = translate_text(voice_text, source_language_voice, target_language_voice)
                    
                    # Display results
                    st.success("Translation Completed!")
                    st.markdown(f"<div class='section-header'>{target_language_voice} Translation:</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='translation-result'>{translated_text}</div>", unsafe_allow_html=True)
                    
                    # Actions for translated text
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="Download Translation",
                            data=translated_text.encode(),
                            file_name=f"translated_{target_language_voice}.txt",
                            mime="text/plain"
                        )
                    with col2:
                        st.button("Listen to Translation", 
                                on_click=text_to_speech, 
                                args=(translated_text,),
                                key="listen_voice_translation")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>TranslateX: AI-Powered Multi-Language Translator made using Gemini AI and Streamlit</p>
</div>
""", unsafe_allow_html=True)