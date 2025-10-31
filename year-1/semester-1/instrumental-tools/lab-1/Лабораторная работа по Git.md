## Ход работы

### 1. Клонирование репозитория
```bash
git clone https://github.com/smartiqaorg/geometric_lib
```

**Результат:**
```bash
$ git clone https://github.com/smartigaorg/geometric_lib
Cloning into 'geometric_lib'.
remote: Enumerating objects: 35, done.
remote: Total 35 (delta 0), reused 0 (delta 0), pack-reused 35 (from 1)
Receiving objects: 100% (35/35), 4.69 KiB | 1.56 MiB/s, done.
Resolving deltas: 100% (5/5), done.
```

*Репозиторий успешно склонирован в локальную директорию*

### 2. Создание и переключение на новую ветку
```bash
git branch new_features_505013
git switch new_features_505013
```

**Результат:**
```bash
Switched to branch 'new_features_505013'
```

*Создана ветка `new_features_505013`  и выполнено переключение с основной ветки *

### 3. Создание и редактирование файла rectangle.py

**Создание файла:**
```bash
touch rectangle.py
```

**Содержание файла после редактирования:**
```python
def area(a, b):
    return a * b

def perimeter(a, b):
    return a + b  
```

### 4. Коммит добавления rectangle.py
```bash
git add rectangle.py
git commit -m "feat: add rectangle.py with area and perimeter functions"
```

**Результат:**
```bash
[new_features_505013 8d0f7e] feat: add rectangle.py with area and perimeter functions
 1 file changed, 5 insertions(+)
 create mode 100644 rectangle.py
```

### 5. Добавление файла triangle.py

**Создание файла:**
```bash
touch triangle.py
```

**Содержание файла:**
```python
def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c
```

### 6. Исправление ошибки в rectangle.py

**Исправленное содержание:**
```python
def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)  # Исправлено: правильная формула периметра
```

### 7. Коммит исправления ошибки
```bash
git add .
git commit -m "fix: correct perimeter calculation in rectangle.py"
```

**Результат:**
```bash
[new_features_505013 f81fde4] fix: correct perimeter calculation in rectangle.py
 2 files changed, 7 insertions(+), 1 deletion(-)
 create mode 100644 triangle.py
```

### 8. Построение графа истории репозитория

```bash
git log --oneline --graph --all
```

**Аргументы команды:**
- `--oneline` - вывод хэша и сообщения каждого коммита на одной строке
- `--graph` - визуализация истории в виде графа
- `--all` - отображение коммитов всех веток репозитория

**Результат:**
```bash
* f81fde4 (HEAD -> new_features_505013) fix: correct perimeter calculation in rectangle.py
* 8d0f7e feat: add rectangle.py with area and perimeter functions
* cfc7fe0 (origin/main, main) initial commit
* e868ba initial commit
```

### 9. Построение графа истории текущей ветки

```bash
git log --oneline --graph 
```

**Результат:**
```bash
* f81fde4 fix: correct perimeter calculation in rectangle.py
* 8d0f7e feat: add rectangle.py with area and perimeter functions
```

*Отображены только коммиты ветки `new_features_505013`, исключая историю `main`*

### 10. Просмотр изменений в коммитах

**Просмотр первого коммита:**
```bash
git show 8d0f7e
```

**Просмотр второго коммита:**
```bash
git show f81fde4
```

*Команда `show` отображает полную информацию о коммите: автор, дата, сообщение и все внесенные изменения*

### 11. Удаление ветки new_features_505013

**Переключение на основную ветку:**
```bash
git switch main
```

**Результат:**
```bash
Switched to branch 'main'
```

**Удаление ветки:**
```bash
git branch -D new_features_505013
```

**Результат:**
```bash
Deleted branch new_features_505013 (was f81fde4).
```
