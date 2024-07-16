import csv 
from math import exp, log 
"""
This script helps you find the best skin that you can buy on the trade site and sell it on steam.
You can use it after you have made a prior selection to find the most profitable variant.
This script creates a csv file with a table of the best and worst purchase options (from top to bottom).
"""

steam_share = 0.15
buy_commission = 0.05
tradelock = False
tradelock_max_time = 0
print("\nTradelocked skins are generally more profitable money-wise.")
answer = input("Consider tradelocked skins? (Y/N): ").lower()
if (answer == "y"):
    tradelock = True
    tradelock_max_time = int(input("If you sell your skin in, say, 1-2 days, \nhow long are you willing to wait for the tradelock to expire? (at most, in hours): ")) 
    
elif (answer == "n"):
    pass 
else:
    print("invalid input, tradelocked skins are not considered.")
    
skins = []
index = 1
print('\nPlease input the skins you consider to buy.')
while(True):
    print(f"\n-------------- Skin #{index} --------------")
    skin_name = input("Skin name (or tag): ")
    buy_price = float(input("Skin buy price: "))
    if (tradelock): time_lock_remaining = int(input("Time until unlocked (in hours): "))
    else: time_lock_remaining = 0
    steam_sell_price = float(input("Skin steam sell price: "))
    
    my_profit = (steam_sell_price * (1 - steam_share)) - (buy_price * (1 + buy_commission))
    if (tradelock):
        weight = my_profit * exp(-(time_lock_remaining / tradelock_max_time) ** 2 * log(4/3))
    else:
        weight = my_profit
        
    skin = [skin_name, buy_price, steam_sell_price, time_lock_remaining, my_profit, weight]
    skins.append(skin)
    index += 1
    
    print("-------------------------------------\n") 
    answer = input("Continue? (Y/N): ").lower()
    if (answer == "y"):
        pass
    elif (answer == "n"):
        break

skins.sort(key=lambda skin:skin[-1], reverse=True)
with open("Best Deals.csv", "w+", newline='') as f:
    writer = csv.writer(f)
    f.write("sep=,\n") # to avoid Excel's stupid regional formats 
    headers = ["Skin name", "Buy price", "Steam sell price", "Tradelock", "My profit", "Weight"]
    writer.writerow(headers)
    for skin in skins:
        writer.writerow(skin)

