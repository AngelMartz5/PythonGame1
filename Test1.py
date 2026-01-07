# Importaciones necesarias
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from PySide6.QtCore import Qt, QTimer, QRect
# Esto habilita el estilo de escritura con guiones bajos que te gusta
from __feature__ import snake_case, true_property

class MyGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Configuración inicial de la ventana
        self.window_width = 500
        self.window_height = 500
        self.set_fixed_size(self.window_width, self.window_height)
        self.style_sheet = "background: #242526;"
        self.set_window_role("Juego PySide6")

        # 2. Variables del Jugador
        self.player_pos = {"x": 250, "y": 250}
        self.speed = 5
        
        # Creación del objeto visual (el cuadro azul)
        self.player = QFrame(self)
        self.player.style_sheet = "background: blue"
        self.update_player_visual() # Lo colocamos en su sitio inicial

        # 3. Almacén de teclas presionadas
        # Usamos un conjunto (set) para recordar qué teclas están bajadas
        self.keys_pressed = set()

        # 4. EL GAME LOOP (El reemplazo de tu 'while')
        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(16)  # Ejecuta 'game_loop' cada 16ms (~60 FPS)

    def update_player_visual(self):
        # Esta función traduce los números a posición en pantalla
        self.player.geometry = QRect(
            self.player_pos["x"], 
            self.player_pos["y"], 
            20, 20 # Ancho y alto del jugador
        )

    # Evento nativo de Qt cuando PRESIONAS una tecla
    def key_press_event(self, event):
        self.keys_pressed.add(event.key())

    # Evento nativo de Qt cuando SUELTAS una tecla
    def key_release_event(self, event):
        if event.key() in self.keys_pressed:
            self.keys_pressed.remove(event.key())

    # Esta función se ejecuta 60 veces por segundo
    def game_loop(self):
        # Verificamos qué teclas están en nuestro conjunto y movemos
        if Qt.Key.Key_W in self.keys_pressed or Qt.Key.Key_Up in self.keys_pressed:
            self.player_pos["y"] -= self.speed
        
        if Qt.Key.Key_S in self.keys_pressed or Qt.Key.Key_Down in self.keys_pressed:
            self.player_pos["y"] += self.speed
            
        if Qt.Key.Key_A in self.keys_pressed or Qt.Key.Key_Left in self.keys_pressed:
            self.player_pos["x"] -= self.speed
            
        if Qt.Key.Key_D in self.keys_pressed or Qt.Key.Key_Right in self.keys_pressed:
            self.player_pos["x"] += self.speed

        # Salir con ESC
        if Qt.Key.Key_Escape in self.keys_pressed:
            self.close()

        # IMPORTANTE: Aplicar el movimiento visualmente
        self.update_player_visual()

# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MyGameWindow()
    window.show()
    
    # Esto inicia el bucle infinito de Qt de forma correcta
    sys.exit(app.exec())