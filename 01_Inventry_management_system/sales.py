import json
from datetime import datetime

Time=(datetime.now().strftime("%B %d, %Y %I:%M %p"))

with open("data/products.json","r") as f:
    Products_json=json.load(f)
    
with open("data/sales.json","r") as f:
    Sales_json=json.load(f)   
    
class Sales:
    
    def User(self):
        Name=input("Please enter your name: ")
        
        print(f"°=============== Heyyy {Name} =============°")
        print("\nAvailable products are")
        
        for products in Products_json:
            print(products["Name"])
        # print(json.dumps(Products_json,indent=4))

        Product_choice=input("Enter product name: ").capitalize()
        
        for i in Products_json:
            if Product_choice==i["Name"]:  
                              
                print(f"Product is selected ' {i["Name"]} '")
                print(f"Quantity must me less that or equal to {i["Quantity"]} ")
                print(f"Product price is {i["Price"]}/stock")
                Quantity_select=int(input("Enter quantity: "))
                                  
                if Quantity_select<i["Quantity"]:
                    print("Type Yes or No")
                    
                    total_money=Quantity_select*i["Price"]
                    
                    print(f"\nYour total price is {total_money}")
                    
                    Sure_or_not=input("\nAre you sure want to buy: ").capitalize()
                    
                    if Sure_or_not == "Yes":
                        print(f"Thankyuu for purchasing have a nice day 🤞🤗")
                        
                        i["Quantity"]-=Quantity_select
                        
                        Data={
                            "Date":Time,
                            "Customer Name":Name,
                            "Total Moaney":total_money,
                            "Quantity":Quantity_select
                        }
                        
                        Sales_json.append(Data)
                        
                        with open("data/products.json","w") as f:
                            json.dump(Products_json,f,indent=4)
                            
                        with open("data/sales.json","w") as file:
                            json.dump(Sales_json,file,indent=4)
                        
                        break
                    
                    elif Sure_or_not=="No":
                        
                        print("Thankyou for visiting 😊")    
                        break       
                                 
                    else:
                        print("Please enter valid option")
                else:
                    print(f"Please enter the quantity upto {i["Quantity"]}") 
        else:
            print("Invalid choice")    
               
