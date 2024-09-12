"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###
#final = principal * ((1 + (rate / 100)) ** n)

principal = 33000000000

# 10 year bonds
rate10 = 3.96
n10 = 10

# final answer for 10-year
ten_year_final = principal * ((1 + (rate10 / 100)) ** n10)

# 20 year bonds
rate20 = 4.32
n20= 20

# final answer for 20-year
twenty_year_final = principal * ((1 + (rate20 / 100)) ** n20)

print('Elons investment would have been worth $', ten_year_final, 'in 10 years')
print('Elons investment would have been worth $', twenty_year_final, 'in 20 years')

##SUBMITTED