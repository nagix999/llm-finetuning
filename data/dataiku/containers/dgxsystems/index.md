Using NVIDIA DGX Systems[¶](#using-nvidia-dgx-systems "Permalink to this heading")
==================================================================================



Warning


**Tier 2 support**: NVidia DGX support is experimental and covered by [Tier 2 support](../../troubleshooting/support-tiers.html)



You can use containerized execution using DGX Kubernetes cluster as the underlying Kubernetes engine.


Dataiku has been tested for use on DGX Systems and is certified as DGX\-Ready Software.


To use DGX Systems you will need to add DGX Kubernetes cluster as an unmanaged cluster in Dataiku.


Additional configuration includes:


* Building an image with CUDA support to set up a cluster with a CUDA\-enabled base image.
* Adding a custom reservation to request multiple GPUs.


Both cloud and on\-premises DGX systems have been successfully tested. Multi\-Instance GPU (MIG) support has not been tested