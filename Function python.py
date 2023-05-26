#!/usr/bin/env python
# coding: utf-8

# In[1]:


def test():
    pass


# In[2]:


test()


# In[3]:


def test1():
    print("Hi Lucky")


# In[4]:


test1()


# In[5]:


def test2():
    return "Hi Lucky"


# In[6]:


test2()


# In[7]:


test2() + "Have you completed your assignement" #so in return value we can add string


# In[9]:


def test3():
    return "Lucky",23,345.68,[12,34,56]


# In[10]:


test3()


# In[11]:


def test4():
    return 2+3j


# In[12]:


test4()


# In[13]:


def test5():
    a = 4
    b = 5
    c = a+b
    return c


# In[14]:


test5()


# In[15]:


def test6(a,b):
    c = a+b
    return c


# In[16]:


test6(5,4)


# In[18]:


def test7(a,b):
    return  a+b


# In[19]:


test7("Lucky","Kumar")


# In[20]:


test7([1,2,3],[4,5,6])


# find the integer value from list

# In[23]:


l = [1,2,3,4,5,"Lucky","Kumar",[6,7,8],5+6j]
for i in l:
    if type(i) == int or type(i) == float or type(i) == list:
        print(i)
        
        


# Now we shall make a function

# In[57]:


l=[1,2,3,2+3j,"lucky",[1,1,2,3]]



# In[81]:


l1 = []

for i in l:
    if type(i) == int or type(i) == float:
        
     l1.append(i)
    


# In[64]:


l1


# In[82]:


def c():
    
    c1 = []
    
    for i in l:        
        if type(i) == int or type(i) == float:
            
            
            c1.append(i)
            
    return c1


# In[83]:


c()


# In[93]:


def testt(l):
    
    l2 = []
    
    for i in l:
        
        if type(i) == list: 
            
            for j in i:
                
                l2.appnd(j)
        else:
            
            if type(i) == int or type(i)==float:
                
                l2.append(i)
    return l2
                
                    


# In[94]:


testt(l)


# In[102]:


def testt2(*args): #*args in this function you can take n number of data and it wil come in tuple
  return args


# In[99]:


testt2()


# In[100]:


testt2("lucky")


# In[101]:


testt2("Lucky","Kumar",12,3,5+6j)


# In[103]:


def testt3(*Lucky): #so in that case after * you can keep any name it will work
    return Lucky


# In[104]:


testt3(256)


# In[105]:


def testt4(*args,a): # here we can take many variable like args,a here we are taking 2 variables
    return args,a


# In[107]:


testt4(1,2,3, a =4)


# In[108]:


def testt5(a,b,c=4,d=5): #here we are taking variables
    return a,b,c,d


# In[109]:


testt5(5,6)


# In[110]:


def testt6(**kwargs): ## so when you keep ** it is called dictionary
    return kwargs


# In[112]:


type(testt6())


# In[113]:


testt6(a = [1,2,3], b =[4,5,6], c="Lucky")


# In[115]:





# In[ ]:




