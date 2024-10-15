'''DOYUN KIM (100924397)
Assignment AV Calc
TPRG2131
Oct 15th, 2024
This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving
credit to the original author(s).
The program Assignment_AV_Calc_TPRG2131_DK.py '''
'''1. https://www.w3schools.com/python/python_try_except.asp I used this website to further learn how to use try and except while also utilizing the slidwhsow provided to me about it. W3Schools is an educational program that shows step by step on how to use certain python code'''
'''2. https://docs.python.org/3/library/math.html I used this website to double check math syntax in python. This website is from the Python Software Foundation Website'''


import math #I need pi and other stuff for math calculations

def area_of_rectangle(length, width):
    """calculate the area of a rectangle."""
    return length*width
def volume_of_cylinder(radius, height):
    """Calculate the volume of a cylinder"""
    return math.pi*radius **2*height
def area_of_circle(radius):
    """Calculate the area of a circle"""
    return math.pi*radius**2
def volume_of_cube(side):
    """calculate the volume of a cube"""
    return side**3
def area_of_triangle(base, height):
    """Calculate the area of a triangle"""
    return (base*height)/2
def display():
    """display options for calculations"""
    print("Calculator Menu")
    print("Enter Q/q to quit")
    print("Enter V/v to switch calculated view")
    print("Enter D/d to go back to default view")
    print("1. Area of Rectangle")
    print("2. Volume of Cylinder")
    print("3. Area of Circle")
    print("4. Volume of Cube")
    print("5. Area of Triangle")
    
def main():
    """defining the main function of the calculator"""
    view_formula=False #default is on when booted
    
    while True:
        display()
        choice = input("Pick an option: ").strip().lower() #giving the user choice for inputs that branch off into other instructions in the code
        
        if choice =='q':
            print ("exiting program!")#pressing q quits the program
            break
        elif choice == 'v':
            view_formula =True #simple true false statement for the formual view will help toggling between both easier
            print ("Formula view")
        elif choice == 'd':
            view_formula = False
            print("Default view")
        else:
            try:#if q, v, or d are not pressed the only inputs should be # 1-5 until told otherwise
                if choice =='1':
                    length = float(input("Enter length:"))#float inputs of needed measurements for the calculation
                    width = float(input("Enter width:"))#float inputs of needed measurements for the calculation
                    result = area_of_rectangle(length, width)#shoots out the result as the definitions we set above for each calculation
                    if view_formula:
                        print(f"Area = {length} *{width} = {result}")#when it is set to the formula view it prints the equation
                    else:
                        print (f"Area = {result}")#prints the calculated value only
                elif choice =='2': #volume of cylinder
                    radius = float(input("Enter radius: "))#float inputs of needed measurements for the calculation
                    height = float(input("Enter height: "))#float inputs of needed measurements for the calculation
                    result = volume_of_cylinder(radius, height)#shoots out the result as the definitions we set above for each calculation
                    if view_formula:
                        print(f"Volume = π * {radius}^2 * {height} = {result}")#when it is set to the formula view it prints the equation
                    else:
                        print(f"Volume = {result}")#prints the calculated value only

                elif choice == '3':  # Area of Circle
                    radius = float(input("Enter radius: "))#float inputs of needed measurements for the calculation
                    result = area_of_circle(radius)#shoots out the result as the definitions we set above for each calculation
                    if view_formula:
                        print(f"Area = π * {radius}^2 = {result}")#when it is set to the formula view it prints the equation
                    else:
                        print(f"Area = {result}")#prints the calculated value only

                elif choice == '4':  # Volume of Cube
                    side = float(input("Enter side length: "))#float inputs of needed measurements for the calculation
                    result = volume_of_cube(side)#shoots out the result as the definitions we set above for each calculation
                    if view_formula:
                        print(f"Volume = {side}^3 = {result}")#when it is set to the formula view it prints the equation
                    else:
                        print(f"Volume = {result}") #prints the calculated value only

                elif choice == '5':  # Area of Triangle
                    base = float(input("Enter base: ")) #float inputs of needed measurements for the calculation
                    height = float(input("Enter height: "))#float inputs of needed measurements for the calculation
                    result = area_of_triangle(base, height)#shoots out the result as the definitions we set above for each calculation
                    if view_formula:
                        print(f"Area = 0.5 * {base} * {height} = {result}") #when it is set to the formula view it prints the equation
                    else:
                        print(f"Area = {result}")#prints the calculated value only
                else:
                    print("Invalid option, try again.") #if given anything other than a # then it is invalid 

            except ValueError:'''used the 1st website cited above to double check I was using this try and escept code properly'''
            print("Invalid input. Please enter numeric values.")#if it is not any of the above inputs it is seen as error and asks for valid input

if __name__ == "__main__":#this is to grab the data in this file into the pytest section to test our code
    main()


