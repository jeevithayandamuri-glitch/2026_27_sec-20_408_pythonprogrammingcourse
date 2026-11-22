#3D_Rectangle_Area_Perimeter_Function
#Implement a Python program that defines a function to calculate the area and perimeter of a rectangle (length and breadth as parameters) and returns both values
def rect_area_perimeter(length,breadth):
    area=length*breadth
    perimeter=2*(length*breadth)
    return area,perimeter

length=int(input("Enter length:"))
breadth=int(input("Enter breadth:"))
area,perimeter=rect_area_perimeter(length,breadth)
print("Area:",area)
print("Perimeter:",perimeter)
