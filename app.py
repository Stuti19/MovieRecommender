import pandas as pd
import requests
import streamlit as st
import pickle

def fetch_poster(title):
    url="http://www.omdbapi.com/?t={}&apikey=6ef91acb".format(title)
    data = requests.get(url)
    data = data.json()
    full_path = data['Poster']
    return full_path
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    recommended_movies_posters = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].title))
    return recommended_movies,recommended_movies_posters


st.title('Movie Recommender System')

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Recommend more movies'):
    names, posters = recommend(selected_movie_name)
    columns = st.columns(5)

    for i in range(len(names)):
        with columns[i % 5]:  # Ensure it wraps around to the first column after the fifth
            st.markdown(
                f"<div style='height: 100px; margin-top: 10px; display: flex; align-items: center; overflow: hidden; text-overflow: ellipsis;'><p style='font-size:16px; line-height:1.6; margin: 0 auto;'>{names[i]}</p></div>",
                unsafe_allow_html=True)  # Fixed height, margin, and vertical alignment for text
            st.image(posters[i])  # Display the movie poster






# For only names and no poster
# import pandas as pd
# import requests
# import streamlit as st
# import pickle
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
#     recommended_movies = []
#     for i in distances[1:6]:
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
#
#
# st.title('Movie Recommender System')
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# selected_movie_name = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movies['title'].values
# )
#
# if st.button('Recommend'):
#     names=recommend(selected_movie_name)
#     for i in names:
#         st.write(i)