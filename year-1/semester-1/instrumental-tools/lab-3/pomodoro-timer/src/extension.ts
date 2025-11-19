import * as vscode from 'vscode';

interface PomodoroSession {
    type: 'work' | 'break';
    duration: number;
    timeLeft: number;
    isActive: boolean;
    startTime?: number; // optional
}

let currentSession: PomodoroSession | undefined;
let statusBarItem: vscode.StatusBarItem;

export function activate() {
    statusBarItem = vscode.window.createStatusBarItem(
        vscode.StatusBarAlignment.Right,  // position
        100                               // priority
    );
    statusBarItem.text = "🍅 Ready";
    statusBarItem.show();
}