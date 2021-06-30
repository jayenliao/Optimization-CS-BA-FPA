import argparse

def init_arguments():
    parser = argparse.ArgumentParser(prog='Optimization - HW3: CS, BA, and FPA')

    parser.add_argument('-a', '--algorithm', type=str, default='CS', choices=['CS', 'BA', 'FPA'])
    parser.add_argument('-as', '--algorithms', type=str, nargs='+', default='')
    parser.add_argument('-s', '--seed', type=int, default=4028)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-g', '--gpu', action='store_true')
    parser.add_argument('-d', '--dimension', type=int, default=20)
    parser.add_argument('-t', '--training_times', type=int, default=1000)
    parser.add_argument('-f', '--obj_fun', type=int, default=2, choices=[1, 2])
    parser.add_argument('-N', '--N', type=int, default=50, help='No. of initialized points')
    parser.add_argument('-l', '--lamb', type=float, default=.5)
    parser.add_argument('-ls', '--lambdas', type=float, nargs='+', default=[.5, 1., 1.5, 2.])
    parser.add_argument('-r', '--replications', type=int, default=20)
    parser.add_argument('-path', '--savePATH', type=str, default='./output/')
    
    return parser
