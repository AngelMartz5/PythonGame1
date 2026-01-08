class GameObject:
    def __init__(self, game_window, x=50, y=50, w=30, h=30, color="black"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.visual_frame = None 
        game_window.add_game_object(self)

class Pointer(GameObject):
    def __init__(self, game_window, x=50, y=50, w=30, h=30, color="black"):
        super().__init__(game_window, x, y, w, h, color)
    
    def move_to(self, target_x, target_y):
        # Mueve el objeto directamente a una posición 
        self.x = target_x
        self.y = target_y
        if self.visual_frame:
            self.visual_frame.move(self.x, self.y)

class Collisionables(GameObject):
    def __init__(self, game_window, x=50, y=50, w=30, h=30, color="blue"):
        super().__init__(game_window, x, y, w, h, color)

class Person(Collisionables):
    def __init__(self, game_window, x=50, y=50, w=30, h=30, color="purple"):
        super().__init__(game_window, x, y, w, h, color)
    
    def movement(self,dx,dy):
        self.x += dx
        self.y += dy
        
        # 2. Actualizamos lo VISUAL usando la conexión que guardamos
        if self.visual_frame:
            self.visual_frame.move(self.x, self.y)


class Player(Person):
    def __init__(self, game_window, x=100, y=100, w = 30, h = 30, color="gray"):
        super().__init__(game_window, x, y, w, h, color)