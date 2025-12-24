# Changelog - история изменений

## [1.0.0] - 
### Добавлено
- **Новая функциональность**: Добавлен модуль `rectangle.py` с функциями:
  - `area(a, b)` - вычисление площади прямоугольника
  - `perimeter(a, b)` - вычисление периметра прямоугольника
- **Новая функциональность**: Добавлен модуль `triangle.py` с функциями:
  - `area(a, h)` - вычисление площади треугольника
  - `perimeter(a, b, c)` - вычисление периметра треугольника
- **Система контроля версий**: Создана feature-ветка `new_features_505013` для разработки новой функциональности

### Изменено
- **Исправление**: В функции `perimeter(a, b)` модуля `rectangle.py` исправлена формула вычисления периметра
  - Было: `return a + b`
  - Стало: `return 2 * (a + b)`

### Технические детали
- Клонирован репозиторий geometric_lib
- Создана и активирована ветка для разработки
- Выполнено 2 коммита с сообщениями:
  - `new file add - rectangle.py`
  - `The error with the perimeter calculation ahs been succsessfully fixed`
- Ветка разработки удалена после завершения работы

### Репозиторий
- Исходный код: https://github.com/smartiqaorg/geometric_lib
- Граф коммитов: 
```bash
* 91fde4 (HEAD -> new features_505013) The error with the perimeter calculation has been successfully fixed
* 8cb7f7e new file add - rectangle.py
* cfe7fe0 (origin/main，main) initial commit
* ee8d5ba initial commit
```