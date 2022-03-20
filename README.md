# PLNTTER

PLNTTER is a Python library for developing and testing navigation algorithms

PLNTTER = Pythonic Localization / Navigation Toolkit for Terrestrial / Extraterrestrial Roving


## Usage

Before using PLNTTER's utility classes, run the following:

```python
pip install --upgrade matplotlib numpy opencv-python pytest seaborn spiceypy
```

Then, build the package:

```python
python3 setup.py install
```

Finally, verify the build by running:

```python
python3 main.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## TODO's

- finish spiceypy auto-builder
- finish defining vector / quaternion operations
- decide on matrix class
- create plotting class for seaborn and plotly
- add EKF and UKF predict / update equations
