print("Enter Husbands age:")
mage=int(input())
print("Enter husbands salary:")
msal=float(input())
print("Enter Wife age:")
fage=int(input())
print("Enter wife salary:")
fsal=float(input())
if mage<30:
    print("husband age less than 30")
if fage<25:
    print("wife age less than 25")
if msal<100000:
    print("husbands salary less than 1 lakh")
if fsal<50000:
    print("wifes salary less than 50 k")
if mage>=30 and fage>=25 and msal>=100000 and fsal>=25:
    print("Loan sanctioned")