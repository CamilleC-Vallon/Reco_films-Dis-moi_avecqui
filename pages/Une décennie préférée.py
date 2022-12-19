# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:31:55 2022

@author: ccus
"""
import streamlit as st
import pandas as pd 


from PIL import Image

st.title('Vous préférez faire un voyage dans le temps ?')
decennie = Image.open('temps.jpg')

df_all = pd.read_csv('ivan_cleaning_2', sep='\t', index_col = 0 ) 
#import avec index_col = 0 pour ne pas avoir de nouvelle colonne unnamed : 0 

# une valeur exceptionnelle supérieure à supprimer : pas plus de 4h
df_all = df_all[df_all['runtimeMinutes'] < 240]

# une valeur exceptionnelle inférieure à supprimer : pas moins de 25mn
df_all = df_all[df_all['runtimeMinutes'] > 25]

# on ne garde que les notes supérieures à 6
df_all = df_all[df_all['averageRating'] >= 6]
#-----------------------------------------------------------------------------------------------------------------
year_category = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

choix_3 = st.selectbox('Veuillez choisir votre décennie favorite :', ('1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'))

st.write('Vous avez choisi :', choix_3)
#choix_3 = input(f"\nVous avez une décennie favorite ?\n Veuillez choisir parmi les décennies suivants :\n {year_category}\n")
if choix_3 in year_category:
    df_year_category = df_all[(df_all.loc[:,'year_category']==choix_3)]
    df_year_category = df_year_category.reset_index(drop=True)
    film_year_category = df_year_category.sample(1)
        # Pour récupérer l'observation la plus proche de ses caractéristiques: NearestNeighbors
    from sklearn.neighbors import NearestNeighbors
    X = df_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']]
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(X)
    voisin = neigh.kneighbors(film_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']])
        # récupérer le 2e chiffre de l'array au dessus
    position_reco = voisin[1][0][1]
        # afficher le titre
    reco = df_year_category.iloc[[position_reco]]
        
    #print(f"Le film recommandé est : {reco['title'].item()}")

    st.write('Vous allez certainement aimer :', reco['title'])
    st.image(decennie)