import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

@st.cache_resource
def load_data():
    df         = pickle.load(open('movies_small.pkl', 'rb'))
    similarity = pickle.load(open('similarity_small.pkl', 'rb'))
    return df, similarity

df, similarity = load_data()

def recommend(movie_title):
    movie_index = df[df['title'] == movie_title].index[0]
    movie_list  = similarity[movie_index]
    
    return [(df['title'][i], round(score * 100, 2)) 
            for i, score in movie_list[:5]]

# ── UI ────────────────────────────────────────────
st.title("🎬 Movie Recommender System")
st.markdown("Find movies similar to your favorites!")
st.divider()

selected_movie = st.selectbox(
    "🔍 Search or select a movie:",
    df['title'].values
)

if st.button("🎯 Get Recommendations", use_container_width=True):
    recommendations = recommend(selected_movie)
    
    st.divider()
    st.subheader(f"Because you watched **{selected_movie}**:")
    st.markdown(" ")

    for i, (title, score) in enumerate(recommendations, 1):
        if score >= 15:
            color = "#2ecc71"
        elif score >= 10:
            color = "#f39c12"
        else:
            color = "#e74c3c"

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