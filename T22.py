# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
import random

s_l = []
n = int(input("write a lenght for first list: "))
for i in range(n):
    s_l.append(random.randint(0,10))
print(f'this is first list{s_l}')
s_l2 = []
m = int(input("write a lenght for second list: "))
for i in range(m):
    s_l2.append(random.randint(0,10))
print(f'this is second list{s_l2}')
goal = []
for i in s_l:
    if i in s_l and i in s_l2:
        goal.append(i)
print(f'this is all elements in 2 lists which have in both {goal}')
goal_set = set(goal)
print(f'its what you ask me to find {goal_set}')
