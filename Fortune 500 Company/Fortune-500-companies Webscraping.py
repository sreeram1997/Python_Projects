#!/usr/bin/env python
# coding: utf-8

# # FORTUNE INDIA COMPANIES RANKING

# The Fortune India 500 is a ranking of the top 500 corporations in India compiled on the basis of latest sales and gross revenue figures. The list is published annually by Fortune magazine

# For more details:
# https://realpython.com/beautiful-soup-web-scraper-python/

# In[1]:


import requests 
from bs4 import BeautifulSoup 
import csv 


# In[23]:


print('The following are the details to be extracted\n1.Top 500 Companies & their details\n2.Company Revenue Details\n3.Company History')


# In[2]:


year=int(input("Enter the year"))
URL = "https://www.fortuneindia.com/fortune-500/company-list/reliance-industries?year=%s"%(year)
print(URL)
r = requests.get(URL) 
r


# In[3]:


soup = BeautifulSoup(r.content, 'html5lib') 
soup


# In[4]:


r.content


# In[10]:


# # TOP 500 COMPANIES AND THEIR DETAILS

# In[ ]:



import numpy as np
import pandas as pd
answer=input("Do you want to extract Top 500 Company Details")
if (answer=="yes" or answer=="y" or answer=="Y"):
    tables = soup.find('ul', attrs = {'id':'filter-companies-desktop'})
    company_names=[]
    company_address=[]

    for i in range(0,len(tables.find_all('a'))):
        company_names.append(tables.find_all('a')[i].text.strip())
        company_address.append(tables.find_all('a')[i].get("href"))
    

    company_user_name=[]
    for i in range(0,len(company_address)):
        company_user_name.append(company_address[i].split('/')[5].split('?')[0])

    comp_type=tables.find_all_next('div', attrs = {'class': 'company-industry'})
    comp_type


    def comp_details(comp,year):
        url1='https://www.fortuneindia.com/fortune-500/company-list/%s?year=%s'%(comp,year)
        r1 = requests.get(url1) 
        soup1 = BeautifulSoup(r1.content, 'html5lib') 
        soup1
        industry=soup1.find('p', attrs = {'class':'industry'}).text.split(':')[1]
        inc_year=soup1.find('p', attrs = {'class':'inc-year'}).text.split(':')[1]
        yield industry,inc_year


    comp_industry=[]
    inc_year=[]
    for i in company_user_name:
        a,b=next(comp_details(i,year))
        comp_industry.append(a)
        inc_year.append(b)
    #print(i)

    
    Companies=pd.DataFrame(zip(company_names,company_address,np.arange(1,501),comp_industry,inc_year),columns=['Company_Name','Company_Details','Rank','Industry type','Foundation_Year'])
    Companies
    with pd.ExcelWriter(r'C:\Users\Sreeram\Downloads\Fortune500 Companies List.xlsx') as writer:
        Companies.to_excel(writer,sheet_name='Company_Details')

elif (answer=="no" or answer=="n" or answer=="N"):
    tables = soup.find('ul', attrs = {'id':'filter-companies-desktop'})
    company_names=[]
    company_address=[]
    for i in range(0,len(tables.find_all('a'))):
        company_names.append(tables.find_all('a')[i].text.strip())
        company_address.append(tables.find_all('a')[i].get("href"))
    
    company_user_name=[]
    for i in range(0,len(company_address)):
        company_user_name.append(company_address[i].split('/')[5].split('?')[0])

    comp_type=tables.find_all_next('div', attrs = {'class': 'company-industry'})
    comp_type

else:
    print('Enter your choice(yes|no)')
    


# # SELECTING A COMPANY TO OBTAIN THEIR REVENUE DETAILS

# In[21]:


print("Use '-' instead of a space")
com_search=input("Enter a Company/MNC name to get their Revenue details")
com_search1=com_search.lower()

count=0
recent_details=[]
for i in company_user_name:
    if com_search1 in i.lower():
        count+=1
        recent_details.append(i.lower())
        #print(i.lower())

def comp_link(year):
    search1=input('Company Name')
    url2="https://www.fortuneindia.com/fortune-500/company-list/%s?year=%s"%(search1,year)
    return search1,url2
print(recent_details)
for i in range(0,len(recent_details)):   
    if ((count>0) & (com_search1!=np.array(recent_details)[i])):
        print('Choose from Any of the Industries')
        com_search1,company_det=comp_link(year)
        print(company_det)
        break
        
    elif ((count==1)&(com_search1==np.array(recent_details)[i])):
        print('All fine')
        company_det="https://www.fortuneindia.com/fortune-500/company-list/%s?year=%s"%(com_search1,year)        
        print(company_det)
if (count == 0):
    print('Company Name not available.Enter Again')
    exit()
#print(count)        
    


# In[29]:


import pandas as pd
def comp_details_1(comp,year):
    url1='https://www.fortuneindia.com/fortune-500/company-list/%s?year=%s'%(comp,year)
    r1 = requests.get(url1) 
    soup1 = BeautifulSoup(r1.content, 'html5lib') 
    #soup1
    #soup1.find('div', attrs = {'class':'company-parameters'})
    final=soup1.find('div', attrs={'id':{comp}})
    total=final.find('div', attrs={'class':'company-parameters'})
    Column=total.find_all('tr')[0].text.strip().replace("\n", "").replace(" ", "-").split('--------')
    parameters1=[]
    crores1=[]
    change_percent1=[]
    for i in range(0,len(total.find_all_next('tr', attrs = {'class': 'table-body'}))-2):
        parameters1.append(total.find_all_next('tr', attrs = {'class': 'table-body'})[i].text.strip().replace("\n", "").replace(" ", "-").split('--------')[0])
        crores1.append(total.find_all_next('tr', attrs = {'class': 'table-body'})[i].text.strip().replace("\n", "").replace(" ", "-").split('--------')[1])
        change_percent1.append(total.find_all_next('tr', attrs = {'class': 'table-body'})[i].text.strip().replace("\n", "").replace(" ", "-").split('--------')[2])
    
    Comp_Revenue=pd.DataFrame(zip(parameters1,crores1,change_percent1),columns=Column)
    return Comp_Revenue  
Comp_Revenue=comp_details_1(com_search1,year)


# In[664]:


Comp_Revenue


# # FORTUNE 500 COMPANY HISTORY

# In[744]:


url1='https://www.fortuneindia.com/fortune-500/company-list/%s?year=%s'%(com_search1,year)
r1 = requests.get(url1)


# In[745]:


url1


# In[746]:


soup1=BeautifulSoup(r1.content, 'html5lib') 
soup1


# In[747]:


rank=soup1.select_one('script:contains("rank")').text.split(';')[1].split('                    ')[1].split()[2][1:231]


# In[748]:


revenue=soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[2].split()[2][1:319]


# In[749]:


net_operating_revenue=soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[3].split()[2][1:319]


# In[750]:



profit=soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[4].split()[2][1:308]


# In[751]:


assests=soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[5].split()[2][1:316]


# In[752]:


net_worth=soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[6].split()[2][1:316]


# In[753]:


equity_dividend=soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[7].split()[2][1:273]


# In[755]:


employee_cost=soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[8].split()[2][1:299]

#re.findall(r"[-+]?\d*\.\d+|\d+",object name)-Regular Expression method to extract all type of numbers
#re.findall(r"[-+]?\d*\.\d+",object name)-Regular expression method to extract only Float integers
# In[762]:

import re
year1=np.array(re.findall(r"\d{4}",employee_cost), dtype=np.int32).min()


# In[763]:


int(year)


# In[765]:


from datetime import datetime,date
def value_extraction(pattern,year):
    length=datetime.today().year-year
    print(length)
    values=re.findall(r"[-+]?\d*\.\d+",pattern)
    #print(values)
    if len(values)==length:
        #print('1')
        return values
    else:
        #print('2')
        ss=abs(len(values)-length)
        org_value=tuple(values)+tuple(np.zeros(ss))
        return org_value
    


# In[766]:


employee_cost_value=value_extraction(soup1.select_one('script:contains("rank")').text.strip().replace("\n","").split(';')[1].split('                    ')[8].split()[2][1:299],year1)

print(employee_cost_value)


# In[767]:


assets_value=value_extraction(assests,year1)
print(assets_value)


# In[768]:


net_operating_revenue_value=value_extraction(net_operating_revenue,year1)
print(net_operating_revenue_value)


# In[769]:


revenue_value=value_extraction(revenue,year1)
print(revenue_value)


# In[770]:


profit_value = value_extraction(profit,year1)
print(profit_value)


# In[771]:


equity_dividend_value = value_extraction(equity_dividend,year1)
print(equity_dividend_value)


# In[772]:


net_worth_value = value_extraction(employee_cost,year1)
print(net_worth_value)


# In[773]:


import re
numbers = re.findall(r"\d+",rank)

#print(numbers)

np.array(numbers, dtype=np.float32)

rank_value = [x for x in np.array(numbers, dtype=np.float32) if x<=500]

print(rank_value)


# In[774]:


fortune_500_hist = pd.DataFrame(zip(np.arange(2010,2021),rank_value,revenue_value,net_operating_revenue_value,profit_value,assets_value,net_worth_value,equity_dividend_value,employee_cost_value),columns=['Year','Rank','Revenue','Net_Operating_Revenue','Profit','Assets','Networth','Equity Dividend','Employee Cost'])
fortune_500_hist


# # SELECTING A COMPANY TO OBTAIN THEIR PROFIT RATIOS

# In[775]:


def profit_ratios(comp,year):
    url_link = 'https://www.fortuneindia.com/fortune-500/company-list/%s?year=%s'%(comp,year)
    r2 = requests.get(url_link)
    soup2 = BeautifulSoup(r2.content, 'html5lib')
    #print(soup1)
    table = soup2.find('div', attrs = {'id':{comp}})
    #print(table)
    table_profit = table.find_all_next('div', attrs = {'class': 'profit-ratios'})[0]
    Column_profit = table_profit.find_all_next('tr', attrs = {'class':'table-body'})[0].text.strip().replace("\n", "").replace(" ", "-").split('------')
    profits = table_profit.find_all_next('tr', attrs = {'class':'table-body'})[1].text.strip().replace("\n", "").replace(" ", "-").split('------')
    Profits = pd.DataFrame(profits).transpose()
    Profits.columns = [Column_profit]
    return Profits


prof_ratio = profit_ratios(com_search1,year)


# In[776]:


prof_ratio


# In[ ]:





# In[40]:





# In[25]:


with pd.ExcelWriter(r'C:\Users\Sreeram\Downloads\Fortune500 (%s) Companies Details.xlsx'% (com_search1)) as writer:
    Comp_Revenue.to_excel(writer, sheet_name=f'{com_search1}')
    fortune_500_hist.to_excel(writer, sheet_name=f'{com_search1} Company_History')
    prof_ratio.to_excel(writer, sheet_name=f'{com_search1}Profit_Ratios')


# In[ ]:




