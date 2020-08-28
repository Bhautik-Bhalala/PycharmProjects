# test_case = int(input())
# lst = []
# lst2 = []
# lst3 = []
# if(1< test_case<10):
#     for i in range(test_case):
#         no_of_employee = int(input())
#         if(1<no_of_employee<100000):
#             # for i in range(no_of_employee):
#             rank_of_employee = input()
#             rank_of_employee_split = rank_of_employee.split()
#             lst.extend(rank_of_employee_split)
#             lst2 = [1] * len(lst)
#             # for i in rank_of_employee_split:
#             #     # lst.append(i)
#             #     lst2.append(1)
#             for i in lst:
#                if (int(i) <1000000000):
#                     continue
#                else:
#                    exit()
#             if (no_of_employee != len(rank_of_employee_split)):
#                 print("no of employees not matching with the number of ranks provided ")
#             else:
#                 for temp in range(len(lst)):
#                     if(no_of_employee<3):
#                         if (temp == 0):
#                             if (lst[0] > lst[1]):
#                                 lst2[0] = lst2[0] + 1
#                         else:
#                             if (lst[temp - 1] < lst[temp]):
#                                 lst2[temp] = lst2[temp] + 1
#                     else:
#                         if(temp == 0):
#                             if(lst[0]>lst[1]):
#                                lst2[0] = lst2[0]+1
#                         elif(1< temp+1 < len(lst)):
#                             if(lst[temp]>lst[temp+1]
#                             or lst[temp+1] < lst[temp+2]):
#                                 lst2[temp] = lst2[temp]+1
#                         else:
#                             if(lst[temp-1]<lst[temp]):
#                                 lst2[temp] = lst2[temp]+1
#             lst3.append(sum(lst2))
#             lst2 *= 0
#             lst *= 0
# for i in lst3:
#     print(int(i))


from itertools import permutations
paragraph = input("enter the para here ")
dam_keys = input("enter the damaged keys with space ")
dam_keys = dam_keys.replace(" ", "")
lst = ["".join(x) for x in permutations(dam_keys)]
lst2 =[]
print(lst)
lst.sort()
print(lst)
for i in range(len(lst)):
    temp = paragraph.find(lst[i])
    if (temp != 0 ):
        print(lst[i])
        exit()
# for i in paragraph:
#     if i in lst:
#         # lst2.append(dam_keys)
#         print(dam_keys)
# print(lst2[0])
