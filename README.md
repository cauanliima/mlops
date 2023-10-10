# Ambiente virtual
Para instalar as biblitecas utilizadas crie um ambiente virtual python
```
apt install python3-venv
python3 -m venv meu_ambiente_virtual
source meu_ambiente_virtual/bin/activate
```

# Processo de melhoria de código
Instalar as bibliotecas necessárias para o processo
```
./meu_ambiente_virtual/bin/python -m pip install pylint autopep8
```
### Utilizando autopep8 para ajuste de código inplace
```
./meu_ambiente_virtual/bin/autopep6 --agressive --agressive meu-codigo.py
```
### Utilização pylint para analise de código
```
./meu_ambiente_virtual/bin/pylint meu-codigo.py
```