from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

def recursion():
  if touch() == 'fruit':
    move()
  if left_side() == 'fruit':
    turn(-1)
    recursion()
  if right_side() == 'fruit':
    turn(1)
    recursion()
    
    