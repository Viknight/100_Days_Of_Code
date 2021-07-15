def jump():
    move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
        while not wall_in_front():
            move()
        turn_left()
    else:
        jump()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#start
while not at_goal():
    if front_is_clear():
        move()
    else:
        if wall_in_front():
            turn_left()
            jump()