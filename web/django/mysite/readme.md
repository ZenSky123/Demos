# 项目说明

`python manage.py startapp [appname]` 创建一个应用

`python manage.py migrate` 创建一些表

`python manage.py makemigrations polls` 修改模型之后进行迁移

`python manage.py sqlmigrate polls 0001` 迁移之后使用sqlmigrate用sql来表示迁移，之后再次使用migrate命令来进行创建表

`python manage.py createsuperuser` 创建超级管理员