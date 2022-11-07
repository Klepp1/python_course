
def turn_right():
    turn_left()
    turn_left()
    turn_left()





while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and right_is_clear(): 
        turn_right()
    elif wall_in_front():
        turn_left()
    else:
        turn_left()
        move()