# ISOXML quirks

this document list some pitfalls and quirks of ISOXML.


## v3 vs v4

this notes should help us to keep track of the wierd differences between the versions

### v3 LineSting Type 1 & 2

If you work with GeoJSON or WKT, you are probably used to the fact that a polygon is a closed LineString, i.e. the first and last points are the same (coordinates).
ISOXML v3 has a different approach for this: a polygon contains several LineStrings, the LineStringType specifies whether a LineString is the polygon exterior or interior (type 1 or 2).
If a LineString is of type 1 or 2, the closing of the LineString is implicit, i.e. the first point does not necessarily have to be included as the last point.

### Partfield

version 3 only allowed one polygon element per subfield (divided fields had to be mapped over several subfields?).
version 4 allows multiple polygons

### Multipolygons

there is no multipolgon in ISOXML, but in version 3 it was possible to combine several LineStrings that represent exterior boundaries (no intersections and presumably of Type1) into one polygon.
A quasi multipolgon. version 4 no longer allows this.

## single point LineString

one could assume that a LineString of length 0 is not valid. WRONG!
ISOXML allows a LineString with only one point for GuidancePatterns A+ and Pivot.
I still have no idea how to convert this correctly... ideas?
why not just use a point? i think because the LineString width is used to determine the swath width.
One could just as well have used an attribute for the GuidancePatterns width... 

## Customer & Farm

As far as I know, it is not necessary to add a customer and a farm to a Task. 
However, some terminals use these entries for navigation, 
and therefore you might run into a situation where the terminal accepts the input, but your task doesn't show up anywhere.
So you should set these entries to avoid this kind of problem.

