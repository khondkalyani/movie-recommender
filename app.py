import streamlit as st
import pickle
import pandas as pd

# ── Page Config ──────────────────────────────────────
st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# ── Load Data ─────────────────────────────────────────
@st.cache_resource
def load_data():
    df         = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return df, similarity

df, similarity = load_data()

# ── Helper Function ───────────────────────────────────
def recommend(movie_title):
    movie_index = df[df['title'] == movie_title].index[0]
    distances   = similarity[movie_index]
    movie_list  = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]
    return [(df['title'][i], round(score * 100, 2)) 
            for i, score in movie_list]

# ── UI ────────────────────────────────────────────────
st.title("🎬 Movie Recommender System")
st.markdown("Find movies similar to your favorites!")
st.divider()

# Movie selection dropdown
selected_movie = st.selectbox(
    "🔍 Search or select a movie:",
    df['title'].values
)

# Recommend button
if st.button("🎯 Get Recommendations", use_container_width=True):
    
    recommendations = recommend(selected_movie)
    
    st.divider()
    st.subheader(f"Because you watched **{selected_movie}**:")
    st.markdown(" ")

    # Display each recommendation as a card
    for i, (title, score) in enumerate(recommendations, 1):
        
        # Color bar based on similarity score
        if score >= 15:
            color = "#2ecc71"    # green  — high similarity
        elif score >= 10:
            color = "#f39c12"    # orange — medium similarity
        else:
            color = "#e74c3c"    # red    — low similarity

        st.markdown(f"""
        <div style="
            background-color: #1e1e1e;
            border-left: 5px solid {color};
            padding: 15px 20px;
            border-radius: 8px;
            margin-bottom: 12px;
        ">
            <span style="color: white; font-size: 16px;">
                <b>{i}. {title}</b>
            </span>
            <span style="
                float: right;
                color: {color};
                font-weight: bold;
                font-size: 15px;
            ">
                {score}% match
            </span>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.caption("Built with Python, TF-IDF & Cosine Similarity")