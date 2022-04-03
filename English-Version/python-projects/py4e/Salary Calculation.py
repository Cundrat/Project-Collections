# eh = enter hours
# er = enter rate
# ot = overtime
# rg = regular pay


eh = input("Enter Hours: ")
er = input("Enter Rate: ")
fh = float(eh)
fr = float(er)

if fh > 40:
    #overtime
    rg = fh * fr
    ot = (fh - 40) * (fr * 0.5)
    ro = rg + ot
else:
    #regular
    ro = fh * fr

print("Pay:", ro)
