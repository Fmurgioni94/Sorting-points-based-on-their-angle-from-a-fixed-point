"""
    Author: Francesco Murgioni
    
"""
import math
import ast

list_of_points = []
list_of_points_angles = []
list_of_sorted_points = []

# in the following lines of code the program took his inputs from a text file
with open("mock_test1.txt", "r") as points_file:
    for line in points_file:
        list_of_points.append([ast.literal_eval(line.strip())])

# assuming that the point (0, 0) is the position of our sniper
# I remove that point from the list.
if (0, 0) in list_of_points:
    list_of_points.remove([(0, 0)])


def find_the_angle(point):
    """
    This function is the core of the solution of my project given the tuple of coordinates it calculates the angle in
    radiant and then turn it into degrees.
    :param point: as a parameter it takes the tuples of coordinates (x, y)
    :return: the angle in degree rounded at the 2nd decimal point
    """
    theta = math.pi / 2 - math.atan2(point[0][1], point[0][0])
    if theta < 0:
        theta += 2 * math.pi
    degree = math.degrees(theta)
    rounded_degree = round(degree, 2)
    return rounded_degree


def find_list_of_angles(sample_list):
    """
    this function is used to calculate for all the points in the list the correct angle in degree and append it to
    the list of points
    :param sample_list: as a parameter it takes the list of points
    :return: nothing
    """
    for point in sample_list:
        angle = find_the_angle(point)
        list_of_points_angles.append((point, angle))


def merge_sort(arr):
    """
    this is the sort algorithm that I decide to use to solve the problem, this algorithm breaks the array into small
    arrays of maximum one element (calling recursively itself). Ones the elements have been divided it compares those
    elements one by one and merge them together, the result is a sorted array.
    :param arr: as a parameter it takes and array
    :return: and return an array
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index][1] < right[right_index][1]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result


def finding_list_of_sorted_points(arr):
    """
    this function takes one list as an input and return a list as an output
    :param arr: in this case the input list is going to be the list of sorted points returned from the merge function
    :return: the list of sorted points
    """
    final_result = []
    for element in arr:
        final_result.append(element[0][0])

    return final_result


find_list_of_angles(list_of_points)  # find the angles
list_of_sorted_points = finding_list_of_sorted_points(merge_sort(list_of_points_angles))
print(list_of_sorted_points)
