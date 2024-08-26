Using Jupyter Widgets[¶](#using-jupyter-widgets "Permalink to this heading")
============================================================================


Jupyter Widgets (a.k.a ipywidgets) are a way to build interactive GUIs in Jupyter notebooks.


For more information about widgets, see the [documentation](https://ipywidgets.readthedocs.io).



Setup[¶](#setup "Permalink to this heading")
--------------------------------------------


Support for widgets needs to be enabled globally in the DSS Jupyter notebook by an administrator


* Go to the DSS data directory
* Run the following commands, where



> + DATADIR is the absolute path to the DSS data directory
> 	+ INSTALLDIR is the absolute path to the DSS installation directory (`dataiku-dss-X.Y.Z`)
> 
> ```
> JUPYTER_CONFIG_DIR="$DATADIR/jupyter-run/jupyter" JUPYTER_DATA_DIR="$DATADIR/jupyter-run/jupyter"  PYTHONPATH="$INSTALLDIR/dku-jupyter/packages/" ./bin/python -m notebook.nbextensions install --py widgetsnbextension --user
> 
> JUPYTER_CONFIG_DIR="$DATADIR/jupyter-run/jupyter" JUPYTER_DATA_DIR="$DATADIR/jupyter-run/jupyter"  PYTHONPATH="$INSTALLDIR/dku-jupyter/packages/" ./bin/python -m notebook.nbextensions enable --py widgetsnbextension
> 
> ```
* Check installation:



> ```
> JUPYTER_CONFIG_DIR="$DATADIR/jupyter-run/jupyter" JUPYTER_DATA_DIR="$DATADIR/jupyter-run/jupyter"  PYTHONPATH="$INSTALLDIR/dku-jupyter/packages/" ./bin/python -m notebook.nbextensions list
> 
> ```



> This command should have output like:
> 
> 
> 
> > ```
> > jupyter-js-widgets/extension  enabled
> >  - Validating: OK
> > 
> > ```


* Edit `bin/env-site.sh` and add the following line



> ```
> export JUPYTER_CONFIG_DIR="$DIP_HOME/jupyter-run/jupyter"
> 
> ```
* Restart DSS




Using widgets[¶](#using-widgets "Permalink to this heading")
------------------------------------------------------------


Open a new notebook, and enter sample widget code:



Note


If you are using a custom code env, don’t forget to included the ipywidgets package in your code env




```
import ipywidgets

ipywidgets.IntSlider()

```


A slider should appear. You can now use ipywidgets.