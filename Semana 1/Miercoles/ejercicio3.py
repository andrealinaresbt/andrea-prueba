savings= int(input('please enter your savings'))
profit=savings * 0.04
year1=savings + profit
profit=year1 * 0.04
year2= year1 + profit 
profit= year2 * 0.04
year3=year2 + profit
print(f'Your initial amount was {savings}')
print(f'The first year was {year1}')
print(f'The second year was {year2}')
print(f'The third year was {year3}')