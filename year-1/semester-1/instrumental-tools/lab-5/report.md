# Лабораторная работа №5
## Знакомство с CI/CD. Настройка GitHub Actions для запуска Unit-тестов

---

### 1. Цель работы

Настроить автоматический запуск unit-тестов проекта при каждом **git push** кода в репозитории, используя систему (CI) GitHub Actions. Тесты должны выполняться на двух операционных системах: Ubuntu и Windows.

### 2. Выполнение работы

#### 2.1 Содержание файла `.github/workflows/main.yml`
```yaml
name: Python Unittests CI

on:
  push:
    branches: [ "main" ]

jobs:
  test:
    strategy:
      # ОС: Ubuntu и Windows
      matrix:
        os: [ubuntu-latest, windows-latest]

    runs-on: ${{ matrix.os }}

    steps:
      # 1. Download the code from the repository
      - name: Checkout repository
        uses: actions/checkout@v4

      # 2. Install Python on local machine
      - name: Set up Python
        uses: actions/setup-python@v5

      #3. Run your unit tests with unittest
      - name: Run unit tests
        run: python -m unittest discover -s tests -p "test_*.py" -v
```

#### 2.2 Объяснение ключевых элементов конфигурации

1. **Триггер (`on: push`)**: Workflow активируется автоматически при каждом пуше в ветку `main`.
2. **Матрица стратегии: Позволяет запустить на двух операционных системах: `ubuntu-latest` и `windows-latest`.
3. **Основные шаги (steps)**:
    - `Checkout repository`: Клонирует код репозитория на раннер.
    - `Install Python`: Устанавливает последнюю стабильную версию Python 3.
    - `Run unit tests`: Выполняет команду для запуска unit-тестов, которая ищет все файлы с паттерном `test_*.py` в папке `tests`.

### 3. Вывод

В ходе лабораторной работы был успешно настроен процесс непрерывной интеграции с помощью GitHub Actions. Созданный workflow автоматически проверяет код на корректность при каждом обновлении репозитория, запуская unit-тесты на двух разных операционных системах: Ubuntu, Windows.

---

Скриншот выполненой работы:

![Отчёт](./screenshots/photo_2025-12-19_16-28-39.jpg)