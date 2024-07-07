FROM python:3.12

# Создаем директорию /src внутри контейнера
RUN mkdir /src

# Устанавливаем /src как рабочую директорию
WORKDIR /src

# Копируем requirements.txt из контекста сборки в /src в контейнере
COPY requirements.txt .

# Устанавливаем зависимости Python из requirements.txt
RUN pip install -r requirements.txt

# Копируем все остальные файлы из текущего контекста сборки в /src в контейнере
COPY . .

# Открываем порт 7000 для веб-приложения
EXPOSE 7000

# Запускаем приложение с помощью uvicorn
CMD uvicorn src.presentation.main:build_app --host=0.0.0.0 --port=7000 --factory --workers=4
