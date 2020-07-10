import numpy as np

# 1. Convert the given Python list into a NumPy
# array and check its data type.
list_1 = [1, 2, 3, 4, 5]
arr = np.array(list_1)
print("1. {}, {}".format(arr, type(arr)))

# 2. Generate array [0,1,2,3,4,5] using the NumPy built-in 
# function, arange()
arr = np.arange(0, 6)
print("2. {}".format(arr))

# 3. Generate an array of 5 zeros.
arr = np.zeros(5)
print("3. {}".format(arr))

# 4. Generate the following matrix. (a 3x4 matrix of 0s)
arr = np.zeros((3, 4))
print("4. {}".format(arr))

# 5. Generate [1.,1.,1.,1.,1.] using a NumPy built-in function.
arr = np.ones(5)
print("5. {}".format(arr))

# 6. Generate an array of 5 tens.
arr = np.ones(5) * 10
print("6. {}".format(arr))

# 7. Use arange() to generate an array of even numbers between 
# 50 and 100. (50 and 100 not included)
arr = np.arange(52, 100, 2)
print("7. {}".format(arr))

# 8. Generate an array of 10 linearly spaced points between 
# 0 and 1. Output step size as well.
arr = np.linspace(0, 1, retstep=True)
print("8. {}".format(arr))

# 9. Perform the following tasks:
# a) Generate a vector array of 25 numbers using arange().
# b) Write code to convert the vector array into 2-D matrix
# using reshape.
# c) Can we use shape instead of reshape as well?
arr = np.arange(0, 25).reshape(5, 5)
# or arr.shape = (5, 5) to reshape
print("9. {}\nShape: {}".format(arr, arr.shape))

# 10. Generate the following matrix. (5x5 with a step of .1)
arr = np.arange(1, 26).reshape(5, 5) * .1
print("10. {}".format(arr))

# 11. Write code to generate the output below. Use linspace.
# (5x5 with 0-24 as floats)
arr = np.linspace(0, 24, 25, retstep=True)
arr_shaped = arr[0].reshape(5, 5)
print("11. {}\nStep size: {}".format(arr_shaped, arr[1]))

# 12. Generate a random number using NumPy built-in function.
arr = np.random.rand()
print("12. {}".format(arr))

# 13. Generate a 7x5 matrix of 35 random numbers.
arr = np.random.rand(7, 5)
print("13. {}".format(arr))

# 14. Generate the following matrix using NumPy's built-in 
# method for identity matrix. (5x5 with 5s down the diagonal)
arr = np.eye(5) * 5
print("14. {}".format(arr))

# 15. Generate the following outputs.
# a) 6x5 with 0-29
# b) [[17, 18, 19], [22, 23, 24], [27, 28, 29]]
# c) [[1], [6], [11]]
# d) [10, 11, 12, 13, 14]
# e) [10, 11, 12, 13, 14],[15, 16, 17, 18, 19]]
arr = np.arange(0, 30).reshape(6, 5)
print("15a. {}".format(arr))
print("15b. {}".format(arr[3:, 2:]))
print("15c. {}".format(arr[:3, 1:2]))
print("15d. {}".format(arr[5, 4]))
print("15e. {}".format(arr[2:4, :]))

# 16. Calculate the sum of all the numbers in the array.
print("16. {}".format(sum(sum(arr))))

# 17. Calculate sum of all the rows and columns.
row_sums = []
for row in range(0, arr.shape[0]):
	row_sum = 0
	row_sums.append(0)
	for num in arr[row]:
		row_sums[row] += num

col_sums = sum(arr)
print(
	"""17. Row sum: {}
	Column sum: {}""".format(row_sums, col_sums))

# 18. Calculate the standard deviation of the values.
print("18. {}".format(arr.std()))

# 19. Create a boolean mask and list out the numbers
# that are not divisible by 3.
bool_mask = arr % 3 > 0
not_mod_3 = arr[bool_mask]
print(
	"""19. Bool mask: {}
	Indivisible by 3: {}""".format(bool_mask, not_mod_3))


















