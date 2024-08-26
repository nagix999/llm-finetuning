Extract date elements[¶](#extract-date-elements "Permalink to this heading")
============================================================================


Extract various elements of a ISO\-8601 formatted date (`yyyy-MM-ddTHH:mm:ss.SSSZ`) to other columns.



Options[¶](#options "Permalink to this heading")
------------------------------------------------


**Date column**


Column containing data in ISO\-8601 format. Use a Prepare step to parse your data into this format if it isn’t already.


**Timezone**


Change the timezone from the UTC default. Options include using a TZ column, an IP column, or specifying a timezone from the dropdown.


**Date elements**


To extract a given date element into a column, give the corresponding column a name. Each output column is optional; if left empty, the processor will not extract the date element.



Note


Year, month (1\-12\), day, day of week (1\-7, 1\=Monday, 7\=Sunday), hour, minutes, seconds, milliseconds, week of year (1\-53\), timestamp (UNIX timestamp in seconds since Epoch) can all be extracted as separate outputs.





Related resources[¶](#related-resources "Permalink to this heading")
--------------------------------------------------------------------


For more information on managing dates with Dataiku DSS, please see the [reference documentation](https://doc.dataiku.com/dss/latest/preparation/dates.html).