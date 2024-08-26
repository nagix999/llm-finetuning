Unnest object (flatten JSON)[¶](#unnest-object-flatten-json "Permalink to this heading")
========================================================================================


Unnest, or flatten, JSON objects or arrays. By default, arrays are kept untouched.



Example[¶](#example "Permalink to this heading")
------------------------------------------------


The following JSON, `jsoncol = {"firstname": "a", "lastname": "b", "details": { "uid": 237, "comment": " a comment"}`, unnested to 1 level of depth yields:


* `jsoncol_firstname = a`
* `jsoncol_lastname = b`
* `jsoncol_details = {"uid": 237, “comment”: “a comment”}`




Options[¶](#options "Permalink to this heading")
------------------------------------------------


**Input column**


Column containing a JSON object or array.


**Maximum depth**


Limit the depth at which the processor stops unnesting the JSON object or array.


**Flatten arrays**


By default, this processor does not flatten arrays when unnesting JSON. If the column contains a JSON array nested *within* a JSON object, the JSON array will be preserved as a single column. If the column contains a JSON array at the top level, the processor will do nothing.



Note


Be aware that unnesting large arrays by selecting this option can lead to high memory and CPU consumption.



**Convert null to empty cell**


Convert a null value in a JSON property — flattened as a cell with the string “null” in it — to an empty cell.


**Prefix output columns**


Prefix output column names with the input column name.