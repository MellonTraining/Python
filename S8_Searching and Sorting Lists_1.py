Appleproducts = ["mac", "iphone", "ipad", "apple watch", "ipod"] 
AppleproductsSelect = ""
while str.upper(AppleproductsSelect) != "QUIT":
    AppleproductsSelect = input("Please type an Apple Product name: ")    
    if (Appleproducts.count(AppleproductsSelect) >= 1):
        print("The Apple Product exists in the list!")    
    elif (str.upper(AppleproductsSelect) != "QUIT"):
        print("The list doesn't contain the Apple Product.")
