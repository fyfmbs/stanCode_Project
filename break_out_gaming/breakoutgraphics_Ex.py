"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create input
        self.lives = 3
        self.ball_radius = ball_radius
        self.paddle_width = paddle_width
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Create a graphical window, with some extra space.
        window_width = self.brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (self.brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.__paddle = GRect(self.paddle_width, paddle_height)
        self.__paddle.filled = True
        self.window.add(self.__paddle, x=(self.window.width - self.paddle_width) / 2, y=self.window.height -
                                                                                   paddle_offset)
        # Center a filled ball in the graphical window.
        self.__ball = GOval(2 * self.ball_radius, 2 * self.ball_radius)
        self.__ball.filled = True
        self.window.add(self.__ball, x=(self.window.width - 2 * self.ball_radius) / 2,
                        y=(self.window.height - 2 * self.ball_radius) / 2)
        # Default initial velocity for the ball.

        # Initialize our mouse listeners.
        onmousemoved(self.m_pad)
        self.__dx = 0
        self.__dy = 0

        onmouseclicked(self.serve_ball)
        # Draw bricks.
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.__brick = GRect(brick_width, brick_height)
                self.__brick.filled = True
                if i < 2:
                    self.__brick.fill_color = 'red'
                elif 2 <= i < 4:
                    self.__brick.fill_color = 'orange'
                elif 4 <= i < 6:
                    self.__brick.fill_color = 'yellow'
                elif 6 <= i < 8:
                    self.__brick.fill_color = 'blue'
                else:
                    self.__brick.fill_color = 'green'
                self.window.add(self.__brick, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing))
        # Set score
        self.total_score = self.brick_rows * self.brick_cols
        self.score = 0
        print(self.total_score)

        # Create end_game label
        self.game_over = GLabel('GAME OVER')
        self.game_over.font = 'Helvetica-30-bold'
        self.game_over.color = 'tomato'



    def m_pad(self, event):
        if event.x < 0:
            self.__paddle.x = 0
        elif event.x > self.window.width - self.__paddle.width:
            self.__paddle.x = self.window.width - self.__paddle.width
        else:
            self.__paddle.x = event.x
            self.__paddle.y = self.window.height - PADDLE_OFFSET

    def serve_ball(self, event):
        # 連續點會重發
        if self.__dx == 0 and self.__dy == 0 and not self.lives == 0:
            self.__ball.x = self.window.width // 2
            self.__ball.y = self.window.height // 2
            self.__set_ball_velocity()

    def __set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def move_ball(self):
        self.__ball.move(self.__dx, self.__dy)

    def check_wall(self):
        if self.__ball.x < 0 or self.__ball.x + self.__ball.width > self.window.width:
            self.__dx = -self.__dx
            # or self.__ball.y + self.__ball.height > self.window.height
        if self.__ball.y < 0:
            self.__dy = -self.__dy

    def check_brick(self):
        if self.__ball.y < self.window.height / 2:
            re_brick1 = self.window.get_object_at(self.__ball.x, self.__ball.y)
            re_brick2 = self.window.get_object_at(self.__ball.x + self.__ball.width, self.__ball.y)
            re_brick3 = self.window.get_object_at(self.__ball.x, self.__ball.y + self.__ball.height)
            re_brick4 = self.window.get_object_at(self.__ball.x + self.__ball.width, self.__ball.y + self.__ball.height)
            if re_brick1 is not None:
                self.window.remove(re_brick1)
                self.__dy *= -1
                self.score += 1
                print(self.score)
            elif re_brick2 is not None:
                self.window.remove(re_brick2)
                self.__dy *= -1
                self.score += 1
                print(self.score)
            elif re_brick3 is not None:
                self.window.remove(re_brick3)
                self.__dy *= -1
                self.score += 1
                print(self.score)
            elif re_brick4 is not None:
                self.window.remove(re_brick4)
                self.__dy *= -1
                self.score += 1
                print(self.score)
        elif self.__ball.y > self.window.height / 2:
            re_brick1 = self.window.get_object_at(self.__ball.x, self.__ball.y + self.__ball.height)
            re_brick2 = self.window.get_object_at(self.__ball.x + self.__ball.width, self.__ball.y + self.__ball.height)
            if re_brick1 is not None and self.__dy > 0:
                self.__dy *= -1
            elif re_brick2 is not None:
                self.__dy *= -1

    def check_lives(self):
        if self.__ball.y + self.__ball.height > self.window.height:
            self.window.remove(self.__ball)
            self.window.add(self.__ball, x=(self.window.width - self.__ball.width) / 2,
                            y=(self.window.height - self.__ball.height) / 2)
            self.__dx = 0
            self.__dy = 0
            return False

