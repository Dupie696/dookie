import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class FlashcardApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Flashcards")
        self.setGeometry(100, 100, 480, 780)  # Adjusted for your specified size

        self.current_card_index = 0
        self.showing_question = True
        self.flashcards = []  # List of (question, answer) tuples

        # Add background images for question and answer
        question_image_path = r"C:\git\dookie\question.png"
        answer_image_path = r"C:\git\dookie\answer.png"

        self.question_background = QPixmap(question_image_path) if os.path.exists(question_image_path) else QPixmap()
        self.answer_background = QPixmap(answer_image_path) if os.path.exists(answer_image_path) else QPixmap()

        # Main layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Background image label
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.question_background.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.setGeometry(0, 0, 480, 780)  # Full window size

        # Overlay text label
        self.card_label = QLabel("Load flashcards to begin", self)
        self.card_label.setWordWrap(True)
        self.card_label.setAlignment(Qt.AlignCenter)
        self.card_label.setFont(QFont("Arial", 16))  # Increase font size
        self.card_label.setStyleSheet("background-color: rgba(247, 243, 235, 180); border-radius: 10px;")
        self.card_label.setGeometry(100, 220, 260, 400)  # Positioning in the middle

        # Control buttons
        self.flip_button = QPushButton("Flip", self)
        self.flip_button.clicked.connect(self.flip_card)
        self.layout.addWidget(self.flip_button)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_card)
        self.layout.addWidget(self.next_button)

        self.load_button = QPushButton("Load Flashcards", self)
        self.load_button.clicked.connect(self.load_flashcards)
        self.layout.addWidget(self.load_button)

    def load_flashcards(self):
        """Load flashcards from a text file with each line as 'question|answer'."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Flashcards File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'r') as f:
                self.flashcards = [tuple(line.strip().split('|')) for line in f if '|' in line]

            if self.flashcards:
                self.current_card_index = 0
                self.showing_question = True
                self.update_card()
            else:
                self.card_label.setText("No valid flashcards found in the file.")

    def flip_card(self):
        """Flip between question and answer."""
        if self.flashcards:
            self.showing_question = not self.showing_question
            self.update_card()

    def next_card(self):
        """Move to the next flashcard."""
        if self.flashcards:
            self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)
            self.showing_question = True
            self.update_card()

    def update_card(self):
        """Update the displayed text based on the current state."""
        if self.flashcards:
            question, answer = self.flashcards[self.current_card_index]
            if self.showing_question:
                self.background_label.setPixmap(self.question_background.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                self.card_label.setText(question)
            else:
                self.background_label.setPixmap(self.answer_background.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                self.card_label.setText(answer)
        else:
            self.background_label.clear()
            self.card_label.setText("No flashcards loaded.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlashcardApp()
    window.show()
    sys.exit(app.exec_())
