import requests
import json
import numpy as np
import datetime 

#Function to get the Average Number of cases
def daily_average(country):
    for country in countries:
        avg = (cases[-1]/len(cases))
    return(round(avg, 2))

#Function that retrieves days with the highest and lowest number of confirmed cases
def high_low_day(country):
    test = 0
    high = 0
    low = 0
    x = 0
    none = 1
    high_counter = 0
    low_counter = 0
    counter = 0
    no_case_counter = 0
    for country in countries:
        for case in cases:
            x = 0
            
            if len(cases) > 1 and case !=0:
                #print(cases[x])
                test = cases[x+1] - cases[x]
                if test >= high:
                    high = test
                    high_counter = counter
                elif test<= high and low == 0:
                    low = test
                    low_counter = counter
                elif test<= high and test<= low:
                    low = test
                elif test == 0:
                    no_case_counter = counter
                else:
                    pass 
            else:
                pass
               
            cases.pop(0)
            x+=1
            counter += 1
    
    return( "highest number of cases on " + dateList[high_counter], high) 
    #"lowest number of cases on ", dateList[low_counter], low,
    
#Function to find the last day with no new cases
def no_cases(country):
    test = 0
    x = 0
    nocase = 0
    num_case = 0
    counter = 0
    for country in countries:
        for case in cases:
            x = 0
            if len(cases) > 3 and case !=0:
                #print(cases[x])
                test = cases[x+1] - cases[x]
                if test == 0:
                    nocase = counter
                else:
                    pass
            else:
                pass
            
            counter += 1
            cases.pop(0)
            x+= 1
    return("No new cases on " + dateList[nocase])

#Function for Monthly High and low
def high_low_month(country): # I never got this function working because I couldn't figure out how to compare the two lists together
    counter = 0
    idx = 0
    x = 0
    lst = []
    for country in countries: #Compare Both date lists one iteration apart to find the index of the cases within a month
        for case in cases:
            if newdate[x] == dateList[x + 1][0:8]:
                pass
            elif newdate[x] != dateList[x+1][0:8]:
                idx = counter
                lst.append(idx)
            counter+=1
            x+=1
     #use lst[2]-lst[1]... to find the number of confirmed cases within a month
  
    
    #Return the Max and the Min

x = 0
countries = ["US", "Russia", "Canada"] 
results = {}

#Get data a dump it into a json file

for country in countries:
    url = "https://covid-api.mmediagroup.fr/v1/history?country=" + countries[x] + "&status=confirmed"
    request = requests.get(url)
    data =json.loads(request.text)
    json.dump(data, open(country + ".json", "w"))
    
    
    #Keys and Lists 
    key1 = "All"
    key2 = "dates"
    
    #List with the Running total of confirmed cases
    cases = [] #Running total of cases
    for case in data[key1][key2]:
        #print(data[key1][key3])
        cases.append((data[key1][key2][case]))
    cases.reverse()
    
    #List of all the dates in the data set
    dateList = list(data[key1][key2].keys()) 
    
    #New list of dates with only the months and years to compare with the other list
    newdate = []
    for date in dateList:
        x = 0
        if date[0:8] == dateList[x + 1][0:8]:
            newdate.append(date[0:8])
        else:
            newdate.append(date[0:8])
    
   
    #Call the Functions to get the Average, High Day, and last day without any Confirmed cases 
    
    avg = daily_average(countries)
    results[country + "'s Daily Average"] = avg


    high_low = high_low_day(countries)
    results[country + "'s Day with the highest cases"] = high_low
    
    no_case = no_cases(countries)
    results[country + "'s last day without any cases"] = no_case
    
    # #I never got my monthly functions working
    
    # high_month = high_low_month()
    # results[country + " Month with the highest and lowest"] = high_month
    
print(results)

