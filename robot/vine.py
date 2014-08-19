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

def recursion(count):
  if touch() == 'fruit':
    move()
    recursion(count+1)
    
  if left_side() == 'fruit':
    turn(-1)
    countleft = countleft + 1
    recursion()
    
  if right_side() == 'fruit':
    turn(1)
    countright = countright + 1
    recursion()
  
  turn(2)
  for i in range(0,count):
    move()
    recursion(0)
    
recursion(0)