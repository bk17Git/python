peoples = [
    {"name" : "Harry" , "House" : "Assam"},
    {"name" : "Sam" , "House" : "Madhya Pradesh"},
    {"name" : "Johny" , "House" : "Delhi"},
    {"name" : "Bill" , "House" : "Punjab"}
]

peoples.sort(key= lambda person: person["name"])

print(peoples)