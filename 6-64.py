# Escaping the Maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Note: this part of code is using a built-in function: is_facing_north(), which means it is optimisable by only using basic operation funcitons. 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    while front_is_clear() and not at_goal():
        move()
        if right_is_clear() and is_facing_north() and front_is_clear():
            move()
        elif right_is_clear() and is_facing_north() and not front_is_clear():
            turn_right()
            move()
        elif right_is_clear():
            turn_right()
    if not front_is_clear() and right_is_clear():
        turn_right()
    else:
        turn_left()
    