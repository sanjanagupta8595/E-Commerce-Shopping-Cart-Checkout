topic = "E-Commerce Shopping Cart & Checkout" 
print(topic.center(100))

product_list = {
            "GROCERY STORE": 
                {"MILK" : 50 ,
                 "BREAD": 50,
                 "1 EGG":12,
                 "1 kg RICE":80,
                 "1L OIL": 180},
            "MEN'S SECTION": 
                {"SHIRT" : 250,
                 "T-SHIRT":150,
                 "JEAANS" : 500,
                 "CAP": 120,
                 "SHORT PANTS":200,
                 "LOWER PANTS":300},
            "WOMEN'S SECTION":
                {"TOPS": 250,
                 "JEANS":550,
                 "PANTS" : 350,
                 "DENIM SHIRTS":300,
                 "FROCKS":350,
                 "ONE PIECE":510,
                 "SUITS":380},
            "KIDS SECTION":
                {"T-SHIRT": 150,
                 "PANTS":180,
                 "COORD-SETS":350,
                 "FROCKS":250},
            "HOUSEHOLD ITEMS":
                {"DUSTBIN":200,
                 "1 DOZEN SPOON":250,
                 "3 SET OF GLASS": 300,
                 "5 SET OF FORK":320,
                 "2 SET OF PLATE": 160,
                 "3 SET OF CUP":150,
                 "COOKER":400},
                }
exit = "QUIT"

i = 0
total = 0
while i<=1000:
    item = input("Enter your item : ").upper()

    if item == "QUIT":
        break

    found = False
    price = 0

    for category in product_list.values():
        if item in category:
            found = True
            price = category[item]
            break

    if found:
            print(f"Your listed item : {item}")
            print (f"price : {price}")
            total +=price
            i +=1
    else :
            print (f"{item} : product is not found")

print(f"your total bill : {total}")

print("thanks for shopping")
print("HAVE A NICE DAY")
