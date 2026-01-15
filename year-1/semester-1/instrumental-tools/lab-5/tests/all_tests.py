import unittest
import sys
import os

if __name__ == '__main__':
    # Добавляем src в путь
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if os.path.exists(src_path):
        sys.path.insert(0, src_path)

    # Запускаем все тесты из tests/
    tests_dir = os.path.dirname(__file__)

    # Проверяем существование директории
    if not os.path.exists(tests_dir):
        print(f"ОШИБКА: Директория 'tests' не найдена!")
        print(f"Текущая рабочая директория: {os.getcwd()}")
        print(f"Ожидаемый путь к tests: {tests_dir}")
        sys.exit(1)

    # Запускаем тесты
    result = unittest.main(
        module=None,
        argv=['', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v'],
        exit=False
    ).result

    sys.exit(0 if result.wasSuccessful() else 1)