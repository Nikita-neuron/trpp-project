# Загружаем образ python версии 3.9 с dockerhub
FROM python:3.9

# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /app

# Копирование файла в образ
COPY requirements.txt /app

# Обновляем pip
RUN pip3 install --upgrade pip

# Устанавливаем библиотеки
RUN pip3 install -r requirements.txt

# Копируем содержимое папки, где находится Dockerfile, в рабочую директорию контейнера
COPY . /app

# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000