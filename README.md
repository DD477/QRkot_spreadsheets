# QRKot

### Описание:
Благотворительный фонд поддержки котиков.

### Ключевые возможности:
- В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается. Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.
- Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.
- Создание отчетов по проектам с помощью Google Sheets API и Google Drive API.

### Используемые технологии:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/10.1/)
- [Google Sheets API](https://developers.google.com/sheets/api/)
- [Google Drive API](https://developers.google.com/drive/api/)
- [Google Api Python Client](https://github.com/googleapis/google-api-python-client/)
- [Aiogoogle](https://aiogoogle.readthedocs.io/en/latest/)

### Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/DD477/cat_charity_fund.git
```
```
cd cat_charity_fund
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
```
source venv/bin/activate
```

- Обновить менеджер пакетов (pip) 

```
pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

- Создайть файл с переменными окружения `.env`.Пример его содержимого ниже:
```sh
# название проекта
APP_TITLE=Фонд QRKot
# описание проекта
APP_DESCRIPTION=Благотворительный фонд поддержки котиков
# используемая база данных
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
# секретный ключ
SECRET=hn%h33Qc(0X4%h%R
# email первого суперпользователя
FIRST_SUPERUSER_EMAIL=admin@admin.com
# пароль первого суперпользователя
FIRST_SUPERUSER_PASSWORD=admin
```
- Для работы с `Google Sheets API` / `Google Drive API` нужно дополнить файл `.env` данными из JSON-файла о вашем сервисном аккаунте и email'ом на который будет приходить шаринг документа.
```sh
# email для шаринга
EMAIL=private_E-mail
# данные из JSON-файла сервисного аккаунта
TYPE=service_account
PROJECT_ID=project_id
PRIVATE_KEY_ID=private_key_id
PRIVATE_KEY=private_key
CLIENT_EMAIL=email
CLIENT_ID=client_id
# эти данные можно не изменять
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/service-user%40watchful-gear-351810.iam.gserviceaccount.com
```

## Использование
Запуск проекта
```
uvicorn app.main:app --reload
```
Переменные `FIRST_SUPERUSER_EMAIL` и `FIRST_SUPERUSER_PASSWORD` файле `.env`нужны для создания суперпользователя при первом запуске приложения.

### Документация API
Документация по проекту доступна на следующих эндпойнтах:
 - `/docs` — документация в формате Swagger;
 - `/redoc` — документация в формате ReDoc.



### Автор:

- [Dmitrii Dobrodeev](https://github.com/DD477)

## Лицензия
- MIT

