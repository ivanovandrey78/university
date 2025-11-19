import * as vscode from 'vscode';

interface PomodoroSession {
    type: 'work' | 'break';
    duration: number;
    timeLeft: number;
    isActive: boolean;
}

export function activate() {
    vscode.window.showInformationMessage('Плагин запущен!');
}