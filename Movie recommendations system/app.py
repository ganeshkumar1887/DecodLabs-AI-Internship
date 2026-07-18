import streamlit as st
import pickle
import pandas as pd
from recommendation import recommend

# 👇 FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ab data load karo
movies = pickle.load(open("movies.pkl", "rb"))

movies = pickle.load(open("movies.pkl","rb"))

# ---------------------------------------
# Custom CSS
# ---------------------------------------

st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#FFFFFF;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:3px solid #E50914;
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color:#141414 !important;
}

/* Headings */
h1{
    color:#E50914;
    text-align:center;
    font-weight:700;
}

h2,h3{
    color:#141414;
}

/* Buttons */
.stButton>button{
    background:#E50914;
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#B20710;
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:#F8F8F8;
    border:2px solid #E50914;
    border-radius:12px;
    padding:15px;
}

/* DataFrame */
[data-testid="stDataFrame"]{
    border:2px solid #E50914;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# Header
# ---------------------------------------

st.title("🎬 AI Movie Recommendation System")

st.markdown(
"""
<center>

### Discover movies similar to your favourite movies using Artificial Intelligence.

Content-Based Recommendation using TF-IDF & Cosine Similarity

</center>

""",
unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------------------
# Dashboard
# ---------------------------------------

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("🎥 Movies",len(movies))

with col2:
    st.metric("🤖 Algorithm","TF-IDF")

with col3:
    st.metric("📊 Similarity","Cosine")

with col4:
    st.metric("⭐ Dataset","TMDB 5000")

st.markdown("---")

# ---------------------------------------
# Sidebar
# ---------------------------------------

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg",
    width=180
)

st.sidebar.markdown("# 🎬 Movie Recommender")

st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="
background:#E50914;
padding:15px;
border-radius:12px;
color:white;
text-align:center;
">

<h3 style="color:white;">🍿 AI Movie Recommendation</h3>

<p style="color:white;">
Discover movies similar to your favourite movie using AI.
</p>

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 📂 Project Details")

st.sidebar.write("🎥 **Dataset:** TMDB 5000 Movies")

st.sidebar.write("🤖 **Algorithm:** Content Based Filtering")

st.sidebar.write("📈 **Similarity:** Cosine Similarity")

st.sidebar.write("👨‍💻 **Developer:** Ganesh Kumar")

st.sidebar.markdown("---")

st.sidebar.markdown("## 🛠 Tech Stack")

st.sidebar.markdown("""
- 🐍 Python
- 📊 Pandas
- 🎬 Streamlit
- 🤖 Scikit-Learn
- 🧠 TF-IDF
- 📈 Cosine Similarity
""")
search_movie = st.sidebar.text_input("🔍 Search Movie")

if search_movie:

    result = movies[movies["title"].str.contains(search_movie, case=False)]

    if len(result) > 0:

        st.sidebar.success("Movie Found ✅")

        st.sidebar.write(result["title"].tolist())

    else:

        st.sidebar.error("Movie Not Found ❌")

st.subheader("📊 Dataset Analytics")

col1, col2 = st.columns(2)

with col1:

    st.metric("Total Movies", len(movies))

with col2:

    st.metric("Average Rating", round(movies["vote_average"].mean(),2))

st.subheader("🏆 Top 10 Highest Rated Movies")

top_movies = movies.sort_values(
    by="vote_average",
    ascending=False
).head(10)

st.dataframe(
    top_movies[
        [
            "title",
            "vote_average",
            "release_date"
        ]
    ],
    use_container_width=True
)

# ---------------------------------------
# Movie Selection
# ---------------------------------------

st.subheader("🔍 Search Your Favourite Movie")

selected_movie = st.selectbox(
    "Select Movie",
    movies["title"].values
)

# ---------------------------------------
# Button
# ---------------------------------------

# ---------------------------------------
# Recommend Button
# ---------------------------------------

recommend_btn = st.button("🎯 Recommend Movies")

if recommend_btn:

    recommended_movies = recommend(selected_movie)

    st.markdown("## 🍿 Recommended Movies")

    st.markdown("---")

    for movie in recommended_movies:

        st.markdown(f"""
        <div style="
            background-color:#1E1E1E;
            padding:20px;
            border-radius:15px;
            margin-bottom:20px;
            border-left:6px solid #E50914;
        ">

        <h3 style="color:#E50914;">🎬 {movie['title']}</h3>

        <p style="font-size:16px;">
        ⭐ <b>Rating:</b> {movie['rating']} <br>
        📅 <b>Release Date:</b> {movie['release']}
        </p>

        <p style="color:#DDDDDD;">
        {movie['overview']}
        </p>

        </div>
        """, unsafe_allow_html=True)
import random

if st.button("🎲 Surprise Me"):

    random_movie = random.choice(
        movies["title"].values
    )

    st.success(random_movie)
st.markdown("---")

st.markdown("""
<center>

🎬 AI Movie Recommendation System

Made with ❤️ by Ganesh Kumar

DecodeLabs AI Internship

</center>
""", unsafe_allow_html=True)