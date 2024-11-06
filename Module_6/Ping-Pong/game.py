import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
SCREEN_TITLE = "Pong Game"
MOVEMENT_SPEED = 5
ZERO_BAR_y = 20
class Ball (arcade.Sprite):
    def __init__(self):
        super().__init__('ball.gif',0.15)
        self.change_x = 2.5
        self.change_y = 2

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right>=SCREEN_WIDTH or self.left<=0:
            self.change_x = - self.change_x
        if self.top>=SCREEN_HEIGTH or self.bottom<=0:
            self.change_y = - self.change_y
class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.gif', 0.5)

    def update(self):
        self.center_x +=self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class Game (arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH/2
        self.bar.center_y = SCREEN_HEIGTH/5
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGTH/2


    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self,delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
            self.ball.change_x = -self.ball.change_x
        if self.ball.bottom<=ZERO_BAR_y:
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.bar.change_x =5
        if key == arcade.key.LEFT:
            self.bar.change_x =-5

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

if __name__=='__main__':
    windows = Game(SCREEN_WIDTH, SCREEN_HEIGTH, SCREEN_TITLE)
    arcade.run()
