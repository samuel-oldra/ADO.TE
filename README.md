<h1 align="center">
  ADO.TE - PyStack Week 5.0
</h1>
<p align="center">
  <a href="#tecnologias-e-práticas-utilizadas">Tecnologias e práticas utilizadas</a> •
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#comandos">Comandos</a>
</p>

Aplicação que conecta pessoas que possuem animais para doação com interessadas em ter um animal de estimação.

Desenvolvida uma aplicação completa para adoção de animais.

## Tecnologias e práticas utilizadas
- Python 3.8
- Django 4.2
- SQLite
- Arquitetura MVT

## Funcionalidades
- Autenticação e Cadastro de Usuários
- Listagem, Cadastro e Remoção de Pets
- Listagem, Busca e Detalhes de Pets para adoção
- Listagem e Aprovação/Recusa dos pedidos de adoção
- Dashboard com gráfico de pedidos de adoção por raça

###

![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/logar.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/cadastre-se.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/novo_pet.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/seus_pets.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/adote.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/ver_pet.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/ver_pedido_adocao.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/ADO.TE/main/README_IMGS/dashboard.png)

## Comandos

### pip
```
pip list --outdate
pip install --upgrade pip setuptools Django ...
```

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
(env) python manage.py createsuperuser (admin/admin)
```

### Criar apps
```
(env) python manage.py startapp usuarios
(env) python manage.py startapp divulgar
(env) python manage.py startapp adotar
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
