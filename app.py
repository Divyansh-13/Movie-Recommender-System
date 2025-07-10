import streamlit as st
import pandas as pd
import requests
import pickle
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Load the processed data and similarity matrix
@st.cache_data
def load_data():
    try:
        with open('movie_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("movie_data.pkl not found. Please run the Jupyter notebook first to generate this file.")
        st.stop()

movies, cosine_sim = load_data()

# Create a session with retry strategy
def create_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    try:
        idx = movies[movies['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  # Get top 10 similar movies
        movie_indices = [i[0] for i in sim_scores]
        return movies[['title', 'movie_id']].iloc[movie_indices]
    except IndexError:
        st.error(f"Movie '{title}' not found in the database.")
        return pd.DataFrame()

# Fetch movie poster from TMDB API with error handling
@st.cache_data
def fetch_poster(movie_id):
    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  # Replace with your TMDB API key
    
    # Default placeholder image URL
    placeholder_image = "https://via.placeholder.com/500x750/cccccc/000000?text=No+Image+Available"
    
    try:
        session = create_session()
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
        
        # Add timeout and headers
        headers = {
            'User-Agent': 'Movie-Recommendation-System/1.0',
            'Accept': 'application/json'
        }
        
        response = session.get(url, timeout=10, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = response.json()
        
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
        else:
            return placeholder_image
            
    except requests.exceptions.ConnectionError:
        st.warning(f"Connection error for movie ID {movie_id}. Using placeholder image.")
        return placeholder_image
    except requests.exceptions.Timeout:
        st.warning(f"Timeout error for movie ID {movie_id}. Using placeholder image.")
        return placeholder_image
    except requests.exceptions.HTTPError as e:
        st.warning(f"HTTP error {e.response.status_code} for movie ID {movie_id}. Using placeholder image.")
        return placeholder_image
    except requests.exceptions.RequestException as e:
        st.warning(f"Request error for movie ID {movie_id}: {str(e)}. Using placeholder image.")
        return placeholder_image
    except Exception as e:
        st.warning(f"Unexpected error for movie ID {movie_id}: {str(e)}. Using placeholder image.")
        return placeholder_image

# Streamlit UI
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommendation System")
st.markdown("---")

# Add sidebar with information
with st.sidebar:
    st.header("About")
    st.write("This system recommends movies based on cosine similarity using movie features like genres, keywords, cast, and crew.")
    
    st.header("Instructions")
    st.write("1. Select a movie from the dropdown")
    st.write("2. Click 'Get Recommendations'")
    st.write("3. View the top 10 similar movies")
    
    st.header("Note")
    st.write("If poster images don't load, it might be due to network issues or API limits.")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    selected_movie = st.selectbox(
        "🔍 Select a movie:", 
        movies['title'].values,
        help="Choose a movie to get recommendations based on similarity"
    )

with col2:
    st.write("")  # Add spacing
    recommend_button = st.button('🎯 Get Recommendations', type="primary")

if recommend_button:
    if selected_movie:
        with st.spinner('Finding similar movies...'):
            recommendations = get_recommendations(selected_movie)
            
        if not recommendations.empty:
            st.success(f"Top 10 movies similar to **{selected_movie}**:")
            st.markdown("---")
            
            # Create a 2x5 grid layout with progress bar
            progress_bar = st.progress(0)
            
            for i in range(0, 10, 5):  # Loop over rows (2 rows, 5 movies each)
                cols = st.columns(5)  # Create 5 columns for each row
                for col, j in zip(cols, range(i, i+5)):
                    if j < len(recommendations):
                        movie_title = recommendations.iloc[j]['title']
                        movie_id = recommendations.iloc[j]['movie_id']
                        
                        # Update progress
                        progress_bar.progress((j + 1) / 10)
                        
                        with col:
                            with st.container():
                                poster_url = fetch_poster(movie_id)
                                st.image(poster_url, width=130, caption=movie_title)
                                
                        # Small delay to prevent overwhelming the API
                        time.sleep(0.1)
            
            progress_bar.empty()  # Remove progress bar when done
        else:
            st.error("No recommendations found. Please try a different movie.")
    else:
        st.warning("Please select a movie first.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Powered by TMDB API | Built with Streamlit"
    "</div>", 
    unsafe_allow_html=True
)
