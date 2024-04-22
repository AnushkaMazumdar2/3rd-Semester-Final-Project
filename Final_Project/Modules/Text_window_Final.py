from PyQt5.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QMessageBox, QPushButton, QDialog, QHBoxLayout, QLabel, QTextEdit, QWidget
from PyQt5 import QtGui, QtCore
import sys
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import *
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from PyQt5.QtWidgets import QApplication , QFileDialog  , QFrame,QComboBox,  QLineEdit, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QPixmap
from keras.models import load_model
from pylab import *
import re
import string
from keras.preprocessing.sequence import pad_sequences
import nltk
nltk.download("stopwords")
nltk.download("punkt")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def test_text(self, input_text, bert_model_path, lstm_model_path, use_bert=True):
        """
        Text Forgery Detection using BERT and LSTM
        :param input_text: Input text to be tested
        :param bert_model_path: Path to the BERT model
        :param lstm_model_path: Path to the LSTM model
        :param use_bert: Boolean indicating whether to use BERT or LSTM
        :return: label [Spam, Not Spam], prob [class probability]
        """
        # Load the model
        if use_bert:
            model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

            # Preprocess text
            tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
            inputs = tokenizer(input_text, return_tensors='tf', padding=True, truncation=True, max_length=128)

            # Predict
            outputs = model(inputs)
            logits = outputs.logits.numpy()
            probabilities = tf.nn.softmax(logits, axis=1).numpy()
            label_index = tf.argmax(probabilities, axis=1).numpy()[0]
            label = "Not Fraud" if label_index == 1 else "Fraud"
            prob = probabilities[0][label_index]

            return label, prob
        else:
                # Load the LSTM model
            model = load_model("G:/model (1).h5")
            stop_words = stopwords.words('english')
            more_stopwords = ['u', 'im', 'c']
            stop_words = stop_words + more_stopwords
            stemmer = nltk.SnowballStemmer("english")
            def clean_text(text):
                text = str(text).lower()
                text = re.sub('\[.*?\]', '', text)
                text = re.sub('https?://\S+|www\.\S+', '', text)
                text = re.sub('<.*?>+', '', text)
                text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
                text = re.sub('\n', '', text)
                text = re.sub('\w*\d\w*', '', text)
                return text
            def preprocess_text(input_text):
                # Clean puntuation, urls, and so on
                text = clean_text(text)
                # Remove stopwords
                text = ' '.join(word for word in text.split(' ') if word not in stop_words)
                # Stemm all the words in the sentence
                text = ' '.join(stemmer.stem(word) for word in text.split(' '))
    
                return text
                
            # Preprocess the input text
            preprocessed_text = preprocess_text(input_text)
            tokenized_text = word_tokenize(preprocessed_text)
            padded_text = pad_sequences(tokenized_text, maxlen=20, padding='post')

            # Make predictions
            predictions = model.predict(padded_text)

            # Interpret predictions
            label = "Fraud" if predictions > 0.5 else "Not Fraud"
            probability = float(predictions)

            return label, probability
            

class Text_Window(QWidget):
    def __init__(self, parent=None, bert_model_path="bert_model.pth", lstm_model_path="G:/model (1).h5"):
        super().__init__()
        self.title = "Text Forgery Detection"
        self.top = 200
        self.left = 500
        self.width = 550
        self.height = 345
        self.file_path = ""
        self.bert_model_path = bert_model_path
        self.lstm_model_path = lstm_model_path
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico"))  # Icon Pic File name
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        
        layout = QVBoxLayout()

        # Add image label
        image_label = QLabel(self)
        pixmap = QtGui.QPixmap("sms.png")
        pixmap = pixmap.scaledToWidth(300)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(QtCore.Qt.AlignCenter)
        image_label.setAlignment(QtCore.Qt.AlignCenter)
        image_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)  # Set size policy
        layout.addWidget(image_label)

        # Add ComboBox to choose between BERT and LSTM
        self.model_combo = QComboBox(self)
        self.model_combo.addItems(["BERT", "LSTM"])
        layout.addWidget(self.model_combo)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Enter text here...")
        layout.addWidget(self.text_edit)

        button_layout = QHBoxLayout()
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setGeometry(QRect(450, 40, 90, 20))
        self.browse_button.setToolTip("<h5>Browse Text from your computer to start the testing!<h5>")
        self.browse_button.setIcon(QtGui.QIcon("698831-icon-105-folder-add-512.png"))
        self.browse_button.setIconSize(QtCore.QSize(15, 15))
        self.browse_button.clicked.connect(self.browse_text_file)
        button_layout.addWidget(self.browse_button)

        self.test_button = QPushButton("Test", self)
        self.test_button.setGeometry(QRect(270, 310, 90, 20))
        self.test_button.setToolTip("<h5>Test whether text is Forged or Not!<h5>")
        self.test_button.setIcon(QtGui.QIcon("698827-icon-101-folder-search-512.png")) #icon Pic File name
        self.test_button.setIconSize(QtCore.QSize(15, 15)) # Icon Pic File name
        self.test_button.clicked.connect(self.on_click)
        button_layout.addWidget(self.test_button)

        layout.addLayout(button_layout)

        self.result_label = QLabel(self)
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.result_label)

        # Add back and quit buttons
        back_quit_layout = QHBoxLayout()
        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(QRect(180, 310, 90, 20))
        self.back_button.setToolTip("<h5>Go back to Previous Menu<h5>")  # Notice using h2 tags From Html
        self.back_button.setIcon(QtGui.QIcon("repeat-pngrepo-com.png")) #icon Pic File name
        self.back_button.setIconSize(QtCore.QSize(15, 15)) # Icon Pic File name
        self.back_button.clicked.connect(self.back_to_Main)
        back_quit_layout.addWidget(self.back_button)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.setGeometry(QRect(360, 310, 90, 20))
        self.quit_button.setToolTip("<h5>Close the program!<h5>")  # Notice using h2 tags From Html
        self.quit_button.setIcon(QtGui.QIcon("cancel-symbol-transparent-9.png")) #icon Pic File name
        self.quit_button.setIconSize(QtCore.QSize(15, 15)) # Icon Pic File name
        self.quit_button.clicked.connect(self.close_main_window)
        back_quit_layout.addWidget(self.quit_button)

        layout.addLayout(back_quit_layout)

        self.setLayout(layout)
        self.show()

        
    def on_model_selected(self):
        selected_model = self.model_combo.currentText()
        if selected_model == "BERT":
            self.use_bert = True
        else:
            self.use_bert = False

    def back_to_Main(self):
        from Main_window_Final import MainWindow
        self.Main_window = MainWindow()
        self.Main_window.show()
        self.close()

    def close_main_window(self):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?", QMessageBox.Cancel | QMessageBox.Close)
        if reply == QMessageBox.Close:
            self.close()

    def browse_text_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text Files (*.txt)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            if file_names:
                file_name = file_names[0]
                with open(file_name, "r") as file:
                    text = file.read()
                    self.text_edit.setText(text)

    @QtCore.pyqtSlot()
    def on_click(self):
        input_text = self.text_edit.toPlainText()
        if not input_text:
            self.show_error_message("Please enter text!")
            return

        # Call the BERT model for prediction
        try:
            self.myThread = Thread()
            label, prob = self.myThread.test_text(input_text,self.bert_model_path, self.lstm_model_path, use_bert=True)
            self.update_result_label(label, prob)
            self.plot_pie_chart(label, prob)
        except Exception as e:
            self.show_error_message(f"Error testing text: {str(e)}")

    def update_result_label(self, label, prob):
        self.result_label.setText(f"Prediction: {label}\nProbability: {prob:.2f}")

    def plot_pie_chart(self, label, prob):
        labels = ['Not Fraud', 'Fraud']
        sizes = [1 - prob, prob]

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(f"Text Forgery Detection: {label}")
        plt.show()

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico"))
        msg.exec_()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = Text_Window()
    sys.exit(App.exec())
