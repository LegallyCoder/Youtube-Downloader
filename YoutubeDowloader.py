import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit
import youtube_dl

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("YouTube Video Downloader")
        
        self.label = QLabel("YouTube Video URL:", self)
        self.label.move(20, 20)
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(150, 20)
        
        self.downloadButton = QPushButton("Download", self)
        self.downloadButton.move(20, 60)
        self.downloadButton.clicked.connect(self.download)
        
        self.textEdit = QTextEdit(self)
        self.textEdit.move(20, 100)
        self.textEdit.resize(300, 200)
        
        self.show()
        
    def download(self):
        video_url = self.lineEdit.text()
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'logger': MyLogger(),
            'outtmpl': '%(title)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            file_path = ydl.prepare_filename(info)
            self.textEdit.setText(file_path)

class MyLogger(object):
    def debug(self, msg):
        pass
    
    def warning(self, msg):
        pass
    
    def error(self, msg):
        print(msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
