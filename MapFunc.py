 # Use Map func to add values from 3 list with same index and return 
 # a list with sum of all values for a index
#input_list_1 = [3, 4, 5, 6]
#input_list_2 = [1, 8, 4, 9]
#input_list_3 = [13, 14, 15, 10]
input_list_1 = [3, 4, 5, 6]
input_list_2 = [1, 8, 4, 9]
input_list_3 = [13, 14, 15, 10]
input_list = list(map(lambda input_list_1,input_list_2,input_list_3:input_list_1 + input_list_2 + input_list_3,input_list_1,input_list_2,input_list_3))
print(input_list)
