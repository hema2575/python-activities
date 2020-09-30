candies = ["snickers", "lollypop", "milkduds","peanutbutter", "ahoy"]
allowance = 5
candyCart=[]
for i, candy in enumerate(candies):
    print ("["+str(i)+"]"+candy)
   
for x in range(allowance):      
        candyIndex = int(input("Choose your candy index "))
        candyCart.append(candies[candyIndex])
        print([candyCart])
    
print("please choose an integer")
   
                
 