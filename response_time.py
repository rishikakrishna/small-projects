"""
    Facebook Pages offer users insight into the response time.
    If administrators are responding to messages under 15 minutes,
    a green badge appears on the Facebook Page and indicates
    
    args:
        current: input string indicating the numerical value of the current response time
        time_period: input string, adding a unit to "current"
        attempt: the response rate at which you are willing to respond to messages to bring your response time down to 15 minutes

    prints:
        the number of messages you must respond to within your specified response time ("attmpt")
"""


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
    print("Sorry, I don't understant your units :(")

