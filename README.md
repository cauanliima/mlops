## Resumo dos passos

### instalar python e pip
```
sudo apt install python3 python3-pip python3-venv
```

### Criar ambiente virual python3
```
python3 -m venv meu_ambiente_virtual
source meu_ambiente_virtual/bin/activate
```

### Instalar airflow
```
AIRFLOW_HOME=~/airflow
AIRFLOW_VERSION=2.7.1

# Extract the version of Python you have installed. If you're currently using Python 3.11 you may want to set this manually as noted above, Python 3.11 is not yet supported.
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.7.1 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.8.txt

sudo pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

### instalar bibliotecas python
```
sudo pip install pandas xmltodict requests vosk pydub pysqlite3
```

###
```
pip install ffmpeg