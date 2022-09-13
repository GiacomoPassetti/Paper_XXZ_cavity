#for omega in 0.0100 0.0162 0.0264 0.0428 0.0695 0.1129 0.1833 0.2976 0.4833 0.7848 1.2743 2.0691 3.3598 5.4556 8.8587 14.3845 23.3572 37.9269 61.5848 100.0000
for omega in 1
do
for L in   110
do
for chi in 600
do
#for U in 0 0.25 0.5 0.75 1 1.25 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4. 4.73844431 5.61321363 6.64947505 7.87704182 9.331231    11.05387963  13.09454827  15.51194695  18.37562421 21.76796801 25.78657607 30.5470637 36.18639008  42.86679858 50.78048451 60.15512453 71.26042696 84.41589125 100.
for U in 3
do
for g in 0.3
do

echo "#!/usr/local_rwth/bin/zsh




#SBATCH --job-name=GS_fast$L$g # The job name.
#SBATCH -c 4                # The number of cpu cores to use.
#SBATCH --time=23:59:00              # The time the job will take to run.
#SBATCH --mem-per-cpu=3200M        # The memory the job will use per cpu core.
###SBATCH --account=rwth0926
#SBATCH --account=theophysc
#SBATCH --mail-type=NONE
#SBATCH --mail-user=passetti@physik.rwth-aachen.de


#SBATCH --output=$HOME/output/cori
#

### Change to the work directory
cd $HOME/DMRG/MF
### Execute your application

MKL_NUM_THREADS = 6
export MKL_NUM_THREADS


module load pythoni/3.7
export PYTHONPATH=$HOME/TeNPy
MKL_NUM_THREADS = 6
export MKL_NUM_THREADS


python3 mf_complete.py $omega $L $chi $U $g


echo \$?

date
" >$HOME/DMRG/MF/Bash/addBash_GSs

sbatch <$HOME/DMRG/MF/Bash/addBash_GSs

done
done
done
done
done

