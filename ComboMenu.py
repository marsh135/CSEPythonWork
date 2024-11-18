foods = ["", "Burger", "Hot Dog", "Pizza", "Milkshake", "Turkey", "Quit"]
prices = [0, 5.99, 2.99, 6.99, 15.99, 0.99, 0]
total = 0
orderedItem = 0
order = []
while orderedItem != 6:
  for i in range(1, len(foods)):
    print(f"{i}. {foods[i]} -  ${prices[i]}")
  orderedItem =  int(input("Make a selection: "))
  if orderedItem == 6:
    break
  else:
    print(f"You ordered a {foods[orderedItem]}")
    order.append(foods[orderedItem])
    total =  total + prices[orderedItem]
    print(f"Your total is ${total}.")
print(order)
print(f"Total: ${total}")