Drift reference[¶](#drift-reference "Permalink to this heading")
================================================================


When you are viewing a [Model Evaluation in a Model Evaluation Store](../model-evaluations/analyzing-evaluations.html), you have access to the three types of Drift.


Drift is always about comparing the behavior of the current Model Evaluation with regards to a “reference”.


For each type of drift, you need to select the “reference”.


![../../_images/reference-selector.png](../../_images/reference-selector.png)
The reference must be an evaluation that is compatible. It may come from:


* The evaluation that was created automatically when training the Saved Model that was used to compute the current Model Evaluation (default)
* Another Model Evaluation (either in the same store or in another)
* The evaluation that was created automatically when training a model in a Visual Analysis (even if it was never deployed)


By default, DSS automatically selects the evaluation that was created automatically when training the Saved Model that was used to compute the current Model Evaluation. This is most frequently what you need.