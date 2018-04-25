import json
from osmtogeojson.osmtogeojson import process_osm_json

f = open("tests/fixtures/summitschool_overpass.json", "r").read()
#f = open("tests/fixtures/np_overpass.json", "r").read()
j = json.loads(f)

resulting_geojson = process_osm_json(j)

with open("tests/fixtures/summitschool_geojson.json", "r") as f:
#with open("tests/fixtures/np_geojson.json", "r") as f:
    gj = json.loads(f.read())

gj_ids = {}
for f in gj["features"]:
    gj_ids[f["id"]] = f

my_ids = {}
for f in resulting_geojson["features"]:
    my_ids[f["id"]] = f

print([x for x in gj_ids if x not in my_ids])
print("\n")
print([x for x in my_ids if x not in gj_ids])
print("\n")
for f in [x for x in gj_ids if x in my_ids]:
    if gj_ids[f] != my_ids[f]:
        for k in gj_ids[f]:
            if gj_ids[f][k] != my_ids[f][k]:
                if k == "geometry":
                    for c in gj_ids[f][k]["coordinates"]:
                            # sometimes OSM to GEOJSON uses "backwards" or "counter clockwise" polygons.
                        try:
                            assert c in my_ids[f][k]["coordinates"] or list(reversed(c)) in my_ids[f][k]["coordinates"]
                        except:
                            pass
                            print((f, gj_ids[f][k]["type"]))
#                            print(list(reversed(c)))
#                            print("\n")
#                            for mmm  in my_ids[f][k]["coordinates"]:
#                                print(mmm)
                            #print("theirs")
                            #print(json.dumps(gj_ids[f]))
                            #print("mine")
                            #print(json.dumps(my_ids[f]))
#
                else:
                    raise Exception()
                    print((f, k, gj_ids[f][k] == my_ids[f][k], gj_ids[f][k], my_ids[f][k]))

#print(json.dumps(resulting_geojson))
