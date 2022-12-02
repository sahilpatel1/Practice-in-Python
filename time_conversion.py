#this script performs time conversion from 24hr format to 12hr format and vice-versa
#Written by: Sahil patel
"""
Using the below function like this
time_conversion("12:59AM", "12", "24")
"""
def time_conversion(given_time:str, format_time:str, target_time:str):
    given_time = given_time.replace(" ", "")
    get_time = given_time[0:len(given_time)- 2].split(":")
    am_or_pm = given_time[-2:].upper()
    
    if target_time == "24" and format_time == "12":
        
        if int(get_time[0]) >= 12 and am_or_pm == "AM":
            new_time = (str(int(get_time[0]) - 12)) + ":" + get_time[1] + am_or_pm
            
        elif int(get_time[0]) >= 1 and int(get_time[0]) <= 11 and am_or_pm == "PM":
            new_time = (str(int(get_time[0]) + 12)) + ":" + get_time[1] + am_or_pm  
            
        else:
            new_time = given_time
        
        print("Given time in " + format_time + "hr format -> " + given_time)
        print("Changed time to " + target_time + "hr format -> " + new_time)
    
    elif target_time == "12" and format_time == "24":
        
        if int(get_time[0]) >= 0 and am_or_pm == "AM":
            new_time = (str(int(get_time[0]) + 12)) + ":" + get_time[1] + am_or_pm
            
        elif int(get_time[0]) >= 13 and int(get_time[0]) <= 23 and am_or_pm == "PM":
            new_time = (str(int(get_time[0]) - 12)) + ":" + get_time[1] + am_or_pm
            
        else:
            new_time = given_time
        
        print("Given time in " + format_time + "hr format -> " + given_time)
        print("Changed time to " + target_time + "hr format -> " + new_time)
        
            
time_conversion("21:45PM", "24", "12")