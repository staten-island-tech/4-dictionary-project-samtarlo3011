import random
blood_types = ["O positive", "O negative", "A negative","A positive","B negative","B positive","AB negative","AB positive"]
rand=random.randint(0,7)
organs=[
    {
        "name":"kidney", 
        "price": "$200000",
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

]

print(organs[1]["blood_type"])