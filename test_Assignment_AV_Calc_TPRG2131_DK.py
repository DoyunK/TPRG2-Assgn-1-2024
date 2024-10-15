'''DOYUN KIM (100924397)
Test Assignment AV Calc
TPRG2131
Oct 15th, 2024
This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving
credit to the original author(s).
The program Test_Assignment_AV_Calc_TPRG2131_DK.py '''

import pytest  # Import pytest to run the test cases
from Assignment_AV_Calc_TPRG2131_DK import area_of_rectangle, volume_of_cylinder, area_of_circle, volume_of_cube, area_of_triangle
 # Import the functions from Assignment_AV_Calc_TPRG2131_DK.py
def test_area_of_rectangle(): #test for rectangle area 
    assert area_of_rectangle(3, 4) == 12 #assert helps verify the correct result from the tests
    assert area_of_rectangle(5, 6) == 30#assert helps verify the correct result from the tests
    assert area_of_rectangle(0, 4) == 0#assert helps verify the correct result from the tests

def test_volume_of_cylinder():#test for volume for cylinder
    assert round(volume_of_cylinder(3, 5), 2) == 141.37#assert helps verify the correct result from the tests
    assert round(volume_of_cylinder(1, 1), 2) == 3.14#assert helps verify the correct result from the tests
    assert volume_of_cylinder(0, 5) == 0#assert helps verify the correct result from the tests

def test_area_of_circle():#test for area of circle
    assert round(area_of_circle(3), 2) == 28.27#assert helps verify the correct result from the tests
    assert round(area_of_circle(5), 2) == 78.54#assert helps verify the correct result from the tests
    assert area_of_circle(0) == 0#assert helps verify the correct result from the tests

def test_volume_of_cube():#test for volume for cube
    assert volume_of_cube(3) == 27#assert helps verify the correct result from the tests
    assert volume_of_cube(4) == 64#assert helps verify the correct result from the tests
    assert volume_of_cube(0) == 0#assert helps verify the correct result from the tests

def test_area_of_triangle():#test for triangle area
    assert area_of_triangle(3, 4) == 6.0#assert helps verify the correct result from the tests
    assert area_of_triangle(5, 6) == 15.0#assert helps verify the correct result from the tests
    assert area_of_triangle(0, 4) == 0#assert helps verify the correct result from the tests

if __name__ == "__main__": 
    pytest.main()#makes sure this code runs everything with a test in it