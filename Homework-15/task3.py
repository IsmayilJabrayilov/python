capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "UK": "London"
}

country = input("Chose your country:" )

if country in capitals:
    capital = capitals[country] 
    print (f"{country} : {capital}")
else :
    print ("Wrong input")