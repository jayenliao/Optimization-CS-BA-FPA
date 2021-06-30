import os, time, random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from algorithms import cuck, bat, flower
from objs import f1, f2
from args import init_arguments

def save_txt(out:list, PATH:str):
    with open(PATH+'.txt', 'w') as f:
        for row in out:
            f.write(str(row) + '\n')

def main(args, r=None, return_results=False):
    t0 = time.time()
    np.random.seed(args.seed)
    random.seed(args.seed)
    N = args.N
    OBJ = f2 if args.obj_fun == 2 else f1
    algorithm_name = args.algorithm

    if algorithm_name == 'CS':
        algorithm = cuck(lamb=args.lamb, pa=.25, N=N, d=args.dimension, obj=OBJ)
    elif algorithm_name == 'BA':
        algorithm = bat(fmax=1, A0=1, R0=1, N=N, d=args.dimension, obj=OBJ)
    elif algorithm_name == 'FPA':
        algorithm = flower(lamb=args.lamb, pa=.25, N=N, d=args.dimension, obj=OBJ)
    initial_vectexs = algorithm.vectexs['x'].copy()

    if r:
        print('Training for replication %d ...' % r)
    else:
        print('Training ...')
    algorithm.train(args.training_times)
    dt = datetime.now().strftime('%y-%m-%d-%H-%M-%S')
    folder_name = os.path.join(args.savePATH, dt + '_' + algorithm_name + '_' + '_N=' + str(N) + '_t=' + str(args.training_times))
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    print('Results are save as')
    fn = folder_name + '/time_cost'
    save_txt(algorithm.time_cost, fn)
    print('-->', fn + '.txt')
    fn = folder_name + '/lst_globalv'
    save_txt(algorithm.lst_globalv, fn)
    print('-->', fn + '.txt')
    
    print('Time cost of %s: %6.2f s.\n' % (algorithm_name, time.time() - t0))
    if return_results:
        return algorithm.time_cost, algorithm.lst_globalv, algorithm.vectexs['x'], initial_vectexs

def training_curve(args, COLORS, i, legend=False):
    arr_time_cost, arr_globalv = [], []
    fn = os.path.join(args.savePATH, 'plot_globalv.png')
    for r in range(args.replications):
        time_cost, lst_globalv, vectexs, initial_vectexs = main(args, r=r, return_results=True)
        args.seed += 1
        arr_time_cost.append(time_cost)
        arr_globalv.append(lst_globalv)

    x = np.arange(args.training_times)
    arr_globalv = np.array(arr_globalv)
    m = arr_globalv.mean(axis=0)
    err = arr_globalv.std(axis=0)
    if legend:
        plt.plot(x, m, c=COLORS['deep'][i], label=args.lamb)
        plt.legend()
    else:
        plt.plot(x, m, c=COLORS['deep'][i])
    plt.fill_between(x, m-err, m+err, facecolor=COLORS['light'][i], alpha=.2)
    plt.title('The Training Curve of The Global Best Value of ' + args.algorithm)
    plt.xlabel('Epoch')
    plt.ylabel('Global Best Value')
    plt.grid(linestyle='--')
    plt.savefig(fn)    
    print('Results of %d replications are save together as' % args.replications)
    print('-->', fn)

    fn = os.path.join(args.savePATH, 'vectexs.txt')
    np.savetxt(fn, np.array(vectexs))
    print('-->', fn)

    fn = os.path.join(args.savePATH, 'initial_vectexs.txt')
    np.savetxt(fn, np.array(initial_vectexs))
    print('-->', fn)

    fn = os.path.join(args.savePATH, 'arr_globalv.txt')
    np.savetxt(fn, arr_globalv)
    print('-->', fn)
        
    fn = os.path.join(args.savePATH, 'arr_time_cost.txt')
    arr_time_cost = np.array(arr_time_cost)
    np.savetxt(fn, arr_time_cost)
    print('-->', fn)

    print('Average time cost per run of %s: %.4f\n' % (args.algorithm, arr_time_cost.mean()))
    print('-'*30)
    print()


if __name__ == '__main__':
    args = init_arguments().parse_args()
    args.algorithms = [args.algorithm] if args.algorithms == '' else args.algorithms
    PATH = args.savePATH
    COLORS = {
        'deep': ('salmon', 'seagreen', 'royalblue'),
        'light': ('sandybrown', 'limegreen', '#089FFF')
    }
    
    for i, A in enumerate(args.algorithms):
        args.algorithm = A
        args.savePATH = os.path.join(PATH, A)
        plt.figure()
        training_curve(args, COLORS, i)
        