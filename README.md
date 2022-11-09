# Aplicação usando Python e Django 4.1

## ADO.TE - PyStack Week: O Retorno

Aplicação que conecta pessoas que possuem animais para doação com interessadas em ter um animal de estimação.

Desenvolvida uma aplicação completa para adoção de animais.

## Tecnologias e práticas utilizadas
- Python
- Django 4.1
- SQLite
- Arquitetura MVT

## Funcionalidades
- Autenticação e Cadastro de Usuários
- Listagem, Cadastro e Remoção de Pets
- Listagem e Busca de Pets para adoção

###

![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/logar.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/cadastre-se.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/novo_pet.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/seus_pets.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/adote.png)

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

### Criar super user (Django Administration)
```
(env) python manage.py createsuperuser
```

### Criar apps
```
(env) python manage.py startapp usuarios
(env) python manage.py startapp divulgar
```

### Migrations
```
(env) python manage.py makemigrations
(env) python manage.py migrate
```

### Executar projeto
```
(env) python manage.py runserver
```