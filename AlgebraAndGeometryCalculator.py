'''
Created on Oct 12, 2018

@author: ekinkade20
'''
name=input("Please enter your name:")
print("Hello, ",name,", Welcome to the Algebra and Geometry Calculator",sep="")
input("Press enter to continue")
print("Area of a Triangle:")
baseValue=float(input("Please enter your base value:"))
heightValue=float(input("Please enter your height value:"))
triangleUnits=input("Please enter your unit type:")
print()
area=.5*baseValue*heightValue
print("The area of that triangle is ",format(area,'.2f')," ",triangleUnits,"^2",sep="")
print()
input("Press enter to continue")
print()
print("Volume of a Cube:")
sideLengthValue=float(input("Please enter side length value:"))
