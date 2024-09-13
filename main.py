actual_price = 499
sell_price = int(input("Enter sell price : "))

profit = sell_price - actual_price
loss = actual_price - sell_price

if(sell_price>actual_price):
 print("The profit is ",profit)
else :
 print("The loss is ",loss)