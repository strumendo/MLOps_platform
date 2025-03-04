FROM python:3.9
LABEL authors="strumendo"
WORKDIR /app

# Instala o MLFlow
RUN pip install mlflow

# Expõe a porta do MLFlow
EXPOSE 5000

# Comando para iniciar o servidor MLFlow
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]