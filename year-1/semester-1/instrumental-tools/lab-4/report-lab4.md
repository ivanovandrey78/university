# Отчет по лабораторной работе №4
## Написание Unit-тестов для геометрического калькулятора

## 1. Цели и задачи тестирования

### Основные цели:
1. **Проверка корректности** математических вычислений площадей и периметров геометрических фигур
2. **Обнаружение дефектов** на ранних этапах разработки
3. **Документирование поведения** системы

### Задачи тестирования:
- Создание набора unit-тестов для всех функций модуля
- Тестирование валидных сценариев использования
- Тестирование граничных случаев (нулевые значения)
- Тестирование обработки ошибок (невалидные входные данные)

---

## 2. Описание тестируемого продукта

### Функциональность продукта:
Программа представляет собой модуль для вычисления геометрических параметров четырех фигур:

1. **Круг**:
   - Вычисление площади круга: `S = π * r * r`
   - Вычисление длины окружности: `P = 2 * pi * r`

2. **Прямоугольник**:
   - Вычисление площади: `S = a * b`
   - Вычисление периметра: `P = 2 * (a + b)`

3. **Квадрат**:
   - Вычисление площади: `S = a * a`
   - Вычисление периметра: `P = 4 * a`

4. **Треугольник**:
   - Вычисление площади: `S = (a * h) / 2`
   - Вычисление периметра: `P = a + b + c`

### Требования к продукту:
- Корректность математических вычислений
- Обработка некорректных входных данных (отрицательные значения)
- Работа с целыми и дробными числами
- Четкая документация функций

---

## 3. Область тестирования

### Тестируемые компоненты:
| Компонент | Функции | Количество тестов |
|-----------|---------|-------------------|
| `circle.py` | `area(r)`, `perimeter(r)` | 8 тестов |
| `rectangle.py` | `area(a, b)`, `perimeter(a, b)` | 12 тестов |
| `square.py` | `area(a)`, `perimeter(a)` | 10 тестов |
| `triangle.py` | `area(a, h)`, `perimeter(a, b, c)` | 14 тестов |

### Итого: 4 модуля, 8 функций, 44 unit-теста

### Границы тестирования:
- **Включено**: математическая логика, обработка входных данных, документация
- **Исключено**: пользовательский интерфейс, интеграция с другими системами

---

## 4. Стратегия тестирования

### Типы тестирования:
1. **Функциональное тестирование**:
   - Проверка соответствия результатов математическим формулам
   - Тестирование всех объявленных функций

2. **Тестирование граничных значений**:
   - Нулевые значения параметров
   - Большие числовые значения
   - Дробные числа

3. **Негативное тестирование**:
   - Передача отрицательных значений
   - Проверка генерации исключений

4. **Модульное тестирование**:
   - Изолированное тестирование каждой функции
   - Использование фреймворка unittest

### Методы тестирования:
- **Автоматизированное тестирование** с использованием Python unittest
- **Ручное тестирование** для проверки специфических сценариев

### Техники тестирования:
- **Эквивалентное разбиение**: валидные/невалидные значения
- **Анализ граничных значений**: минимум, ноль, максимум

---

## 5. Критерии приемки

### Условия успешного завершения тестирования:

1. **Полное покрытие функционала**:
   - Все 8 функций протестированы
   - Каждая функция имеет как минимум 4 теста (нормальный, граничный, негативный)

2. **Критерии качества кода**:
   - 100% тестов проходят успешно
   - Отсутствие необработанных исключений
   - Корректная обработка ошибок

3. **Критерии документирования**:
   - Все тесты имеют понятные названия и документацию

4. **Технические критерии**:
   - Тесты могут быть запущены одной командой
   - Результаты тестирования понятны и интерпретируемы

---

## 6. Ожидаемые результаты

### Метрики качества:
| Метрика | Целевое значение |
|---------|------------------|
| Процент прохождения тестов | 100% |
| Покрытие функций тестами | 100% |
| Количество тестов на функцию | >= 4 |
| Время выполнения всех тестов | < 0.2 секунды |

### Документационные результаты:
1. **Отчет о тестировании** (данный документ)
2. **Протокол выполнения тестов** с детализацией результатов
3. **Лог ошибок** (если будут обнаружены дефекты)

### Ожидаемые артефакты:
- Набор из 42 unit-тестов
- Скрипт для запуска всех тестов
- Документация по запуску и использованию тестов
- Рекомендации по улучшению кода (если необходимо)

---

## 7. Актуальные результаты тестирования

### Статус тестирования:
- ✅ **Тестирование завершено** - 05.12.2025
- ✅ **Все тесты написаны** - 44 unit-теста
- ✅ **Тесты выполнены успешно** - 44/44 пройдено
- ✅ **Критерии приемки выполнены** - 100% успеха

### Результаты выполнения тестов:

#### Для модуля `circle.py`:
```text
test_area_large_radius (tests.test_circle.CircleTestCase.test_area_large_radius)
Тест площади круга с большим радиусом ... ok
test_area_negative_radius (tests.test_circle.CircleTestCase.test_area_negative_radius)
Тест площади круга с отрицательным радиусом ... ok
test_area_normal_radius (tests.test_circle.CircleTestCase.test_area_normal_radius)
Тест площади круга с нормальным радиусом ... ok
test_area_zero_radius (tests.test_circle.CircleTestCase.test_area_zero_radius)
Тест площади круга с нулевым радиусом ... ok
test_perimeter_large_radius (tests.test_circle.CircleTestCase.test_perimeter_large_radius)
Тест длины окружности с большим радиусом ... ok
test_perimeter_negative_radius (tests.test_circle.CircleTestCase.test_perimeter_negative_radius)
Тест длины окружности с отрицательным радиусом ... ok
test_perimeter_normal_radius (tests.test_circle.CircleTestCase.test_perimeter_normal_radius)
Тест длины окружности с нормальным радиусом ... ok
test_perimeter_zero_radius (tests.test_circle.CircleTestCase.test_perimeter_zero_radius)
Тест длины окружности с нулевым радиусом ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.010s

OK
```

#### Для модуля `rectangle.py`:
```text
test_area_both_zero (tests.test_rectangle.RectangleTestCase.test_area_both_zero)
Тест площади прямоугольника с нулевыми сторонами ... ok
test_area_negative_side_a (tests.test_rectangle.RectangleTestCase.test_area_negative_side_a)
Тест площади прямоугольника с отрицательной первой стороной ... ok
test_area_negative_side_b (tests.test_rectangle.RectangleTestCase.test_area_negative_side_b)
Тест площади прямоугольника с отрицательной второй стороной ... ok
test_area_normal (tests.test_rectangle.RectangleTestCase.test_area_normal)
Тест площади прямоугольника с нормальными сторонами ... ok
test_area_zero_side_a (tests.test_rectangle.RectangleTestCase.test_area_zero_side_a)
Тест площади прямоугольника с нулевой первой стороной ... ok
test_area_zero_side_b (tests.test_rectangle.RectangleTestCase.test_area_zero_side_b)
Тест площади прямоугольника с нулевой второй стороной ... ok
test_perimeter_both_zero (tests.test_rectangle.RectangleTestCase.test_perimeter_both_zero)
Тест периметра прямоугольника с нулевыми сторонами ... ok
test_perimeter_negative_side (tests.test_rectangle.RectangleTestCase.test_perimeter_negative_side)
Тест периметра прямоугольника с отрицательной стороной ... ok
test_perimeter_normal (tests.test_rectangle.RectangleTestCase.test_perimeter_normal)
Тест периметра прямоугольника с нормальными сторонами ... ok
test_perimeter_square (tests.test_rectangle.RectangleTestCase.test_perimeter_square)
Тест периметра квадрата (частный случай прямоугольника) ... ok
test_perimeter_zero_side_a (tests.test_rectangle.RectangleTestCase.test_perimeter_zero_side_a)
Тест периметра прямоугольника с нулевой первой стороной ... ok
test_perimeter_zero_side_b (tests.test_rectangle.RectangleTestCase.test_perimeter_zero_side_b)
Тест периметра прямоугольника с нулевой второй стороной ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.015s

OK
```

#### Для модуля `square.py`:
```text
test_area_decimal (tests.test_square.SquareTestCase.test_area_decimal)
Тест площади квадрата с дробной стороной ... ok
test_area_large (tests.test_square.SquareTestCase.test_area_large)
Тест площади квадрата с большой стороной ... ok
test_area_negative (tests.test_square.SquareTestCase.test_area_negative)
Тест площади квадрата с отрицательной стороной ... ok
test_area_normal (tests.test_square.SquareTestCase.test_area_normal)
Тест площади квадрата с нормальной стороной ... ok
test_area_zero (tests.test_square.SquareTestCase.test_area_zero)
Тест площади квадрата с нулевой стороной ... ok
test_perimeter_decimal (tests.test_square.SquareTestCase.test_perimeter_decimal)
Тест периметра квадрата с дробной стороной ... ok
test_perimeter_large (tests.test_square.SquareTestCase.test_perimeter_large)
Тест периметра квадрата с большой стороной ... ok
test_perimeter_negative (tests.test_square.SquareTestCase.test_perimeter_negative)
Тест периметра квадрата с отрицательной стороной ... ok
test_perimeter_normal (tests.test_square.SquareTestCase.test_perimeter_normal)
Тест периметра квадрата с нормальной стороной ... ok
test_perimeter_zero (tests.test_square.SquareTestCase.test_perimeter_zero)
Тест периметра квадрата с нулевой стороной ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.013s

OK
```

#### Для модуля `triangle.py`:
```text
test_area_both_zero (tests.test_triangle.TriangleTestCase.test_area_both_zero)
Тест площади треугольника с нулевыми основанием и высотой ... ok
test_area_decimal (tests.test_triangle.TriangleTestCase.test_area_decimal)
Тест площади треугольника с дробными параметрами ... ok
test_area_negative_base (tests.test_triangle.TriangleTestCase.test_area_negative_base)
Тест площади треугольника с отрицательным основанием ... ok
test_area_negative_height (tests.test_triangle.TriangleTestCase.test_area_negative_height)
Тест площади треугольника с отрицательной высотой ... ok
test_area_normal (tests.test_triangle.TriangleTestCase.test_area_normal)
Тест площади треугольника с нормальными параметрами ... ok
test_area_zero_base (tests.test_triangle.TriangleTestCase.test_area_zero_base)
Тест площади треугольника с нулевым основанием ... ok
test_area_zero_height (tests.test_triangle.TriangleTestCase.test_area_zero_height)
Тест площади треугольника с нулевой высотой ... ok
test_perimeter_all_zero (tests.test_triangle.TriangleTestCase.test_perimeter_all_zero)
Тест периметра треугольника с нулевыми сторонами ... ok
test_perimeter_decimal (tests.test_triangle.TriangleTestCase.test_perimeter_decimal)
Тест периметра треугольника с дробными сторонами ... ok
test_perimeter_equilateral (tests.test_triangle.TriangleTestCase.test_perimeter_equilateral)
Тест периметра равностороннего треугольника ... ok
test_perimeter_isosceles (tests.test_triangle.TriangleTestCase.test_perimeter_isosceles)
Тест периметра равнобедренного треугольника ... ok
test_perimeter_negative_side (tests.test_triangle.TriangleTestCase.test_perimeter_negative_side)
Тест периметра треугольника с отрицательной стороной ... ok
test_perimeter_normal (tests.test_triangle.TriangleTestCase.test_perimeter_normal)
Тест периметра треугольника с нормальными сторонами ... ok
test_perimeter_zero_side (tests.test_triangle.TriangleTestCase.test_perimeter_zero_side)
Тест периметра треугольника с нулевой стороной ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.016s

OK
```

### Сводная статистика:
```
----------------------------------------------------------------------
Всего выполнено тестов: 44
Все тесты пройдены успешно: 44
Проваленных тестов: 0
Ошибок выполнения: 0
Процент успешного выполнения: 100%
----------------------------------------------------------------------
```

### Обнаруженные дефекты:
- ❌ **Дефекты не обнаружены** - все функции работают корректно
- ⚠ **Улучшения**: добавлена проверка на отрицательные значения во все функции

---

## 8. Инструкция по запуску тестов

### Структура проекта:
```
lab-4/
├── src/
│   ├── circle.py
│   ├── rectangle.py
│   ├── square.py
│   └── triangle.py
├── tests/
│   ├── test_circle.py
│   ├── test_rectangle.py
│   ├── test_square.py
│   └── test_triangle.py
├── report-lab4.md
└── README.md
```

### Команды для запуска:

1. **Запуск всех тестов**:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

2. **Запуск тестов для конкретной фигуры**:
```bash
python -m unittest tests.test_circle -v
python -m unittest tests.test_rectangle -v
python -m unittest tests.test_square -v
python -m unittest tests.test_triangle -v
```

---

## 9. Выводы

### Достигнутые результаты:
1. Создан полный набор unit-тестов для геометрического калькулятора
2. Обеспечено 100% покрытие тестируемого функционала
3. Подтверждена корректность математических вычислений
4. Верифицирована обработка граничных случаев и ошибок
5. Документирован процесс тестирования и его результаты

### Качество продукта:
На основе результатов тестирования можно сделать вывод, что модуль геометрического калькулятора:
- **Корректен** - все вычисления соответствуют математическим формулам
- **Надежен** - корректно обрабатывает некорректные входные данные
- **Тестируем** - код хорошо структурирован для автоматизированного тестирования
- **Документирован** - функции имеют полную документацию

---
*Дата выполнения: 06.12.2025*