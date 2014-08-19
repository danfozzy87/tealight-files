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
  elif left_side() == 'fruit':
    turn(-1)
    #recursion(0, 'false') 
  else:
    turn(2)
    for i in range(0,count):
      move()
      recursion(0, 'true')
    
    turn(-1)
    #recursion(0, 'false')
    
recursion(0, 'false')