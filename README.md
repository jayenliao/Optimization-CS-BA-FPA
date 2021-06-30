# Optimization-CS-BA-FPA

This project aimed to implement three well-known meta-heuristic algorithms: cuckoo search (CS), bat algorithm (BA), and flower pollination algorithm (FPA).

## Files

- `Optimization_hw3_RE6094028-updated.pdf`: the report file

- `args.py`: the definition the arguments parser

- `objs.py`: the definitions of objective functions

- `algorithms.py`: the implements of CS, BA, and FPA

- `main.py`: the main program of training CS, BA, and FPA

- `exp_lambda.py`: the procedure of training CS, BA, and FPA with lambda-tuning

- `scatter_plots.py`: the production of scatter plots of initial and final points with 2 randomly-seleced dimensions and with 2 tSNE dimensions.

- `stacked_plots.py`: the production of stacked plots which plot training curves together.

- `./output_r1/` contains subfolders with results of different trainings with 1 replication.

    - `~/f1d10/`: trained on objective 1 with 10-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

    - `~/f2d10`: trained on objective 2 with 10-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

    - `~/f1d20/`: trained on objective 1 with 20-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

    - `~/f2d20`: trained on objective 2 with 20-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

- `./output_r20/` contains subfolders with results of different trainings with 20 replications.

    - `~/f1d10/`: trained on objective 1 with 10-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

    - `~/f2d10`: trained on objective 2 with 10-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

    - `~/f1d20/`: trained on objective 1 with 20-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

    - `~/f2d20`: trained on objective 2 with 20-d points
        - `~/CS/`, `~/BA/`, and `~/FPA/`

- `./output_exp_lambda/` contains subfolders with results of different trainings with lambda-tuning.

    - `~/f1d10/`: trained on objective 1 with 10-d points
        - `~/CS/` and `~/FPA/`

    - `~/f2d10`: trained on objective 2 with 10-d points
        - `~/CS/` and `~/FPA/`

    - `~/f1d20/`: trained on objective 1 with 20-d points
        - `~/CS/` and `~/FPA/`

    - `~/f2d20`: trained on objective 2 with 20-d points
        - `~/CS/` and `~/FPA/`

- `./scatter_plots/` contains scatter plots of initial and final points with 2 randomly-seleced dimensions and with 2 tSNE dimensions.

- `./stacked_plots/` contains stacked plots which plot training curves together.

## Usage examples

1. Train **CS** on the defaulted objective function with defaulted #runs, #replications, and #dimensions.

```bash
python3 main.py -a 'CS' 
```

2. Train **CS**, **BA**, and **FPA** with 10 and 20 dimensions, **1000** runs and **1** replication on objective function 1 and 2 and save outputs under the given folder.

```bash
python3 main.py -as 'CS' 'BA' 'FPA' -r 1 -t 1000 -f 1 -d 10 -path './output_r1/f1d10'
python3 main.py -as 'CS' 'BA' 'FPA' -r 1 -t 1000 -f 2 -d 10 -path './output_r1/f2d10'
python3 main.py -as 'CS' 'BA' 'FPA' -r 1 -t 1000 -f 1 -d 10 -path './output_r1/f1d20'
python3 main.py -as 'CS' 'BA' 'FPA' -r 1 -t 1000 -f 2 -d 20 -path './output_r1/f2d20'
```

3. Train **CS**, **BA**, and **FPA** with 10 and 20 dimensions and **1000** runs and **20** replications on objective function 1 and 2 and save outputs under the given folder.

```bash
python3 main.py -as 'CS' 'BA' 'FPA' -r 20 -t 1000 -f 1 -d 10 -path './output_r20/f1d10'
python3 main.py -as 'CS' 'BA' 'FPA' -r 20 -t 1000 -f 2 -d 10 -path './output_r20/f2d10'
python3 main.py -as 'CS' 'BA' 'FPA' -r 20 -t 1000 -f 1 -d 20 -path './output_r20/f1d20'
python3 main.py -as 'CS' 'BA' 'FPA' -r 20 -t 1000 -f 2 -d 20 -path './output_r20/f2d20'
```

4. Train **CS** and **FPA** with 10 and 20 dimensions and **1000** runs and **20** replication on objective function 1 and 2 with lambda-tuning with given candidate values and save outputs under the given folder. (Note: BA has no hyper-parameter, lambda)

```bash
python3 exp_lambda.py -as 'CS' 'FPA' -r 20 -t 1000 -f 1 -d 10 -path './output_exp_lambda/f1d10/'
python3 exp_lambda.py -as 'CS' 'FPA' -r 20 -t 1000 -f 1 -d 20 -path './output_exp_lambda/f1d20/'
python3 exp_lambda.py -as 'CS' 'FPA' -r 20 -t 1000 -f 2 -d 10 -path './output_exp_lambda/f2d10/'
python3 exp_lambda.py -as 'CS' 'FPA' -r 20 -t 1000 -f 2 -d 20 -path './output_exp_lambda/f2d20/'
```

5. Plot training curves together

Please run command 2 before running this command.

```bash
python3 scatter_plots.py -path 'scatter_plots'
```

6. Plot training curves together

Please run command 3 before running this command.

```bash
python3 stacked_plots.py -path './stacked_plots/'
```
