# To use it locally in `Jupyter Notebook` or `Jupyter Lab` 
Install dependecies:

1. Rasterio using:

    a. First install linux (ubuntu) dependencies

        - sudo add-apt-repository ppa:ubuntugis/ppa
        - sudo apt-get update
        - sudo apt-get install python-numpy gdal-bin libgdal-dev

    b. Then install rasterio   
        `conda install -c conda-forge rasterio` 

2. Matplotlib

    `conda install -c conda-forge matplotlib`

3. Plotly

    `conda install -c conda-forge plotly`

You can use pip to install those libraries as well.
Also, It is suggested to create a environment before installing these dependencies, either using `venv` or `conda env`

Note: Inside notebook, use `pio.renderers.default = 'jupyterlab'`, if the COG visualization is not showing up.

# To use it in `Google colab`

Upload it and run.

Note: Inside notebook, use `pio.renderers.default = 'colab'`, if the COG visualization is not showing up.
