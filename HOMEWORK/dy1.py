rice_p=45
sugar_p=40
oil_p=130
rice_q=3
sugar_q=2.5
oil_q=1.8
rice_total=(rice_p*rice_q)
rice_total=str(rice_total)
print("total price of rice=",rice_total)
sugar_total=(sugar_p*sugar_q)
sugar_total=str(sugar_total)
print("total price of sugar=",sugar_total)
oil_total=(oil_p*oil_q)
oil_total=str(oil_total)
print("total price of oil=",oil_total)
total_bill=rice_total+sugar_total+oil_total
print("total bill is",total_bill)
total_bill=int(total_bill)
print(total_bill)
print(type(total_bill))