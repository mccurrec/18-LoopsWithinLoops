"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Ezrie McCurry.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate them. """
    # run_test_draw_L()
    run_test_draw_wall_on_right()


def run_test_draw_L():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = 'Draw an L of circles.  Two tests'
    window = rg.RoseWindow(width, height, title)

    window.continue_on_mouse_click('Click to run Test 1.')

    # ------------------------------------------------------------------
    starting_point = rg.Point(50, 50)
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # First L.
    # ------------------------------------------------------------------
    radius = 10
    starting_circle = rg.Circle(starting_point, radius)
    green_circle = starting_circle.clone()
    green_circle.fill_color = 'green'

    draw_L(window, green_circle, 10, 5)
    window.continue_on_mouse_click('Click to run Test 2.')

    # ------------------------------------------------------------------
    # Second L.
    # ------------------------------------------------------------------
    starting_circle.move_by(250, 100)
    blue_circle = starting_circle.clone()
    blue_circle.fill_color = 'blue'

    window.continue_on_mouse_click('Click to run Test 2.')
    draw_L(window, blue_circle, 6, 15)

    window.close_on_mouse_click()


def draw_L(window, circle, r, c):
    """
    See   L.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an 'L' of circles on the given rg.RoseWindow.
      The 'column' part of the L should have r rows and 3 columns.
        (That is, it is r 'tall' and 3 'thick'.)
      The 'shared corner' part of the L should be 3 x 3.
      The 'row' part of the L should have c columns and 3 rows.
        (That is, it is c 'long' and 3 'thick'.)

      The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
      - The fill_color that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type r: int
      :type c: int
    and m and n are small, positive integers.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    # for j in range(3):
    #     starting_position = rg.Point(circle.center.x, circle.center.y)
    #     position = starting_position
    #     for k in range(r + 3):
    #         position = rg.Point()
    #         new_circle = rg.Circle(position, circle.radius)
    #         new_circle.attach_to(window)
    #         window.render(0.1)
    #         position.y = position.y + circle.radius * 2
    position = circle.center.clone()
    for j in range(3):
        for k in range(r + 3):
            new_circle = rg.Circle(position, circle.radius)
            new_circle.fill_color = circle.fill_color
            new_circle.attach_to(window)
            window.render(0.1)
            position.y = position.y + circle.radius * 2
        position.x = position.x + circle.radius * 2
        position.y = circle.center.y
    position.y = position.y + circle.radius * 2 * r
    end_of_first_segment = position.x
    for j in range(3):
        for k in range(c):
            new_circle = rg.Circle(position, circle.radius)
            new_circle.fill_color = circle.fill_color
            new_circle.attach_to(window)
            window.render(0.1)
            position.x = position.x + circle.radius * 2
        position.y = position.y + circle.radius * 2
        position.x = end_of_first_segment

def run_test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    window.continue_on_mouse_click('Click to run Test 1.')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), rg.Point(250 + 30, 30 + 20))
    draw_wall_on_right(rectangle1, 8, window)

    window.continue_on_mouse_click('Click to run Test 2.')
    rectangle2 = rg.Rectangle(rg.Point(470, 40), rg.Point(470 + 50, 40 + 50))
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    # start = rectangle.get_upper_right_corner()
    # hor_side = rectangle.get_width()
    # vert_side = rectangle.get_height()
    # for j in range(n):
    #     for k in range(n - j):
    #         new_rectangle_corner1 = rg.Point(start.x, start.y + k * vert_side)
    #         new_rectangle_corner2 = rg.Point(start.x - (k + 1) * hor_side, start.y + (k + 1) * vert_side)
    #         new_rectangle = rg.Rectangle(new_rectangle_corner1, new_rectangle_corner2)
    #         new_rectangle.attach_to(window)
    #         window.render(0.1)
    #     start.x = start.x - hor_side * (j + 1)
    #     start.y = start.y -
    #
    # start = rectangle.get_upper_right_corner().clone()
    # width = rectangle.get_width()
    # height = rectangle.get_height()
    # new_rectangle = rg.Rectangle(start, rg.Point(start.x - width, start.y + height))
    # for j in range(n):
    #     for k in range(n - j):
    #         new_rectangle = rg.Rectangle(start, rg.Point(start.x - width, start.y + height))
    #         new_rectangle.corner_1.y = start.y + height * k
    #         new_rectangle.corner_2.y = new_rectangle.corner_1.y + height
    #         new_rectangle.attach_to(window)
    #         window.render(0.1)
    #     new_rectangle.corner_1.x = start.x - width * (j + 1)
    #     new_rectangle.corner_2.x = new_rectangle.corner_1.x - width
    position = rectangle.get_upper_right_corner().clone()
    height = rectangle.get_height()
    width = rectangle.get_width()
    for j in range(n):
        for k in range(n - j):
            corner_2 = rg.Point(position.x - width, position.y + height)
            new_rectangle = rg.Rectangle(position, corner_2)
            new_rectangle.attach_to(window)
            window.render(0.1)
            position.y = position.y + height
        position.y = rectangle.get_upper_right_corner().y + height * (j + 1)
        position.x = position.x - width

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
