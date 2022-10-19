# :closed_lock_with_key: Лабораторные работы по предмету `Защита информации`

## О репозитории
**data-protection** - репозиторий, в котором находятся лабораторные работы, теория к ним и лекции по предмету `Защита информации`

## Необходимые инструменты
- [Git](https://git-scm.com/downloads)
- [Python 3.6 и выше](https://www.python.org/downloads/)

 ## Подготовка
1. Склонируете репозиторий (или скачайте архив репозитория):
```shell
git clone git@github.com:Hunter-99/data-protection.git
```
2. Создайте виртуальное окружение:
```shell
python -m venv venv
```
3. Активируйте виртуальное окружение:
```shell
# Linux
. venv/bin/activate
# Windows
.\venv\Scripts\activate
```
4. Установите зависимости из `requirements.txt`:
```shell
pip isntall -r requiremetns.txt
```

## Запуск скриптов
В папке `labs` находятся скрипты для каждой лабораторной работы. Также в папке со скриптом находятся задания (`README.md`).
Для запуска скрипта необходимо ввести команду:
```shell
# n - номер лабораторой работы
python -m labs.lab_n.lab_n
```
Например:
```shell
python -m labs.lab_3.lab_3
```
