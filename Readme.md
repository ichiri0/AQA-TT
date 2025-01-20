# AQA-TT Project

## Описание

Этот проект содержит решения и тесты для задач `sol_1` и `sol_2`. 

## Задачи

1. Разработать метод, на вход которого подается PDF файл (сам файл предоставляется во вложении). Нужно прочитать всю возможную информацию из файла и на выходе вернуть в виде словаря.
    * При оценке решения будут учитываться как покрытие, так и архитектурные решения (по возможности – подумайте о потенциальном масштабировании).

2. Используя этот файл как эталон для последующих проверок, разработать механизм, проверяющий другие входящие pdf-файлы (как тестируемые) на соответствие структуры эталона.
    * При оценке решения будут учитываться тесты на: расположение на листе и наличие всех необходимых элементов, структуру текста, данные баркодов.

3. Дополнительное задание:
    * У вас есть таблица, в которой вы передаете свои значения (переменная `table`) и ответ из вебсокета бэкенда.
    * Вам нужно написать механизм, который будет принимать таблицу (`table`) и преобразовывать её в запрос JSON.
    * Также мы знаем, что ключи из таблицы = значениям в `base_ws`, также учитывать, что ключи в `table` могут находиться в разном порядке.
    * Как результат, вы должны собрать то, что в переменной `result` (файл - `additional_task.py`).
    * При оценке решения будут учитываться сбор, гибкость и устойчивость к ошибкам.

## Структура проекта

- `app/sol_1.py` - Решение для задачи 1
- `app/sol_2.py` - Решение для задачи 2
- `tests/sol_1_test.py` - Тесты для задачи 1
- `tests/sol_2_test.py` - Тесты для задачи 2
- `requirements.txt` - Зависимости проекта

## Команды Makefile

### Установить зависимости

```sh
make install
```

### Создать виртуальную среду

```sh
make venv
```

### Запуск sol_1

```sh
make run_sol_1
```

### Запуск тестов для sol_1

```sh
make test_sol_1
```

### Запуск sol_2

```sh
make run_sol_2
```

### Запуск тестов для sol_2

```sh
make test_sol_2
```

### Запуск всех тестов

```sh
make test_all
```

### Очистка виртуальной среды

```sh
make clean
```

## Как начать

1. Установите зависимости:
    ```sh
    make install
    ```

2. Создайте виртуальную среду:
    ```sh
    make venv
    ```

3. Активируйте виртуальную среду:
    ```sh
    source venv/bin/activate
    ```

4. Запустите нужные команды для выполнения кода или тестов.

## Лицензия

Этот проект лицензирован под MIT License.
## Команды для Windows

Если вы используете Windows и у вас нет Makefile, вы можете выполнить следующие команды вручную:

### Установить зависимости

```sh
pip install -r requirements.txt
```

### Создать виртуальную среду

```sh
python -m venv venv
```

### Активировать виртуальную среду

```sh
venv\Scripts\activate
```

### Запуск sol_1

```sh
python app/sol_1.py
```

### Запуск тестов для sol_1

```sh
pytest tests/sol_1_test.py
```

### Запуск sol_2

```sh
python app/sol_2.py
```

### Запуск тестов для sol_2

```sh
pytest tests/sol_2_test.py
```

### Запуск всех тестов

```sh
pytest
```

### Очистка виртуальной среды

```sh
rmdir /s /q venv
del *.egg-info /s /q
```