Compute distance between geospatial objects[¶](#compute-distance-between-geospatial-objects "Permalink to this heading")
========================================================================================================================


This processor computes the geodesic distance between a geospatial column and another geospatial object.


You can compare a column with:


* A fixed geopoint
* A fixed geospatial object
* Another geospatial column


The computation outputs a number of distance units (kilometers, miles)
in another column.


In the case of a distance between two geometries, the distance is the shortest distance between these two.


The processor assumes that the data uses GPS coordinates, also known as WGS\-84, SRID 4326 or EPSG:4326\.


GeoJSON format is not supported with the SQL Engine when using PostgreSQL.