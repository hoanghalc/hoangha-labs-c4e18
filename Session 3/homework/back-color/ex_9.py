def is_inside(point,rectangle):
    if point[0] in range(rectangle[0],rectangle[0]+rectangle[2]+1) and point[1] in range(rectangle[1],rectangle[1]+rectangle[3]+1):
        return True
    else: 
        return False



# point_test = [100, 120]
# rec_test = [140, 60, 100, 200]
# is_inside = is_inside(point_test,rec_test)
# if is_inside:
#     print('ben trong')
# else:
#     print('ben ngoai')