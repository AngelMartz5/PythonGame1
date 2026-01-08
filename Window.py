import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from PySide6.QtCore import Qt, QRect
from __feature__ import snake_case, true_property
from Objects import GameObject

# --- 2. LA VENTANA (Igual que antes) ---
class MyGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_fixed_size(500, 500)
        self.style_sheet = "background: #242526;"
        self.all_objects = []

    def add_game_object(self, obj_data):
        visual = QFrame(self)
        visual.style_sheet = f"background-color: {obj_data.color}; border: 1px solid white;"
        visual.geometry = QRect(obj_data.x, obj_data.y, obj_data.w, obj_data.h)
        visual.show()
        
        self.all_objects.append(obj_data)