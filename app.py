import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pdfplumber
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Preprocessing text function
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words('english') and token.isalnum()]
    return ' '.join(tokens)

# Function to read text from uploaded text file
def read_text_file(file):
    return preprocess_text(file.read().decode('utf-8'))

# Function to read text from uploaded PDF file
def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        pages = [page.extract_text() for page in pdf.pages if page.extract_text() is not None]
    return preprocess_text("\n".join(pages))

# Initialize the vectorizer
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))

# Function to calculate cosine similarity between two texts
def calculate_similarity(text1, text2):
    vectors = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

# Streamlit application interface
st.title('Resume to Job Description Matcher')

# File uploader allows user to upload a resume in text or PDF format
uploaded_file = st.file_uploader("Upload your resume", type=['txt', 'pdf'])

# Text area for pasting the job description
job_description = st.text_area("Paste the Job Description here:")

# Progress bar
progress_bar = st.progress(0)

# When the 'Calculate Similarity' button is pressed
if st.button('Calculate Similarity'):
    if uploaded_file is not None and job_description:
        job_description = preprocess_text(job_description)
        
        # Show progress bar
        progress_bar.progress(10)
        
        try:
            # Determine file type and read content
            if uploaded_file.type == "application/pdf":
                try:
                    resume_text = read_pdf(uploaded_file)
                    progress_bar.progress(50)
                except Exception as e:
                    st.error(f'Error reading PDF file: {str(e)}')
                    st.stop()
            elif uploaded_file.type == "text/plain":
                resume_text = read_text_file(uploaded_file)
                progress_bar.progress(50)

            # Calculate the similarity score between the resume and job description
            similarity_score = calculate_similarity(resume_text, job_description)
            progress_bar.progress(100)
            st.write(f'Similarity Score: {similarity_score:.2f}')

            # Provide feedback based on the similarity score
            if similarity_score < 0.3:
                st.warning('The similarity score is quite low. Consider revising your resume to include more relevant skills and experiences.')
            elif similarity_score < 0.6:
                st.info('The similarity score is moderate. Try to tailor your resume more closely to the job description.')
            else:
                st.success('Great match! Your resume closely matches the job description.')
        
        except Exception as e:
            st.error(f'An unexpected error occurred: {str(e)}')
    else:
        st.error('Please upload a resume and paste a job description.')

