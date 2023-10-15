## Projeto de recomendação de vídeo
Sistema de recomendação de filme com base em uma indicação do usuário

Baseado em: [DataQuest-Tutorial](https://app.dataquest.io/c/93/m/99994/build-a-movie-recommendation-system-in-python)

## Projeto de sumarização de podcast
Sistema de reconhecimento e resumo de fala que pode ser usado para transcrever automaticamente arquivos de áudio, como notas de aula, podcasts ou vídeos, e transformá-los em um breve resumo.

Baseado em: [DataQuest-Tutorial](https://app.dataquest.io/c/93/m/99995/build-a-speech-recognition-and-summarization-system)

## [Vídeo explicativo](https://example.com)

## Certificados
- [Python Basics for Web Development](/Python_Essentials_for_MLOps/certificates/Python-Basics-for-Web-Development.pdf)
- [Machine Learning in Python](/Python_Essentials_for_MLOps/certificates/Machine-Learning-in-Python.pdf)

## Referências

| Reference                                                     | Link                                                                                           |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| :man: Teacher Ivanovitch                                      | [GIthub](https://github.com/ivanovitchm/mlops)         |
| :books: Github MLOPS - Teacher                                | [Practical MLOps](https://www.oreilly.com/library/view/practical-mlops/9781098103002/)         |
| :books: Chip Huyen                                            | [Designing ML Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)                                          |
| :books: Jason Brownlee                                        | [Deep Learning for NLP](https://machinelearningmastery.com/deep-learning-for-nlp/)            |
| :bomb: ChatGPT                                                | [OpenAI Chat](https://chat.openai.com/chat)                                                   |
| :smiley: CS329S - ML Systems Design                           | [Stanford's MLOps course](https://stanford-cs329s.github.io/syllabus.html)                    |
| :dart: Machine Learning Operations                            | [MLOps Community](https://ml-ops.org/)                                                        |

## Ambiente virtual python
Uma das alternativas para executar programas que necessitam de instalar bibliotecas em python é utilizar ambientes virtuais. Para utiliza-lo siga os procedimentos a seguir:

### Ativação
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

### Score de código com o pylint
```
./meu_ambiente_virtual/bin/pylint meu-codigo.py
```

### Utilização pylint para analise de código
```
./meu_ambiente_virtual/bin/pylint meu-codigo.py
```