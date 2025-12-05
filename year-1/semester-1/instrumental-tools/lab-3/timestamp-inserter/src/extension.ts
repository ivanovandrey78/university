// extension.ts

const vscode = require('vscode');

/**
 * Основная функция активации расширения
 * Вызывается VS Code при загрузке плагина
 * @param {vscode.ExtensionContext} context - контекст расширения для управления ресурсами
 */
function activate(context) {
    // CREATE STATUS BAR
    
    /**
     * Создает элемент статус-бара в левой части интерфейса VS Code
     * @type {vscode.StatusBarItem}
     */
    const statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left);
    
    /**
     * Обновляет отображаемое время в статус-баре
     * Форматирует часы и минуты с ведущими нулями
     */
    function updateTime() {
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        statusBar.text = `${hours}:${minutes}`;
    }
    
    // Инициализация и запуск периодического обновления
    updateTime(); // Первоначальное отображение
    setInterval(updateTime, 60000); // Обновление каждые 60 секунд
    statusBar.show(); // Отображение статус-бара в интерфейсе
    
    /**
     * Регистрирует команду 'timestamp.insert' для вставки временной метки
     * @type {vscode.Disposable}
     */
    const insertCommand = vscode.commands.registerCommand('timestamp.insert', () => {
        // Проверка наличия активного текстового редактора
        const editor = vscode.window.activeTextEditor;
        
        if (!editor) {
            // Если редактор не активен, команда не выполняется
            return;
        }

        // Доступные форматы для отображения в меню выбора
        const timeFormats = [
            'HH:MM',                // Только время (14:30)
            'YYYY-MM-DD',           // Дата в ISO формате (2024-11-21)
            'DD.MM.YYYY HH:MM:SS'   // Полная дата и время (21.11.2024 14:30:45)
        ];

        // Отображение меню выбора формата (QuickPick)
        vscode.window.showQuickPick(timeFormats)
            .then(selectedFormat => {
                // Проверка: пользователь сделал выбор и редактор все еще активен
                if (!selectedFormat || !editor) {
                    return;
                }

                const now = new Date();
                let formattedTime = '';
                
                // Выбор функции форматирования в зависимости от выбора пользователя
                switch (selectedFormat) {
                    case 'HH:MM':
                        formattedTime = formatTimeOnly(now);
                        break;
                        
                    case 'YYYY-MM-DD':
                        formattedTime = formatDateOnly(now);
                        break;
                        
                    case 'DD.MM.YYYY HH:MM:SS':
                        formattedTime = formatDateTime(now);
                        break;
                }

                // Вставка отформатированного текста в редактор
                insertTextAtCursor(editor, formattedTime);
            });
    });

    // Делаем статус-бар кликабельным
    statusBar.command = 'timestamp.insert';
    
    // Регистрация ресурсов для корректного освобождения памяти
    context.subscriptions.push(statusBar, insertCommand);
}

/**
 * Форматирует объект Date в строку времени формата "ЧЧ:ММ"
 * @param {Date} date - объект даты для форматирования
 * @returns {string} отформатированное время (например, "14:30")
 */
function formatTimeOnly(date) {
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

/**
 * Форматирует объект Date в строку даты формата "ГГГГ-ММ-ДД"
 * @param {Date} date - объект даты для форматирования
 * @returns {string} отформатированная дата в ISO формате (например, "2024-11-21")
 */
function formatDateOnly(date) {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Месяцы 0-11
    const day = date.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
}

/**
 * Форматирует объект Date в полную строку даты и времени
 * @param {Date} date - объект даты для форматирования
 * @returns {string} отформатированная дата и время (например, "21.11.2024 14:30:45")
 */
function formatDateTime(date) {
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const seconds = date.getSeconds().toString().padStart(2, '0');
    
    return `${day}.${month}.${year} ${hours}:${minutes}:${seconds}`;
}

/**
 * Вставляет текст в позицию курсора активного редактора
 * @param {vscode.TextEditor} editor - активный текстовый редактор
 * @param {string} text - текст для вставки
 */
function insertTextAtCursor(editor, text) {
    editor.edit(editBuilder => {
        // Замена выделенного текста (или вставка в позицию курсора)
        editBuilder.replace(editor.selection, text);
    });
}

// Экспорт функций для VS Code
module.exports = {
    activate
};