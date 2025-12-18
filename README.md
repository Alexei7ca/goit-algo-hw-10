# Analysis of Numerical Integration Methods

## Overview
This project compares the Monte Carlo method for numerical integration against the analytical results provided by the SciPy `quad` function for the function f(x) = x^2 on the interval [0, 2].

## Results Comparison
- **Monte Carlo Method**: Estimated the integral value by simulating random points within a bounding box. With 50,000 samples, the result typically lands around 2.66 - 2.67.
- **SciPy Quad Method**: Calculated the integral value as 2.666666666666667 with a very high precision (error estimate ~2.96e-14).

## Conclusions
The Monte Carlo method is an effective tool for approximating integrals, especially when the function is complex or the integration region is oddly shaped. However, its accuracy is strictly dependent on the number of random samples. In this experiment, the approximation was highly accurate, confirming that random sampling can effectively mimic analytical integration. For simple 1D functions, SciPy's `quad` is superior in both speed and precision, but Monte Carlo remains a vital tool for high-dimensional simulations.