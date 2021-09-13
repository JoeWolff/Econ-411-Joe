#!/usr/bin/env python
# coding: utf-8

# In[2]:



print('Hello World')


# In[3]:


msg="Hello Joe"
print(msg)


# In[4]:


msg="Joe Wolff"
print(msg)

msg_upper= msg.upper()
print(msg_upper)

msg_title= msg.title()
print(msg_title)


# In[6]:


msg="Joe"+" "+"Wolff"
print(msg)


# In[7]:


line1 = "You thought it would be easy"
line2 = "You thought it wouldn't be strange"
line3 = "But then you started coding"
line4 = "Things never were the same"

print(line1 + line2 + line3 + line4)


# In[8]:


line1 = "You thought it would be easy"
line2 = "You thought it wouldn't be strange"
line3 = "But then you started coding"
line4 = "Things never were the same"

print(line1 + " " + line2 + " " + line3 + " " + line4)


# In[9]:


line1 = "You thought it would be easy"
line2 = "You thought it wouldn't be strange"
line3 = "But then you started coding"
line4 = "Things never were the same"

print(line1, line2, line3, line4)


# In[10]:


line1 = "You thought it would be easy"
line2 = "You thought it wouldn't be strange"
line3 = "But then you started coding"
line4 = "Things never were the same"

print(line1, line2, line3, line4, sep = "")


# In[11]:


line1 = "You thought it would be easy"
line2 = "You thought it wouldn't be strange"
line3 = "But then you started coding"
line4 = "Things never were the same"

print(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4)


# In[12]:


line1 = "You thought it would be easy"
line2 = "You thought it wouldn't be strange"
line3 = "But then you started coding"
line4 = "Things never were the same"

print(line1, line2, line3, line4, sep = "\n")


# In[13]:


single_in_double = "We may use 'single quotes' within double quotes"
double_in_single = 'We may use "double quotes" within single quotes'
print(single_in_double)
print(double_in_single)


# In[14]:


single_quotes = 'We may use \'single quotes\' in single quotes.'
double_quotes = "Or we may use \"double quotes\" in double quotes."
read_backslash = "We may use two backslashes to print a single backslash: \\"
lines = "Every\nword\nis\na\nnew\nline"
new_line_and_tab = "We may start a new line \n\tand use tab for a hanging indent"

print(single_quotes)
print(double_quotes)
print(read_backslash)
print(lines)
print(new_line_and_tab)


# In[15]:


spaces = "    Look at all the spaces in the text!    "
print("no spaces removed:\n", spaces)

remove_left_spaces = spaces.lstrip()
remove_right_spaces = spaces.rstrip()
remove_left_and_right_spaces = spaces.strip()

print("Remove left spaces:\n" + remove_left_spaces)
print("Remove right spaces:\n" + remove_right_spaces)
print("Remove left and right spaces:\n" + remove_left_and_right_spaces)


# In[16]:


spaces = "    Look at all the spaces in the text!    "
print("no spaces removed:\n", spaces)

remove_all_spaces = spaces.replace(" ", "")
print("Remove all spaces:\n" + remove_all_spaces)


# In[17]:


x = """Everything in this object will be recorded exactly as entered,
if we enter a new line or 
    a new line with a tab."""
    
print(x)


# In[18]:


num1 = 7 + 9
num1s = "7" + "9"

print("num1:", num1,"\nnum1s:", num1s)


# In[19]:


num1 = 7 / 23
num2 = 8 / 69
num3 = 420 / 13

print("num1:", num1, "\nnum2:", num2, "\nnum3:", num3)


# In[22]:


num1 = 8675309 / 22
num2 = 404 / 40
num3 = 500 / 3
sum_nums = num1 + num2 + num3

print( sum_nums)


# In[23]:


num1 = 578 / 32
num2 = 785 / 44
num3 = 44 / 300
sum_nums = num1 + num2 + num3

print("num1 + num2 + num3: " + str(sum_nums))


# In[24]:


import sys
print(sys.float_info)


# In[25]:


x = 2.0 ** 1023
print(x)


# In[27]:


2.0 * 1024


# In[28]:


x = 2.0 ** 1023
print("x is of", type(x), "and is equal to", x)
y = 2 ** 1025
print("y is of", type(y), "and is equal to", y)


# Exercises

# In[29]:


#1
x="Joe Wolff"
print(x)


# In[ ]:




