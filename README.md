# MLOPS
## Projeto de recomendação de vídeo
Sistema de recomendação de filme com base em uma indicação do usuário

Baseado em: [DataQuest-Tutorial](https://app.dataquest.io/c/93/m/99994/build-a-movie-recommendation-system-in-python)

## projeto de sumarização de podcast
Sistema de reconhecimento e resumo de fala que pode ser usado para transcrever automaticamente arquivos de áudio, como notas de aula, podcasts ou vídeos, e transformá-los em um breve resumo.

Baseado em: [DataQuest-Tutorial](https://app.dataquest.io/c/93/m/99995/build-a-speech-recognition-and-summarization-system)


## Instalação de ambiente virtual python
Para instalar as biblitecas utilizadas crie um ambiente virtual python
```
pip install virtualenv
python3 -m venv meu_ambiente_virtual
source meu_ambiente_virtual/bin/activate
```

### Instale as bibliotecas necessárias
```
./meu_ambiente_virtual/bin/python -m pip install pylint autopep8
```

### Utilizando autopep8 para ajuste de código inplace
```
./meu_ambiente_virtual/bin/autopep8 --in-place --aggressive --aggressive meu-codigo.py
```

### Utilização pylint para analise de código
```
./meu_ambiente_virtual/bin/pylint meu-codigo.py
```