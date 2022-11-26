import pydirectinput
from KeyCodes import *

###################################
# Valorant Code
###################################
def Valorant(msg, username):
    # If the chat message is "forward", then hold down the W key for 2 seconds
    if msg == "forward":
        HoldAndReleaseKey(W, 2)

    # If the chat message is "back", then hold down the S key for 2 seconds
    if msg == "back":
        HoldAndReleaseKey(S, 2)

    # If the chat message is "left", then hold down the A key for 2 seconds
    if msg == "left":
        HoldAndReleaseKey(A, 2)

    # If the chat message is "right", then hold down the D key for 2 seconds
    if msg == "right":
        HoldAndReleaseKey(D, 2)

    # Spacebar
    if msg == "jump":
        HoldAndReleaseKey(SPACE, 0.7)

    # Move the mouse up
    if msg == "aim up":
        pydirectinput.moveRel(0, -100, relative=True)

    # Move the mouse down
    if msg == "aim down":
        pydirectinput.moveRel(0, 100, relative=True)

    # Move the mouse Left
    if msg == "aim left":
        pydirectinput.moveRel(-100, 0, relative=True)

    # Move the mouse Right
    if msg == "aim right":
        pydirectinput.moveRel(100, 0, relative=True)

    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot":
        pydirectinput.mouseDown(button="left")
        time.sleep(1)
        pydirectinput.mouseUp(button="left")

    # Press the right mouse button down for 1 second, then release it
    if msg == "aim":
        pydirectinput.mouseDown(button="right")
        time.sleep(1)
        pydirectinput.mouseUp(button="right")

    # Reload
    if msg == "reload":
        HoldAndReleaseKey(R, 0.7)

    # Q
    if msg == "q":
        HoldAndReleaseKey(Q, 0.7)

    # E
    if msg == "e":
        HoldAndReleaseKey(E, 0.7)

    # C
    if msg == "c":
        HoldAndReleaseKey(C, 0.7)

    # X -> Ult
    if msg == "x":
        HoldAndReleaseKey(X, 0.7)




