# Ativação de ambiente virtual python
Para instalar as biblitecas utilizadas crie um ambiente virtual python
```
pip install virtualenv
python3 -m venv meu_ambiente_virtual
source meu_ambiente_virtual/bin/activate
```

# Processo de melhoria de código

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
