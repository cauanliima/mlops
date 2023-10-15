"""
Programa para fazer recomendações de filmes baseado em uma indicação
"""
import re
import logging
import ipywidgets as widgets
import requests
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from IPython.display import display

# Basic logging configuration

# Configuração do arquivo de log, nível de log, modo de arquivo e formato
# de mensagem
logging.basicConfig(
    filename='./results.log',  # Caminho do arquivo de log
    level=logging.DEBUG,  # Nível de log: DEBUG, INFO, WARNING, ERROR, CRITICAL
    filemode='w',  # Modo de arquivo: 'w' para sobrescrever, 'a' para adicionar
    # Formato da mensagem no arquivo de log
    format='%(name)s - %(levelname)s - %(message)s'
)


logging.debug("Inicialização de logs")


def clean_title(title):
    """
    Limpeza de dados
    Remove todos os caracteres que não são:
    letras, dígitos ou espaços em branco da variável title.
    """

    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title


def search(title):
    """
    Realiza uma pesquisa por títulos de filmes semelhantes usando a técnica TF-IDF.

    Esta função recebe um título de filme, limpa e vetoriza o título usando um
    modelo pré-treinado, e em seguida, calcula a similaridade de cosseno entre
    o título inserido e os títulos na base de dados.
    Retorna uma lista dos 5 filmes mais semelhantes ao título fornecido.

    Args:
        title (str): O título do filme para o qual deseja-se encontrar filmes semelhantes.

    Exemplo:
        search("Matrix")
        # Retorna uma lista dos 5 filmes mais semelhantes ao filme "Matrix".

    Retorna:
        pandas.DataFrame: Um DataFrame contendo informações sobre os filmes mais semelhantes,
        incluindo título, gêneros e outras informações relevantes.
    """
    # Limpa o título removendo caracteres especiais e transforma para
    # minúsculas
    title = clean_title(title)

    # Converte o título em um vetor usando o modelo de vetorização previamente
    # treinado (vectorizer)
    query_vec = vectorizer.transform([title])

    # Calcula a similaridade de cosseno entre o título inserido e os títulos
    # na base de dados (tfidf)
    similarity = cosine_similarity(query_vec, tfidf).flatten()

    # Obtém os índices dos 5 filmes mais semelhantes
    indices = np.argpartition(similarity, -5)[-5:]

    # Reordena os resultados para mostrar os filmes mais semelhantes primeiro
    results = movies.iloc[indices].iloc[::-1]

    return results


def find_similar_movies(movie_id):
    """
    Encontra e retorna uma lista de filmes similares com base no ID do filme fornecido.

    Esta função analisa os dados de classificação para encontrar usuários
    que atribuíram uma alta pontuação ao filme especificado. Em seguida,
    identifica outros filmes que esses usuários também classificaram
    positivamente e calcula uma pontuação de similaridade.
    Os filmes com as pontuações de similaridade mais altas são retornados
    como recomendações.

    Args:
        movie_id (int): O ID do filme para o qual se deseja encontrar filmes similares.

    Exemplo:
        find_similar_movies(123)
        # Retorna uma lista de até 10 filmes similares ao filme com o ID 123.

    Retorna:
        pandas.DataFrame: Um DataFrame contendo informações sobre filmes similares,
        incluindo a pontuação de similaridade, título e gêneros.
    """

    # Encontra usuários que deram uma classificação alta (maior que 4) para o
    # filme especificado (movie_id)
    similar_users = ratings[(ratings["movieId"] == movie_id) & (
        ratings["rating"] > 4)]["userId"].unique()

    # Filtra as classificações dos filmes por usuários que também
    # classificaram positivamente outros filmes
    similar_user_recs = ratings[(ratings["userId"].isin(
        similar_users)) & (ratings["rating"] > 4)]["movieId"]

    # Calcula a frequência relativa dos filmes recomendados pelos usuários
    # similares
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    # Filtra filmes que foram recomendados por pelo menos 10% dos usuários
    # similares
    similar_user_recs = similar_user_recs[similar_user_recs > .10]

    # Filtra todas as classificações dos usuários que recomendaram filmes
    # similares
    all_users = ratings[(ratings["movieId"].isin(
        similar_user_recs.index)) & (ratings["rating"] > 4)]

    # Calcula a frequência relativa dos filmes recomendados por todos os
    # usuários
    all_user_recs = all_users["movieId"].value_counts(
    ) / len(all_users["userId"].unique())

    # Cria um DataFrame combinando as frequências dos filmes recomendados
    # pelos usuários similares e por todos os usuários
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]

    # Calcula uma pontuação de similaridade dividindo as recomendações dos
    # usuários similares pelo total de recomendações
    rec_percentages["score"] = rec_percentages["similar"] / \
        rec_percentages["all"]

    # Ordena os filmes com base na pontuação de similaridade em ordem
    # decrescente
    rec_percentages = rec_percentages.sort_values("score", ascending=False)

    # Seleciona os 10 filmes com as pontuações de similaridade mais altas e mescla com o
    # DataFrame 'movies' para obter informações adicionais retorna um DataFrame contendo
    # as pontuações de similaridade, títulos e gêneros dos 10 filmes mais semelhantes
    return rec_percentages.head(10).merge(
        movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]


def on_type(data):
    """
    Atualiza a lista de recomendações quando o usuário digita um título de filme.

    Esta função é chamada quando o usuário digita um novo título de filme em um campo de entrada.
    Ela pesquisa o título fornecido, exibe filmes similares com base na primeira correspondência
    e os apresenta na lista de recomendações.

    Args:
        data (dict): Um dicionário contendo os dados fornecidos pelo usuário.
            Espera-se que o dicionário tenha uma chave "new" contendo o título do filme inserido
            pelo usuário.

    Exemplo:
        on_type({"new": "Matrix"})
        # Atualiza a lista de recomendações com filmes semelhantes a "Matrix".

    Retorna:
        None
    """
    try:
        with recommendation_list:
            # Limpa a saída anterior da lista de recomendações
            recommendation_list.clear_output()

            # Obtém o título inserido pelo usuário
            title = data["new"]

            # Verifica se o título inserido possui mais de 5 caracteres
            if len(title) > 5:
                # Realiza uma pesquisa com base no título inserido
                results = search(title)

                # Obtém o ID do primeiro filme na lista de resultados
                movie_id = results.iloc[0]["movieId"]

                # Encontra e exibe filmes similares com base no ID do filme
                display(find_similar_movies(movie_id))
                logging.debug("Quantidade de títulos maior que 5")
            else:
                logging.debug("Quantidade de títulos menor ou igual que 5")
    except requests.RequestException as get_exception:
        logging.error("❌ On_type failed: %s",get_exception)


movies = pd.read_csv("ml-25m/movies.csv")
ratings = pd.read_csv("ml-25m/ratings.csv")
# Converte uma coleção de documentos em uma matriz de recursos do TF-IDF.
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
movies["clean_title"] = movies["title"].apply(clean_title)
tfidf = vectorizer.fit_transform(movies["clean_title"])

movie_name_input = widgets.Text(
    value='Toy Story',
    description='Movie Title:',
    disabled=False
)
recommendation_list = widgets.Output()

movie_name_input.observe(on_type, names='value')

display(movie_name_input, recommendation_list)
