from PySide6.QtWidgets import QMainWindow

from PySide6.QtCore import QPropertyAnimation, QRect, QThread
from PySide6.QtGui import QPixmap
from file_class.window01_ui import Ui_MainWindow
import time

duration_animation = 2000

class AnimationThread(QThread):
    def __init__(self, animation):
        super().__init__()
        self.animation = animation

    def run(self):
        self.animation.start()
        while self.animation.state() == QPropertyAnimation.Running:
            self.animation.setCurrentTime(self.animation.currentTime() + 50)  # Actualizar la posición
            time.sleep(0.1)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        # Configurar la interfaz de usuario
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # -----------------------> Animacion 01 <--------------------
        
        self.ui.label_animation01.setPixmap(QPixmap('images/cube01.png'))
        self.ui.label_animation01.setScaledContents(True)
        
        self.animation01 = QPropertyAnimation(self.ui.label_animation01, b'geometry')
        
        self.animation01.setStartValue(QRect(
            300,  # Mantener x constante
            0,  # Y inicia en la parte superior
            self.ui.label_animation01.width(),
            self.ui.label_animation01.height()
        ))
        
        self.animation01.setEndValue(QRect(
            300,  # Mantener x constante
            self.height() - self.ui.label_animation01.height(),  # Y termina en la parte inferior
            self.ui.label_animation01.width(),
            self.ui.label_animation01.height()
        ))
        
        self.animation01.setDuration(duration_animation)
        self.animation01.setLoopCount(50)
        
        # -----------------------> Animacion 02 <--------------------

        self.ui.label_animation02.setPixmap(QPixmap('images/cube02.png'))
        self.ui.label_animation02.setScaledContents(True)
        
        self.animation02 = QPropertyAnimation(self.ui.label_animation02, b'geometry')
        
        self.animation02.setStartValue(QRect(
            0,  # Mantener x constante
            300,  # Y inicia en la parte superior
            self.ui.label_animation02.width(),
            self.ui.label_animation02.height()
        ))
        
        self.animation02.setEndValue(QRect(
            self.height() - self.ui.label_animation02.height(),  # Mantener x constante
            300,  # Y termina en la parte inferior
            self.ui.label_animation02.width(),
            self.ui.label_animation02.height()
        ))
        
        self.animation02.setDuration(duration_animation)
        self.animation02.setLoopCount(50)
        
        
        # Crear hilos para las animaciones
        self.thread1 = AnimationThread(self.animation01)
        self.thread2 = AnimationThread(self.animation02)

        # Iniciar los hilos
        self.thread1.start()
        self.thread2.start()

         

        
