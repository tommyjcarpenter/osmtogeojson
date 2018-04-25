def merge_polygon(rel):
    """
    takes a relation that might possibly be a bunch of ways that HAPPEN to be a polygon, and transforms
    the MultiLineString object into a polygon object
    """
    return rel

def merge_line_string(rel):
    return _merge_line_string(rel, 0)

def _merge_line_string(rel, startindex):
    """
    takes a relation that might possibly be a bunch of ways that HAPPEN to be a single line, and transforms
    the MultiLineString object into a single LineString object
    """

    coordinate_list = rel["geometry"]["coordinates"]
    for clindex, cl in enumerate(coordinate_list):
        if clindex <= startindex:
            pass
        elif clindex < len(rel["geometry"]["coordinates"]):
            if cl[0] == coordinate_list[startindex][-1]:
                rel["geometry"]["coordinates"][startindex] = rel["geometry"]["coordinates"][startindex] + cl[1:]
                del rel["geometry"]["coordinates"][clindex]
                return _merge_line_string(rel, startindex)
            else:
                clreversed = list(reversed(cl))
                if clreversed[0] == coordinate_list[startindex][-1]:
                    rel["geometry"]["coordinates"][startindex] = rel["geometry"]["coordinates"][startindex] + clreversed[1:]
                    del rel["geometry"]["coordinates"][clindex]
                    return _merge_line_string(rel, startindex)

    # see if we've swuashed everything down into one
    if len(rel["geometry"]["coordinates"]) == 1:
        # see if we got a line string, or a polygon
        if rel["geometry"]["coordinates"][startindex][0] == rel["geometry"]["coordinates"][startindex][-1]:
            print("POLYGON!!!")
            raise Exception()
        else:  # linestring
            rel["geometry"]["type"] = "LineString"
            rel["geometry"]["coordinates"] = rel["geometry"]["coordinates"][0]

    elif startindex < len(rel["geometry"]["coordinates"])-1:
        return _merge_line_string(rel, startindex+1)

    return rel
