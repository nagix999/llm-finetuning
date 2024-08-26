Your first Computer vision model[¶](#your-first-computer-vision-model "Permalink to this heading")
==================================================================================================


Here is how you can quickly train an **Object detection** or **Image classification** model:



Install the required packages[¶](#install-the-required-packages "Permalink to this heading")
--------------------------------------------------------------------------------------------


First, you need the appropriate packages to be able to run the model.
Luckily there is one code environment (see [Code environments](../../code-envs/index.html)) containing all the appropriate packages already
built for you, that you just need to install:


Go to the “Administration \>\> Settings \>\> Misc” tab. In the section “Computer vision code environment”, you can create either an Object detection or
an Image classification code environment by selecting your
Python interpreter and clicking on create the environment. It will install all the required packages for the corresponding task.




Create the analysis[¶](#create-the-analysis "Permalink to this heading")
------------------------------------------------------------------------


Make sure to have the correct [Computer vision analysis inputs](inputs.html) before continuing.


Then create the analysis: select the Dataset then click on “Action panel \>\> Lab \>\> Object detection” (or Image classification depending on your need).
Choose your target column and the image folder. Then click “Create” and you’re done !




Review the design of your model (optional)[¶](#review-the-design-of-your-model-optional "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------------


If you want to train a model with the default parameters you can simply proceed by clicking the “Train” button. You
will be asked whether or not you want to select GPUs for training.


If you prefer reviewing the design of the model first, here are some tips on what you can configure:


* The **Target tab** displays a sample of your data with the class labels or bounding boxes previewed on the images. If the boxes or labels do not correspond with your image as you expect, you may have an issue with the format of your targets. See [Computer vision analysis inputs](inputs.html) for the expected format.
* The **Training tab** allows you to change the default training parameters according to your data. See [Model architectures \& training parameters](architecture.html) for the complete list of parameters available.
* The **Train / Test tab** allows you to change the ratio of test samples compared to the training samples. See [Settings: Train / Test set](../supervised/settings.html#settings-train-test) for more information.
* The **Metrics tab** allows you to choose which metric will be optimized during training. See [Evaluation Metrics](evaluation-metrics.html).
* The **Data augmentation tab** allows you to introduce some diversity in your training dataset, and visualize dynamically some examples of those augmentations on your images. See [Data augmentation](data-augmentation.html) for more information.
* You shouldn’t need to change anything in the **Runtime Environment tab** for now.


Once you’re ready, Click on “Train”, select your GPU settings (see [GPU support](runtime-gpu.html)) then click “Train” again.
This will prepare your model then start the training loop.




Monitor the performance of your model during training[¶](#monitor-the-performance-of-your-model-during-training "Permalink to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------


The chart displays the performance of your model at the end of each epoch, against your chosen metric.
Once training completes, you can assess the performance of your model (see
[Performance assessment](performance-assessment.html)), then deploy, retrain and score it, like any other Visual Machine Learning model in
DSS.