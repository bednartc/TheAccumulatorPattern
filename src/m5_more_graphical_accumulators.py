"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python. 
  
Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    #run_test_draw_squares_from_circle()
    #run_test_draw_circles_from_rectangle()
    run_test_draw_lines_from_rectangles()


def run_test_draw_squares_from_circle():
    """ Tests the   draw_squares_from_circle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_squares_from_circle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_SQUARES_FROM_CIRCLE: '
    title = title + ' 7 little squares from green circle, 4 big squares'
    window1 = rg.RoseWindow(650, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = 'green'
    draw_squares_from_circle(7, circle, window1)

    # Test 2:
    circle = rg.Circle(rg.Point(350, 70), 50)
    draw_squares_from_circle(4, circle, window1)
    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_SQUARES_FROM_CIRCLE: '
    title += ' 20 teeny squares from blue circle!'
    window2 = rg.RoseWindow(525, 300, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 50), 10)
    circle.fill_color = 'blue'
    draw_squares_from_circle(20, circle, window2)

    window2.close_on_mouse_click()


def draw_squares_from_circle(n, circle, window):
    """
    What comes in:  Three arguments:
      -- A positive integer n.
      -- An rg.Circle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_squares_from_circle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Circle on the given rg.RoseWindow.
      Then draws  n  rg.Squares on the given rg.RoseWindow, such that:
        -- The first rg.Square circumscribes the given rg.Circle.
        -- Each subsequent rg.Square has its upper-left quarter
             on top of the lower-right quarter of the previous rg.Square,
             so that the squares form an overlapping sequence
             that goes down and to the right.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n: int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each square,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------

    circle.attach_to(window)
    radius = circle.radius
    center = circle.center
    x = center.x
    y = center.y
    for _ in range (n + 1):
        square = rg.Square(center, 2 * radius)
        square.attach_to(window)
        center = rg.Point(x, y)
        x = x + radius
        y = y + radius
    window.render()


def run_test_draw_circles_from_rectangle():
    """ Tests the   draw_circles_from_rectangle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_circles_from_rectangle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TODO: 3. Implement this TEST function.
    #   It TESTS the  draw_circles_from_rectangle  function
    #   defined below.  Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #
    ####################################################################
    # HINT: Consider using the same test cases as suggested by the
    #   pictures in  draw_circles_from_rectangle.pdf   in this project.
    #   Follow the same form as the example in a previous problem.
    ####################################################################
    # ------------------------------------------------------------------

    title = 'Tests 1 and 2 of DRAW_CIRCLES_FROM_RECTANGLES: '
    title = title + ' yay'
    window1 = rg.RoseWindow(650, 350, title)

    corner1 = rg.Point(150, 100)
    corner2 = rg.Point(125, 120)
    rectangle = rg.Rectangle(corner1, corner2)
    draw_circles_from_rectangle(3, 2, rectangle, window1)

    corner1 = rg.Point(550, 200)
    corner2 = rg.Point(400, 100)
    rectangle = rg.Rectangle(corner1, corner2)
    draw_circles_from_rectangle(2, 3, rectangle, window1)
    window1.close_on_mouse_click()

def draw_circles_from_rectangle(m, n, rectangle, window):
    """
    What comes in:  Four arguments:
      -- Positive integers m and n.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_circles_from_rectangle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Rectangle on the given rg.RoseWindow.
      Then draws  m  rg.Circles on the given rg.RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the height
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately to the left of the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately to the left
             of the previous rg.Circle, so that the circles form a row
             that goes to the left.
        -- Each rg. Circle has the same fill_color as the given
             rg.Rectangle (and has no outline_color).
      Then draws  n  rg.Circles on the given RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the width
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately above the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately above the previous
             rg.Circle, so that the circles form a column that goes up.
        -- Each rg.Circle has the same outline_color as the given
             rg.Rectangle (and has no fill_color).
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type m: int
      :type n: int
      :type rectangle: rg.Rectangle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each circle,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------

    rectangle.attach_to(window)
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    center_y = (corner1.y + corner2.y) / 2

    if corner1.y > corner2.y:
        radius_height = (corner1.y - corner2.y) / 2
    else:
        radius_height = (corner2.y - corner1.y) / 2

    if corner1.x > corner2.x:
        distance_left = corner1.x - corner2.x
        center_x = corner1.x - distance_left - radius_height
        for _ in range (m):
            center = rg.Point(center_x, center_y)
            circle = rg.Circle(center, radius_height)
            circle.attach_to(window)
            center_x = center_x - 2 * radius_height

    else:
        center_x = corner1.x - radius_height
        for _ in range(m):
            center = rg.Point(center_x, center_y)
            circle = rg.Circle(center, radius_height)
            circle.attach_to(window)
            center_x = center_x - 2 * radius_height

    center_x = (corner1.x + corner2.x) / 2
    if corner1.x > corner2.x:
        radius_width = (corner1.x - corner2.x) / 2
    else:
        radius_width = (corner2.x - corner1.x) / 2

    if corner1.y > corner2.y:
        distance_up = corner1.y - corner2.y
        center_y = corner1.y - distance_up - radius_width
        for _ in range(n):
            center = rg.Point(center_x, center_y)
            circle = rg.Circle(center, radius_width)
            circle.attach_to(window)
            center_y = center_y - 2 * radius_width
    else:
        center_y = corner1.y - radius_width
        for _ in range(n):
            center = rg.Point(center_x, center_y)
            circle = rg.Circle(center, radius_width)
            circle.attach_to(window)
            center_y = center_y - 2 * radius_width



    window.render()


def run_test_draw_lines_from_rectangles():
    """ Tests the   draw_lines_from_rectangles  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_lines_from_rectangles  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of DRAW_LINES_FROM_RECTANGLES:'
    title += '  5 lines, 8 lines!'
    window1 = rg.RoseWindow(900, 400, title)

    rectangle1 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
    rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
    rectangle1.outline_color = 'red'
    rectangle2.outline_color = 'blue'
    draw_lines_from_rectangles(rectangle1, rectangle2, 5, window1)

    rectangle1 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
    rectangle2 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
    rectangle2.outline_color = 'green'
    draw_lines_from_rectangles(rectangle1, rectangle2, 8, window1)

    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of DRAW_LINES_FROM_RECTANGLES:  11 lines!'
    window2 = rg.RoseWindow(700, 700, title)

    rectangle1 = rg.Rectangle(rg.Point(550, 200), rg.Point(650, 100))
    rectangle2 = rg.Rectangle(rg.Point(600, 50), rg.Point(650, 75))
    rectangle1.outline_color = 'brown'
    rectangle2.outline_color = 'cyan'
    rectangle2.outline_thickness = 10
    draw_lines_from_rectangles(rectangle1, rectangle2, 11, window2)

    window2.close_on_mouse_click()


def draw_lines_from_rectangles(rectangle1, rectangle2, n, window):
    """
    What comes in:  Four arguments:
      -- Two rg.Rectangles.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_lines_from_rectangles.pdf   in this project
      for pictures that may help you better understand
      the following specification:

      First draws the given rg.Rectangles on the given rg.RoseWindow.
      Then draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The 1st rg.Line goes from the center of one of the
             1st rg.Rectangle to the center of the 2nd rg.Rectangle.
        -- The 2nd rg.Line goes from the lower-left corner of the
              1st rg.Rectangle and is parallel to the 1st rg.Line,
              with the same length and direction as the 1st rg.Line.
        -- Subsequent rg.Lines are shifted from the previous rg.Line in
              the same way that the 2nd rg.Line is shifted from the 1st.
        -- Each of the rg.Lines has thickness 5.
        -- The colors of the rg.Lines alternate, as follows:
             - The 1st, 3rd, 5th, ... rg.Line has color R1_color
             - The 2nd, 4th, 6th, ... rg.Line has color R2_color
            where
             - R1_color is the outline color of the 1st rg.Rectangle
             - R2_color is the outline color of the 2nd rg.Rectangle
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rectangle1: rg.Rectangle
      :type rectangle2: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
      """
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------

    rectangle1.attach_to(window)
    rectangle2.attach_to(window)

    color1 = rectangle1.outline_color
    color2 = rectangle2.outline_color

    rectangle1_corner1 = rectangle1.corner_1
    rectangle1_corner2 = rectangle1.corner_2
    rectangle2_corner1 = rectangle2.corner_1
    rectangle2_corner2 = rectangle2.corner_2

    rec1_center_x = (rectangle1_corner1.x + rectangle1_corner2.x) / 2
    rec1_center_y = (rectangle1_corner1.y + rectangle1_corner2.y) / 2
    rec2_center_x = (rectangle2_corner1.x + rectangle2_corner2.x) / 2
    rec2_center_y = (rectangle2_corner1.y + rectangle2_corner2.y) / 2

    rec1_center = rg.Point(rec1_center_x, rec1_center_y)
    rec2_center = rg.Point(rec2_center_x, rec2_center_y)

    line = rg.Line(rec1_center, rec2_center)
    line.attach_to(window)

    if rectangle1_corner1.y > rectangle1_corner2.y:
        distance_y = rectangle1_corner1.y - rec1_center_y
    else:
        distance_y = rectangle1_corner2.y - rec1_center_y

    if rectangle1_corner1.x > rectangle1_corner2.x:
        distance_x = rectangle1_corner1.x - rec1_center_x
    else:
        distance_x = rectangle1_corner2.x - rec1_center_x

    change_dx = distance_x
    change_dy = distance_y
    counter = 0
    for _ in range (n):
        point = rg.Point(rec1_center_x - change_dx, rec1_center_y + change_dy)
        point2 = rg.Point(rec2_center_x - change_dx, rec2_center_y + change_dy)
        line = rg.Line(point, point2)
        if counter % 2 == 0:
            line.color = color2
        else:
            line.color = color1
        line.attach_to(window)
        change_dy = change_dy + distance_y
        change_dx = change_dx + distance_x
        counter = counter + 1

    window.render()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
