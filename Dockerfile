#определяем версию python
FROM python:3.8.10-slim
#это указывает Python работать в небуфернном
ENV PYTHONUNBUFFERED 1

# устанавливаем каталог на диске
WORKDIR /django

# копируем всякие библиотке для это проекта
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
# устанавливаем их
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]