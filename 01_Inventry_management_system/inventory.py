import json

with open("data/products.json","r") as R:
    data = json.load(R)

class Inventory:
    
         
    def add_product(self):
        
        self.Adding_as_dict={
                        
            "Id": input("Enter Unique Id: "),
            "Name": input("Enter Product name: "),
            "Category": input("Enter Product category: "),
            "Price": int(input("Enter Price: ")),
            "Quantity": int(input("Enter Quantity: ")),
            "Supplier": input("Enter Supplier Name: "),
            "Created_Date":  input("Enter Created date: ")           
        }
            
        for i in data:
            
            if i["Id"] == self.Adding_as_dict["Id"]:
                print("Product is already exist") 
                return # End of function 
                
        data.append(self.Adding_as_dict)
        
        with open("data/products.json","w") as file:
            json.dump(data,file,indent=4) 
            print("Product is succesfully added")
        
    def update_product(self):
            
        Cheaking_id=input("Please enter product id: ")
        
        for product in data:  
            
            if Cheaking_id == product["Id"]:
        
                print("1.Name")
                print("2.Category")
                print("3.Price")
                print("4.Quantity")
                print("5.Supplier")
                print("Please enter your command by number ")
        
                user=input("Chose 1/2/3/4/5: ")
                if user not in ["1", "2", "3", "4", "5"]:
                    
                    print("Invalid input please chose the candrect option ")
                    break
                    
                if user =="1":
                    
                    a=input("Enter new product name: ")
                    product["Name"] = a
                            
                    with open("data/products.json","w")as file:
                        json.dump(data,file,indent=4)
                        print("Product updated successfully.")
                        
                        
                elif user == "2":
                    b=input("Enter new Product Category: ")
                    product["Category"]=b
                    
                    with open("data/products.json","w")as file:
                        json.dump(data,file,indent=4)
                        print("Product updated successfully.")
                        
                    
                elif user =="3":
                    b=int(input("Enter new Product Category: "))
                    product["Price"]=b
                    
                    with open("data/products.json","w")as file:
                        json.dump(data,file,indent=4)
                        print("Product updated successfully.")
                
                elif user == "4":
                    a=int(input("Enter new product name: "))
                    product["Quantity"] = a
                            
                    with open("data/products.json","w")as file:
                        json.dump(data,file,indent=4)
                        print("Product updated successfully.")
                    
                
                elif user =="5":
                    a=input("Enter new product name: ")
                    product["Supplier"] = a
                            
                    with open("data/products.json","w")as file:
                        json.dump(data,file,indent=4)
                        print("Product updated successfully.")
                break
        else:
            print("Invalid product id")

    def delete_product(self):
            
        user=input("please enter product id: ")
        
        for product in data:
            if product["Id"] == user:
                data.remove(product)
                
                with open("data/products.json","w")as file:
                    json.dump(data,file,indent=4)
                    print("Product removed successfully.")
                
        

    def search_product(self): 
                
        user=input("enter product id: ")
        
        for product in data:           
            if product["Id"] == user:
                print(json.dumps(data[0],indent=4))

