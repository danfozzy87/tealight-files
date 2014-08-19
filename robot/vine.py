from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
countleft = 0
countright = 0

def recursion():
  if touch() == 'fruit':
    move()
    recursion()
    
  if left_side() == 'fruit':
    turn(-1)
    countleft = countleft + 1
    recursion()
    
  if right_side() == 'fruit':
    turn(1)
    countright = countright + 1
    recursion()
    
    
recursion()