# Resume to Job Description Matcher

## Overview
This project provides a tool that matches resumes to job descriptions using TF-IDF vectorization and cosine similarity. Built with Streamlit, this application not only serves as a practical utility for job seekers and recruiters but also as an educational tool for those interested in learning about text similarity metrics and vectorization techniques in Natural Language Processing (NLP).

## Features
- **Text Preprocessing**: Converts raw text into a cleaner format removing stopwords and using lemmatization to improve the analysis accuracy.
- **TF-IDF Vectorization**: Transforms preprocessed text into numerical data, emphasizing important words.
- **Cosine Similarity**: Calculates the similarity score between the vectorized forms of the resume and the job description.

## Prerequisites
Before you can run this project, you'll need the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Installation

Clone the repository:
```bash
git clone https://github.com/AbhijitChallapalli/Kafka.git
```
Install the required packages:

```bash
pip install -r requirements.txt

## Usage
To start the application, run:

```bash
streamlit run app.py
```
Navigate to http://localhost:8501 in your web browser to view the application.

## How It Works
Upload a Resume: You can upload a resume in .txt or .pdf format.
Paste a Job Description: Input the text of a job description into the provided text area.
Calculate Similarity: Click the 'Calculate Similarity' button to see how similar the uploaded resume is to the job description provided.

## Learning Outcomes
Understand the implementation of TF-IDF.
Learn how cosine similarity can be used to measure text similarity.
Explore basic text preprocessing techniques in NLP.

## Contributing
Contributions to this project are welcome! Please consider the following ways you can contribute:

## Reporting a bug
Discussing the current state of the code
Submitting a fix
Proposing new features
Becoming a maintainer

## License
This project is licensed under the MIT License 

## Acknowledgments
This project was inspired by a desire to merge practical utility with educational opportunities in the field of data science and NLP.
