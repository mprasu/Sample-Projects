
import numpy as np
x=[1,2,3,4,5]

a=np.array(x)
b=a+100
print(b)
o/p
array([101, 102, 103, 104, 105])

print(a.ndim)
o/p
1

x=[10,20,30,40,50]
a=np.array(x)
print(a.sum())

o/p
150

print(a.size)
5
print(a.mean())
30.0
print(a.max())
50
print(a.min())
10
print(a.min())

there 3 different means
1)AM
2)GM
3)HM

AM=total/n

GM=(x1*x2*x3....xn)1/n

x=[10,20,30,40,50]
m=1
for v in x:
	m=m*v
gm=m**(1/len(x))
print(gm)

HRM=n/(1/x1+1/x2.....1/xn)

x=[10,20,30,40,50]

1/x #error

A=np.array(x)

1/A 	#no error
1/A 	#means 1/10,1/20,....
B=1/A
HRM=A.size/B.sum()

a=np.arange(15).reshape(3,5)//it is not arrange i.e a range
			     i.e array of the given range of elements
arange:generates elements b/w 0,1,2.....14 as single dim arrays.
reshape: used to reshape the 1-dim to multi dim array
o/p
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
print(a.shape) #returns size of the 2dim array
o/p(3,5)

print(a.ndim)	#returns number of dims
o/p 2
print(a.size)	#returns number of elements
o/p
15

a=np.array([2,3,4])
print(a.dtype)
o/p dtype('int32')

a=np.array([1.2,3.5,4.6])
print(a.dtype)
o/p
dtype('float64')

a=np.array([(1.2,3,5),(4,5,6)])
print(a)
array([[1.2, 3. , 5. ],
       [4. , 5. , 6. ]])

every element is converted into float b/c float having highest preference

a=np.array([(1,2),(3,4)],dtype=complex)
print(a)
o/p
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
a=np.array([(1,2),(3,4)],dtype=int)
print(a)
o/p
array([[1, 2],
       [3, 4]])
o/p
a=np.array([(1,2),(3,4)],dtype=float)
print(a)
array([[1., 2.],
       [3., 4.]])

a=np.zeros((3,4))
print(a)
o/p
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
a=np.zeros([3,4])
print(a)
o/p
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])

np.ones((2,3,5))
array([[[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]]])


x=np.arange(30).reshape(2,3,5)
print(x)
array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9],
        [10, 11, 12, 13, 14]],

       [[15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]]])
x=np.arange(30).reshape(3,2,5)
print(x)
array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9]],

       [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19]],

       [[20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]]])
x=np.arange(30).reshape(5,2,3)
print(x)
array([[[ 0,  1,  2],
        [ 3,  4,  5]],

       [[ 6,  7,  8],
        [ 9, 10, 11]],

       [[12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23]],

       [[24, 25, 26],
        [27, 28, 29]]])
**************************************************************************
2nd day class
**************************************************************************
>>> import numpy as np
>>> np.arange(10,30,5)
o/p array([10, 15, 20, 25])
>>> np.arange(0,2,0.3)
o/p array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
>>> np.linspace(0,2,9)
o/p array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
here 0 is min, 2 is max,9 represents no of elements(not step element).
increment value is decided by run time based on number of elements.

>>> np.linspace(0,2,15)
array([0.        , 0.14285714, 0.28571429, 0.42857143, 0.57142857,
       0.71428571, 0.85714286, 1.        , 1.14285714, 1.28571429,
       1.42857143, 1.57142857, 1.71428571, 1.85714286, 2.        ])
there are 5 methods to create multidim arrays
1)array 2)arange 3)zeros 4)ones 5)linspace
>>> x=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x=np.arange(1,10).reshape(3,3)
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x=np.zeros((1,9)).reshape(3,3)
>>> x
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
>>> x=np.ones((1,9)).reshape(3,3)
>>> x
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
 x=np.linspace(1,9,9).reshape(3,3)
>>> x
array([[1., 2., 3.],
       [4., 5., 6.],
       [7., 8., 9.]])
>>> x=np.linspace(0,2*pi,10)
>>> x
array([0.        , 0.6981317 , 1.3962634 , 2.0943951 , 2.7925268 ,
       3.4906585 , 4.1887902 , 4.88692191, 5.58505361, 6.28318531])
>>> f=np.sin(x)
>>> f
array([ 0.00000000e+00,  6.42787610e-01,  9.84807753e-01,  8.66025404e-01,
        3.42020143e-01, -3.42020143e-01, -8.66025404e-01, -9.84807753e-01,
       -6.42787610e-01, -2.44929360e-16])
>>> f=np.cos(x)
>>> f
array([ 1.        ,  0.76604444,  0.17364818, -0.5       , -0.93969262,
       -0.93969262, -0.5       ,  0.17364818,  0.76604444,  1.        ])
>>> f=np.tan(x)
>>> f
array([ 0.00000000e+00,  8.39099631e-01,  5.67128182e+00, -1.73205081e+00,
       -3.63970234e-01,  3.63970234e-01,  1.73205081e+00, -5.67128182e+00,
       -8.39099631e-01, -2.44929360e-16])
>>> x=np.arange(10000)
>>> x
here lower bound is 0. it will not display all elements.
array([   0,    1,    2, ..., 9997, 9998, 9999])
>>> x=np.arange(10000).reshape(100,100)
>>> x
array([[   0,    1,    2, ...,   97,   98,   99],
       [ 100,  101,  102, ...,  197,  198,  199],
       [ 200,  201,  202, ...,  297,  298,  299],
       ...,
       [9700, 9701, 9702, ..., 9797, 9798, 9799],
       [9800, 9801, 9802, ..., 9897, 9898, 9899],
       [9900, 9901, 9902, ..., 9997, 9998, 9999]])
if want all elements
>>> from numpy import nan
>>> np.set_printoptions(threshold=nan)
>>> x=np.arange(10000).reshape(100,100)
>>>x
      then it will display all elements
******************************************
Arithmetic Operations
*******************************************
>>> a=np.array([10,20,30,40,50])
>>> b=np.arange((5))
>>> a
array([10, 20, 30, 40, 50])
>>> b
array([0, 1, 2, 3, 4])
>>> c=a-b
>>> c
array([10, 19, 28, 37, 46])
>>> b**2
array([ 0,  1,  4,  9, 16], dtype=int32)
>>> a<35
array([ True,  True,  True, False, False])

>>> A=np.array([1,2,3,4]).reshape(2,2)
>>> A
array([[1, 2],
       [3, 4]])
>>> B=np.arange(5,9).reshape(2,2)
>>> B
array([[5, 6],
       [7, 8]])
>>> A*B
array([[ 5, 12],
       [21, 32]])
	here o/p is [
                     [1*5 2*6]
		     [3*7 4*8]
		    ]	
>>> A.dot(B)

array([[19, 22],
       [43, 50]])
o/p will be 
		[
		  [1*5+2*7 1*6+2*8]
		  [3*5+4*7 3*6+4*8]
		]


>>> a=np.ones((2,3),dtype=int)
>>> a
array([[1, 1, 1],
       [1, 1, 1]])
>>> from numpy import random
>>> b=np.random.random((2,3))
>>> b
array([[0.8542447 , 0.67028432, 0.19123725],
       [0.75090054, 0.8709357 , 0.27977465]])
>>> a*=3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b+=3
>>> b
array([[3.8542447 , 3.67028432, 3.19123725],
       [3.75090054, 3.8709357 , 3.27977465]])
>>> b+=a
>>> b
array([[6.8542447 , 6.67028432, 6.19123725],
       [6.75090054, 6.8709357 , 6.27977465]])
result is stored in b. b is already float so results will be float
>>> a+=b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int32') with casting rule 'same_kind'



******************************************
>>> b=np.arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

>>> b.sum()	#all elements sum
  66

>>> b.sum(axis=0) #col wise sum(i.e 0+4+8=12 1+5+9=15 ...) 
array([12, 15, 18, 21])
>>> b.sum(axis=1)# row wise sum(i.e 0+1+2+3=6 4+5+6+7=22 ....)
array([ 6, 22, 38])
>>> b.min(axis=1) #row wise min
array([0, 4, 8])
>>> b.min(axis=0)# col wise min
array([0, 1, 2, 3])
>>> b.cumsum(axis=1) #cumilative sum
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]], dtype=int32)

when to use cumilative sum?

for ex:
assume that the above matrix data is cricketers scores.
assume that 
0=>first player score
1=>second player score
3=>third player score
........
........
after first player totoal score=0
after second player totoal score=0+1=1(first player score+second player score)
after third player totoal score=1+2=3(total first two players scores+third player score)
after 4th player totoal score=0=3+3=6(total first three players+4th player score)
...........
>>> A=np.arange(3)
>>> B=np.array([2.,-1.,4.])
>>> np.add(A,B)
array([2., 0., 6.])
>>> A
array([0, 1, 2])
>>> np.exp(A)
array([1.        , 2.71828183, 7.3890561 ])
>>> np.sqrt(A)
array([0.        , 1.        , 1.41421356])

>>> A=np.arange(10)**3
>>> A
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729], dtype=int32)
>>> A[2]
8
>>> A[2:5] #2=>start index ,5=>end index . but we will get end index-1 elements
array([ 8, 27, 64], dtype=int32)
>>> A[7]=300
>>> A
array([  0,   1,   8,  27,  64, 125, 216, 300, 512, 729], dtype=int32)
8 th element is replace by 300
>>> A[5:7]=500
>>> A
array([  0,   1,   8,  27,  64, 500, 500, 300, 512, 729], dtype=int32)
from 5th index 2 elements are replaced by 500


>>> A[:6:2]=-1000
>>> A
array([-1000,     1, -1000,    27, -1000,   500,   500,   300,   512,
         729], dtype=int32)
>>> A[0:6:2]=-1000
>>> A
array([-1000,     1, -1000,    27, -1000,   500,   500,   300,   512,
         729], dtype=int32)
from index 0 upto 5th index every alternate element is replaced by -1000

>>> for i in a:
...     print(i**(1/3))
...
[1.44224957 1.44224957 1.44224957]
[1.44224957 1.44224957 1.44224957]
for every element cube root is applied


>>> a=np.arange(12).reshape(3,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> a[0]
array([0, 1, 2, 3])
>>> a[1]
array([4, 5, 6, 7])
>>> a[1,2]
6
2'nd row 3rd col
>>> a[1,3]
7
2'nd row 4th col

>>> a[:,:]
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

>>> a[0:3,0:4]  #lly to a[:,:]

array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

first : represents rows
0:3 means 0=>start row index. 3 => end row index
second : represents cols
0:4 means 0=>start col index. 4=>end col index








