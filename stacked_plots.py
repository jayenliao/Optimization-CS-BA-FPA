import os
import numpy as np
import matplotlib.pyplot as plt
from args import init_arguments

def plot_together(args, loadPATH, COLORS, i, label, fn):
    arr_globalv = np.loadtxt(loadPATH)
    m = arr_globalv.mean(axis=0)
    err = arr_globalv.std(axis=0)
    x = np.arange(len(m))
    
    plt.plot(x, m, c=COLORS['deep'][i], label=label)
    plt.legend()
    plt.fill_between(x, m-err, m+err, facecolor=COLORS['light'][i], alpha=.2)
    plt.title('The Training Curve of The Global Best Value')
    plt.xlabel('Epoch')
    plt.ylabel('Global Best Value')
    plt.grid(linestyle='--')
    plt.savefig(fn)
    print('The plot is save as')
    print('-->', fn)

if __name__ == '__main__':
    args = init_arguments().parse_args()
    if not os.path.exists(args.savePATH):
        os.makedirs(args.savePATH)
    COLORS = {
        'deep': ('salmon', 'seagreen', 'royalblue', 'mediumorchid'),
        'light': ('sandybrown', 'limegreen', '#089FFF', 'violet')
    }

    # Plot different algorithms together
    for OBJ in (1, 2):
        plt.figure()
        fn = os.path.join(args.savePATH, 'plot_globalv_algorithms_f' + str(OBJ) + '.png')
        for i, A in enumerate(('CS', 'BA', 'FPA')):
            loadPATH = os.path.join('output_f' + str(OBJ), A, 'arr_globalv.txt')
            plot_together(args, loadPATH, COLORS, i, A, fn)
            
    
    # Plot different objective functions together
    for A in ('CS', 'BA', 'FPA'):
        plt.figure()
        fn = os.path.join(args.savePATH, 'plot_globalv_functions_' + A + '.png')
        for OBJ in (1, 2):
            loadPATH = os.path.join('output_f' + str(OBJ), A, 'arr_globalv.txt')
            plot_together(args, loadPATH, COLORS, OBJ-1, 'function '+ str(OBJ), fn)
