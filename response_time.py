current = input("What is your current response time (just the numerical value)?  ")
time_period = input("Is this in minutes, hours, days, weeks, months, or years?  ")
attempt = input("How quickly are you currently able to respond to messages (in minutes)?  ")
print("")

time_dict = {'minutes'  : 1,
             'hour'     : 60,
             'hours'    : 60,
             'day'      : 1440,
             'days'     : 1440,
             'week'     : 10080,
             'weeks'    : 10080,
             'month'    : 43805,
             'months'   : 43805,
             'year'     : 525600,
             'years'    : 525600
                                        }
time_period = time_period.lower()  
if time_period in time_dict:
    current = float(current) * time_dict[time_period]
    messages = 0
    while current > 15:
        current = (current + float(attempt))/2
        messages += 1
        
    print("To activate the green, 'Very Responsive' badge on your Facebook Page,")
    print("respond to the next", messages, "messages")
    print("in or under", int(attempt), "minutes.")

else:
    print("None")

