# TranslateX

## Problem Statement:

TransLingua is a cutting-edge web application designed to harness the power of advanced AI to provide seamless language translation services. Built using Streamlit and Google's Generative AI, TransLingua offers an intuitive and user-friendly interface for translating text between multiple languages. By simply inputting text and selecting the desired source and target languages, users can instantly receive accurate translations powered by the latest AI models. This tool is ideal for anyone needing reliable and fast translations, whether for personal, educational, or professional purposes.

## Features 

1.⁠ ⁠*Text Translation*:
   - Translate text between 30+ languages.
   - Auto-detect the source language.
   - Listen to translations using text-to-speech.

2.⁠ ⁠*File Translation*:
   - Upload and translate text files, PDFs, and Word documents.
   - Extract text from files and translate it seamlessly.

3.⁠ ⁠*Voice Translation*:
   - Speak into the microphone and get real-time translations.
   - Supports voice input in multiple languages.

4.⁠ ⁠*User-Friendly Interface*:
   - Clean and intuitive design with animated headings.
   - Dark mode compatibility for better visibility.

5.⁠ ⁠*Download Translations*:
   - Download translated text as a ⁠ .txt ⁠ file for offline use.

---

## Technologies Used 🛠️

•⁠  ⁠*Google Gemini AI*: For language detection and translation.
•⁠  ⁠*Streamlit*: For building the web application.
•⁠  ⁠*PyPDF2*: For extracting text from PDF files.
•⁠  ⁠*python-docx*: For extracting text from Word documents.
•⁠  ⁠*SpeechRecognition*: For voice input and transcription.
•⁠  ⁠*pyttsx3*: For text-to-speech functionality.

---

## Setup Instructions 🚀

### Prerequisites
•⁠  ⁠Python 3.8 or higher.
•⁠  ⁠A Google API key for Gemini AI.

### Steps to Run the Project

1.⁠ ⁠*Clone the Repository*:
   ⁠ bash
   git clone https://github.com/your-username/TranslateX.git
   cd TranslateX
    ⁠

2.⁠ ⁠*Install Dependencies*:
   ⁠ bash
   pip install -r requirements.txt
    ⁠

3.⁠ ⁠*Set Up Environment Variables*:
   - Create a ⁠ .env ⁠ file in the project root directory.
   - Add your Google API key:
     ⁠ plaintext
     GOOGLE_API_KEY=your_api_key_here
      ⁠

4.⁠ ⁠*Run the Application*:
   ⁠ bash
   streamlit run app.py
    ⁠

5.⁠ ⁠*Access the App*:
   - Open your browser and navigate to ⁠ http://localhost:8501 ⁠.

---

## Usage Guide 📖

1.⁠ ⁠*Text Translation*:
   - Select the source and target languages.
   - Enter the text you want to translate.
   - Click "Translate Text" to get the translation.

2.⁠ ⁠*File Translation*:
   - Upload a text file, PDF, or Word document.
   - Select the source and target languages.
   - Click "Translate File" to get the translation.

3.⁠ ⁠*Voice Translation*:
   - Click "Record Voice" and speak into your microphone.
   - Select the source and target languages.
   - Click "Translate" to get the translation.

4.⁠ ⁠*Listen to Translations*:
   - Use the "Listen to Translation" button to hear the translated text.

5.⁠ ⁠*Download Translations*:
   - Use the "Download Translation" button to save the translated text as a ⁠ .txt ⁠ file.

---

## Customization 🎨

•⁠  ⁠*Add More Languages*:
  - Update the ⁠ LANGUAGE_FLAGS ⁠ dictionary in the code to include additional languages.
  
•⁠  ⁠*Change Styling*:
  - Modify the CSS in the ⁠ st.markdown ⁠ section to customize the app's appearance.

•⁠  ⁠*Add New Features*:
  - Integrate additional APIs or libraries for advanced functionality (e.g., sentiment analysis, cultural context).

---

## Screenshots 📸

### Text Translation
![Text Translation](screenshots/text_translation.png)

### File Translation
![File Translation](screenshots/file_translation.png)

### Voice Translation
![Voice Translation](screenshots/voice_translation.png)

---

## Contributing 🤝

Contributions are welcome! If you'd like to contribute to TranslateX, please follow these steps:

1.⁠ ⁠Fork the repository.
2.⁠ ⁠Create a new branch for your feature or bug fix.
3.⁠ ⁠Commit your changes and push to the branch.
4.⁠ ⁠Submit a pull request.

---

## License 📜

This project is licensed under the *MIT License*. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments 🙏

•⁠  ⁠*Google Gemini AI*: For providing the powerful translation API.
•⁠  ⁠*Streamlit*: For making it easy to build and deploy web apps.
•⁠  ⁠*Open Source Community*: For the libraries and tools used in this project.

