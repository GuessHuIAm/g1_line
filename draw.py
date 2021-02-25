from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    x = int(x0)
    y = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    dx = x1 - x0
    dy = y1 - y0
   
    #1
    if (dy <= dx and dy > 0):
        p = 2*dy - dx
        while (x <= x1):
            plot(screen, color, x, y)
            x += 1
            p += 2*dy
            if (p > 0):
                y += 1
                p -= 2*dx

    #2
    elif (dy >= dx and dx > 0):
        p = -2*dx + dy
        while (y <= y1):
            plot(screen, color, x, y)
            y += 1
            p += 2*dx
            if (p > 0):
                x += 1
                p -= 2*dy

    #3
    elif (dy >= -dx and dx < 0):
        p = dy + 2*dx
        while (y <= y1):
            plot(screen, color, x, y)
            y += 1
            p -= 2*dx
            if (p > 0):
                x -= 1
                p -= 2*dy

    #4
    elif (dy <= -dx and dy > 0):
        p = 2*dy - dx
        while (x >= x1):
            plot(screen, color, x, y)
            x -= 1
            p += 2*dy
            if (p > 0):
                y += 1
                p += 2*dx

    #5
    elif (dy >= dx and dy < 0):
        p = 2*dy - dx
        while (x >= x1):
            plot(screen, color, x, y)
            x -= 1
            p -= 2*dy
            if (p > 0):
                y -= 1
                p += 2*dx

    #6
    elif (-dy >= -dx and dx < 0):
        p = -2*dx + dy
        while (y >= y1):
            plot(screen, color, x, y)
            y -= 1
            p -= 2*dx
            if (p > 0):
                x -= 1
                p += 2*dy

    #7
    elif (-dy >= dx and dx > 0):
        p = dy + 2*dx
        while (y >= y1):
            plot(screen, color, x, y)
            y -= 1
            p += 2*dx
            if (p > 0):
                x += 1
                p += 2*dy

    #8
    elif (-dy <= dx and dy < 0):
        p = 2*dy - dx
        while (x <= x1):
            plot(screen, color, x, y)
            x += 1
            p -= 2*dy
            if (p > 0):
                y -= 1
                p -= 2*dx
        
    # horizontal
    elif (dy == 0):
        if (dx < 0):
            while (x >= x1):
                plot(screen, color, x, y)
                x -= 1
        else:
            while (x <= x1):
                plot(screen, color, x, y)
                x+= 1
    
    # vertical
    elif (dx == 0):
        if (dy < 0):
           while (y >= y1):
               plot(screen, color, x, y)
               y -= 1
        else:
            while (y <= y1):
                plot(screen, color, x, y)
                y += 1
