from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



def recursion(count, end):
  if touch() == 'fruit':
    move()
    recursion(count+1, 'false')
    
  if left_side() == 'fruit':
    turn(-1)
    recursion(0, 'false')
    
  if right_side() == 'fruit':
    turn(1)
    recursion(0, 'false')
  
  if end == 'false':
    turn(2)
    for i in range(0,count):
      move()
    recursion(0, 'true')
    
    
recursion(0, 'false')