FROM python:3.9
LABEL authors="strumendo"
WORKDIR /app

# Copia o projeto Kedro para o contêiner
COPY . .

# Instala dependências
RUN pip install -r requirements.txt
RUN pip install kedro mlflow

# Comando padrão para executar o pipeline
CMD ["kedro", "run"]