"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

from multiprocessing import Value
from os import system
if system("clear") != 0: system("cls")

def find_first_sum(nums :list[int], goal :int) -> list:
    """This function finds the first two numbers in a list that sum up to a given goal"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]
    return [None]

print(find_first_sum([4, 5, 6, 2], 8))


def find_first_sum_dictionary(nums :list[int], goal :int):
    """This function finds the first two numbers in a list that sum up to a given goal"""
    seen = {}
    for index,value in enumerate(nums):
        print(f"index: {index} - value: {value}")
        print(f"seen: {seen}")
        missing = goal - value
        if missing in seen:
            return [seen[missing], index]

        seen[value] = index

    return None

print(find_first_sum_dictionary([4, 5, 6, 4, 6, 2], 8))
print(find_first_sum_dictionary([4, 5, 6, 2], 10))