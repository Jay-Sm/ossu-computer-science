total_cost = 250000
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = 120000
portion_saved = 0.1


def monthly_return(savings, r): 
    return savings*r/12

print(monthly_return(current_savings, r))