import jmespath
import json
from rich import print

with open("people.json", "r") as f:
    people = json.load(f)
    
print(people)

search = "people[?(age==`28`)]"

print(jmespath.search(search, people))