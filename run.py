import json
from osmtogeojson.osmtogeojson import process_osm_json

#f = open("tests/fixtures/summitschool_overpass.json", "r").read()
f = open("tests/fixtures/np_overpass.json", "r").read()
j = json.loads(f)

resulting_geojson = process_osm_json(j)

#with open("tests/fixtures/summitschool_geojson.json", "r") as f:
with open("tests/fixtures/np_geojson.json", "r") as f:
    gj = json.loads(f.read())

gj_ids = {}
for f in gj["features"]:
    gj_ids[f["id"]] = f

my_ids = {}
for f in resulting_geojson["features"]:
    my_ids[f["id"]] = f

print("in their not in mine")
print([x for x in gj_ids if x not in my_ids])
print("in mine not in theirs")
print([x for x in my_ids if x not in gj_ids])
print("\n")
for f in [x for x in gj_ids if x in my_ids]:
    if gj_ids[f] != my_ids[f]:
        for k in gj_ids[f]:
            if gj_ids[f][k] != my_ids[f][k]:
                printstuff = False
                if k == "geometry":
                    for cindex, c in enumerate(gj_ids[f][k]["coordinates"]):
                        # sometimes OSM to GEOJSON uses "backwards" or "counter clockwise" polygons.
                        try:
                            assert c in my_ids[f][k]["coordinates"] or list(reversed(c)) in my_ids[f][k]["coordinates"]
                        except:
                            print(("FAILING", f))
                            printstuff = True
                            break
                    if printstuff:
                        print("theirs")
                        print([len(y) for y in gj_ids[f][k]["coordinates"]])
                        print(json.dumps(gj_ids[f]))
                        print("mine")
                        print([len(y) for y in my_ids[f][k]["coordinates"]])
                        print(json.dumps(my_ids[f]))
                else:
                    print(k)
                    raise Exception("Non-gemoetry field differs, investigate!")

#print(json.dumps(resulting_geojson))
