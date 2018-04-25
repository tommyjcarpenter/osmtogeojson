import json


def _determine_feature_type(way_nodes):
    # get more advanced???
    if way_nodes[0] == way_nodes[-1]:
        return "Polygon"
    else:
        return "LineString"


def _preprocess(j):
    """preprocess the file out into nodes ways and relations"""
    node_storage = {}
    nodes_reused = {}
    way_storage = {}
    ways_reused = {}
    relation_storage = {}
    for elem in j["elements"]:
        # on our first pass, we go through and put all the nodes into storage
        eid = elem["id"]
        if elem["type"] == "node":
            # sometimes a node is repeated twice in the OSM output; once with tags, once without. This affects filtering out nodes in ways
            if eid not in node_storage:
                node_storage[eid] = elem
            else:
                # if it's just a pure duplicate, which DOES AND CAN happen with certain overpass queries, just drop it
                if elem != node_storage[eid]:
                    nodes_reused[eid] = 1
                    # take the one that has the tags.
                    if "tags" in elem:
                        node_storage[eid] = elem

        # handle ways
        elif elem["type"] == "way":
            if eid not in way_storage:
                way_storage[eid] = elem
            else:
                # if it's just a pure duplicate, which DOES AND CAN happen with certain overpass queries, just drop it
                if elem != way_storage[eid]:
                    ways_reused[eid] = 1
                    # take the one that has the tags.
                    if "tags" in elem:
                        way_storage[eid] = elem

        # handle relations
        elif elem["type"] == "relation":
            if eid not in relation_storage:
                relation_storage[eid] = elem
            else:
                raise Exception()

    return way_storage, ways_reused, node_storage, nodes_reused, relation_storage


def _process_relations(resulting_geojson, relation_storage, way_storage, node_storage, nodes_used_in_ways):
    for rel_id in relation_storage:
        r = relation_storage[rel_id]
        rel = {}
        rel["type"] = "Feature"
        rid = "relation/{}".format(rel_id)
        rel["id"] = rid
        rel["properties"] = r["tags"] if "tags" in r else {}
        rel["properties"]["id"] = rid

        way_types = []
        way_coordinate_blocks = []
        for mem in r["members"]:
            if mem["type"] == "way":
                way_id = mem["ref"]
                processed = _process_single_way(way_id, way_storage[way_id], node_storage, nodes_used_in_ways)
                way_types.append(processed["geometry"]["type"])
                way_coordinate_blocks.append(processed["geometry"]["coordinates"])
            else:
                print(mem["type"])

        rel["geometry"] = {}

        if len([x for x in way_types if x == "Polygon"]) == len(way_types):
            #all polygons, the resulting relation geometry is polygon
            rel["geometry"]["type"] = "Polygon"
            rel["geometry"]["coordinates"] = [x for x in way_coordinate_blocks]

        elif len([x for x in way_types if x == "LineString"]) == len(way_types):
            rel["geometry"]["type"] = "MultiLineString"

            #coordinate_list = []
            #clist = []
            #for x in way_coordinate_blocks:
            #    if clist == []:
            #        clist = x[0]
            #    else:
            #        if clist[-1] == x[0]:
            #            clist += x[1:]
            #        else:
            #            coordinate_list.append(clist)
            #            clist = x
            #coordinate_list.append(clist)
            #rel["geometry"]["coordinates"] = coordinate_list
            rel["geometry"]["coordinates"] = [x for x in way_coordinate_blocks]

        else:
            print(way_types)

        resulting_geojson["features"].append(rel)


def _process_single_way(way_id, w, node_storage, nodes_used_in_ways):
    way = {}
    way["type"] = "Feature"
    wid = "way/{}".format(way_id)
    way["id"] = wid
    way["properties"] = w["tags"] if "tags" in w else {}
    way["properties"]["id"] = wid  # the original osmtogeojson does this, so following suit
    way["geometry"] = {}

    geo_type = _determine_feature_type(w["nodes"])
    way["geometry"]["type"] = geo_type

    if geo_type == "Polygon":
        way["geometry"]["coordinates"] = [[]]  # Polygons are list of list of lists...
        append_here = way["geometry"]["coordinates"][0]
    elif geo_type == "LineString":
        way["geometry"]["coordinates"] = []
        append_here = way["geometry"]["coordinates"]

    for n in w["nodes"]:
        node = node_storage[n]
        append_here.append([node["lon"], node["lat"]])
        nodes_used_in_ways[n] = 1

    return way


def _process_ways(resulting_geojson, way_storage, ways_reused, node_storage, nodes_used_in_ways):
    ways_used_in_relations = {}
    for way_id in way_storage:
        if way_id not in ways_used_in_relations or way_id in ways_reused:
            w = way_storage[way_id]
            way = _process_single_way(way_id, w, node_storage, nodes_used_in_ways)
            resulting_geojson["features"].append(way)


def _process_nodes(resulting_geojson, node_storage, nodes_used_in_ways, nodes_reused):
    # dump the nodes that were not a part of a way into the resulting json
    for nid in node_storage:
        if nid not in nodes_used_in_ways or nid in nodes_reused:
            n = node_storage[nid]
            node = {}
            node["type"] = "Feature"
            new_id = "node/{}".format(n["id"])
            node["id"] = new_id
            node["properties"] = n["tags"] if "tags" in n else {}
            node["properties"]["id"] = new_id
            node["geometry"] = {}
            node["geometry"]["type"] = "Point"
            node["geometry"]["coordinates"] = [n["lon"], n["lat"]]
            resulting_geojson["features"].append(node)


def process_osm_json(j):
    resulting_geojson = {}
    resulting_geojson["type"] = "FeatureCollection"
    resulting_geojson["features"] = []
    way_storage, ways_reused, node_storage, nodes_reused, relation_storage = _preprocess(j)
    nodes_used_in_ways = {}
    _process_relations(resulting_geojson, relation_storage, way_storage, node_storage, nodes_used_in_ways)
    _process_ways(resulting_geojson, way_storage, ways_reused, node_storage, nodes_used_in_ways)
    _process_nodes(resulting_geojson, node_storage, nodes_used_in_ways, nodes_reused)
    return resulting_geojson



#f = open("summitschooloverpass.json", "r").read()
f = open("tests/fixtures/np_overpass.json", "r").read()
j = json.loads(f)

resulting_geojson = process_osm_json(j)

#with open("summitschoolgeo.json", "r") as f:
with open("tests/fixtures/np_geojson.json", "r") as f:
    gj = json.loads(f.read())

gj_ids = {}
for f in gj["features"]:
    gj_ids[f["id"]] = f

my_ids = {}
for f in resulting_geojson["features"]:
    my_ids[f["id"]] = f

#print([x for x in gj_ids if x not in my_ids])
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
                            print(f)
                            print(gj_ids[f][k]["type"])
#                            print(list(reversed(c)))
#                            print("\n")
#                            for mmm  in my_ids[f][k]["coordinates"]:
#                                print(mmm)
                            print("theirs")
                            print(json.dumps(gj_ids[f][k]))
                            print("mine")
                            print(json.dumps(my_ids[f][k]))
#
                else:
                    raise Exception()
                    print((f, k, gj_ids[f][k] == my_ids[f][k], gj_ids[f][k], my_ids[f][k]))

#print(json.dumps(resulting_geojson))
