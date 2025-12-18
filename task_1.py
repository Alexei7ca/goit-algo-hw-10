import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total_Output"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1 * lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

model.solve(pulp.PULP_CBC_CMD(msg=0))

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal quantity of Lemonade: {pulp.value(lemonade)}")
print(f"Optimal quantity of Fruit Juice: {pulp.value(fruit_juice)}")
print(f"Maximized Total Production: {pulp.value(model.objective)}")