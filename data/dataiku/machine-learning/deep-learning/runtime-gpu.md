Runtime and GPU support[¶](#runtime-and-gpu-support "Permalink to this heading")
================================================================================


The training/scoring of Keras models can be run on either a CPU, or one or more GPUs. Training on GPUs is usually much faster, especially when images are involved.



Code environment[¶](#code-environment "Permalink to this heading")
------------------------------------------------------------------


Deep Learning in DSS uses specific Python libraries (such as Keras and TensorFlow) that are not shipped with the DSS built\-in Python environment.


Therefore, before training your first deep learning model, you must create a code environment with the required packages. See [Code environments](../../code-envs/index.html) for more information about code environments.


To help you, you can simply click “Add additional packages” in the “Packages to install” section of the code environment.


![../../_images/code-env-add-packages.png](../../_images/code-env-add-packages.png)
There you can select the “Visual Deep Learning: Tensorflow. CPU, and GPU with CUDA11\.2 \+ cuDNN 8\.1” package preset.


Once the proper environment is set\-up, you can create a Deep Learning model. DSS will look for an environment that has the required packages and select it by default. You can select a different code environment at your own risk.




Selection of GPU[¶](#selection-of-gpu "Permalink to this heading")
------------------------------------------------------------------


If your DSS instance has access to any GPU resource(s), you can opt to train the model on a selection of these when you click ‘TRAIN’.


![../../_images/gpu-selection1.png](../../_images/gpu-selection1.png)
When you deploy a scoring or evaluation recipe, you can also choose to score or evaluate using GPU(s), configured in the recipe settings.


If a model trained on a GPU code environment is deployed as a service endpoint on an API node, the endpoint will require access to a GPU on the API node, and will automatically use GPU resources.


We enforce ‘allow growth’ on deep learning models ran on API nodes to ensure they only allocate the required memory (see TensorFlow [documentation](https://www.tensorflow.org/guide/gpu#limiting_gpu_memory_growth)).




Using multiple GPUs for training[¶](#using-multiple-gpus-for-training "Permalink to this heading")
--------------------------------------------------------------------------------------------------


If you have access to GPU(s) on your DSS instance server or on any available containers, you can use them to speed up training. You will not need to change your model architecture to allow you to use GPUs, as DSS will manage this.


DSS will replicate the model on each GPU, then split each batch equally between GPUs. During the backwards pass, gradients computed on each GPU are summed. This is made possible thanks to TensorFlow’s [MirroredStrategy](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy).


This means that on each GPU, the actual batch\_size will be batch\_size / n\_gpus. Therefore you should use a batch\_size that is a multiple of the number of GPUs.


Note: To compare the speed of two trainings, you should always compare trainings with the same per GPU batch\_size, i.e. if the first training is run on one GPU with a batch\_size of 32, and the second on two GPUs, the batch\_size should be 64\.