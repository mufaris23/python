# Python code to demonstrate
# to calculate difference
# between adjacent elements in list


# initialising _list
ini_list = [5, 4, 89, 12, 32, 45]

# printing iniial_list
print("intial_list",  str(ini_list))

# Calculating difference list
diff_list = []
for x, y in zip(ini_list[0::], ini_list[1::]):
    diff_list.append(y - x)

res = list(map(abs,diff_list))
# printing difference list
print("difference list: ", str(res))

