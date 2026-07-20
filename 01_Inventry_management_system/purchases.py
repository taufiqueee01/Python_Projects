import json
from datetime import datetime

Time=(datetime.now().strftime("%B %d, %Y %I:%M %p"))

with open("data/products.json","r") as opn:
    Products_json=json.load(opn)
    
with open("data/purchases.json","r") as opn:
    Purchases_json=json.load(opn)
    
class Purchases:
    
    def BuyStocks(self):
        
        print("Welcome to buy stock area !")
        
        Name=input("Enter product name: ")
        
        for product in Products_json:
            
            if Name != product["Name"]:
                continue
                
            elif Name == product["Name"]:
                
                print(f"Product name : Quantity \n{product["Name"]} : {product["Quantity"]}")
                print(f"If you want to purchase more stocks of {product["Name"]} \n1.Yes\n2.No")
                
                choice=input("Enter here--->    ").capitalize()
                
                if choice=="Yes":
                    
                    Quantity=int(input("Enter quantity: "))
                    
                    if Quantity<=0:
                        print("Invalid quantity")
                        
                    else:
                        product["Quantity"]+=Quantity
                        print(f"Now the product have {product["Quantity"]} stocks")
                        
                        History={
                            "Date":Time,
                            "Id":product["Id"],
                            "Name":product["Name"],
                            "Quantity":Quantity
                        }
                        
                        Purchases_json.append(History)
                        
                        with open("data/purchases.json","w") as f:
                            json.dump(Purchases_json,f,indent=4)
                            
                        with open("data/products.json","w") as Buy:
                            json.dump(Products_json,Buy,indent=4)
                        break
                        
                
                elif choice=="No":
                    print("Thnakuu 😊 for visiting ")
                    break
                
                else:
                    print("Please enter valid options")
        else:
            print("Product not found")                    
    
    def View_history(self):   
        print(json.dumps(Purchases_json,indent=4))
         
                
                

        
        
# Date
# quantity