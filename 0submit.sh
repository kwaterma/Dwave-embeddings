#!/bin/bash -l
#SBATCH --time=11:30:00
#SBATCH --job-name=KnC_timed
#SBATCH --output=%x-%j.out
#SBATCH --account=def-nike-ab

python KnC_timed.py
