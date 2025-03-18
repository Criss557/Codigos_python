#15---------------------------------------------------------------------------------------------------------------
numbers1 = [1,2,3,4,5,6,7,8,9,10]
numbers_par = [ num for num in numbers1 if num %2 == 0]
print(numbers_par)
#a)
numbers_inpar= [ num for num in numbers1 if num %2 == 1]
print(numbers_inpar)