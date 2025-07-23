from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, jd_text):
    """
    Calculate a similarity score between resume and job description using TF-IDF and cosine similarity.
    Returns a match percentage.
    """
    try:
        # Prepare text
        documents = [resume_text.lower(), jd_text.lower()]
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(documents)

        # Calculate cosine similarity
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_percentage = round(score * 100, 2)
        return match_percentage
    except Exception as e:
        print(f"Error in calculating match score: {e}")
        return 0.0
