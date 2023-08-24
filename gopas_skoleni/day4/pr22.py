import tomllib #pro python11
from pprint import pprint

from pprint import pprint
with open("konf.toml", "rb") as f:
    data = tomllib.load(f)

pprint(data)
print(data["owner"],["name"])