import numpy as np
from models import Circle


def square_simple(d_1, d_2, s):
    '''
    The centers of the disks are fit to a grid with spacing d_1.
    Repeating width: d_1
    '''
    if (d_1 == 'name'):
        return 'square_simple'

    disks = []

    xy_start = d_1 / 2

    x_end = s.length - (s.length % d_1) + xy_start
    y_end = s.height - (s.height % d_1) + xy_start

    disk_no = 0
 
    for i in np.arange(start=xy_start, stop=x_end, step=d_1):
        for j in np.arange(start=xy_start, stop=y_end, step=d_1):
            if disk_no % 3 == 0:            
                disks.append(Circle(i, j, d_1))
            else:
                disks.append(Circle(i, j, d_2))
            disk_no += 1

    return disks


def square_vertical(d_1, d_2, s):
    '''
    The disks are placed one on top of the other in columns width d_1.
    Repeating width: d_1
    '''
    if (d_1 == 'name'):
        return 'square_vertical'

    d_3 = d_1 / 2 + d_2 / 2
    disks = []

    x_start = d_1 / 2
    x_end = s.length - (s.length % d_1) + x_start

    y = d_1 / 2

    disk_no = 0
 
    for i in np.arange(start=x_start, stop=x_end, step=d_1):
        while y <= s.height - d_1 / 2:
            if disk_no % 3 == 0:            
                disks.append(Circle(i, y, d_1))
                y += d_3
            else:
                disks.append(Circle(i, y, d_2))
                if disk_no % 3 == 1:
                    y += d_2
                else:
                    y += d_3
            disk_no += 1
        if disk_no % 3 == 0:
            y = d_1 / 2
        else:
            y = d_2 / 2

    return disks


def square_vertical_optimised(d_1, d_2, s): # not yet implemented
    '''
    The disks are placed one on top of the other in columns width d_1.
    Repeating width: d_1
    
    Optimisation: 
    1.  If there is room to fit two d_2 disks horizontally, they are placed next to one another
    2.  
    '''
    
    if (d_1 == 'name'):
        return 'square_vertical_optimised'

    d_3 = d_1 / 2 + d_2 / 2
    disks = []

    x_start = d_1 / 2
    x_end = s.length - (s.length % d_1) + (d_1 / 2)

    y = d_1 / 2

    disk_no = 0
 
    for i in np.arange(start=x_start, stop=x_end, step=d_1):
        while y <= s.height - d_1 / 2:
            if disk_no % 3 == 0:            
                disks.append(Circle(i, y, d_1))
                y += d_3
            else:
                disks.append(Circle(i, y, d_2))
                if disk_no % 3 == 1:
                    y += d_2
                else:
                    y += d_3
            disk_no += 1
        if disk_no % 3 == 0:
            y = d_1 / 2
        else:
            y = d_2 / 2

    return disks

def hexagonal(d_1, d_2, s):
    '''
    Disks are aranged within a hexagon grid, just the right size to fit a d_1 circle
    -> hexagon side length: 2/sqrt(3) * d_1
    Repeating width: 2 * d_1
    '''

    if (d_1 == 'name'):
        return 'hexagonal'
    
    disks = []

    r_1 = d_1 / 2

    x_end = s.length - (s.length % (1.5 * r_1)) + r_1
    y_end = s.height - (s.height % (1.5 * r_1)) + r_1

    disk_no = 0
    
    at_bottom = True

    for i in np.arange(start=r_1, stop=x_end, step=1.73205 * r_1):
        if at_bottom:
            j = r_1
        else:
            j = d_1
        while j < y_end - r_1:
            if disk_no % 3 == 0:            
                disks.append(Circle(i, j, d_1))
            else:
                disks.append(Circle(i, j, d_2))
            j += d_1
            disk_no += 1
        at_bottom = not at_bottom
    
    return disks
    
