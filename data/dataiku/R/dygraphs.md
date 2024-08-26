Using Dygraphs[¶](#using-dygraphs "Permalink to this heading")
==============================================================


The dygraphs package is an R interface to the dygraphs JavaScript charting library. It provides rich facilities for charting time\-series data in R.


More information on dygraphs can be found at <https://rstudio.github.io/dygraphs/>



Installing dygraphs[¶](#installing-dygraphs "Permalink to this heading")
------------------------------------------------------------------------


The dygraphs package is not installed by default in DSS.
The recommended method for doing so is to use a [code environment](../code-envs/index.html). See [how to install R packages](packages.html)


You need to install the `dygraphs` package. If you are using a Conda environment, you can also choose to install in the Conda section the `r-dygraphs` package.




Displaying charts in a Jupyter notebook[¶](#displaying-charts-in-a-jupyter-notebook "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------


dygraphs charts will not work properly if you only use the `dygraph()` method in a Jupyter R notebook.


To display dygraphs charts in a Jupyter notebook, use:



```
library(dataiku)
library(dygraphs)

the_graph <- dygraph(mydata)

dkuDisplayDygraph(the_graph)

```


For example, to display the sample `lungDeaths` dataset



```
library(dygraphs)
library(dataiku)
lungDeaths <- cbind(mdeaths, fdeaths)
dkuDisplayDygraph(dygraph(lungDeaths))

```



### Converting a date column to a time\-series[¶](#converting-a-date-column-to-a-time-series "Permalink to this heading")


Dygraphs works primarily with time series. If you have a DSS dataset with a “date” column, you’ll need to convert your dataframe to a time series or XTS object.


For example, the following will create a time\-series of `revenue` by `order_ts`



```
library(xts)
df <- dkuReadDataset("orders")

timeseries <- xts(df$revenue, order.by=as.Date(df$order_ts))

# You can then plot timeseries
dkuDisplayDygraph(dygraph(timeseries) %>% dyRangeSelector())

```





Displaying charts on a dashboard[¶](#displaying-charts-on-a-dashboard "Permalink to this heading")
--------------------------------------------------------------------------------------------------


dygraphs charts generated using R code can be shared on a DSS dashboard using the “static insights” system.


Each dygraphs chart can become a single insight in the dashboard. Each chart will retain full interactive capabilities (if you have defined them in your dygraph)


To do so, create [static insights](../R-api/static_insights.html)



```
# dg is a dygraphs object, created using the dygraph() function

dkuSaveHTMLInsight("my-dygraphs-plot", dg)

```


From the Dashboard, you can then add a new “Static” insight, select the `my-dygraphs-plot` insight



### Refreshing charts on a dashboard[¶](#refreshing-charts-on-a-dashboard "Permalink to this heading")


You can refresh the charts automatically on a dashboard by using a scenario to re\-run the above piece of code.


This call to `dkuSaveHTMLInsight` code can be:


* In a DSS recipe (use a regular “Build” scenario step)
* In a Jupyter notebook (use a “Export notebook” scenario step)





Using in Shiny[¶](#using-in-shiny "Permalink to this heading")
--------------------------------------------------------------


Dygraphs can be used directly in Shiny. See <https://rstudio.github.io/dygraphs/shiny.html> for more information.


See [https://github.com/dataiku/dss\-code\-samples/tree/master/visualization/shiny/shiny\-and\-dygraphs](https://github.com/dataiku/dss-code-samples/tree/master/visualization/shiny/shiny-and-dygraphs) for a complete code sample