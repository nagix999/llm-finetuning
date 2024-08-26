Evaluation recipe[¶](#evaluation-recipe "Permalink to this heading")
====================================================================



* [Input dataset](#input-dataset)
* [Output datasets](#output-datasets)




Warning


*Model Evaluation Stores* (MES) are not supported for causal prediction models.




[Input dataset](#id1)[¶](#input-dataset "Permalink to this heading")
--------------------------------------------------------------------


The input dataset for the evaluation recipe must contain at least:


* The outcome column
* The treatment column.




[Output datasets](#id2)[¶](#output-datasets "Permalink to this heading")
------------------------------------------------------------------------



### Output dataset[¶](#output-dataset "Permalink to this heading")


The evaluation recipe computes the evaluation dataset by computing the predicted effect based on the input data and the saved causal model. For multi\-valued treatment variables, the recipe outputs as many treatment effects as there are treatment values (excluding the control value).


If a propensity model was trained by enabling the [Treatment Analysis](settings.html#treatment-analysis) setting in the Lab Analysis, it is possible to use it to predict the propensity (probability of receiving the treatment) and in turn compute prediction performance metrics on the propensity model (log loss, ROC\-AUC and calibration loss).




### Metrics dataset[¶](#metrics-dataset "Permalink to this heading")


The output metrics dataset contains the computed metrics. Causal performance metrics and treatment prediction metrics of the propensity model (if enabled in [Treatment Analysis](settings.html#treatment-analysis)) can be computed.


For multi\-valued treatments, the values displayed are the aggregates across treatments, weighted by the relative size of each treatment group.