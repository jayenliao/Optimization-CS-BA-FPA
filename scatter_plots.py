import os, random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from args import init_arguments

def scatter_plots_2d(args, loadPATH, A, OBJ, d, tsne):
    FOLDER_load = os.path.join(loadPATH, 'f' + OBJ + 'd' + d, A)
    FOLDER_save = os.path.join(args.savePATH, 'f' + OBJ + 'd' + d, A)
    if not os.path.exists(FOLDER_save):
        os.makedirs(FOLDER_save)
    
    initial_vectexs = np.loadtxt(os.path.join(FOLDER_load, 'initial_vectexs.txt'))
    vectexs = np.loadtxt(os.path.join(FOLDER_load, 'vectexs.txt'))
    assert initial_vectexs.shape == vectexs.shape
    
    plt.figure()
    if tsne:
        init_arr2d = TSNE(n_components=2).fit_transform(initial_vectexs)
        arr2d = TSNE(n_components=2).fit_transform(vectexs)
        plt.scatter(init_arr2d[:,0], init_arr2d[:,1], label='Initial')
        plt.scatter(arr2d[:,0], arr2d[:,1], label='Final')
        plt.title('Scatter Plot of Initial and Final Points of training ' + A + ' on f' + OBJ + ' with 2d-tSNE')
        plt.xlabel('Dimension 1 of tSNE')
        plt.ylabel('Dimension 2 of tSNE')
        fn = os.path.join(FOLDER_save, 'scatter_tSNE_' + A + '.png')
    else:
        dims = random.sample(range(initial_vectexs.shape[1]), k=2)
        dims.sort()
        i, j = dims
        plt.scatter(initial_vectexs[:,i], initial_vectexs[:,j], label='Initial')
        plt.scatter(vectexs[:,i], vectexs[:,j], label='Final')
        plt.title('Scatter Plot of Initial and Final Points of training ' + A + ' on f' + OBJ + '\nwith dimension ' + str(i) + ' and ' + str(j))
        plt.xlabel('Dimension ' + str(i))
        plt.ylabel('Dimension ' + str(j))
        fn = os.path.join(FOLDER_save, 'scatter_dim_' + str(i) + '_' + str(j) + '_' + A + '.png')
    plt.grid(linestyle='--')
    plt.legend()
    plt.savefig(fn)
    print('The plot is save as')
    print('-->', fn)

if __name__ == '__main__':
    args = init_arguments().parse_args()
    loadPATH = './output_r1/'
    for OBJ in ('1', '2'):
        for A in ('CS', 'BA', 'FPA'):
            for d in ('10', '20'):
                scatter_plots_2d(args, loadPATH, A, OBJ, d, False)
                scatter_plots_2d(args, loadPATH, A, OBJ, d, True)
