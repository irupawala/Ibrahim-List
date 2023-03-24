import math

# https://math.libretexts.org/Bookshelves/Precalculus/Book%3A_Precalculus__An_Investigation_of_Functions_(Lippman_and_Rasmussen)/05%3A_Trigonometric_Functions_of_Angles/5.03%3A_Points_on_Circles_Using_Sine_and_Cosine#:~:text=Values%20for%20Sine%20and%20Cosine&text=Since%20the%20sine%20and%20cosine%20are%20equal%2C%20sin(%CF%804,2%2C%E2%88%9A22).&text=Find%20the%20coordinates%20of%20the%20point%20on%20a%20circle%20of,an%20angle%20of%20%CF%804.
# Using the Sin, Cos Formulae. Refer the link above
def drawCircleMathFunctions(a, b, radius):
    for angle in range(0, 360, 45):
        x = a + (radius * math.cos(angle))
        y = b + (radius * math.sin(angle))
        print(x,y)
    
    return 

# Using the property r**2 = x**2 + y**2
def drawCircleProperty(a, b, radius):
    for x in range(radius+1):
        y = math.sqrt(radius**2 - x**2)
        print((a+x, b+y), (a+x, b-y), (a-x, b+y), (a-x, b-y))
        
if __name__ == "__main__":
   #drawCircleMathFunctions(0, 0, 3) 
   drawCircleProperty(0, 0, 3)        
   
   
# Midpoint Circle Algorithm
   
# https://www.youtube.com/watch?v=Rv9qIjMVyxM
# https://www.youtube.com/watch?v=k5YZBOsw3Jw

# Bersenham's Circle Algorithm

# https://www.youtube.com/watch?v=1Te8U_JR8SI