#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 07:57:28 2022

@author: sarthak
"""

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import pickle5 as pickle
import requests


st.set_page_config(page_title='Movie Recomendation System', layout="wide")


clf = pickle.load(open('sentiment_nlp_model.pkl', 'rb'))
vectorizer = pickle.load(open('transform.pkl','rb'))


def create_similarity():
    movies = pd.read_csv('main_data_till21.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(movies['comb'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return movies, similarity

def rcmd(m):
    m = m.lower()
    try:
        movies.head()
        similarity.shape
    except:
        movies, similarity = create_similarity()
    if m in movies['movie_title'].unique():
        i = movies.loc[movies['movie_title']==m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(movies['movie_title'][a])
            
        return l

def second(list):
    list = rcmd(selected_movie)
    photo = []
    for list in list:
        url = "https://api.themoviedb.org/3/search/movie?api_key=bce8b94968a79cd90c7d3cbe5005203b&query=" + list
        data = requests.get(url)
        data = data.json()
        poster_path = data['results'][0]['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        photo.append(full_path)
    return photo






st.header('Movie Recomendation System')

movies = pd.read_csv("/home/sarthak/Data_Science_Deploy_Project/Movie_Recommendation/main_data_till21.csv")
movie_list = movies['movie_title'].values
selected_movie = st.selectbox(
    "Type or select movie from the drop list", movie_list
)


def fetch_movie():
  url = "https://api.themoviedb.org/3/search/movie?api_key=bce8b94968a79cd90c7d3cbe5005203b&query=" + selected_movie
  data = requests.get(url)
  data = data.json()
  poster_path = data['results'][0]['poster_path']
  movie_id = data['results'][0]['id']
  full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
  original_title = data['results'][0]['original_title']
  overview = data['results'][0]['overview']
  release_date = data['results'][0]['release_date']
  vote_average = data['results'][0]['vote_average']

  return movie_id, full_path, original_title, overview, release_date, vote_average


movie_details = fetch_movie()


col1, col2 = st.columns(2)

with col1:
    #st.header("A cat")
    st.image(movie_details[1])

with col2:
    st.header("Movie Details")
    st.write('Movie : ', movie_details[2])
    st.write('Overview : ', movie_details[3])
    st.write('Release Date : ', movie_details[4])
    st.write('Movie Ratings : ', movie_details[5])


st.header('Recomended Movie')

if st.button('Recommendations'):
    l = rcmd(selected_movie)
    photo = second(selected_movie)
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
    with col1:
        st.text(l[1])
        st.image(photo[1])
    with col2:
        st.text(l[2])
        st.image(photo[2])
    with col3:
        st.text(l[3])
        st.image(photo[3])
    with col4:
        st.text(l[4])
        st.image(photo[4])
    with col5:
        st.text(l[5])
        st.image(photo[5])
    with col6:
        st.text(l[6])
        st.image(photo[6])
    with col7:
        st.text(l[7])
        st.image(photo[7])
    with col8:
        st.text(l[8])
        st.image(photo[8])
    with col9:
        st.text(l[9])
        st.image(photo[9])
        
        
        

