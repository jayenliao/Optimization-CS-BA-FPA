import random, time
import numpy as np
from tqdm import tqdm
from math import gamma

'''
from args import init_arguments
SEED = init_arguments().parse_args().seed
np.random.seed(SEED)
random.seed(SEED)
'''

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


class cuck:       
    def __init__(self, lamb, pa, N, d, obj):      # N:點數量,  d:parameter dimention,  obj:objective function 
        self.lamb = lamb
        self.pa = pa
        self.N = N
        self.d = d
        self.obj = obj
        self.alpha = d / 100

        self.vectexs = {'x':[], 'v':[]}
        self.globalm = [None, None]    # 目前最小的點
        self.sigma = None

        print('Initializing weights ...', end='  ')
        self.initW()
        print('Done!')

    def train(self, t):
        self.time_cost = []
        self.lst_globalv = []
        loader = tqdm(range(t), desc='Cuckoo Search')
        for _ in loader:
            t0 = time.time()
            if (self.globalm[1] - 0.) < 10 ** (-15):
                return t

            for i in range(self.N):
                x = self.vectexs['x'][i]
                v = self.vectexs['v'][i]
                L = self.levy(x)
                newx = x + L
                newv = self.obj(newx)

                if newv < v:
                    self.vectexs['x'][i] = newx
                    self.vectexs['v'][i] = newv

                    if newv < self.globalm[1]:
                        self.globalm[0] = newx
                        self.globalm[1] = newv
                        #print('nice point 1', newv)

            b = int(0.2 * self.d)
            blist = np.argsort(self.vectexs['v'])[b:]
            for j in blist:
                x = self.vectexs['x'][j]
                v = self.vectexs['v'][j]
                U = self.H()
                newx = x + U
                newv = self.obj(newx)
                r = np.random.uniform(0, 1, 1)[0]
                if r < self.pa and newv < v:
                    self.vectexs['x'][j] = newx
                    self.vectexs['v'][j] = newv

                    if newv < self.globalm[1]:
                        self.globalm[0] = newx
                        self.globalm[1] = newv
                        #print('nice point 2', newv)
            
            self.time_cost.append(time.time() - t0)
            self.lst_globalv.append(self.globalm[1])
            loader.set_description('Current value = %.4f' % self.globalm[1])
        
        return t

    def initW(self):
        for i in range(self.N):
            x = self.randoms()
            v = self.obj(x)
            self.vectexs['x'].append(x)
            self.vectexs['v'].append(v)
            if i == 0:
                self.globalm[0] = x
                self.globalm[1] = v

            elif v < self.globalm[1]:
                self.globalm[0] = x
                self.globalm[1] = v
        
        s1 = gamma(1 + self.lamb)
        s2 = self.lamb * gamma((1 + self.lamb) / 2)
        s3 = np.sin(np.pi * self.lamb / 2)
        s4 = 2 ** ((self.lamb - 1) / 2)
        self.sigma = ((s1 / s2) * (s3 / s4)) ** (1 / self.lamb)

    def levy(self, x, sf=0):
        u = np.random.normal(0, self.sigma, 1)[0]
        v = np.random.normal(0, 1, 1)[0]
        s = u / (np.absolute(v)) ** (1 / self.lamb)
        if sf == 1:
            return s

        vd = np.random.normal(0, 1, self.d)

        p = self.globalm[0] - x

        outputs = self.alpha * vd * s * p
        return outputs

    def H(self, sf=0):
        r = random.sample([i for i in range(len(self.vectexs['x']))], k=2)
        xi, xj = self.vectexs['x'][r[0]], self.vectexs['x'][r[1]]
        p = xi - xj
        
        ed = np.random.uniform(0, 1, self.d)

        outputs = ed * p

        if sf==1:
            print(outputs)
        return outputs

    def randoms(self):
        x = np.random.rand(self.d)*40 - 20.
        return x


class bat:       
    def __init__(self, fmax, A0, R0, N, d, obj):      # N:點數量,  d:parameter dimention,  obj:objective function 
        self.fmax = fmax
        self.A0 = A0
        self.R0 = R0
        self.obj = obj
        self.alpha = d / 100

        self.A = A0
        self.R = 0

        self.N = N
        self.d = d
        self.obj = obj

        self.vectexs = {'x':[], 'val':[], 'vel':[]}
        self.globalm = [None, None]    # 目前最小的點
        self.sigma = None

        print('Initializing weights ...', end='  ')
        self.initW()
        print('Done!')

    def train(self, iteration, logs=None):
        self.time_cost = []
        self.lst_globalv = []
        loader = tqdm(range(iteration), desc='Bat Algorithm')
        for t in loader:
            t0 = time.time()

            if (self.globalm[1] - 0.) < 10 ** (-15):
                return t

            for i in range(self.N):
                # 目標飛行
                x = self.vectexs['x'][i]
                val = self.vectexs['val'][i]
                vel = self.vectexs['vel'][i]
                newx = x + vel
                newVal = self.obj(newx)
                newVel = self.goalFly(i)
                self.vectexs['vel'][i] = newVel
                
                r = np.random.uniform(0, 1, 1)[0]

                if r > self.R and newVal < val:
                    self.vectexs['x'][i] = newx
                    self.vectexs['val'][i] = newVal

                    if newVal < self.globalm[1]:
                        self.globalm[0] = newx
                        self.globalm[1] = newVal
                        #print('nice point 1', newVal)

                # 亂飛
                x = self.vectexs['x'][i]
                val = self.vectexs['val'][i]
                randomF = self.randomFly()
                newx = x + randomF
                newVal = self.obj(newx)
                r = np.random.uniform(0, 1, 1)[0]
                if newVal < val:
                    self.vectexs['x'][i] = newx
                    self.vectexs['val'][i] = newVal

                    if newVal < self.globalm[1]:
                        self.globalm[0] = newx
                        self.globalm[1] = newVal
                        #print('nice point 2', newVal)

            self.time_cost.append(time.time() - t0)
            self.lst_globalv.append(self.globalm[1])
            loader.set_description('Current value = %.4f' % self.globalm[1])

    def initW(self):
        for i in range(self.N):
            x = self.randoms()
            v = self.obj(x)
            self.vectexs['x'].append(x)
            self.vectexs['val'].append(v)
            self.vectexs['vel'].append(0)
            if i == 0:
                self.globalm[0] = x
                self.globalm[1] = v

            elif v < self.globalm[1]:
                self.globalm[0] = x
                self.globalm[1] = v

    def goalFly(self, xIndex, sf=0):
        u = np.random.normal(0, 0.6, 1)[0]
        v = np.random.normal(0, 1, 1)[0]
        s = u / (np.absolute(v)) ** (1 / 1.5)
        if sf == 1:
            return s
        
        vd = np.random.normal(0, 1, self.d)

        p = self.globalm[0] - self.vectexs['x'][xIndex]

        outputs = self.alpha * vd * s * p
        return outputs

    def randomFly(self, sf=0):
        u = np.random.normal(0, 0.6, 1)[0]
        v = np.random.normal(0, 1, 1)[0]
        s = u / (np.absolute(v)) ** (1 / 1.5)
        e = np.random.uniform(-1, 1, self.d)
        outputs = 0.01 * e * self.A * s
        return outputs

    def randoms(self):
        x = np.random.rand(self.d) * 40 - 20.
        return x


class flower:   
    def __init__(self, lamb, pa, N, d, obj):      # N:點數量,  d:parameter dimention,  obj:objective function 
        self.lamb = lamb
        self.pa = pa
        self.N = N
        self.d = d
        self.obj = obj
        self.alpha = d / 100
        self.vectexs = {'x':[], 'v':[]}
        self.globalm = [None, None]    # 目前最小的點
        self.sigma = None
        print('Initializing weights ...', end='  ')
        self.initW()
        print('Done!')

    def train(self, t):
        self.time_cost = []
        self.lst_globalv = []
        loader = tqdm(range(t), desc='Flower Pollination Algorithm')
        for _ in loader:
            t0 = time.time()
            if (self.globalm[1] - 0.) < 10 ** (-15):
                return t

            for i in range(len(self.vectexs['x'])):
                e = np.random.uniform(0, 1, 1)[0]
                x = self.vectexs['x'][i]
                v = self.vectexs['v'][i]
                if e > self.pa:
                    L = self.levy(x)
                    newx = x + L
                    newv = self.obj(newx)
                    if newv < v:
                        self.vectexs['x'][i] = newx
                        self.vectexs['v'][i] = newv
                        if newv < self.globalm[1]:
                            self.globalm[0] = newx
                            self.globalm[1] = newv
                            #print('nice point 1', newv)
                else:
                    U = self.H()
                    newx = x + U
                    newv = self.obj(newx)
                    if newv < v:
                        self.vectexs['x'][i] = newx
                        self.vectexs['v'][i] = newv
                        if newv < self.globalm[1]:
                            self.globalm[0] = newx
                            self.globalm[1] = newv
                            #print('nice point 2', newv)

            self.time_cost.append(time.time() - t0)
            self.lst_globalv.append(self.globalm[1])
            loader.set_description('Current value = %.4f' % self.globalm[1])
        
        return t
                    
    def initW(self):
        for i in range(self.N):
            x = self.randoms()
            v = self.obj(x)
            self.vectexs['x'].append(x)
            self.vectexs['v'].append(v)
            if i == 0:
                self.globalm[0] = x
                self.globalm[1] = v

            elif v < self.globalm[1]:
                self.globalm[0] = x
                self.globalm[1] = v
        
        s1 = gamma(1 + self.lamb)
        s2 = self.lamb * gamma((1 + self.lamb) / 2)
        s3 = np.sin(np.pi * self.lamb / 2)
        s4 = 2 ** ((self.lamb - 1) / 2)
        self.sigma = ((s1 / s2) * (s3 / s4)) ** (1 / self.lamb)

    def levy(self, x):
        u = np.random.normal(0, self.sigma, 1)[0]
        v = np.random.normal(0, 1, 1)[0]
        s = u / (np.absolute(v)) ** (1 / self.lamb)

        vd = np.random.normal(0, 1, self.d)

        p = self.globalm[0] - x

        outputs = self.alpha * vd * s * p
        return outputs

    def H(self, sf=0):
        r = random.sample([i for i in range(len(self.vectexs['x']))], k=2)
        xi, xj = self.vectexs['x'][r[0]], self.vectexs['x'][r[1]]
        p = xi - xj
        
        ed = np.random.uniform(0, 1, self.d)

        outputs = ed * p

        if sf==1:
            print(outputs)
        return outputs

    def randoms(self):
        x = np.random.rand(self.d) * 40 - 20.
        return x
