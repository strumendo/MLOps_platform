FROM jupyterhub/jupyterhub:latest
LABEL authors="strumendo"
WORKDIR /srv/jupyterhub

# Copia o arquivo de configuração do JupyterHub
COPY jupyterhub_config.py .

# Instala dependências adicionais
RUN pip install -r requirements.txt

# Comando para iniciar o JupyterHub
CMD ["jupyterhub"]