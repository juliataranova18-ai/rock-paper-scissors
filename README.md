# Rock Paper Scissors

Современная версия классической игры "Камень-Ножницы-Бумага" на Python.

##  Как запустить игру

### Простой способ:
1. Скачайте файлы проекта
2. Установите Python с сайта python.org
3. Запустите файл `rock_paper_scissors.py` (двойной клик)

### Через командную строку:
```bash
python rock_paper_scissors.py

##  Запуск через Docker

### Установи Docker:
1. Скачайте Docker Desktop с [официального сайта](https://www.docker.com/products/docker-desktop/)
2. Установите и запустите Docker

### Сборка и запуск контейнера:
```bash
# Собрать образ
docker build -t rock-paper-scissors .

# Запустить контейнер
docker run -it --rm rock-paper-scissors