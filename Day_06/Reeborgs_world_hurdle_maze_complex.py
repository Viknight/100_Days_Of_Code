def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_right():
    turn_right()
    move()
        
while not at_goal():
    if right_is_clear():
        go_right()
        if right_is_clear():
            go_right()
            if right_is_clear():
                go_right()
                if right_is_clear():
                    if front_is_clear():
                        move()
                    else:
                        turn_left()
                        if front_is_clear():
                            move()
                        else:
                            turn_left()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''        
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''