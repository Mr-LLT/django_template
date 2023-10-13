Django Template
===
这是一个 Django 项目模板，从此处开始创建项目，例如创建 `mysite` 项目：
```bash
# 请将 $DJ_TEMP_PATH 修改为实际模板路径
django-admin startproject --template $DJ_TEMP_PATH mysite
```

介绍
---
该模板重新定义了 Django 项目结构，与默认的项目结构有所出入。通常情况下，
创建 Django 项目后还需创建至少一个应用，于此才能正常使用 Django ORM；但在该模板中，项目即应用。

模板中将应用和项目结构内聚到一起，在创建项目后可以立即编写模型、试图、测试，也可定义模型基类、代理模型等基础结构；
同样也可以什么都不做，闲话少絮，请看文件结构：

```yml
project_root:
    project_name:
        migrations:
        apps.py
        urls.py
        asgi.py
        wsgi.py
        admin.py
        views.py
        tests.py
        models.py
        settings.py
        __init__.py
    deploy.py
    manage.py
    requirements.txt
```

教程
---
```bash
export DJANGO_SECRET_KEY=""
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

部署
---
运行 `python deploy.py` 即可一键部署，要求生产环境已安装 uwsgi 和 nginx；
文件 `deploy.py` 中包含最基础的 uwsgi 和 nginx 配置模板，如果必要请根据事实出发进行修改。
