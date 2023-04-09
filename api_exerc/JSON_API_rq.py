import requests

req=requests.get("https://swapi.dev/api/people/2/")
person=req.json()
print(f"Name of this person is\t\t{person['name']}")
print(f"Films with this person are\t\t{person['films']}")

print("Films involcved in")
for film in person["films"]:
    req=requests.get(film)
    film=req.json()
    print(f"Title of film is :{film['title']}") 