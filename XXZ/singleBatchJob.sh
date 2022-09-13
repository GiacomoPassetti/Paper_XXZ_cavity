#!/bin/sh
#SBATCH --job-name=XXZ # The job name.
#SBATCH -c 10                # The number of cpu cores to use.
#SBATCH --time=00:30:00              # The time the job will take to run.
#SBATCH --mem=4000M        # The memory the job will use per cpu core.
##SBATCH --partition=mpsd
###SBATCH --account=rwth0926
#SBATCH --mail-type=ALL
#SBATCH --mail-user=christian.eckhardt@mpsd.mpg.de

#SBATCH --output=/u/ceckhardt/XXZ/BATCH_OUT/testout${SLURM_JOB_ID}.out
#

### Change to the work directory
###cd $HOME/DMRG/Dynamical_Localization
### Execute your application

###MKL_NUM_THREADS = 10
###export MKL_NUM_THREADS

module purge
module load anaconda
export PYTHONPATH=/u/ceckhardt/.local/bin
export PATH=$PATH:/u/ceckhardt/.local/bin
MKL_NUM_THREADS=40
export MKL_NUM_THREADS


###python gs_progressive.py $L $g $U $omega
python gs_progressive.py 10 1 1 1
