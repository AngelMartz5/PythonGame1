from Objects import *
from Window import *

# --- 3. EJECUCIÓN ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyGameWindow()
    window.show()
    
    # Jugador
    player = Player(window)

    # Obstáculo
    muro = Collisionables(window)
    

    print(f"Se han creado {len(window.all_objects)} objetos automáticamente.")

    sys.exit(app.exec())