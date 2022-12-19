# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:50:32 2022

@author: ccus
"""
import pandas as pd
import streamlit as st

st.title('Combo de filtres')



# import dataset
df_all = pd.read_csv("ivan_cleaning_2", sep = "\t", index_col=0)
#------------------------------------------------------------------------------------------------------------------
choix = st.select_slider('Avec qui venez-vous ?', options=['En famille', 'Seul','En couple', "Avec les copains de l'EHPAD", 'Entre potes'])
#st.write('Vous avez indiquer venir :', choix)
#choix = input("Comment venez-vous ?\nVeuillez choisir parmi les propositions suivantes :\n En famille / Entre potes / En couple / Seul / EHPAD\nVous avez choisi : ")
#------------------------------------------------------------------------------------------------------------------
#---- En famille --------------------------------------------------------------------------------------------------
#----------- CHOIX 1-----------------------------------------------------------------------------------------------
if choix == 'En famille':
    # création du dataframe "En famille"
    df_famille = df_all[(df_all['Animation']==1)|
                    (df_all['Family']==1)|
                    (df_all['Adventure']==1)]
    # on reset l'index
    df_famille = df_famille.reset_index(drop=True)
    # échantillon d'un film "En famille"
    film_famille = df_famille.sample(1)
    # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
    from sklearn.neighbors import NearestNeighbors
    # choix des vraiables explicatives
    X = df_famille[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    # instanciation du modèle
    neigh = NearestNeighbors(n_neighbors=2)
    # entrainement du modèle
    neigh.fit(X)
    # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
    voisin = neigh.kneighbors(film_famille[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])
    # on récupère le 2e chiffre de l'array ci-dessus
    position_reco = voisin[1][0][1]
    # on récupère la position de la recommandation
    reco = df_famille.iloc[[position_reco]]
    # on affiche le titre
    #print(f"Le film recommandé est : {reco['title'].item()}")
    st.write('Le film recommandé est: ', reco['title'])
#---- FAMILLE ---------------------------------------------------------------------------------------------------
#------------CHOIX 2---------------------------------------------------------------------------------------------

    # on crée la liste de genres utilisés pour le tri
    list_of_genres = ['Animation','Adventure','Family']
    choix_2 = st.select_slider('Avez-vous un genre préféré ? ', options=['Animation','Adventure','Family'])
    #choix_2 = str(input(f"\nVous avez un genre préféré ?\n Veuillez choisir parmi les genres suivants :\n {list_of_genres}\n"))
    if choix_2 in list_of_genres:
        # création du dataframe "genres"
        df_genres = df_famille[(df_famille.loc[:,choix_2]==1)]
        # on reset l'index
        df_genres = df_genres.reset_index(drop=True)
        # échantillon d'un film "genres"
        film_genres = df_genres.sample(1)
        # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
        from sklearn.neighbors import NearestNeighbors
        # choix des vraiables explicatives
        X = df_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']]
        # instanciation du modèle
        neigh = NearestNeighbors(n_neighbors=2)
        # entrainement du modèle
        neigh.fit(X)
        # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
        voisin = neigh.kneighbors(film_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']])
        # on récupère le 2e chiffre de l'array ci-dessus
        position_reco = voisin[1][0][1]
        # on récupère la position de la recommandation
        reco = df_genres.iloc[[position_reco]]
        # on affiche le titre
        #print(f"Le film recommandé est : {reco['title'].item()}")
        st.write('Le film recommandé est: ', reco['title'])
#---- FAMILLE --------------------------------
#------------CHOIX 3------------------------
        # on crée la liste des décénnies du dataframe
        year_category = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
        #choix_3 = input(f"\nVous avez une décennie favorite ?\n Veuillez choisir parmi les décennies suivants :\n {year_category}\n")
        choix_3 = st.select_slider('Avez-vous une décénnie préférée ? ', options=['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
        if choix_3 in year_category:
            # création du dataframe "year_category"
            df_year_category = df_genres[(df_genres.loc[:,'year_category']==choix_3)]
            # on reset l'index
            df_year_category = df_year_category.reset_index(drop=True)
            # échantillon d'un film "genres"
            film_year_category = df_year_category.sample(1)
            # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
            from sklearn.neighbors import NearestNeighbors
            # choix des vraiables explicatives
            X = df_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']]
            # instanciation du modèle
            neigh = NearestNeighbors(n_neighbors=2)
            # entrainement du modèle
            neigh.fit(X)
            # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
            voisin = neigh.kneighbors(film_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']])
            # on récupère le 2e chiffre de l'array ci-dessus
            position_reco = voisin[1][0][1]
            # on récupère la position de la recommandation
            reco = df_year_category.iloc[[position_reco]]
            # on affiche le titre
            #print(f"Le film recommandé est : {reco['title'].item()}")
            st.write('Le film recommandé suivant vos différents critères est : ',reco['title'])
            
#------Entre potes ------------------------------------------------------------------------------------------------------------          
#choix = st.select_slider('Avec qui venez-vous ?', options=['En famille', 'Seul','En couple', "Avec les copains de l'EHPAD", 'Entre potes'])
#st.write('Vous avez indiquer venir :', choix)
#choix = input("Comment venez-vous ?\nVeuillez choisir parmi les propositions suivantes :\n En famille / Entre potes / En couple / Seul / EHPAD\nVous avez choisi : ")
#------------------------------------------------------------------------------------------------------------------
#---- Entre potes --------------------------------------------------------------------------------------------------
#----------- CHOIX 1-----------------------------------------------------------------------------------------------
if choix == 'Entre potes':
    # création du dataframe "En famille"
    df_potes = df_all[(df_all['Thriller']==1)|
                    (df_all['Crime']==1)|
                    (df_all['Mystery']==1)|
                    (df_all['Action']==1)]
    # on reset l'index
    df_potes = df_potes.reset_index(drop=True)
    # échantillon d'un film "En famille"
    film_potes = df_potes.sample(1)
    # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
    from sklearn.neighbors import NearestNeighbors
    # choix des vraiables explicatives
    X = df_potes[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    # instanciation du modèle
    neigh = NearestNeighbors(n_neighbors=2)
    # entrainement du modèle
    neigh.fit(X)
    # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
    voisin = neigh.kneighbors(film_potes[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])
    # on récupère le 2e chiffre de l'array ci-dessus
    position_reco = voisin[1][0][1]
    # on récupère la position de la recommandation
    reco = df_potes.iloc[[position_reco]]
    # on affiche le titre
    #print(f"Le film recommandé est : {reco['title'].item()}")
    #st.write('Le film recommandé est: ', reco['title'])
#---- Entre potes ---------------------------------------------------------------------------------------------------
#------------CHOIX 2---------------------------------------------------------------------------------------------

    # on crée la liste de genres utilisés pour le tri
    list_of_genres = ['Action','Crime','Mystery','Thriller']
    choix_2 = st.select_slider('Avez-vous un genre préféré ? ', options=['Action','Crime','Mystery','Thriller'])
    #choix_2 = str(input(f"\nVous avez un genre préféré ?\n Veuillez choisir parmi les genres suivants :\n {list_of_genres}\n"))
    if choix_2 in list_of_genres:
        # création du dataframe "genres"
        df_genres = df_potes[(df_potes.loc[:,choix_2]==1)]
        # on reset l'index
        df_genres = df_genres.reset_index(drop=True)
        # échantillon d'un film "genres"
        film_genres = df_genres.sample(1)
        # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
        from sklearn.neighbors import NearestNeighbors
        # choix des vraiables explicatives
        X = df_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']]
        # instanciation du modèle
        neigh = NearestNeighbors(n_neighbors=2)
        # entrainement du modèle
        neigh.fit(X)
        # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
        voisin = neigh.kneighbors(film_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']])
        # on récupère le 2e chiffre de l'array ci-dessus
        position_reco = voisin[1][0][1]
        # on récupère la position de la recommandation
        reco = df_genres.iloc[[position_reco]]
        # on affiche le titre
        #print(f"Le film recommandé est : {reco['title'].item()}")
        #st.write('Le film recommandé est: ', reco['title'])
#---- FAMILLE --------------------------------
#------------CHOIX 3------------------------
        # on crée la liste des décénnies du dataframe
        year_category = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
        #choix_3 = input(f"\nVous avez une décennie favorite ?\n Veuillez choisir parmi les décennies suivants :\n {year_category}\n")
        choix_3 = st.select_slider('Avez-vous une décénnie préférée ? ', options=['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
        if choix_3 in year_category:
            # création du dataframe "year_category"
            df_year_category = df_genres[(df_genres.loc[:,'year_category']==choix_3)]
            # on reset l'index
            df_year_category = df_year_category.reset_index(drop=True)
            # échantillon d'un film "genres"
            film_year_category = df_year_category.sample(1)
            # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
            from sklearn.neighbors import NearestNeighbors
            # choix des vraiables explicatives
            X = df_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']]
            # instanciation du modèle
            neigh = NearestNeighbors(n_neighbors=2)
            # entrainement du modèle
            neigh.fit(X)
            # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
            voisin = neigh.kneighbors(film_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']])
            # on récupère le 2e chiffre de l'array ci-dessus
            position_reco = voisin[1][0][1]
            # on récupère la position de la recommandation
            reco = df_year_category.iloc[[position_reco]]
            # on affiche le titre
            #print(f"Le film recommandé est : {reco['title'].item()}")
            st.write('Le film recommandé suivant vos différents critères est : ',reco['title'])
            
#---- En couple --------------------------------------------------------------------------------------------------
#----------- CHOIX 1-----------------------------------------------------------------------------------------------
if choix == 'En couple':
    # création du dataframe "En couple"
    df_couple = df_all[(df_all['Romance']==1)|
                    (df_all['Horror']==1)|
                    (df_all['Film-Noir']==1)|
                    (df_all['Musical']==1)]
    # on reset l'index
    df_couple = df_couple.reset_index(drop=True)
    # échantillon d'un film "En couple"
    film_couple = df_couple.sample(1)
    # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
    from sklearn.neighbors import NearestNeighbors
    # choix des vraiables explicatives
    X = df_couple[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    # instanciation du modèle
    neigh = NearestNeighbors(n_neighbors=2)
    # entrainement du modèle
    neigh.fit(X)
    # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
    voisin = neigh.kneighbors(film_couple[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])
    # on récupère le 2e chiffre de l'array ci-dessus
    position_reco = voisin[1][0][1]
    # on récupère la position de la recommandation
    reco = df_couple.iloc[[position_reco]]
    # on affiche le titre
    #print(f"Le film recommandé est : {reco['title'].item()}")
    #st.write('Le film recommandé est: ', reco['title'])
#---- Entre potes ---------------------------------------------------------------------------------------------------
#------------CHOIX 2---------------------------------------------------------------------------------------------

    # on crée la liste de genres utilisés pour le tri
    list_of_genres = ['Romance','Horror','Film-Noir','Musical']
    choix_2 = st.select_slider('Avez-vous un genre préféré ? ', options=['Romance','Horror','Film-Noir','Musical'])
    #choix_2 = str(input(f"\nVous avez un genre préféré ?\n Veuillez choisir parmi les genres suivants :\n {list_of_genres}\n"))
    if choix_2 in list_of_genres:
        # création du dataframe "genres"
        df_genres = df_couple[(df_couple.loc[:,choix_2]==1)]
        # on reset l'index
        df_genres = df_genres.reset_index(drop=True)
        # échantillon d'un film "genres"
        film_genres = df_genres.sample(1)
        # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
        from sklearn.neighbors import NearestNeighbors
        # choix des vraiables explicatives
        X = df_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']]
        # instanciation du modèle
        neigh = NearestNeighbors(n_neighbors=2)
        # entrainement du modèle
        neigh.fit(X)
        # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
        voisin = neigh.kneighbors(film_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']])
        # on récupère le 2e chiffre de l'array ci-dessus
        position_reco = voisin[1][0][1]
        # on récupère la position de la recommandation
        reco = df_genres.iloc[[position_reco]]
        # on affiche le titre
        #print(f"Le film recommandé est : {reco['title'].item()}")
        #st.write('Le film recommandé est: ', reco['title'])
#---- EN COUPLE --------------------------------
#------------CHOIX 3------------------------
        # on crée la liste des décénnies du dataframe
        year_category = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
        #choix_3 = input(f"\nVous avez une décennie favorite ?\n Veuillez choisir parmi les décennies suivants :\n {year_category}\n")
        choix_3 = st.select_slider('Avez-vous une décénnie préférée ? ', options=['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
        if choix_3 in year_category:
            # création du dataframe "year_category"
            df_year_category = df_genres[(df_genres.loc[:,'year_category']==choix_3)]
            # on reset l'index
            df_year_category = df_year_category.reset_index(drop=True)
            # échantillon d'un film "genres"
            film_year_category = df_year_category.sample(1)
            # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
            from sklearn.neighbors import NearestNeighbors
            # choix des vraiables explicatives
            X = df_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']]
            # instanciation du modèle
            neigh = NearestNeighbors(n_neighbors=2)
            # entrainement du modèle
            neigh.fit(X)
            # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
            voisin = neigh.kneighbors(film_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']])
            # on récupère le 2e chiffre de l'array ci-dessus
            position_reco = voisin[1][0][1]
            # on récupère la position de la recommandation
            reco = df_year_category.iloc[[position_reco]]
            # on affiche le titre
            #print(f"Le film recommandé est : {reco['title'].item()}")
            st.write('Le film recommandé suivant vos différents critères est : ',reco['title'])
            
#---- Seul--------------------------------------------------------------------------------------------------
#----------- CHOIX 1-----------------------------------------------------------------------------------------------
if choix == 'Seul':
    # création du dataframe "Seul"
    df_seul = df_all[(df_all['Fantasy']==1)|
                    (df_all['Sci-Fi']==1)|
                    (df_all['Comedy']==1)|
                    (df_all['Adventure']==1)]
    # on reset l'index
    df_seul = df_seul.reset_index(drop=True)
    # échantillon d'un film "En couple"
    film_seul = df_seul.sample(1)
    # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
    from sklearn.neighbors import NearestNeighbors
    # choix des vraiables explicatives
    X = df_seul[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    # instanciation du modèle
    neigh = NearestNeighbors(n_neighbors=2)
    # entrainement du modèle
    neigh.fit(X)
    # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
    voisin = neigh.kneighbors(film_seul[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])
    # on récupère le 2e chiffre de l'array ci-dessus
    position_reco = voisin[1][0][1]
    # on récupère la position de la recommandation
    reco = df_seul.iloc[[position_reco]]
    # on affiche le titre
    #print(f"Le film recommandé est : {reco['title'].item()}")
    #st.write('Le film recommandé est: ', reco['title'])
#---- Entre potes ---------------------------------------------------------------------------------------------------
#------------CHOIX 2---------------------------------------------------------------------------------------------

    # on crée la liste de genres utilisés pour le tri
    list_of_genres = ['Fantasy', 'Sci-Fi','Comedy','Adventure']
    choix_2 = st.select_slider('Avez-vous un genre préféré ? ', options=['Fantasy', 'Sci-Fi','Comedy','Adventure'])
    #choix_2 = str(input(f"\nVous avez un genre préféré ?\n Veuillez choisir parmi les genres suivants :\n {list_of_genres}\n"))
    if choix_2 in list_of_genres:
        # création du dataframe "genres"
        df_genres = df_seul[(df_seul.loc[:,choix_2]==1)]
        # on reset l'index
        df_genres = df_genres.reset_index(drop=True)
        # échantillon d'un film "genres"
        film_genres = df_genres.sample(1)
        # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
        from sklearn.neighbors import NearestNeighbors
        # choix des vraiables explicatives
        X = df_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']]
        # instanciation du modèle
        neigh = NearestNeighbors(n_neighbors=2)
        # entrainement du modèle
        neigh.fit(X)
        # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
        voisin = neigh.kneighbors(film_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']])
        # on récupère le 2e chiffre de l'array ci-dessus
        position_reco = voisin[1][0][1]
        # on récupère la position de la recommandation
        reco = df_genres.iloc[[position_reco]]
        # on affiche le titre
        #print(f"Le film recommandé est : {reco['title'].item()}")
        #st.write('Le film recommandé est: ', reco['title'])
#---- EN COUPLE --------------------------------
#------------CHOIX 3------------------------
        # on crée la liste des décénnies du dataframe
        year_category = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
        #choix_3 = input(f"\nVous avez une décennie favorite ?\n Veuillez choisir parmi les décennies suivants :\n {year_category}\n")
        choix_3 = st.select_slider('Avez-vous une décénnie préférée ? ', options=['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
        if choix_3 in year_category:
            # création du dataframe "year_category"
            df_year_category = df_genres[(df_genres.loc[:,'year_category']==choix_3)]
            # on reset l'index
            df_year_category = df_year_category.reset_index(drop=True)
            # échantillon d'un film "genres"
            film_year_category = df_year_category.sample(1)
            # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
            from sklearn.neighbors import NearestNeighbors
            # choix des vraiables explicatives
            X = df_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']]
            # instanciation du modèle
            neigh = NearestNeighbors(n_neighbors=2)
            # entrainement du modèle
            neigh.fit(X)
            # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
            voisin = neigh.kneighbors(film_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']])
            # on récupère le 2e chiffre de l'array ci-dessus
            position_reco = voisin[1][0][1]
            # on récupère la position de la recommandation
            reco = df_year_category.iloc[[position_reco]]
            # on affiche le titre
            #print(f"Le film recommandé est : {reco['title'].item()}")
            st.write('Le film recommandé suivant vos différents critères est : ',reco['title'])
            
#---- Avec l'EHPAD--------------------------------------------------------------------------------------------------
#----------- CHOIX 1-----------------------------------------------------------------------------------------------
if choix == "Avec les copains de l'EHPAD":
    # création du dataframe "EHPAD"
    df_EHPAD = df_all[(df_all['Drama']==1)|
                    (df_all['Mystery']==1)|
                    (df_all['Biography']==1)|
                    (df_all['History']==1)|
                    (df_all['Western']==1)]
    # on reset l'index
    df_EHPAD = df_EHPAD.reset_index(drop=True)
    # échantillon d'un film "En couple"
    film_EHPAD = df_EHPAD.sample(1)
    # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
    from sklearn.neighbors import NearestNeighbors
    # choix des vraiables explicatives
    X = df_EHPAD[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']]
    # instanciation du modèle
    neigh = NearestNeighbors(n_neighbors=2)
    # entrainement du modèle
    neigh.fit(X)
    # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
    voisin = neigh.kneighbors(film_EHPAD[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                    'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                    'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                    'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                    'Thriller', 'War', 'Western', 'News', 'Short']])
    # on récupère le 2e chiffre de l'array ci-dessus
    position_reco = voisin[1][0][1]
    # on récupère la position de la recommandation
    reco = df_EHPAD.iloc[[position_reco]]
    # on affiche le titre
    #print(f"Le film recommandé est : {reco['title'].item()}")
    #st.write('Le film recommandé est: ', reco['title'])
#---- Entre potes ---------------------------------------------------------------------------------------------------
#------------CHOIX 2---------------------------------------------------------------------------------------------

    # on crée la liste de genres utilisés pour le tri
    list_of_genres = ['Drama','Mystery','Biography','History','Western']
    choix_2 = st.select_slider('Avez-vous un genre préféré ? ', options=['Drama','Mystery','Biography','History','Western'])
    #choix_2 = str(input(f"\nVous avez un genre préféré ?\n Veuillez choisir parmi les genres suivants :\n {list_of_genres}\n"))
    if choix_2 in list_of_genres:
        # création du dataframe "genres"
        df_genres = df_EHPAD[(df_EHPAD.loc[:,choix_2]==1)]
        # on reset l'index
        df_genres = df_genres.reset_index(drop=True)
        # échantillon d'un film "genres"
        film_genres = df_genres.sample(1)
        # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
        from sklearn.neighbors import NearestNeighbors
        # choix des vraiables explicatives
        X = df_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']]
        # instanciation du modèle
        neigh = NearestNeighbors(n_neighbors=2)
        # entrainement du modèle
        neigh.fit(X)
        # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
        voisin = neigh.kneighbors(film_genres[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                        'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                        'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                        'Thriller', 'War', 'Western', 'News', 'Short']])
        # on récupère le 2e chiffre de l'array ci-dessus
        position_reco = voisin[1][0][1]
        # on récupère la position de la recommandation
        reco = df_genres.iloc[[position_reco]]
        # on affiche le titre
        #print(f"Le film recommandé est : {reco['title'].item()}")
        #st.write('Le film recommandé est: ', reco['title'])
#---- EN COUPLE --------------------------------
#------------CHOIX 3------------------------
        # on crée la liste des décénnies du dataframe
        year_category = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
        #choix_3 = input(f"\nVous avez une décennie favorite ?\n Veuillez choisir parmi les décennies suivants :\n {year_category}\n")
        choix_3 = st.select_slider('Avez-vous une décénnie préférée ? ', options=['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
        if choix_3 in year_category:
            # création du dataframe "year_category"
            df_year_category = df_genres[(df_genres.loc[:,'year_category']==choix_3)]
            # on reset l'index
            df_year_category = df_year_category.reset_index(drop=True)
            # échantillon d'un film "genres"
            film_year_category = df_year_category.sample(1)
            # Pour récupérer l'observation la plus proche de ses caractéristiques on utilise "NearestNeighbors"
            from sklearn.neighbors import NearestNeighbors
            # choix des vraiables explicatives
            X = df_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']]
            # instanciation du modèle
            neigh = NearestNeighbors(n_neighbors=2)
            # entrainement du modèle
            neigh.fit(X)
            # on récupère le résultat sous forme d'array indiquant la distance et la position du voisin le plus proche
            voisin = neigh.kneighbors(film_year_category[['startYear','runtimeMinutes', 'averageRating', 'Action', 'Adventure',
                            'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                            'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music',
                            'Musical', 'Mystery', 'Reality-TV', 'Romance', 'Sci-Fi', 'Sport',
                            'Thriller', 'War', 'Western', 'News', 'Short']])
            # on récupère le 2e chiffre de l'array ci-dessus
            position_reco = voisin[1][0][1]
            # on récupère la position de la recommandation
            reco = df_year_category.iloc[[position_reco]]
            # on affiche le titre
            #print(f"Le film recommandé est : {reco['title'].item()}")
            st.write('Le film recommandé suivant vos différents critères est : ',reco['title'])