import random
blood_types = ["O positive", "O negative", "A negative","A positive","B negative","B positive","AB negative","AB positive"]
rand=random.randint(0,7)
cart=[]
price=[]
organs=[
    {
        "name":"kidney", 
        "price": "200000",
        "blood_type": blood_types[rand],
    }
    ,
    {
        "name" : "heart",
        "price" : "800000",
        "blood_type": blood_types[rand],
    }
    ,
    {
        "name" : "brain", 
        "price" : "600",
        "blood_type" : blood_types[rand],
    }
    ,
    
    {"name": "liver", "price": 500000, "blood_type": blood_types[rand]},
    {"name": "lung", "price": 350000, "blood_type": blood_types[rand]},
    {"name": "pancreas", "price": 300000, "blood_type": blood_types[rand]},
    {"name": "cornea", "price": 25000, "blood_type": blood_types[rand]},
    {"name": "bone marrow", "price": 150000, "blood_type": blood_types[rand]},
    {"name": "intestine", "price": 400000, "blood_type": blood_types[rand]},
    {"name": "stomach", "price": 200000, "blood_type": blood_types[rand]},
    {"name": "spleen", "price": 180000, "blood_type": blood_types[rand]},
    {"name": "gallbladder", "price": 120000, "blood_type": blood_types[rand]},
    {"name": "thyroid", "price": 90000, "blood_type": blood_types[rand]},
    {"name": "adrenal gland", "price": 110000, "blood_type": blood_types[rand]},
    {"name": "skin graft", "price": 70000, "blood_type": blood_types[rand]},
    {"name": "bladder", "price": 160000, "blood_type": blood_types[rand]},
    {"name": "appendix", "price": 50000, "blood_type": blood_types[rand]}
]
conti=input("wanna buy an organ? ")
if conti =="no":
    print ("aight then why you even here")

while conti == "yes":
    x=input("which organ you want twin: kidney, heart, brain, liver, lung, pancreas, cornea, bone marrow, intestine, stomach, spleen, gallbladder, thyroid, adrenal gland, skin graft, bladder, appendix "
)
    if x == organs[0]["name"]:
        y = 0
    elif x == organs[1]["name"]:
        y = 1
    elif x == organs[2]["name"]:
        y = 2
    elif x == organs[3]["name"]:
        y = 3
    elif x == organs[4]["name"]:
        y = 4
    elif x == organs[5]["name"]:
        y = 5
    elif x == organs[6]["name"]:
        y = 6
    elif x == organs[7]["name"]:
        y = 7
    elif x == organs[8]["name"]:
        y = 8
    elif x == organs[9]["name"]:
        y = 9
    elif x == organs[10]["name"]:
        y = 10
    elif x == organs[11]["name"]:
        y = 11
    elif x == organs[12]["name"]:
        y = 12
    elif x == organs[13]["name"]:
        y = 13
    elif x == organs[14]["name"]:
        y = 14
    elif x == organs[15]["name"]:
        y = 15
    elif x == organs[16]["name"]:
        y = 16
    cart.append(organs[y]["name"])
    price.append(int(organs[y]["price"]))
    conti = input("you wanna keep going or nah: ")
cost=sum(price)
print ("cart:",cart, "price:",cost )