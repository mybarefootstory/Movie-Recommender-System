import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommender System")

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies_list),
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
else:
    st.write("Goodbye")