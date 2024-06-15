import math

# "point : tuple" defination : (x,y)
# Since we are getting even pow. of subtraction we dont need to use abs or check which one is bigger.
def euclideanDistance(point1: tuple ,point2: tuple):
    return math.sqrt(  
                    (point1[0] - point2[0])**2   
                    +
                    (point1[1] - point2[1])**2
                    )


def printStages(point1:tuple , point2:tuple):
    print("{0},{1} => {2}".format(point1,point2,euclideanDistance(point1,point2)))


#For random tuple list : points = lambda lenth_of_tuple, max_random_item_value : [(random.randint(0, max_random_item_value), random.randint(0, max_random_item_value)) for _ in range(lenth_of_tuple)]

points = [(1,2),(3,4),(5,6),(7,8),(9,10)]

distances = []


for i in range(len(points)):
    for j in range(i,len(points)):
        if j != i:
            #printStages(points[i],points[j])
            distances.append(euclideanDistance(points[i],points[j]))

print(min(distances))