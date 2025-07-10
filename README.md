# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python that suggests movies based on content similarity using genres, keywords, cast, and crew information. The system provides an interactive web interface using Streamlit for easy movie discovery.

## 🎯 Project Overview

This project implements a content-based movie recommender system that analyzes movie characteristics like genres, keywords, cast, and crew to recommend similar movies. The system uses the TMDB (The Movie Database) dataset and provides recommendations through an interactive Streamlit web application with beautiful movie posters.

## ✨ Features

- **Content-Based Filtering**: Recommends movies based on content similarity
- **TF-IDF Vectorization**: Uses Term Frequency-Inverse Document Frequency for feature extraction
- **Cosine Similarity**: Calculates similarity between movies for accurate recommendations
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Movie Posters**: Displays movie posters using TMDB API
- **Top 10 Recommendations**: Shows the most relevant movie suggestions
- **Responsive Grid Layout**: Beautiful 2x5 grid display of recommended movies
- **Fast Performance**: Optimized algorithms for quick recommendation generation

## 🚀 Demo

The system provides recommendations by analyzing:
- Movie genres (Action, Comedy, Drama, etc.)
- Keywords and themes
- Cast members (top 3 actors)
- Directors
- Movie overviews

## 📊 Dataset

The project uses the **TMDB Movie Metadata** dataset from Kaggle:
- **Dataset Link**: [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used**: 
  - `tmdb_5000_movies.csv` - Movie details and metadata
  - `tmdb_5000_credits.csv` - Cast and crew information
- **Total Movies**: 4,809 movies with comprehensive metadata

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Divyansh-13/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Required Files

#### Option A: Download Pre-processed Data (Recommended)
Download the pre-processed movie data and similarity matrix:
- **PKL File**: [movie_data.pkl](https://drive.google.com/file/d/1HxdAM8TjEZ9alBq7AXPZA2EvzpDMoIqa/view?usp=sharing)
- Place the downloaded `movie_data.pkl` file in the project root directory

#### Option B: Process Data from Scratch
1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
2. Extract and place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the project directory
3. Run the Jupyter notebook: `Movie_Recommendation_System.ipynb`

### 4. Get TMDB API Key
1. Sign up at [TMDB](https://www.themoviedb.org/signup)
2. Get your API key from your account settings
3. Replace the API key in `app.py` (line 17)

### 5. Run the Application
```bash
streamlit run app.py
```

## 📁 Project Structure

```
Movie-Recommender-System/
├── Movie_Recommendation_System.ipynb  # Data processing notebook
├── app.py                            # Streamlit web application
├── requirements.txt                  # Python dependencies
├── movie_data.pkl                    # Processed data (download required)
├── tmdb_5000_movies.csv             # Movie dataset (download required)
├── tmdb_5000_credits.csv            # Credits dataset (download required)
├── .gitattributes                   # Git LFS configuration
└── README.md                        # Project documentation
```

## 🔧 Technical Details

### Data Processing Pipeline
1. **Data Merging**: Combines movie and credits datasets
2. **Feature Extraction**: Extracts genres, keywords, cast, and crew
3. **Text Preprocessing**: Combines features into tags and converts to lowercase
4. **TF-IDF Vectorization**: Creates feature vectors from text data
5. **Similarity Calculation**: Computes cosine similarity matrix

### Algorithm
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Similarity Metric**: Cosine Similarity
- **Recommendation Strategy**: Content-based filtering using combined features

### Key Libraries
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms (TF-IDF, cosine similarity)
- **streamlit**: Web application framework
- **requests**: API calls for movie posters
- **pickle**: Data serialization

## 🎮 Usage

1. **Launch the Application**: Run `streamlit run app.py` or 'python -m streamlit run app.py'
2. **Select a Movie**: Choose from the dropdown menu containing 4,809+ movies
3. **Get Recommendations**: Click the "Recommend" button
4. **View Results**: See top 10 similar movies with posters in a beautiful grid layout

## 🌟 Example Recommendations

**For "The Dark Knight Rises":**
- The Dark Knight
- Batman Begins
- Batman
- Batman & Robin
- Batman Returns
- The Prestige
- Catwoman
- Suicide Squad
- And more...

## 🔮 Future Enhancements

- [ ] Add user rating predictions
- [ ] Implement hybrid recommendation system
- [ ] Add movie reviews and ratings display
- [ ] Include user preference learning
- [ ] Add movie trailer integration
- [ ] Implement collaborative filtering
- [ ] Add movie search functionality
- [ ] Include movie release date filtering

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

**Divyansh** - [GitHub Profile](https://github.com/Divyansh-13)

Project Link: [https://github.com/Divyansh-13/Movie-Recommender-System](https://github.com/Divyansh-13/Movie-Recommender-System)

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the movie database and API
- [Kaggle](https://www.kaggle.com/) for hosting the dataset
- [Streamlit](https://streamlit.io/) for the amazing web app framework
- The open-source community for the excellent libraries used in this project

---

⭐ Star this repository if you found it helpful!
