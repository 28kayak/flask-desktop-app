# Descktop App with Flask
## Start App
```sh
pyenv exec python3 main.py
```
# create a new env with virtual env python
```sh
#craete a new env
pyenv virtualenv <python-version> <env-name>

#set the new env as local env 
pyenv local <env-name>

#download whatever you need
pyenv exec pip install <lib-name>
#freeze
pyenv exec pip freeze -l > requirements.txt
```


# Reference 
## pyenv and virtualenv usages 
- https://qiita.com/Kodaira_/items/feadfef9add468e3a85b
- https://qiita.com/ksato9700/items/5d9eba10fe6b8e064178
## Flask 
- https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
