# Programa para fazer recomendações de filmes baseado em uma indicação

## Baixar base de dados
```
wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
unzip ml-25m.zip
```

## Executar com python3
### Instalação das bibliotecas necessárias:
Utilizando o ambiente virtual orientado no README.md na raiz do projeto, instale as seguintes bibliotecas.
```
./meu_ambiente_virtual/bin/python -m pip install -U scikit-learn numpy pandas ipywidgets IPython
```

### Executar o programa
```
./meu_ambiente_virtual/bin/python movie_recommendations/movie_recommendations.py
```