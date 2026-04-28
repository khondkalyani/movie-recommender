# 🎬 Movie Recommender System
## Live Demo: https://movie-recommender-ccyyty3q58ycfpkn99xebq.streamlit.app/

## About
Content-based movie recommendation system that suggests 
similar movies based on genre, cast, director and keywords.

## How It Works
1. Combined movie features into a single tags column
2. Applied TF-IDF vectorization (5000 features)
3. Computed cosine similarity between 4805 movies
4. Returns top 5 most similar movies

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn (TF-IDF, Cosine Similarity)
- Streamlit (UI)

## Dataset
TMDB 5000 Movies Dataset from Kaggle
- 4805 movies
- Features: genres, cast, director, keywords, overview
