FROM pangeo/pangeo-notebook:aadc1aa

RUN pip install pyyaml==5.4.1

COPY process_recipe.py /process_recipe.py

ENTRYPOINT [ "python3", "/process_recipe.py" ]
