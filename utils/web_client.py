import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class WebClient(QWebEnginePage):
    app = None

    def __init__(self, url):
        if not WebClient.app:
            WebClient.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ""
        self.loadFinished.connect(self.on_load_finished)
        self.load(QUrl(url))
        WebClient.app.exec_()

    def on_load_finished(self):
        self.html = self.toHtml(self.Callable)

    def Callable(self,data):
        self.html = data
        WebClient.app.quit()
