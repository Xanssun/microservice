# TestWork73

Простое приложение на fast-api для работы с транзакциями

## Описание команд Makefile
Для управления контейнерами приложения и инфраструктуры можно использовать следующие команды:

### Основные команды
* `make app` — запускает контейнер приложения вместе с базовой инфраструктурой.
* `make app-logs` — отслеживает логи в контейнере приложения в режиме реального времени.
* `make app-down` — останавливает контейнер приложения и всю инфраструктуру.
* `make app-shell` — открывает интерактивный shell (bash) в контейнере приложения.

### Управление хранилищами данных
* `make storage` — запускает контейнеры для хранилищ данных.
* `make storage-down` — останавливает контейнеры для хранилищ данных.

### Полный запуск
* `make all` — запускает все контейнеры для приложения и хранилищ данных вместе.

## Установка и использование
* Создайте файл `.env` с переменными окружения, необходимыми для работы приложения.
* Запустите нужные компоненты, используя команды из списка выше.

## Тестирование
* Введите в консоли `make app-shell`
* Перейдите в папку tests `cd tests`
* Запустите тесты `pytest -v`

## Полезная документация
- http://localhost:8000/api/docs#/ - Документация api
