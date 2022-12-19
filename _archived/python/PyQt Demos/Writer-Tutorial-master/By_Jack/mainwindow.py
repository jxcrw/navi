#!/usr/bin/env python
# 2015/11/19

import sys
import os
import traceback
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtPrintSupport


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.filename = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Writer by Jak – untitled')
        self.setWindowIcon(QIcon('icons/Color/writer4.png'))
        self.setGeometry(100, 100, 1030, 800)

        # Initialize main app widget
        self.text = QTextEdit(self)
        self.text.setTabStopWidth(20) # Default PyQt tab stop width (80px) too big
        self.text.cursorPositionChanged.connect(self.cursorPosition) # Cursor line/column #
        self.setCentralWidget(self.text)

        # Initialize all app features
        self.initToolbarActions()
        self.initFormatbarActions()

        # Initialize GUI elements
        self.initMenubar()
        self.initToolbar()
        self.initFormatbar()
        self.initStatusbar()

    def initMenubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        edit = menubar.addMenu('&Edit')
        view = menubar.addMenu('&View')

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)

    def initToolbar(self):
        self.toolbar = self.addToolBar('Basic Features')

        # Arrange toolbar actions
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.bulletListAction)
        self.toolbar.addAction(self.numberedListAction)

        self.addToolBarBreak()

    def initFormatbar(self):
        self.formatbar = self.addToolBar('Format')

        # Arrange format bar actions
        fontBox = QFontComboBox(self)
        fontBox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))

        fontSize = QSpinBox(self)
        initial_size = 14
        fontSize.setValue(initial_size)
        self.text.setFontPointSize(initial_size) # Set the starting font size in the app
        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))

        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)

        self.formatbar.addSeparator()

        self.formatbar.addAction(self.fontColorAction)
        self.formatbar.addAction(self.highlightAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(self.boldAction)
        self.formatbar.addAction(self.italicAction)
        self.formatbar.addAction(self.underlineAction)
        self.formatbar.addAction(self.strikethroughAction)
        self.formatbar.addAction(self.superscriptAction)
        self.formatbar.addAction(self.subscriptAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(self.alignLeftAction)
        self.formatbar.addAction(self.alignCenterAction)
        self.formatbar.addAction(self.alignRightAction)
        self.formatbar.addAction(self.alignJustifyAction)

    def initStatusbar(self):
        # Initialize a main status bar for status tips and so on
        # self.statustoolbar = self.addToolBar('Status')
        # TODO: Put the QStatusBar() in a toolbar (due to reported problems with QMainWindow.statusBar() on Mac). https://plashless.wordpress.com/2013/09/14/qt-qmainwindow-statusbar-dont-use-it/
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # self.statustoolbar.addWidget(self.statusbar)
        # self.statustoolbar.addSeparator()

        # Initialize an area for line/column #
        self.line_column_number_bar = QLabel()
        self.line_column_number_bar.setContentsMargins(0, 0, 9, 0)
        # self.statustoolbar.addWidget(self.line_column_number_bar)
        self.statusbar.addPermanentWidget(self.line_column_number_bar)

    def initToolbarActions(self):
        # All of the features in the Basic Features toolbar
        self.newAction = QAction(QIcon('icons/Color/new.png'), '&New', self)
        self.newAction.setStatusTip('Create a new document')
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.triggered.connect(self.new)

        self.openAction = QAction(QIcon('icons/Color/open.png'), '&Open', self)
        self.openAction.setStatusTip('Open an existing document')
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.triggered.connect(self.open)

        self.saveAction = QAction(QIcon('icons/Color/save.png'), '&Save', self)
        self.saveAction.setStatusTip('Save the current document')
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.triggered.connect(self.save)

        self.printAction = QAction(QIcon('icons/Color/print.png'), '&Print', self)
        self.printAction.setStatusTip('Print the current document')
        self.printAction.setShortcut('Ctrl+P')
        self.printAction.triggered.connect(self.print)

        self.previewAction = QAction(QIcon('icons/Color/preview.png'), 'Pre&view', self)
        self.previewAction.setStatusTip('Preview the current document')
        self.previewAction.setShortcut('Ctrl+Shift+P')
        self.previewAction.triggered.connect(self.preview)

        self.cutAction = QAction(QIcon('icons/Color/cut.png'), 'Cu&t', self)
        self.cutAction.setStatusTip('Cut to clipboard')
        self.cutAction.setShortcut('Ctrl+X')
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QAction(QIcon('icons/Color/copy.png'), '&Copy', self)
        self.copyAction.setStatusTip('Copy to clipboard')
        self.copyAction.setShortcut('Ctrl+C')
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QAction(QIcon('icons/Color/paste.png'), '&Paste', self)
        self.pasteAction.setStatusTip('Paste from clipboard')
        self.pasteAction.setShortcut('Ctrl+V')
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QAction(QIcon('icons/Color/undo.png'), '&Undo', self)
        self.undoAction.setStatusTip('Undo last action')
        self.undoAction.setShortcut('Ctrl+Z')
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QAction(QIcon('icons/Color/redo.png'), '&Redo', self)
        self.redoAction.setStatusTip('Redo last undone action')
        self.redoAction.setShortcut('Ctrl+Y')
        self.redoAction.triggered.connect(self.text.redo)

        self.bulletListAction = QAction(QIcon('icons/Color/bullet.png'), 'Insert bullet list', self)
        self.bulletListAction.setStatusTip('Insert a bullet list')
        self.bulletListAction.setShortcut('Ctrl+Shift+B')
        self.bulletListAction.triggered.connect(self.bulletList)

        self.numberedListAction = QAction(QIcon('icons/Color/number.png'), 'Insert numbered list', self)
        self.numberedListAction.setStatusTip('Insert a numbered list')
        self.numberedListAction.setShortcut('Ctrl+Shift+L')
        self.numberedListAction.triggered.connect(self.numberedList)

    def initFormatbarActions(self):
        self.fontColorAction = QAction(QIcon('icons/Color/font-color.png'), 'Font Color', self)
        self.fontColorAction.setStatusTip('Change the font color')
        self.fontColorAction.triggered.connect(self.setFontColor)

        self.highlightAction = QAction(QIcon('icons/Color/highlight.png'), 'Highlight Color', self)
        self.highlightAction.setStatusTip('Change the highlight color')
        self.highlightAction.triggered.connect(self.highlight)

        self.boldAction = QAction(QIcon('icons/Color/bold.png'), 'Bold (Ctrl+B)', self)
        self.boldAction.setStatusTip('Bold (Ctrl+B)')
        self.boldAction.setShortcut('Ctrl+B')
        self.boldAction.triggered.connect(self.bold)

        self.italicAction = QAction(QIcon('icons/Color/italic.png'), 'Italic (Ctrl+I)', self)
        self.italicAction.setStatusTip('Italic (Ctrl+I)')
        self.italicAction.setShortcut('Ctrl+I')
        self.italicAction.triggered.connect(self.italic)

        self.underlineAction = QAction(QIcon('icons/Color/underline.png'), 'Underline (Ctrl+U)', self)
        self.underlineAction.setStatusTip('Underline (Ctrl+U)')
        self.underlineAction.setShortcut('Ctrl+U')
        self.underlineAction.triggered.connect(self.underline)

        self.strikethroughAction = QAction(QIcon('icons/Color/strike.png'), 'Strikethrough', self)
        self.strikethroughAction .setStatusTip('Strikethrough')
        self.strikethroughAction .triggered.connect(self.strikethrough)

        self.superscriptAction = QAction(QIcon('icons/Color/superscript.png'), 'Superscript (Ctrl+Shift+=)', self)
        self.superscriptAction.setStatusTip('Superscript (Ctrl+Shift+=)')
        self.superscriptAction.setShortcut('Ctrl+Shift+=')
        self.superscriptAction.triggered.connect(self.superscript)

        self.subscriptAction = QAction(QIcon('icons/Color/subscript.png'), 'Subscript (Ctrl+=)', self)
        self.subscriptAction.setStatusTip('Subscript (Ctrl+=)')
        self.subscriptAction.setShortcut('Ctrl+=')
        self.subscriptAction.triggered.connect(self.subscript)

        self.alignLeftAction = QAction(QIcon('icons/Color/align-left.png'), 'Align Left (Ctrl+L)', self)
        self.alignLeftAction.setStatusTip('Left Align (Ctrl+L)')
        self.alignLeftAction.setShortcut('Ctrl+L')
        self.alignLeftAction.triggered.connect(lambda left: self.text.setAlignment(Qt.AlignLeft))

        self.alignCenterAction = QAction(QIcon('icons/Color/align-center.png'), 'Center (Ctrl+E)', self)
        self.alignCenterAction.setStatusTip('Center (Ctrl+E)')
        self.alignCenterAction.setShortcut('Ctrl+E')
        self.alignCenterAction.triggered.connect(lambda center: self.text.setAlignment(Qt.AlignCenter))

        self.alignRightAction = QAction(QIcon('icons/Color/align-right.png'), 'Align Right (Ctrl+R)', self)
        self.alignRightAction.setStatusTip('Right Align (Ctrl+R)')
        self.alignRightAction.setShortcut('Ctrl+R')
        self.alignRightAction.triggered.connect(lambda right: self.text.setAlignment(Qt.AlignRight))

        self.alignJustifyAction = QAction(QIcon('icons/Color/align-justify.png'), 'Justify (Ctrl+J)', self)
        self.alignJustifyAction.setStatusTip('Justify (Ctrl+J)')
        self.alignJustifyAction.setShortcut('Ctrl+J')
        self.alignJustifyAction.triggered.connect(lambda justify: self.text.setAlignment(Qt.AlignJustify))


    # Define all of the necessary slots
    def new(self):
        spawn = Main(self)
        spawn.show()

    def open(self):
        # Get filename and show only .writer files
        # self.filename = QFileDialog.getOpenFileName(self, 'Open File', '.', '(*.writer)')
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', '.')[0]

        if self.filename:
            with open(self.filename, 'rt') as file:
                self.text.setText(file.read())

    def save(self):
        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self, 'Save File', '.', '(*.html)')[0]

        # Store text file as html
        if self.filename:
            basename = os.path.basename(self.filename)
            self.setWindowTitle('Writer by Jak – ' + basename)

            with open(self.filename, 'wt') as file:
                file.write(self.text.toHtml())

    def preview(self):
        # TODO: Customize the print preview dialog to use your own icons.
        preview = QtPrintSupport.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def print(self):
        printdialog = QtPrintSupport.QPrintDialog()

        if printdialog.exec_() == QDialog.Accepted:
            self.text.document().print_(printdialog.printer())

    def bulletList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QTextListFormat.ListDisc)

    def numberedList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QTextListFormat.ListDecimal)

    def cursorPosition(self):
        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber()

        self.line_column_number_bar.setText('Line: {} | Column: {}'.format(line, column))

    def setFontColor(self):
        color = QColorDialog.getColor()
        self.text.setTextColor(color)

    def highlight(self):
        color = QColorDialog.getColor()
        self.text.setTextBackgroundColor(color)

    def bold(self):
        if self.text.fontWeight() == QFont.Bold:
            self.text.setFontWeight(QFont.Normal)
        else:
            self.text.setFontWeight(QFont.Bold)

    def italic(self):
        state = self.text.fontItalic()
        self.text.setFontItalic(not state)

    def underline(self):
        state = self.text.fontUnderline()
        self.text.setFontUnderline(not state)

    def strikethrough(self):
        fmt = self.text.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.text.setCurrentCharFormat(fmt)

    def superscript(self):
        fmt = self.text.currentCharFormat()
        align = fmt.verticalAlignment()

        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

    def subscript(self):
        fmt = self.text.currentCharFormat()
        align = fmt.verticalAlignment()

        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSubScript)
        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

def main():
    # TODO: Change icon of app in Windows taskbar
    app = QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
