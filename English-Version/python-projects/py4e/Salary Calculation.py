def computepay(hours, rate):
    if hours > 40:
        regular = hours * rate
        overtime = (hours - 40) * (rate * 0.5)
        pay = regular + overtime
    else:
        pay = hours * rate
    return pay

eh = input("Enter Hours: ")
er = input("Enter Rate: ")
fh = float(eh)
fr = float(er)

ro = computepay(fh, fr)
print("Pay", ro)
