#!/usr/bin/env python
# coding: utf-8

# In[1]:


empty_list = []
int_list = [1,2,3,4,5]
float_list = [1.0,2.0,3.0,4.0,5.0]
string_list = ["Many words", "impoverished meaning"]
mixed_list = [1,2.0, "Mix it up"]

print(empty_list)  
print(int_list)  
print(float_list)  
print(string_list)  
print(mixed_list)


# In[2]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = [6, 3, 2, 1, 5, 3]
join_lists = list1 + list2

print("list1:", list1)
print("list2:", list2)
print(join_lists)


# In[5]:


list1 = list(range(9))
list2 = list(range(-9,9))
list3 = list(range(-9,9,3))

print(list1)
print(list2)
print(list3)


# In[6]:


for i in range(10):
    print(i)


# In[7]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = [6, 3, 2, 1, 5, 3]

print("list1 elements:", list1[0], list1[1], list1[2], list1[3], list1[4])
print("list2 elements:", list2[0], list2[1], list2[2], list2[3], list2[4])

list3 = []
j = len(list1)
for i in range(j):
    list3.append(list1[i])

k = len(list2)
for i in range(k):
    list3.append(list2[i])

print("list3 elements:", list3)


# In[8]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = [6, 3, 2, 1, 5, 3]

print("list1 elements:", list1[0], list1[1], list1[2], list1[3], list1[4])
print("list2 elements:", list2[0], list2[1], list2[2], list2[3], list2[4])

list3 = []
j = len(list1)
for i in range(j):
    list3.append(list1[i] + list2[i])
    
print("list3:", list3)


# In[9]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = [6, 3, 2, 1, 5, 3]

print("list1 elements:", list1[0], list1[1], list1[2], list1[3], list1[4])
print("list2 elements:", list2[0], list2[1], list2[2], list2[3], list2[4])

list3 = []
j = len(list1)
for i in range(j):
    list3.insert(0,list1[i] + list2[i])
    
print("list3:", list3)


# In[10]:


if True:
    print("execute script")


# In[11]:


if True:
    print("execute script")
else:
    pass


# In[13]:


if False:
    print("execute script")
else:
    pass


# In[14]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = [6, 3, 2, 1, 5, 3]
print("list1 elements:", list1[0], list1[1], list1[2], list1[3], list1[4])
print("list2 elements:", list2[0], list2[1], list2[2], list2[3], list2[4])

list3 = []
j = len(list1)
if j == len(list2):
    for i in range(0, len(list2)):
        list3.insert(i,list1[i] + list2[i])
print("list3:", list3)


# In[15]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = [6, 3, 2, 1, 5]
print("list1 elements:", list1[0], list1[1], list1[2], list1[3], list1[4])
print("list2 elements:", list2[0], list2[1], list2[2], list2[3], list2[4])

list3 = []
j = len(list1)
if j == len(list2):
    for i in range(0, len(list2)):
        list3.insert(i,list1[i] + list2[i])
else:
    print("Lists are not the same length, cannot perform element-wise operations.")
print("list3:", list3)


# In[16]:


list1 = ["red", "blue", "orange", "black", "white", "golden"]
list2 = ["nose", "ice", "fire", "cat", "mouse", "dog"]
print("lists before deletion: ")
for i in range(len(list1)):
    print(list1[i],"\t", list2[i])
    
del list1[0]
del list2[5]

print()
print("lists after deletion: ")
for i in range(len(list1)):
    print(list1[i], "\t",list2[i])


# In[17]:


list1 = ["red", "blue", "orange", "black", "white", "golden"]
list2 = ["nose", "ice", "fire", "cat", "mouse", "dog"]
print("lists before deletion: ")
for i in range(len(list1)):
    print(list1[i],"\t", list2[i])
    
list1.remove("red")
list2.remove("dog")

print()
print("lists after deletion: ")
for i in range(len(list1)):
    print(list1[i], "\t",list2[i])     


# In[18]:


list1 = ["red", "blue", "orange", "black", "white", "golden"]
list2 = ["nose", "ice", "fire", "cat", "mouse", "dog"]


print("lists before deletion: ")
if len(list1) == len(list2):
    
    for i in range(len(list1)):
        print(list1[i],"\t", list2[i])
    

list1_res = "red"
list2_res = "dog"
list1.remove(list1_res)
list2.remove(list2_res)

print()

print("lists after deletion: ")
if len(list1) == len(list2):
    for i in range(len(list1)):
        print(list1[i], "\t",list2[i])
     
print()
print("Res1", "\tRes2")
print(list1_res, "\t" + (list2_res))


# In[19]:


list1 = ["red", "blue", "orange", "black", "white", "golden"]
list2 = ["nose", "ice", "fire", "cat", "mouse", "dog"]


print("lists before deletion: ")

for i in range(len(list1)):
    print(list1[i],"\t", list2[i])
    

list1_res = list1.pop(0)
list2_res = list2.pop(5)

print()

print("lists after deletion: ")
for i in range(len(list1)):
    print(list1[i], "\t",list2[i])
     
print()
print("Res1", "\tRes2")
print(list1_res, "\t" + (list2_res))


# In[20]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = [6, 3, 2, 1, 5, 3]
print("list1 elements:", list1[0], list1[1], list1[2], list1[3], list1[4])
print("list2 elements:", list2[0], list2[1], list2[2], list2[3], list2[4])

list3 = []
j = len(list1)
if j == len(list2):
    for i in range(0, j, 2):
        list3.append(list1[i] + list2[i])
else:
    print("Lists are not the same length, cannot perform element-wise operations.")
print("list3:", list3)


# In[21]:


obj = ["A", "few", "words", "to", "print"]
for x in obj:
    print(x)


# In[22]:


list1 = ["red", "blue", "orange", "black", "white", "golden"]
list2 = []
for x in list1:
    list2.append(x)

print("list1\t", "list2")
k = len(list1)
j = len(list2)

if len(list1) == len(list2):
    for i in range(0, len(list1)):
        print(list1[i], "\t", list2[i])


# In[23]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = ["red", "blue", "orange", "black", "white", "golden"]

print("list1:", list1)
print("list2:", list2)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

print("sortedList1:", sorted_list1)
print("sortedList2:", sorted_list2)


# In[24]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = ["red", "blue", "orange", "black", "white", "golden"]
list3 = list1 + list2

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

print("sortedList1:", sorted_list1)
print("sortedList2:", sorted_list2)

sorted_list3 = sorted(list3)
print("sortedList3:", sorted_list3)
print("Execution complete!")


# In[25]:


list1 = [5, 4, 9, 10, 3, 5]
list2 = ["red", "blue", "orange", "black", "white", "golden"]
list3 = list1 + list2

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

print("sortedList1:", sorted_list1)
print("sortedList2:", sorted_list2)
try:
    sorted_list3 = sorted(list3)
    print("sortedList3:", sorted_list3)
except:
    print("TypeError: unorderable types: str() < int() "
         "ignoring error")
print("Execution complete!")


# In[26]:


some_list = [3, 1, 5, 6, 1]
print(some_list[:])


# In[27]:


some_list = [3, 1, 5, 6, 1]
min_index = 0
max_index = len(some_list)
print("minimum:", min_index)
print("maximum:", max_index)
print("Full list using slice", some_list[min_index:max_index])
print("Full list without slice", some_list)


# In[28]:


min_index = 3
max_index = 7
full_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
partial_list = full_list[min_index:max_index]
print("Full List:", full_list)
print("Partial List:", partial_list)
print("full_list[7]:", full_list[7])


# In[29]:


print("i", "j")
for i in range(5):
    for j in range(5):
        print(i, j)


# In[30]:


print("i", "j", "i+j")
for i in range(5):
    for j in range(5):
        val = i + j
        print(i, j, val)


# In[31]:


list1 = [20, 30, 40, 50]
max_list_value = max(list1)
min_list_value = min(list1)
print("maximum:", max_list_value, "minimum:", min_list_value)


# In[32]:


list1 = [20, 30, 40, 50]
min_list_val = float("inf")
max_list_val = float("-inf")

for x in list1:
    if x < min_list_val:
        min_list_val = x
    if x > max_list_val:
        max_list_val = x

print("maximum:", max_list_val, "minimum:", min_list_val)


# In[33]:


generator = (i for i in range(20))
print(generator)

list1 = list(generator)
print(list1)

list2 = [2 * i for i in range(20)]
print(list2)


# In[ ]:




