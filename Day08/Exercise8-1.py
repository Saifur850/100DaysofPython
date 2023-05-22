import math
def paint_calc(h,w,c):
    result= math.ceil((h*w)/c)
    print(f"The result is {result}.")


test_h= int(input("Height of the wall: "))
test_w= int(input("Weight of the wall: "))

coverage=5

paint_calc(test_h,test_w,coverage)

