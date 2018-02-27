
# coding: utf-8

# In[27]:

#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#Approach 2
#Input String
str="a c a d g i l d"
LC = str.upper().split()
print(LC)

#Approach 2
#Input String
LC = [x.upper() for x in 'acadgild']
print (LC)


# In[28]:

#Write List comprehensions to produce the following Lists
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
inlist = ['x','y','z']

newlist = [(a+a*j) for a in ['x','y','z'] for j in range(0,4)]

print(newlist)


# In[29]:

#Write List comprehensions to produce the following Lists
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
inlist = ['x','y','z']
newlist = [(j+a*j) for a in range(0,4) for j in ['x','y','z']]
print(newlist)


# In[30]:

#Write List comprehensions to produce the following Lists
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
newlist = [[a+b] for a in range(2, 5) for b in range(0,3)]
print(newlist)


# In[31]:

#Write List comprehensions to produce the following Lists
#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
newlist = [[(a+b) for a in range(2,6)] for b in range(0,4)]
print(newlist)


# In[33]:

#Write List comprehensions to produce the following Lists
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
newlist = [(b,a) for a in range(1,4) for b in range(1,4)]
print(newlist)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



