# introduction
# relational operators
a = 3
b = 6
print(a>b)
print(a<=b)
print(a!=b)
# logical operators
print(a and b)
print(a or b)
# assignment operators
# =,+=,-=
# special operators: is, is not, in not in
x = 10
y = 20
z = x
print(x is y)
print(x is not y)
print(x is z)
# membership in, not in
courseName = "python"
print('p' in courseName)
print('a' in courseName)
print('a' not in courseName)
# bitwise operators: &, /, ^, ~, >>, <<
# condition statement if, elif, else, nested if else
x = 15
y = 25
if x > y:
    print("x is large")
else:
    print("y is large")
    x = 10
    y = 20
    z = 30
    if x > y and x > z:
        print( "x is large")
    elif y > x and y > z:
        print('y is large')
    else:
        print (" z is large")




