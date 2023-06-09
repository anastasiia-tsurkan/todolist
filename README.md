# todolist

This ToDo list is just convenient way to store tasks and other lists. 
This project was created for practice in back-end development.


## Features
* Create, update and delete functions for tasks and tags
* Buttons "Complete" and "Undo" for changing status of the task
* Lists for tags
* Sidebar navigation menu with "Home" and "Tags" links

## Getting started

Python3 must be installed

```shell
git clone https://github.com/anastasiia-tsurkan/todolist
cd todolist
python3 -m venv venv
source venv/bin/activate  # on macOS
venv\Scripts\activate  # on Windows
pip install -r requirements.txt
```
copy .env_sample -> .env and populate with all required data

```shell
python manage.py migrate
python manage.py runserver
```

## Demo
![index_demo.png](images%2Findex_demo.png)
![create_demo.png](images%2Fcreate_demo.png)
![tags_demo.png](images%2Ftags_demo.png)