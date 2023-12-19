#We return values from function, so 
#that we can use them later in our code.
def area_rect(w, h):
 """Calculate the area of a rectangle."""
 area = w * h
 return area

my_area = area_rect(5, 4)
print(my_area)