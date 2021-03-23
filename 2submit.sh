#!/bin/bash -l
#SBATCH --time=71:00:00
#SBATCH --job-name=KnP1_timed
#SBATCH --output=%x-%j.out
#SBATCH --error=ERROR-%j.out
#SBATCH --account=def-nike-ab
#SBATCH --mem=3900
#SBATCH --mail-user=kathryn@pinkninja.net
#SBATCH --mail-type=ALL

module load python python/3.7.4
source ~/ENV/bin/activate
python KnP1_timed.py
