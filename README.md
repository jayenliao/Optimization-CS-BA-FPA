# Optimization-CS-BA-FPA

This project aimed to implement three well-known meta-heuristic algorithms: cuckoo search (CS), bat algorithm (BA), and flower pollination algorithm (FPA).

## Files

- `algorithms.py`: the implements of CS, BA, and FPA
- `objs.py`: the definitions of objective functions
- `main.py`: the main program to train DE, PSO, and FA
- `args.py` defines the arguments parser.
- `./output_f1/` contains subfolders with results of different trainings on objective function 1.
- `./output_f2/` contains subfolders with results of different trainings on objective function 2.

## Usage examples

```bash
python3 main.py -a 'BA' # train CS with defaulted #runs and #replications
python3 main.py -as 'CS' 'BA' 'FPA' -r 20 -t 1000 -f 1 -path './output_f1/' # train CS, BA, and FPA with 1000 runs and 20 replication and save outputs under the given folder
```
