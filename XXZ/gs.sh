for L in 50
do
#for g in 0.3
#for g in 0.05 0.1 0.2 0.4 0.5 1. 2. 4. 5. 10. 20. 40. 50.
for g in 0.9 0.95 1. 1.05 1.1 1.15 1.2
#for g in 0.31622777  0.34551073  0.37750532  0.41246264  0.45065703  0.49238826 0.53798384  0.58780161  0.64223254  0.70170383  0.76668221  0.83767764 0.91524731  1.  1.09260086  1.19377664  1.30432139  1.42510267 1.5570684   1.70125428  1.85879189  2.03091762  2.21898234  2.42446202 2.64896929  2.89426612  3.16227766  3.45510729  3.77505321  4.12462638 4.50657034  4.92388263  5.3798384   5.87801607  6.42232542  7.01703829 7.66682207  8.3767764   9.15247311 10. 
do
for U in 0.05 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95 1.05 1.15 1.25 1.35 1.45 1.55 1.65 1.75 1.85 1.95 2.05 2.15 2.25 2.35 2.45 2.55 2.65 2.75 2.85 2.95 3.05 3.15 3.25 3.35 3.45 3.55 3.65 3.75 3.85 3.95 
#for U in 3.5 3.6 3.7 3.8 3.9
#for U in 3.1 3.6
#for U in 0. 0.25 0.5 0.75 1 1.25 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4.0 4. 4.73844431 5.61321363 6.6494750 7.87704182 9.331231 11.05387963 13.09454827 15.51194695 18.37562421 21.76796801 25.7865760 30.5470637 36.18639008 42.86679858 50.78048451 60.15512453 71.26042696 84.4158912 100.
#for U in 0 0.25 0.5 0.75 1 1.25 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4.0 
#for U in 3.6
#for U in 0
do
#fac=20
#omega=$(echo "$g * $fac" | bc)
#echo $omega
for omega in 1.
do
for Nphot in 16
do
echo "#!/bin/sh

#SBATCH --job-name=$U$omega # The job name.
#SBATCH -c 40
#SBATCH --partition=medium            # The number of cpu cores to use.
#SBATCH --time=23:59:00              # The time the job will take to run.
#SBATCH --mem=90000M        # The memory the job will use per cpu core.
###SBATCH --account=rwth0926
#SBATCH --mail-type=None
#SBATCH --mail-user=christian.eckhardt@mpsd.mpg.de


#SBATCH --output=/u/ceckhardt/XXZ/BATCH_OUT/output_job_%j_$L$g$U$omega$Nphot
#

module purge
module load anaconda
export PYTHONPATH=/u/ceckhardt/.local/bin
export PATH=$PATH:/u/ceckhardt/.local/bin
pip install physics-tenpy
MKL_NUM_THREADS=40
export MKL_NUM_THREADS
OMP_NUM_THREADS=40
export OMP_NUM_THREADS

python gs_progressive_v5.py $L $g $U $omega $Nphot


echo \$?
" > /u/ceckhardt/XXZ/scripts/batchScriptTemp.sh

sbatch /u/ceckhardt/XXZ/scripts/batchScriptTemp.sh

done
done
done
done
done
