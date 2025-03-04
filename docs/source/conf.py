import sphinx_rtd_theme

# Extensões do Sphinx
extensions = [
    'sphinx.ext.autodoc',  # Documentação automática de código Python
    'sphinx.ext.viewcode',  # Adiciona links para o código-fonte
    'sphinx_rtd_theme',     # Tema Read the Docs
]

# Tema da documentação
html_theme = 'sphinx_rtd_theme'

# Caminho para arquivos estáticos
html_static_path = ['_static']

# Configurações adicionais
html_logo = '_static/logo.png'  # Logo do projeto (opcional)
html_favicon = '_static/favicon.ico'  # Ícone do site (opcional)