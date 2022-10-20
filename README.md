# Aplicação usando Python e Django 4.1

## ADO.TE - PyStack Week: O Retorno

Aplicação que conecta pessoas que possuem animais para doação com interessadas em ter um animal de estimação.

Desenvolvida uma aplicação completa para adoção de animais.

## Tecnologias e práticas utilizadas
- Python
- Django 4.1
- SQLite
- Arquitetura MVT

###

![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/cadastre-se.png)

## Comandos

### virtualenv (windows)
```
python -m venv env
env\Scripts\activate.bat
env\Scripts\deactivate.bat
```

### Instalar bibliotecas, gravar/instalar requerimentos
```
(env) pip install Django
(env) pip install Pillow

(env) pip freeze > requirements.txt
(env) pip install -r requirements.txt
```

### Criar projeto
```
(env) django-admin startproject adote .
```

### Criar apps
```
(env) python manage.py startapp usuarios
```

### Executar projeto
```
(env) python manage.py runserver
```