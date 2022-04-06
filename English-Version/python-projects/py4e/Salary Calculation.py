#This project is belongs to py4e, this is just that exercise or project that i've worked
#This program write to prompt prompt the user for hours and rate per hour using input to compute gross pay with own function.


def computepay(hours, rate):
    if hours > 40:
        regular = hours * rate
        overtime = (hours - 40) * (rate *0.5)
        pay = regular + overtime
    else:
        pay = hours * rate
    return pay



hours = input("Enter Hours:")
rate  = input("Enter Rate:")
hours = float(hours)
rate  = float(rate)


pay = computepay(hours,rate)
print("Pay", pay)
