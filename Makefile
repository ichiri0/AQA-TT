# Переменные
PYTHON = python3
PIP = pip
VENV_DIR = venv

# Псевдонимы для выполнения команд
SOL_1 = app/sol_1.py
SOL_1_TEST = tests/sol_1_test.py
SOL_2 = app/sol_2.py
SOL_2_TEST = tests/sol_2_test.py
TESTS = tests

# Установить зависимости
install:
	@echo "Установка зависимостей..."
	$(PIP) install -r requirements.txt

# Создать виртуальную среду
venv:
	@echo "Создание виртуальной среды..."
	python3 -m venv $(VENV_DIR)
	@echo "Активируйте среду командой: source $(VENV_DIR)/bin/activate"
	$(PIP) install -r requirements.txt

# Запуск sol_1
run_sol_1:
	@echo "Запуск кода для sol_1..."
	$(PYTHON) $(SOL_1)

# Запуск тестов для sol_1
test_sol_1:
	@echo "Запуск тестов для sol_1..."
	$(PYTHON) -m pytest $(SOL_1_TEST)

# Запуск sol_2
run_sol_2:
	@echo "Запуск кода для sol_2..."
	$(PYTHON) $(SOL_2)

# Запуск тестов для sol_2
test_sol_2:
	@echo "Запуск тестов для sol_2..."
	$(PYTHON) -m pytest $(SOL_2_TEST)

# Запуск всех тестов
test_all:
	@echo "Запуск всех тестов..."
	$(PYTHON) -m pytest

# Очистка виртуальной среды
clean:
	@echo "Удаление виртуальной среды..."
	rm -rf $(VENV_DIR)
	rm -rf *.egg-info