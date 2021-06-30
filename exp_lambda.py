import os, time, random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from main import save_txt, main, training_curve
from args import init_arguments

def exp_lambda(args_):
    for i, lamb in enumerate(args_.lambdas):
        args_.lamb = lamb
        print(args_.lamb)
        training_curve(args_, COLORS, i, legend=True)

if __name__ == '__main__':
    args = init_arguments().parse_args()
    args.algorithms = [args.algorithm] if args.algorithms == '' else args.algorithms
    PATH = args.savePATH
    COLORS = {
        'deep': ('salmon', 'seagreen', 'royalblue', 'mediumorchid'),
        'light': ('sandybrown', 'limegreen', '#089FFF', 'violet')
    }
    
    for A in args.algorithms:
        args.algorithm = A
        args.savePATH = os.path.join(PATH, A)
        plt.figure()
        exp_lambda(args)