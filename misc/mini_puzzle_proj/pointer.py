class Pointer():
    def __init__(self):
        self.x = 1 
        self.y = 1
        
    def position(self):
        return (self.x, self.y)

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def __str__(self):
        return f"Pointer at position {self.position()}"


