# osmtogeojson

This is a W-I-P reimplementation of osmtogeojson in pure python. 

# Todos

I believe everything is done right now with the exception of "winding order". That is, when I re-assemble a bunch of ways that happen to form a polygon, some GEOJSON linters complain that my polygon violates the "right hand rule". So I have to learn about that and fix it.

For the vast majorty of simple things (i.e., everythign except relations that mush together to form higher level structures) I think this is 100% compliant. 

Needs more Testing. 
