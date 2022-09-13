#!/bin/sh

#SBATCH --job-name=3.951. # The job name.
#SBATCH -c 40
#SBATCH --partition=medium            # The number of cpu cores to use.
#SBATCH --time=23:59:00              # The time the job will take to run.
#SBATCH --mem=90000M        # The memory the job will use per cpu core.
###SBATCH --account=rwth0926
#SBATCH --mail-type=None
#SBATCH --mail-user=christian.eckhardt@mpsd.mpg.de


#SBATCH --output=/u/ceckhardt/XXZ/BATCH_OUT/output_job_%j_501.23.951.16
#

module purge
module load anaconda
export PYTHONPATH=/u/ceckhardt/.local/bin
export PATH=/mpcdf/soft/SLE_12/packages/x86_64/anaconda/3/2020.02/bin:/mpcdf/soft/SLE_12/packages/x86_64/Modules/5.0.1/bin:/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:/usr/games:/usr/lib/mit/bin:/usr/lib/mit/sbin:/afs/ipp/amd64_sles12/bin:/mpcdf/soft/SLE_12/packages/x86_64/find-module/1.0/bin:/u/ceckhardt/.local/bi:/u/ceckhardt/.local/bin
pip install physics-tenpy
MKL_NUM_THREADS=40
export MKL_NUM_THREADS
OMP_NUM_THREADS=40
export OMP_NUM_THREADS

python gs_progressive_v5.py 50 1.2 3.95 1. 16


echo $?

