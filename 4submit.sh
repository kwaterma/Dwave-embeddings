#!/bin/bash -l
#SBATCH --array=161-180
#SBATCH --time=167:30:00
#SBATCH --job-name=KnP_repeat
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --account=def-nike-ab
#SBATCH --mem=3900
#SBATCH --mail-user=kathryn@pinkninja.net
#SBATCH --mail-type=ALL

module load python python/3.7.4
source ~/ENV/bin/activate
python KnP_repeat.py $SLURM_ARRAY_TASK_ID
