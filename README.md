# Optimization-CS-BA-FPA

This project aimed to implement three well-known meta-heuristic algorithms: cuckoo search (CS), bat algorithm (BA), and flower pollination algorithm (FPA).

## Files

- `args.py`: the definition the arguments parser
- `objs.py`: the definitions of objective functions
- `algorithms.py`: the implements of CS, BA, and FPA
- `main.py`: the main program to train CS, BA, and FPA
- `exp_lambda`: the procedure of training CS, BA, and FPA with lambda-tuning
- `./output_f1/` contains subfolders with results of different trainings on objective function 1.
- `./output_f2/` contains subfolders with results of different trainings on objective function 2.
- `./output_exp_lambda/f1/` contains subfolders with results of different trainings on objective function 1 with lambda-tuning.
- `./output_exp_lambda/f2/` contains subfolders with results of different trainings on objective function 2 with lambda-tuning.

## Usage examples

1. Train CS with defaulted #runs and #replications.

```bash
python3 main.py -a 'CS' 
```

2. Rrain CS, BA, and FPA with 1000 runs and 20 replication on objective function 1 and save outputs under the given folder.

```bash
python3 main.py -as 'CS' 'BA' 'FPA' -r 20 -t 1000 -f 1 -path './output_f1/' 
```

3. Train CS, BA, and FPA with 1000 runs and 20 replication on objective function 2 with lambda-tuning and save outputs under the given folder.

```bash
python3 exp_lambda.py -as 'CS' 'BA' 'FPA' -r 20 -t 1000 -f 2 -path './output_exp_lambda/f2/'
```

4. Plot training curves together

Please run command 1 and 2 before running this command.

```bash
python3 stacked_plots.py -path './stack_plots/'
```
