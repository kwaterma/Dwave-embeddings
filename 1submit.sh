#!/bin/bash -l
#SBATCH --time=11:30:00
#SBATCH --job-name=KnP_timed
#SBATCH --output=%x-%j.out
#SBATCH --error=ERROR-%j.out
#SBATCH --account=def-nike-ab
#SBATCH --mem=3900
#SBATCH --mail-user=kathryn@pinkninja.net
#SBATCH --mail-type=ALL

python KnP_timed.py
