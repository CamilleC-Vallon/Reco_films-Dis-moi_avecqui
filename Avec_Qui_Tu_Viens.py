#!/usr/bin/env python
# coding: utf-8

# In[11]:

import streamlit as st
import pandas as pd 

from sklearn.neighbors import NearestNeighbors
#Import des images utilisées pour le streamlit
from PIL import Image

cinema = Image.open('Le.jpg')
en_famille_image = Image.open('En famille.jpg')
en_couple_image = Image.open('en_couple.jpg')
ehpad_image = Image.open('vieux_cine.png')
entre_potes_image = Image.open('entre pote.jpg')
seul_image = Image.open('seul_cine.jpg')

st.set_page_config(page_title=("Le Local"), page_icon="👋")

st.sidebar.success('Filtres disponibles')

st.write("#Bienvenue Cinéphiles ! 👋")
st.title('Dis moi avec qui tu veux aller au cinéma et je te dirai quoi aller voir !')
st.image(cinema)


st.markdown( """ Team Projet 2 """)

df_all = pd.read_csv('ivan_cleaning_2', sep='\t', index_col = 0 ) 
#import avec index_col = 0 pour ne pas avoir de nouvelle colonne unnamed : 0 

# une valeur exceptionnelle supérieure à supprimer : pas plus de 4h
df_all = df_all[df_all['runtimeMinutes'] < 240]

# une valeur exceptionnelle inférieure à supprimer : pas moins de 25mn
df_all = df_all[df_all['runtimeMinutes'] > 25]

# on ne garde que les notes supérieures à 6
df_all = df_all[df_all['averageRating'] >= 6]


#Utilisation d'un st.radio pour le choix utilisateur
option = st.radio(
    "Avec qui voulez-vous allez au cinéma ?",
    ('En famille', 'Seul','En couple', "Avec les copains de l'EHPAD", 'Entre potes'))


if option == 'En famille':
    #Définition du DF_Famille
    df_famille = df_all[(df_all['Animation']==1)|  
                    (df_all['Family']==1)|
                    (df_all['Adventure']==1)&
                   (df_all['numVotes']>=6000)]

    df_famille = df_famille.reset_index(drop=True)
    film_famille = df_famille.sample(1) #soit le film type Famille aléatoire qui va faire marcher l'algo


    #Machine Learning

    X = df_famille[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(X)
    voisin_famille = neigh.kneighbors(film_famille[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])

    position_reco = voisin_famille[1][0][1]
    reco = df_famille.iloc[[position_reco]]
    #st.write('Vous avez apprécié :', film_famille['title'])
    st.write('Vous allez certainement aimer :', reco['title'])
    st.image(en_famille_image, use_column_width = True)


if option == 'Entre potes':
    #Définition du DF_entre_potes
    df_entre_potes = df_all[(df_all['Thriller']==1)|
                (df_all['Mystery']==1)|
                (df_all['Action']==1) |
                (df_all['Crime'] ==1)&
               (df_all['numVotes']>=6000)] 

    df_entre_potes = df_entre_potes.reset_index(drop=True)
    film_entre_potes = df_entre_potes.sample(1) #soit le film type Famille aléatoire qui va faire marcher l'algo

    #Machine Learning

    X = df_entre_potes[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(X)
    voisin_entre_potes = neigh.kneighbors(film_entre_potes[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])

    position_reco = voisin_entre_potes[1][0][1]
    reco = df_entre_potes.iloc[[position_reco]]
    #st.write('Vous avez apprécié :', film_entre_potes['title']) 
    st.write('Vous allez certainement aimer :', reco['title'])
    st.image(entre_potes_image)


if option == 'En couple':
    #Définition du DF_en_couple
    df_en_couple = df_all[(df_all['Romance']==1)|
                (df_all['Horror']==1)|
                (df_all['Musical']==1) |
                (df_all['Film-Noir'] ==1)&
               (df_all['numVotes']>=6000)] 

    df_en_couple = df_en_couple.reset_index(drop=True)
    film_en_couple = df_en_couple.sample(1) #soit le film type Famille aléatoire qui va faire marcher l'algo


    #Machine Learning

    X = df_en_couple[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(X)
    voisin_en_couple = neigh.kneighbors(film_en_couple[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])

    position_reco = voisin_en_couple[1][0][1]
    reco = df_en_couple.iloc[[position_reco]]
    #st.write('Vous avez apprécié :', film_en_couple['title'])
    st.write('Vous allez certainment aimer :', reco['title'])
    st.image(en_couple_image)
    
if option == 'Seul':
    #Définition du DF_seul
    df_seul = df_all[(df_all['Fantasy']==1)|
                (df_all['Sci-Fi']==1)|
                (df_all['Comedy']==1) |
                (df_all['Adventure'] ==1)&
               (df_all['numVotes']>=6000)]

    df_seul = df_seul.reset_index(drop=True)
    film_seul = df_seul.sample(1) 


    #Machine Learning

    X = df_seul[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(X)
    voisin_seul = neigh.kneighbors(film_seul[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])

    position_reco = voisin_seul[1][0][1]
    reco = df_seul.iloc[[position_reco]]
    #st.write('Vous avez apprécié :', film_seul['title'])
    st.write('Vous allez certainement aimer :', reco['title'])
    st.image(seul_image, use_column_width =True)


if option == "Avec les copains de l'EHPAD":
    df_ehpad = df_all[(df_all['Drama']==1)|
                (df_all['Western']==1)|
                (df_all['Biography']==1)|
                (df_all['History'] ==1)&
               (df_all['numVotes']>=6000)]
    df_ehpad = df_ehpad.reset_index(drop=True)
    film_ehpad= df_ehpad.sample(1) 


   #Machine Learning
    X = df_ehpad[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                              'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                              'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                              'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                              'Thriller', 'War', 'Western', 'News', 'Short']]
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(X)
    voisin_ehpad = neigh.kneighbors(film_ehpad[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                              'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 
                              'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                              'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                              'Thriller', 'War', 'Western', 'News', 'Short']])
    
    position_reco = voisin_ehpad[1][0][1]
    reco = df_ehpad.iloc[[position_reco]]
    #st.write('Avec les copains vous avez appréciés :', film_ehpad['title'])
    st.write('Vous allez certainement aimer :', reco['title'])
    st.image(ehpad_image)
   