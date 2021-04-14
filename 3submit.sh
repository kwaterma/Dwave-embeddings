#!/bin/bash -l
#SBATCH --array=176-195
#SBATCH --time=167:30:00
#SBATCH --job-name=KnC_repeat
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --account=def-nike-ab
#SBATCH --mem=3900
#SBATCH --mail-user=kathryn@pinkninja.net
#SBATCH --mail-type=ALL

module load python python/3.7.4
source ~/ENV/bin/activate
python KnC_repeat.py $SLURM_ARRAY_TASK_ID
