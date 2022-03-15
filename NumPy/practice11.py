# # import numpy as np
 
# # # Creating a rank 1 Array
# # arr = np.array([1, 2, 3])
# # print("Array with Rank 1: \n",arr)
 
# # # Creating a rank 2 Array
# # arr = np.array([[1, 2, 3],
# #                 [4, 5, 6]])
# # print("Array with Rank 2: \n", arr)
 
# # # Creating an array from tuple
# # arr = np.array((1, 3, 2))
# # print("\nArray created using "
# #       "passed tuple:\n", arr)





# import numpy as np
 
# # # Initial Array
# # arr = np.array([[-1, 2, 0, 4],
# #                 [4, -0.5, 6, 0],
# #                 [2.6, 0, 7, 8],
# #                 [3, -7, 4, 2.0]])
# # print("Initial Array: ")
# # print(arr)
 
# # # Printing a range of Array
# # # with the use of slicing method
# # sliced_arr = arr[:2, ::2]
# # print ("Array with first 2 rows and"
# #     " alternate columns(0 and 2):\n", sliced_arr)
 
# # # Printing elements at
# # # specific Indices
# # Index_arr = arr[[1, 2, 0, 3], 
# #                 [1, 2, 0, 3]]
# # print ("\nElements at indices (1, 3), "
# #     "(1, 2), (0, 1), (3, 0):\n", Index_arr)


 
# # # First Array
# # arr1 = np.array([[4, 7], [2, 6]], 
# #                  dtype = np.float64)
                  
# # # Second Array
# # arr2 = np.array([[3, 6], [2, 8]], 
# #                  dtype = np.float64) 
 
# # # Addition of two Arrays
# # Sum = np.add(arr1, arr2)
# # print("Addition of Two Arrays: ")
# # print(Sum)
 
# # # Addition of all Array elements
# # # using predefined sum method
# # Sum1 = np.sum(arr1)
# # print("\nAddition of Array elements: ")
# # print(Sum1)
 
# # # Square root of Array
# # Sqrt = np.sqrt(arr1)
# # print("\nSquare root of Array1 elements: ")
# # print(Sqrt)
 
# # # Transpose of Array
# # # using In-built function 'T'
# # Trans_arr = arr1.T
# # print("\nTranspose of Array: ")
# # print(Trans_arr)

# # # Python program to differentiate
# # # between type and dtype.
# # import numpy as np

# # a = np.array([1],dtype = complex)

# # print(a)
# # print("dtype is: ",a.dtype)

# # a = np.array([1,2,3,4,5])
# # a.shape = (5,1)
# # print(a)
# # b = np.arange(24).reshape(2,4,3)
# # print(b)


# # a = np.array([1,2,3], dtype = np.int32)
# # print(a.itemsize)
# # print(a.flags)

# x = np.empty([3,2], dtype = int) 
# print(x)
# # -------------------------------------------zeros------------------------------------------
# p = np.zeros((2,2),dtype = [('x', 'i4'), ('y', 'i4')])
# print(p)
# # -------------------------------------------ones--------------------------------------------
# p2 = np.ones(5,dtype = np.int64)
# print(p2)
# # ------------------------------------------asarray

# v = [1,2,3,4,5]
# x = np.asarray(v, dtype = np.float32)
# print(x)

# v2 = (1,2,3) #tuple
# x2 = np.asarray(v2)
# print(x2)


# # ------------------------------------------frombuffer----------------------------------------

# import numpy as np 
# s = b'Hello World' 
# a = np.frombuffer(s, dtype = 'S1') 
# print(a)

# # ------------------------------------------fromiter-------------------------------------------

# import numpy as np 
# list = range(5) 
# print(list)
# it = iter(list)  
# print(it)
# # use iterator to create ndarray 
# x = np.fromiter(it, dtype = float) 
# print(x)

# # -----------------------------------------linspace--------------------------------------------

# i = np.linspace(1,100,3 ,endpoint=False)
# print(i)
# j = np.linspace(1,2,5,retstep=True)
# print(j) 

# # ----------------------------------------logspace

# a = np.logspace(1.0, 2.0, num = 10) 
# print(a)

# a = np.logspace(1,10,num = 10, base = 2) 
# print(a)

# # --------------------------------------slicing and indexing---------------------------------------------

# a = np.arange(10) 
# s = slice(2,7,2) 
# print(a[s])

# a = np.arange(10) 
# b = a[2:7:2] 
# print(b)

# # -------------------------------------sin-------------------------------------------

# a =np.array([np.pi/2,0,3,4,5])
# y = np.sin(a)
# print(y)
# # -------------------------------------multipication---------------------------
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.arange(12).reshape(3, 4)
# # print(a@b)


# # a.dot(b)

# # d = np.exp(a * 1j)
# # print(d)

# print(b.cumsum(axis=1))
# # print(b)

# print(np.exp(b))

# print(np.sqrt(b))


# # -----------------------------------------------fromfunction

# # def f(x, y):
# #     return 10 * x + y

# # b = np.fromfunction(f, (5, 4), dtype=int)
# # print(b)

# for element in b.flat:
#     print(element)



# # flatten array
# b.ravel()
# print(b.T.shape)



# rng = np.random.default_rng(12345)
# rints = rng.integers(low=0, high=10, size=3)
# print(rints)


# # vstack and hstack--------------------------------------------------------------------

# a = np.array([[1,2,3],[7,8,9]])
# b = np.array([[5,6,7],[10,11,12]])
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))


# var = np.array([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],[8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])
# print(np.hsplit(var, 3))
# import numpy as np
# a = np.array([[1,2,3,7,4],[0,1,22,0,0]])

# print(a[a%2==0])

import numpy as np
print(np.__version__)
print(np.show_config())
print(np.info(np.add))

x = np.array([0, 1, 2, 3])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
print(np.any(x))

a = [np.inf]
print(np.isfinite(a))