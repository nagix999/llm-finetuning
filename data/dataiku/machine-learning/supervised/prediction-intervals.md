Prediction Intervals[¶](#prediction-intervals "Permalink to this heading")
==========================================================================



* [Introduction](#introduction)
* [How does it work](#how-does-it-work)


	+ [Coverage level](#coverage-level)




[Introduction](#id1)[¶](#introduction "Permalink to this heading")
------------------------------------------------------------------


Prediction intervals for regression tasks provide a range within which the actual outcome is expected to fall with a
given probability. They add a layer of transparency and confidence to model predictions by indicating the uncertainty
associated with these predictions.


Prediction intervals are defined in **Analysis \> Basic \> Metrics \> Uncertainty**.


They can also be used as input for [prediction overrides](prediction-overrides.html)




[How does it work](#id2)[¶](#how-does-it-work "Permalink to this heading")
--------------------------------------------------------------------------


To generate prediction intervals, we employ a helper model alongside the primary predictive model.
This helper model is trained to estimate the bounds of the prediction interval, by fitting the residuals (i.e. the
differences between observed and predicted values) from the primary model while taking into account the coverage
level that you specified.



### [Coverage level](#id3)[¶](#coverage-level "Permalink to this heading")


The default coverage level is set at 95%, meaning that the prediction intervals generated is estimated to contain
the actual outcome 95% of the time, under the model’s assumptions. You can adjust this level based on your
requirements for intervals with a higher probability of containing the actual outcome (resulting in wider intervals)
or with a lower probability of containing the actual outcome (resulting in narrower intervals).