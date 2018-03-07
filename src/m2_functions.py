"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ashley Fowoler.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
#
# Done: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
#
###############################################################################

import rosegraphics as rg
import random

def main():
    """
    Makes a TurtleWindow,
    calls the other functions in this module to demo them, and
    waits for the user to click anywhere in the window to close it.
    """
    # A TurtleWindow works "behind the scenes" to enable Turtle movement
    window = rg.TurtleWindow()

    turtle1()
    turtle4()
    turtle3()
    turtle5()
    turtle2()
    turtle2()

    window.close_on_mouse_click()


def turtle1():
    """
    Constructs a square SimpleTurtle.
    Makes that SimpleTurtle draw a yellow-filled circle.
    """
    ada = rg.SimpleTurtle('square')
    ada.speed = 10

    ada.pen = rg.Pen('aquamarine', 30)
    ada.paint_bucket = rg.PaintBucket('yellow')

    ada.begin_fill()
    ada.draw_circle(150)
    ada.end_fill()


def turtle2():
    """
    Constructs a triangle SimpleTurtle.
    Makes that SimpleTurtle go to a RANDOM point,
    draws a cool shape, and return to where it started from.
    """
    grace = rg.SimpleTurtle('triangle')
    grace.speed = 7

    grace.pen = rg.Pen('blue', 15)
    grace.paint_bucket = rg.PaintBucket('magenta')

    # Keep track of where I am, to go back to it at the end.
    # Then choose a RANDOM starting point for the motion in here.
    i_began_here = rg.Point(grace.x_cor(), grace.y_cor())
    i_am_going_here = rg.Point(random.randrange(-500, 500),
                               random.randrange(-300, 0))
    grace.pen_up()
    grace.go_to(i_am_going_here)
    grace.pen_down()

    # Do the motion.
    grace.left(90)
    grace.forward(200)
    grace.begin_fill()
    grace.draw_circle(25)
    grace.end_fill()

    # Go back to where I was when this function began its run.
    grace.go_to(i_began_here)


def turtle3():
    """
    Constructs a default SimpleTurtle.
    Makes that SimpleTurtle go forward 300 units
    and then draw a black-filled circle.
    """
    maja = rg.SimpleTurtle()
    maja.speed = 10
    maja.pen = rg.Pen('black', 10)

    maja.forward(300)

    maja.begin_fill()
    maja.draw_circle(50)
    maja.end_fill()

def turtle4():
    ben = rg.SimpleTurtle()
    ben.speed = 20
    ben.pen = rg.Pen("thistle",10)

    ben.forward(400)

    ben.begin_fill()
    ben.draw_circle(40)
    ben.end_fill()


def turtle5():
    sirphillip = rg.SimpleTurtle()
    sirphillip.speed=10
    sirphillip.pen=rg.Pen("lightsteelblue",15)

    sirphillip.backward(200)
    sirphillip.left(30)
    sirphillip.draw_regular_polygon(6,100)

    william = rg.SimpleTurtle()
    william.speed=12
    william.pen=rg.Pen("sienna",12)

    william.left(20)
    william.forward(100)
    william.draw_regular_polygon(8,80)





###############################################################################
#
# Done: 3.
#   READ the code above.  Be sure you understand:
#     -- How many functions are defined above?
#           (Answer: 4)
#     -- For each function definition:
#          -- Where does that function definition begin?
#             Where does it end?
#     -- How many times does   main   call the   turtle1   function?
#            (Answer: 1)
#     -- How many times does   main   call the   turtle2   function?
#            (Hint: the answer is NOT 1.)
#     -- What line of code calls the   main   function?
#            (Answer: look at the LAST line of this module, far below.)
#
#     ** ASK QUESTIONS if you are uncertain about any of the answers. **
#
#   RELATE what is DRAWN to the CODE above.  Be sure you understand:
#       -- WHEN does the code in   main   run?
#       -- WHEN does the code in   turtle1   run?
#                    the code in   turtle2   run?
#                    the code in   turtle3   run?
#       -- For each of the above, WHY does that code run when it does?
#
#     ** ASK QUESTIONS if you are uncertain about any of the answers. **
#
#   When you believe you understand the answers
#   to all of the above questions, change the above TO-DO to DONE.
#
###############################################################################

###############################################################################
#
# Done: 4.
#   Define another function,
#   immediately below the end of the definition of   turtle3   above.
#   Name your new function   turtle4.
#
#   The Python "pep8" coding standard says to leave exactly 2 blank
#   lines between function definitions, so be sure to do so.
#
#   Your new function should:
#    1. Define a SimpleTurtle.
#    2. Set your SimpleTurtle's
#               pen
#       to a new rg.Pen with a color and thickness of your own choosing.
#       The  COLORS.txt  file in this project has a list of legal color-names.
#    3. Make your SimpleTurtle move around a bit.
#
#   ----------------------------------------------------------------------
#           ** IMPORTANT:                 **
#           ** Nothing fancy is required. **
#           ** Save fancy stuff for exercises later today. **
#   ----------------------------------------------------------------------
#
#   BTW, if you see a RED underline, that means that there is
#     a SYNTAX (notation) error at that line or elsewhere.
#   Get help as needed to fix any such errors.
#
###############################################################################

###############################################################################
#
# Done: 5.
#   Add a line to   main   that CALLS your new function immediately
#   AFTER  main  calls turtle1.  So:
#     -- the SimpleTurtle from turtle1 should move,
#     -- then YOUR SimpleTurtle should move,
#     -- then the other 3 SimpleTurtles should move.
#
#   Run this module.  Check that there is another SimpleTurtle (yours)
#   that uses the pen you chose and moves around a bit.
#   If your code has errors (shows RED in the Console window)
#   or does not do what it should, get help as needed to fix it.
#
###############################################################################

###############################################################################
#
# Done: 6.
#   The previous two TODOs IMPLEMENTED a function (TO-DO 4)
#   and TESTED that function (TO-DO 5).
#
#   Now implement AND test one more function, defining it immediately
#   below the definition of your   turtle4   function.
#   Name your new function   turtle5.
#
#   The Python "pep8" coding standard says to leave exactly 2 blank
#   lines between function definitions, so be sure to do so.
#
#   Your new function should define TWO new SimpleTurtles,
#   set their characteristics (i.e., instance variables) as you choose,
#   and make each move a bit.
#
#   ----------------------------------------------------------------------
#           ** IMPORTANT:                 **
#           ** Nothing fancy is required. **
#           ** Save fancy stuff for exercises later today. **
#   ----------------------------------------------------------------------
#
#    Get help as needed on this (and every!) exercise!
#
###############################################################################

###############################################################################
#
# Done: 7
#   COMMIT-and-PUSH your work (after changing this TO-DO to DONE).
#
#   As a reminder, here is how you should do so:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up:
#          - HOVER over the  Commit  button
#              (in the lower-right corner of the window)
#          - CLICK on  Commit and Push.
#          - (if asked again to Push, select Push)
#
#   COMMIT adds the changed work to the version control on your computer
#   and PUSH adds the changed work into your Github repository in the "cloud".
#
#    COMMIT-and-PUSH your work as often as you want, but for sure
#    after you have tested the module and believe that it is correct.
#
###############################################################################

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
