# PLNTTER

PLNTTER is a Python library for developing and testing navigation algorithms

PLNTTER = Python Library for Navigation Tools (i.e., Sensors), (Algorithm) Testing and Exploratory Research


## Usage

Before using PLNTTER's utility classes, run the following command:

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


## Priority TODO's

- trajectory generator
- state propagator -> pose, sensor error states
- EKF and UKF predict / update equations

## Eventual TODO's

- matrix and state classes
- spiceypy auto-build
- synthetic star image generator
