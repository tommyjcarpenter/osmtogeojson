import json
import unittest

from osmtogeojson import osmtogeojson

class ConversionTest(unittest.TestCase):

    # We want to see the differences
    maxDiff = None

    def test_relation_with_different_member_types_becomes_GeometryCollection(self):
        self.compare_files("geomcollection_overpass.json", "geomcollection_geojson.json")
        
    def not_yet_test_np(self):
        self.compare_files("np_overpass.json", "np_geojson.json")
        
    def not_yet_test_summitschool(self):
        self.compare_files("summitschool_overpass.json", "summitschool_geojson.json")
     
    def compare_files(self, inputfile, geojsonfile):
        with open("tests/fixtures/" + inputfile, "r") as f:
            osm_json = json.loads(f.read())

        with open("tests/fixtures/" + geojsonfile, "r") as f:
            expected_geojson = json.loads(f.read())
        
        actual_geojson = osmtogeojson.process_osm_json(osm_json)
        self.assertEqual(actual_geojson, expected_geojson)

if __name__ == '__main__':
    unittest.main()