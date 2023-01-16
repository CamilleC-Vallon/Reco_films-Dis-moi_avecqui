# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:27:54 2022

@author: ccus
"""

import streamlit as st
import pandas as pd 


#from PIL import Image

#genre = Image.open('genre.png')

st.title('Votre genre préféré !')

df_all = pd.read_csv('ivan_cleaning_2.csv', sep='\t', index_col = 0 ) 
#import avec index_col = 0 pour ne pas avoir de nouvelle colonne unnamed : 0 

# une valeur exceptionnelle supérieure à supprimer : pas plus de 4h
df_all = df_all[df_all['runtimeMinutes'] < 240]

# une valeur exceptionnelle inférieure à supprimer : pas moins de 25mn
df_all = df_all[df_all['runtimeMinutes'] > 25]

# on ne garde que les notes supérieures à 6
df_all = df_all[df_all['averageRating'] >= 6]

#Ajout du filtre genre 
list_of_genres = ['Action','Adventure','Animation','Biography','Comedy','Crime',
                   'Documentary','Drama','Family','Fantasy','Film-Noir','History',
                   'Horror','Music','Musical','Mystery','Reality-TV','Romance',
                    'Sci-Fi','Sport','Thriller','War','Western','News','Short']

choix_2 = st.selectbox('Veuillez choisir votre genre préféré par les genres suivants:', (list_of_genres))

         
st.write('Vous avez choisi :', choix_2)
#choix_2 = str(input(f"\nVous avez un genre préféré ?\n Veuillez choisir parmi les genres suivants :\n {list_of_genres}\n"))

if choix_2 in list_of_genres:
    df_genres = df_all[(df_all.loc[:,choix_2]==1)]
    df_genres = df_genres.reset_index(drop=True)
    film_genres = df_genres.sample(1)
            # Pour récupérer l'observation la plus proche de ses caractéristiques: NearestNeighbors
    from sklearn.neighbors import NearestNeighbors
    X = df_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']]
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(X)
    voisin = neigh.kneighbors(film_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']])
            # récupérer le 2e chiffre de l'array au dessus
    position_reco = voisin[1][0][1]
            # afficher le titre
    reco = df_genres.iloc[[position_reco]]
            
        #print(f"Le film recommandé est : {reco['title'].item()}")
    st.write('Vous allez certainement aimer :', reco['title'])
