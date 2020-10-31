#region reshape
"""
import numpy as np

#reshaping
np.arange(1,10)

np.arange(1,10).reshape(3,3)

"""

#endregion

#region Concatenation
"""

import numpy as np

#Array Birleştirme (Concatenation)

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

np.concatenate([x,y])

#iki boyut

a= np.array([[1,2,3],[4,5,6]])

np.concatenate([a,a],axis=1)
"""

#endregion

#region Splitting
"""
#Array Ayırma(Splitting)

import numpy as np

x= np.array([1,2,3,99,99,3,2,1])

a,b,c= np.split(x,[3,5])

a
b
c

#iki boyutlu ayırma

m=np.arange(16).reshape(4,4)
m

np.vsplit(m,[2])

ust,alt= np.vsplit(m,[2])

ust

alt

m

np.hsplit(m,[2])

sag,sol= np.hsplit(m,[2])

sag

sol

# Çıktı

# >>> #iki boyutlu ayırma
# >>> 
# >>> m=np.arange(16).reshape(4,4)
# >>> m
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15]])
# >>> np.vsplit(m,[2])
# [array([[0, 1, 2, 3],
#        [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
#        [12, 13, 14, 15]])]
# >>> ust,alt= np.vsplit(m,[2])
# >>> ust
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])
# >>> alt
# array([[ 8,  9, 10, 11],
#        [12, 13, 14, 15]])
# >>> m
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15]])
# >>> np.hsplit(m,[2])
# [array([[ 0,  1],
#        [ 4,  5],
#        [ 8,  9],
#        [12, 13]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11],
#        [14, 15]])]
# >>> sag,sol= np.hsplit(m,[2])
# >>> sag
# array([[ 0,  1],
#        [ 4,  5],
#        [ 8,  9],
#        [12, 13]])
# >>> sol
# array([[ 2,  3],
#        [ 6,  7],
#        [10, 11],
#        [14, 15]])

"""

#endregion

#region Array Sıralama (Sorting)

# import numpy as np

# #tek boyutlu
# v= np.array([4,5,8,3,1])
# v
# np.sort(v)

# v.sort()

# v

# #iki boyutlu

# m= np.random.normal(20,5,(3,3))

# m

# np.sort(m,axis=1)
#endregion

#region Slicing ile Elemanlara erişmek (Array alt kümesine erişmek)

# import numpy as np

# a= np.arange(20,30)
# a

# a[0:3]

# a[:3]

# a[3:]

# a[2::2]

# a[0::3]

#iki boyutlu slice işlemleri

# m= np.random.randint(10,size=(5,5))

# m

# m[:,0]
# m[:,1]
# m[:,2]
# m[:,3]

# m[0:2,0:3]

# m[::,:2]

#endregion

#region Alt Küme üzerinden işlem yapmak

# import numpy as np

# a= np.random.randint(10,size=(5,5))

# a

# alt_a= a[0:3,0:2]
# alt_a

#endregion

#region Fancy Index ile elemanlara erişmek

# import numpy as np

# v= np.arange(0,30,2)
# v

# al_getir= [1,3,4]

# v[al_getir]

# # iki boyutlu fancy

# m= np.arange(9).reshape((3,3))

# m

# satir=np.array([0,1])
# sutun=np.array([1,2])

# m[satir,sutun]3

#endregion

#region İki bilinmeyenli denklem çözümü

import numpy as np

# 5 * x0 +x1 = 12
# x0 +3 * x1 = 10

a= np.array([[5,1],[1,3]])
b= np.array([12,10])

a

b

x= np.linalg.solve(a,b)

x
#endregion