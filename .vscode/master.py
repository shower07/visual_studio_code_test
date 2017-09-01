import math
def hypotenuse(a,b):
   exp_c = a*a+b*b
   return(math.sqrt(exp_c))
def rightTrianglePerimeter(a, b):
   return(a+b+hypotenuse(a,b))
def distance2D(x1, y1,x2, y2):
   result = math.sqrt(math.pow(abs(x1-x2),2)+math.pow(abs(y1-y2),2))
   return result
def trianglePerimeter(xA, yA, xB, yB, xC, yC):
   result = distance2D(xA,yA,xB,yB)+distance2D(xA,yA,xC,yC)+distance2D(xB,yB,xC,yC)
   return result
print rightTrianglePerimeter(3,4)
print distance2D(0,0,3,4)
print trianglePerimeter(1,2,3,4,5,6)
print("There is master")