import numpy as np

def f1(x):
    d = x.shape[0]
    outputs = (-20) * np.exp((-0.2) * np.sqrt(np.sum(x * x) / d))
    outputs += (-1) * np.exp((1 / d) * np.sum(np.cos(2 * np.pi * x))) + 20 + np.e
    return outputs

def f2_(x):
    d = x.shape[0]
    x = 0.5 * x / 100
    a = 0.5
    b = 3
    kmax = 20

    outputs1 = 0.
    for i in range(d):
        for k in range(kmax):
            outputs1 += (a ** k) * np.cos(2 * np.pi * (b ** k) * (x[i] + 0.5))

    outputs2 = 0. 
    for k in range(kmax):
        outputs2 += (a ** k) * np.cos(2 * np.pi * (b ** k) * 0.5)
    outputs2 = outputs2 * (-d)
    return outputs1 + outputs2

def f2(x):
    d = x.shape[0]
    x = 0.5 * x / 100
    a = 0.5
    b = 3
    kmax = 20

    outputs1 = 0.
    outputs2 = 0.
    for k in range(kmax):
        outputs1 += np.sum((a ** k) * np.cos(2 * np.pi * (b ** k) * (x + 0.5)))
        outputs2 += (a ** k) * np.cos(2 * np.pi * (b ** k) * 0.5)
    outputs2 = outputs2 * (-d)
    return outputs1 + outputs2