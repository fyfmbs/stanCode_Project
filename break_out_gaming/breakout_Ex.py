"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_Ex import BreakoutGraphics

FRAME_RATE = 1200 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    b_r = input('Ball Radius: ')
    if b_r is '':
        b_r = 10
    else:
        b_r = int(b_r)
    b_c = input('Brick Columns: ')
    if b_c is '':
        b_c = 10
    else:
        b_c = int(b_c)
    b_ro = input('Brick Rows: ')
    if b_ro is '':
        b_ro = 10
    else:
        b_ro = int(b_ro)
    p_w = input('Paddle Width: ')
    if p_w is '':
        p_w = 75
    else:
        p_w = int(p_w)

    graphics = BreakoutGraphics(ball_radius=b_r, brick_rows=b_ro, brick_cols=b_c, paddle_width=p_w)
    lives = NUM_LIVES

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if lives == 0 or graphics.score == graphics.total_score:
            graphics.lives = 0
            game_over = graphics.game_over
            graphics.window.add(game_over, x=(graphics.window.width - game_over.width) // 2,
                                y=(graphics.window.height - game_over.height) // 2)
            print('You are done')
            break
        graphics.move_ball()

        graphics.check_wall()
        graphics.check_brick()
        if graphics.check_lives() is False:
            lives -= 1


if __name__ == '__main__':
    main()
