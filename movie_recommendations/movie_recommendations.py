"""
Programa para fazer recomendações de filmes baseado em uma indicação
"""
import re
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import ipywidgets as widgets
from IPython.display import display


def clean_title(title):
    """
    Limpeza de dados
    Remove todos os caracteres que não são:
    letras, dígitos ou espaços em branco da variável title.
    """

    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title


def search(title):
    """Busca o indice do titulo do base em tfidf"""

    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices].iloc[::-1]

    return results


def find_similar_movies(movie_id):
    """Busca de títulos de filmes similares ao valor atribuido na chamada de função"""

    similar_users = ratings[(ratings["movieId"] == movie_id) &
                            (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) &
                                (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    similar_user_recs = similar_user_recs[similar_user_recs > .10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) &
                        (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts(
    ) / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]

    rec_percentages["score"] = rec_percentages["similar"] / \
        rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(
        movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]


def on_type(data):
    """
    Teste
    """
    with recommendation_list:
        recommendation_list.clear_output()
        title = data["new"]
        if len(title) > 5:
            results = search(title)
            movie_id = results.iloc[0]["movieId"]
            display(find_similar_movies(movie_id))


movies = pd.read_csv("ml-25m/movies.csv")
ratings = pd.read_csv("ml-25m/ratings.csv")

movies["clean_title"] = movies["title"].apply(clean_title)

# Converte uma coleção de documentos em uma matriz de recursos do TF-IDF.
vectorizer = TfidfVectorizer(ngram_range=(1, 2))

tfidf = vectorizer.fit_transform(movies["clean_title"])

movie_name_input = widgets.Text(
    value='Toy Story',
    description='Movie Title:',
    disabled=False
)

recommendation_list = widgets.Output()

movie_name_input.observe(on_type, names='value')

display(movie_name_input, recommendation_list)
