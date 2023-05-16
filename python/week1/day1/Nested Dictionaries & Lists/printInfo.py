dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}
location = "LOCATIONS"
instructor = "INSTRUCTORS"
def printInfo(some_dict):
    for dict in some_dict:
        print(len(some_dict[dict]),dict.upper())
        for x in range (0,len(some_dict[dict])):
            
            print(some_dict[dict][x])


print(printInfo(dojo))

