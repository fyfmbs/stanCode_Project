"""
File: Top Spin on Tennis Court
Name: Shawn Chan
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    I like to play tennis and the Australia Open will start next week,
    so I create a picture to show a nice play.
    """
    # Build a window and set the color of the background
    window = GWindow(600, 700)
    background = GPolygon()
    background.add_vertex((0, 0))
    background.add_vertex((600, 0))
    background.add_vertex((600, 700))
    background.add_vertex((0, 700))
    background.filled = True
    background.fill_color = 'skyblue'
    window.add(background)
    stadium = GLabel('MELBOURNE')
    stadium.font = '-40'
    stadium.color = 'white'
    window.add(stadium, (window.width-stadium.width)/2, window.height-10)
    # draw the periphery of the tennis court
    court = GPolygon()
    court.add_vertex((95, 90))
    court.add_vertex((505, 90))
    court.add_vertex((560, 600))
    court.add_vertex((45, 600))
    court.filled = True
    court.fill_color = 'white'
    window.add(court)

    court1 = GPolygon()
    court1.add_vertex((100, 95))
    court1.add_vertex((500, 95))
    court1.add_vertex((555, 595))
    court1.add_vertex((50, 595))
    court1.filled = True
    court1.fill_color = 'royalblue'
    court1.color = 'royalblue'
    window.add(court1)

    court2 = GPolygon()
    court2.add_vertex((150, 95))
    court2.add_vertex((450, 95))
    court2.add_vertex((500, 595))
    court2.add_vertex((100, 595))
    court2.filled = True
    court2.fill_color = 'white'
    court2.color = 'white'
    window.add(court2)

    court3 = GPolygon()
    court3.add_vertex((155, 95))
    court3.add_vertex((445, 95))
    court3.add_vertex((495, 595))
    court3.add_vertex((105, 595))
    court3.filled = True
    court3.fill_color = 'royalblue'
    court3.color = 'royalblue'
    window.add(court3)

    # draw a court_line
    c_line = GPolygon()
    c_line.add_vertex((149, window.height/2-200))
    c_line.add_vertex((451, window.height/2-200))
    c_line.add_vertex((452, window.height/2-195))
    c_line.add_vertex((148, window.height/2-195))
    c_line.filled = True
    c_line.fill_color = 'white'
    c_line.color = 'white'
    window.add(c_line)

    c_line2 = GPolygon()
    c_line2.add_vertex((124, window.height / 2 + 50))
    c_line2.add_vertex((476, window.height / 2 + 50))
    c_line2.add_vertex((476, window.height / 2 + 55))
    c_line2.add_vertex((124, window.height / 2 + 55))
    c_line2.filled = True
    c_line2.fill_color = 'white'
    c_line2.color = 'white'
    window.add(c_line2)

    c_line3 = GPolygon()
    c_line3.add_vertex((window.width/2-2.5, window.height / 2 - 200))
    c_line3.add_vertex((window.width/2+2.5, window.height / 2 - 200))
    c_line3.add_vertex((window.width/2+2.5, window.height / 2 + 55))
    c_line3.add_vertex((window.width/2-2.5, window.height / 2 + 55))
    c_line3.filled = True
    c_line3.fill_color = 'white'
    c_line3.color = 'white'
    window.add(c_line3)
    # draw two poles to set the net
    pole = GPolygon()
    pole.add_vertex((60, window.height / 2 - 150))
    pole.add_vertex((70, window.height / 2 - 150))
    pole.add_vertex((70, window.height / 2 - 90))
    pole.add_vertex((60, window.height / 2 - 90))
    pole.filled = True
    pole.fill_color = 'burlywood'
    window.add(pole)

    pole2 = GPolygon()
    pole2.add_vertex((window.width - 60, window.height / 2 - 150))
    pole2.add_vertex((window.width - 70, window.height / 2 - 150))
    pole2.add_vertex((window.width - 70, window.height / 2 - 90))
    pole2.add_vertex((window.width - 60, window.height / 2 - 90))
    pole2.filled = True
    pole2.fill_color = 'burlywood'
    window.add(pole2)

    p_head = GOval(10, 10)
    p_head.filled = True
    p_head.fill_color = 'cornsilk'
    window.add(p_head, 60, window.height / 2 - 155)

    p_head2 = GOval(10, 10)
    p_head2.filled = True
    p_head2.fill_color = 'cornsilk'
    window.add(p_head2, window.width - 70, window.height / 2 - 155)
    # draw a net
    net = GPolygon()
    net.add_vertex((p_head.x+10, p_head.y))
    net.add_vertex((window.width/2, window.height/2-148))
    net.add_vertex((window.width/2, window.height/2-143))
    net.add_vertex((p_head.x+10, p_head.y+10))
    net.filled = True
    net.fill_color = 'cornsilk'
    window.add(net)

    net2 = GPolygon()
    net2.add_vertex((p_head2.x, p_head2.y))
    net2.add_vertex((window.width / 2, window.height / 2 - 148))
    net2.add_vertex((window.width / 2, window.height / 2 - 143))
    net2.add_vertex((p_head2.x, p_head2.y + 10))
    net2.filled = True
    net2.fill_color = 'cornsilk'
    window.add(net2)

    net3 = GLine(70, window.height / 2 - 130, window.width - 70, window.height / 2 - 130)
    window.add(net3)
    net4 = GLine(70, window.height / 2 - 110, window.width - 70, window.height / 2 - 110)
    window.add(net4)
    net5 = GLine(70, window.height / 2 - 90, window.width - 70, window.height / 2 - 90)
    window.add(net5)
    net6 = GLine(90, window.height / 2 - 145, 90, window.height / 2 - 90)
    window.add(net6)
    net7 = GLine(110, window.height / 2 - 145, 110, window.height / 2 - 90)
    window.add(net7)
    net8 = GLine(130, window.height / 2 - 145, 130, window.height / 2 - 90)
    window.add(net8)
    net9 = GLine(150, window.height / 2 - 145, 150, window.height / 2 - 90)
    window.add(net9)
    net10 = GLine(170, window.height / 2 - 144, 170, window.height / 2 - 90)
    window.add(net10)
    net11 = GLine(190, window.height / 2 - 144, 190, window.height / 2 - 90)
    window.add(net11)
    net12 = GLine(210, window.height / 2 - 144, 210, window.height / 2 - 90)
    window.add(net12)
    net13 = GLine(230, window.height / 2 - 144, 230, window.height / 2 - 90)
    window.add(net13)
    net14 = GLine(250, window.height / 2 - 144, 250, window.height / 2 - 90)
    window.add(net14)
    net15 = GLine(270, window.height / 2 - 144, 270, window.height / 2 - 90)
    window.add(net15)
    net16 = GLine(290, window.height / 2 - 144, 290, window.height / 2 - 90)
    window.add(net16)
    net17 = GLine(310, window.height / 2 - 144, 310, window.height / 2 - 90)
    window.add(net17)
    net18 = GLine(330, window.height / 2 - 144, 330, window.height / 2 - 90)
    window.add(net18)
    net19 = GLine(350, window.height / 2 - 144, 350, window.height / 2 - 90)
    window.add(net19)
    net20 = GLine(370, window.height / 2 - 144, 370, window.height / 2 - 90)
    window.add(net20)
    net21 = GLine(390, window.height / 2 - 144, 390, window.height / 2 - 90)
    window.add(net21)
    net22 = GLine(410, window.height / 2 - 144, 410, window.height / 2 - 90)
    window.add(net22)
    net23 = GLine(430, window.height / 2 - 144, 430, window.height / 2 - 90)
    window.add(net23)
    net24 = GLine(450, window.height / 2 - 144, 450, window.height / 2 - 90)
    window.add(net24)
    net25 = GLine(470, window.height / 2 - 144, 470, window.height / 2 - 90)
    window.add(net25)
    net26 = GLine(490, window.height / 2 - 144, 490, window.height / 2 - 90)
    window.add(net26)
    net27 = GLine(510, window.height / 2 - 144, 510, window.height / 2 - 90)
    window.add(net27)

    # draw a curve track of the ball
    curve = GArc(370, 410, 90, 190)
    curve.color = 'tomato'
    window.add(curve, 50, 80)

    curve1 = GArc(370, 410, 90, 190)
    curve1.color = 'tomato'
    window.add(curve1, 52, 80)

    curve2 = GArc(370, 410, 90, 190)
    curve2.color = 'tomato'
    window.add(curve2, 54, 80)

    # draw a tennis ball
    ball = GOval(15, 5)
    ball.filled = True
    ball.fill_color = 'yellow'
    window.add(ball, 180, 485)


    # draw two tennis player1
    head = GOval(24, 30)
    head.filled = True
    head.fill_color = 'white'
    window.add(head, 220, 40)
    name = GLabel('F')
    window.add(name, 230, 65)
    body = GLine(232, 70, 232, 100)
    window.add(body)
    r_hand_up = GLine(232, 80, 218, 83)
    window.add(r_hand_up)
    r_hand_low = GLine(218, 83, 205, 80)
    window.add(r_hand_low)
    l_hand_up = GLine(232, 80, 241, 90)
    window.add(l_hand_up)
    l_hand_low = GLine(241, 90, 239, 105)
    window.add(l_hand_low)
    l_lag_up = GLine(232, 100, 223, 115)
    window.add(l_lag_up)
    l_lag_low = GLine(223, 115, 223, 130)
    window.add(l_lag_low)
    r_lag_up = GLine(232, 100, 241, 115)
    window.add(r_lag_up)
    r_lag_low = GLine(241, 115, 241, 130)
    window.add(r_lag_low)
    racquet = GLine(205, 80, 210, 60)
    racquet.color = 'red'
    window.add(racquet)
    racquet2 = GLine(205, 80, 195, 60)
    racquet2.color = 'red'
    window.add(racquet2)
    rac_head = GOval(15, 22)
    rac_head.filled = True
    rac_head.fill_color = 'white'
    rac_head.color = 'red'
    window.add(rac_head, 195, 45)
    rac_net = GLine(197, 50, 209, 50)
    rac_net.color = 'navy'
    window.add(rac_net)
    rac_net2 = GLine(195, 55, 210, 55)
    rac_net2.color = 'navy'
    window.add(rac_net2)
    rac_net3 = GLine(196, 60, 209, 60)
    rac_net3.color = 'navy'
    window.add(rac_net3)
    rac_net4 = GLine(199, 47, 199, 65)
    rac_net4.color = 'navy'
    window.add(rac_net4)
    rac_net5 = GLine(206, 47, 206, 65)
    rac_net5.color = 'navy'
    window.add(rac_net5)

    # draw two tennis player2
    head2 = GOval(24, 30)
    head2.filled = True
    head2.fill_color = 'white'
    window.add(head2, 163, 520)
    name2 = GLabel('D')
    window.add(name2, 170, 543)
    body2 = GLine(175, 550, 166, 578)
    window.add(body2)
    r_hand2_up = GLine(172, 560, 185, 550)
    window.add(r_hand2_up)
    r_hand2_low = GLine(185, 550, 193, 540)
    window.add(r_hand2_low)
    l_hand2_up = GLine(172, 560, 160, 570)
    window.add(l_hand2_up)
    l_hand2_low = GLine(160, 570, 155, 580)
    window.add(l_hand2_low)
    l_lag2_up = GLine(166, 578, 156, 591)
    window.add(l_lag2_up)
    l_lag2_low = GLine(156, 591, 150, 603)
    window.add(l_lag2_low)
    r_lag2_up = GLine(166, 578, 176, 591)
    window.add(r_lag2_up)
    r_lag2_low = GLine(176, 591, 173, 603)
    window.add(r_lag2_low)
    racquet3 = GLine(193, 540, 190, 510)
    racquet3.color = 'red'
    window.add(racquet3)
    racquet4 = GLine(193, 540, 203, 520)
    racquet4.color = 'red'
    window.add(racquet4)
    rac2_head = GOval(15, 22)
    rac2_head.filled = True
    rac2_head.fill_color = 'white'
    rac2_head.color = 'red'
    window.add(rac2_head, 190, 500)
    rac2_net = GLine(192, 505, 203, 505)
    rac2_net.color = 'navy'
    window.add(rac2_net)
    rac2_net2 = GLine(190, 510, 205, 510)
    rac2_net2.color = 'navy'
    window.add(rac2_net2)
    rac2_net3 = GLine(191, 515, 204, 515)
    rac2_net3.color = 'navy'
    window.add(rac2_net3)
    rac2_net4 = GLine(195, 501, 195, 521)
    rac2_net4.color = 'navy'
    window.add(rac2_net4)
    rac2_net5 = GLine(200, 501, 200, 521)
    rac2_net5.color = 'navy'
    window.add(rac2_net5)




if __name__ == '__main__':
    main()
