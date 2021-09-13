#!/usr/bin/env python
# coding: utf-8

# In[1]:


dct = {"run": "to move swiftly by foot",
      "walk" : "to move slowly, leisurely by foot"}
dct


# In[2]:


dct = {"run":{},
       "walk":{}}
dct


# In[3]:


dct = {"run": {"verb":"to move swiftly by foot", 
               "noun":"refers to a period of time while one was running"},
       "walk" :{"verb" : "to move slowly, leisurely by foot",
                "noun": "refers to a period of time while one was walking"}}
dct


# In[5]:


import pandas as pd
df = pd.DataFrame(dct)
df


# In[6]:


dct = {"Tyler": {},
       "Emmanuel": {},
       "Amanda":{}, 
       "Logan":{},
       "Connor":{}, 
       "Dylan":{},
       "Gwen":{}, 
       "Jack":{}, 
       "Ben":{},
       "James":{}}
dct


# In[7]:


dct = {"Tyler": {"Age":21, "Interesting Fact":"I am left-handed / ambidextrious!"},
       "Emmanuel": {},
       "Amanda":{}, 
       "Logan":{},
       "Connor":{}, 
       "Dylan":{},
       "Gwen":{}, 
       "Jack":{}, 
       "Ben":{},
       "James":{}}

dct


# In[8]:


dct["Emmanuel"]["Age"] = 32
dct["Emmanuel"]["Interesting Fact"] = "I have 7 degrees!!! And I'm earning the M.S. Data Analytics"
dct["Dylan"]["Age"] = 21
dct["Dylan"]["Interesting Fact"] = "I am a triplet!"
dct["Jack"]["Age"] = 21
dct["Jack"]["Interesting Fact"] = "I have never broken a bone!" 
dct["Logan"]["Age"] = 22
dct["Logan"]["Interesting Fact"] = "I fight fires!"
dct["Gwen"]["Age"] = 23
dct["Gwen"]["Interesting Fact"] = "I bought my first cow when I was 10 years old!"
dct["James"]["Age"] = 26
dct["James"]["Interesting Fact"] = "I am from Bejou!"
dct["Ben"]["Age"] = 23
dct["Ben"]["Interesting Fact"] = "I like basketball!"
dct["Connor"]["Age"] = 21
dct["Connor"]["Interesting Fact"] = "I like to play tennis!"

dct


# In[9]:


df = pd.DataFrame(dct)
df


# In[10]:


faculty_dict =  {"William Nganje":{"Website":"https://www.ndsu.edu/agecon/faculty/william_nganje/#c622350", 
                                     "Areas of Specialization":"Risk management; financial analysis; economics of obesity, food safety and food terrorism; experimental economics; and consumer choice theory",
                                     "Bio":"NA"},
                 "David Bullock": {"Website":"https://www.ndsu.edu/agecon/faculty/bullock/#c622728",
                                    "Areas of Specialization": "futures and options markets, over-the-counter derivatives, trading, risk management, agrifinance, Monte Carlo simulation, and Big Data",
                                    "Bio":"Dr. David W. Bullock is a Research Associate Professor affiliated with the Center for Trading and Risk at NDSU.  His research interests include futures and options markets, over-the-counter derivatives, trading, risk management, agrifinance, Monte Carlo simulation, and Big Data applications in agriculture.  His academic research in option portfolio theory has been published in both the Journal of Economics and Business and the International Review of Economics and Finance.  Additionally, he was the primary contributor behind the AgriBank Insights publication series which won a National AgriMarketing Association (NAMA) award for the best company publication in 2016. Before coming to NDSU in January 2018, Dr. Bullock held numerous positions for over 25 years in the government and private sectors including the Senior Economist at AgriBank FCB – the regional Farm Credit System funding bank for the Upper Midwest region, Director of Research and Senior Foods Economist at Fortune 500 commodity risk management firm INTL FCStone Inc., the Senior Dairy Analyst at Informa Economics, a Risk Management Specialist with the Minnesota Department of Agriculture, and the Senior Economist at the Minneapolis Grain Exchange. David began his academic career as an Assistant Professor and Extension Marketing Economist at Montana State University after graduating from Iowa State University with a Ph.D. in agricultural economics with fields in agricultural price analysis and econometrics in 1989.  Prior to entering ISU, he received bachelor’s (1982) and master’s (1984) degrees in agricultural economics from Northwest Missouri State University. Dr. Bullock is originally from the small northwestern Missouri farming community of Lathrop which is located 40 miles north of the Kansas City metropolitan area.  While in high school, he served as a regional state Vice-President in the Future Farmers of America (FFA) during his senior year."},
                 "James Caton": {"Website":"https://www.ndsu.edu/centers/pcpe/about/directory/james_caton/",
                                 "Areas of Specialization": "Entrepreneurship, Institutions, Macroeconomics, Computation",
                                 "Bio":"James Caton is a faculty fellow at the NDSU Center for the Study of Public Choice and Private Enterprise (PCPE) and an assistant professor in the NDSU Department of Agribusiness and Applied Economics. He teaches undergraduate courses in the areas of macroeconomics, international trade, and computation. He specializes in research related to entrepreneurship, agent-based computational economics, market process theory, and monetary economics. His research has been published in the Southern Economic Journal, Erasmus Journal for Philosophy and Economics, Journal of Entrepreneurship and Public Policy and other academic publications. He co-edited Macroeconomics, a two volume set of essays and primary sources that represent the core of macroeconomic thought. He is also a regular contributor to the American Institute for Economic Research's Sound Money Project, which conducts research and promotes awareness about monetary stability and financial privacy. He resides in Fargo with his wife, Ingrid, and their children."},
                 "David Englund": {"Website":"https://www.ndsu.edu/agecon/faculty/englund/#c622903",
                                 "Areas of Specialization": "Teaches Economic Principles, Led NDSU NAMA to National Champions",
                                 "Bio":"David Englund is a lecturer in the department.  He came to the department with 16 years of teaching experience, having taught Principles of Microeconomics, Principles of Macroeconomics, Money and Banking, Consumer Behavior, Selected Topics in Business, and several other classes.  He also had 10 years’ experience advising student NAMA chapters, having been awarded the Outstanding Advisor of the Year for a Developing Chapter in 2002, and the Outstanding Advisor of the Year award in 2009.\nDavid primarily teaches Survey of Economics, Principles of Microeconomics, Skills for Academic Success, Agricultural Marketing, and NAMA (co-teaches).  He joined the NAMA team in the 2014-2015 school year as a co-advisor and helped coach the student team to a 3rd place finish in the national student marketing plan competition at the national conference.\nSome of David’s outside interests are jogging, photography, and writing fiction novels.  His latest release, Camouflaged Encounters has received positive reviews."},
                 "Erik Hanson": {"Website":"https://www.ndsu.edu/agecon/faculty/hanson/#c622905",
                                 "Areas of Specialization": "Ag Management, Ag Finance",
                                 "Bio":"Erik Hanson is an Assistant Professor in the Department of Agricultural and Applied Economics. He teaches courses on agribusiness management and agricultural finance. Erik completed his Ph.D. at the University of Minnesota in 2016. Prior to that, Erik completed a master’s degree at the University of Illinois (2013) and a bachelor’s degree at Minnesota State University Moorhead (2011)."},
                 "Ronald Haugen": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Robert Hearne": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Jeremy Jackson": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Siew Lim": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Raymond March": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Dragan Miljkovic": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Frayne Olson": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Bryon Parman": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Tim Petry": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Xudong Rao": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Veeshan Rayamajhee": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "David Ripplinger": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "David Roberts": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Kristi Schweiss": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Anupa Sharma": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Andrew Swenson": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "Cheryl Wachenheim": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                 "William Wilson": {"Website":"",
                                 "Areas of Specialization": "",
                                 "Bio":""},
                }
faculty_dict


# In[11]:


faculty_df = pd.DataFrame(faculty_dict)
faculty_df 


# Homework

# In[21]:


dct={"Joe":{"Major":"Mechanical Engineering",
            "Reason for Class":"To learn more code",
            "Plan for After NDSU":"To Become an engineer"}}
dct


# In[22]:


df = pd.DataFrame(dct)
df


# In[ ]:




