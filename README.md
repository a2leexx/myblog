# MyBlog

Учебный проект, написанный с целью изучения Django.

Поддерживается создание и удаление статей, теги и 
поиск по ним, поиск статей по введенной пользователем строке. 

Для оформления веб-страниц используется Bootstrap. 

## Зависимости
 
 Кроме наличия Django, также необходим пакет [markdown2](https://github.com/trentm/python-markdown2). Установить его можно следующим образом:

 ```
 pip install markdown2
 ```

 ## Запуск сервера для разработки

 Для работы необходимо задать переменные среды `DJANGO_SECRET_KEY` с ключом для локальной разработки и `DJANGO_DEBUG`, со значением `True`. 
 
 После клонирования репозитория выполните:
 
 ```
 python manage.py migrate
 python manage.py createsuperuser
 ```

Для запуска выполните:

```
python manage.py runserver
```

 ## Примечание

 Параметры в файле `myblog\settings.py` заданы для локальной разработки, поэтому его необходимо изменить. Также необходимо задать секретный ключ, 
 указав его в переменной среды `DJANGO_SECRET_KEY`, а переменной среды `DJANGO_DEBUG` присвоить `False`.


