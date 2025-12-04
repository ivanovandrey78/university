const vscode = require('vscode');

function activate(context) {
    // Create a status bar element on the left side
    const statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left);
    
    // Time update function in the status bar
    function updateTime() {
        const now = new Date();
        // Format
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        statusBar.text = `${hours}:${minutes}`;
    }
    
    // Initial update and start timer (every 60 seconds)
    updateTime();
    setInterval(updateTime, 60000);
    statusBar.show();

    // INSERT
    
    // Registering a team 'timestamp.insert'
    const insertCommand = vscode.commands.registerCommand('timestamp.insert', () => {
        const editor = vscode.window.activeTextEditor;
        
        if (!editor) {
            return;
        }

        const timeFormats = [
            'HH:MM',
            'YYYY-MM-DD',
            'DD.MM.YYYY HH:MM:SS'
        ];

        // Show the format selection menu
        vscode.window.showQuickPick(timeFormats)
            .then(selectedFormat => {
                // If the user has not selected anything or the editor has closed
                if (!selectedFormat || !editor) {
                    return;
                }

                const now = new Date();
                
                let formattedTime = '';
                
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

                insertTextAtCursor(editor, formattedTime);
            });
    });

    statusBar.command = 'timestamp.insert';
    
    context.subscriptions.push(statusBar, insertCommand);
}

function formatTimeOnly(date) {
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

function formatDateOnly(date) {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
}

function formatDateTime(date) {
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const seconds = date.getSeconds().toString().padStart(2, '0');
    
    return `${day}.${month}.${year} ${hours}:${minutes}:${seconds}`;
}

function insertTextAtCursor(editor, text) {
    editor.edit(editBuilder => {
        editBuilder.replace(editor.selection, text);
    });
}

module.exports = {
    activate
};