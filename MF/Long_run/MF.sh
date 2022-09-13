for L in  50
do
for g in 0.2 1 2 
do
for U in 0 0.25 0.5 0.75 1 1.25 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4.0 
do

echo "#!/usr/local_rwth/bin/zsh




#SBATCH --job-name=GS_fast$L$g # The job name.
#SBATCH -c 4                # The number of cpu cores to use.
#SBATCH --time=47:59:00              # The time the job will take to run.
#SBATCH --mem-per-cpu=3200M        # The memory the job will use per cpu core.
#SBATCH --account=rwth0926
#SBATCH --mail-type=NONE
#SBATCH --mail-user=passetti@physik.rwth-aachen.de


#SBATCH --output=$HOME/output/cori
#

### Change to the work directory
cd $HOME/DMRG/MF/Long_run
### Execute your application

MKL_NUM_THREADS = 8
export MKL_NUM_THREADS


module load pythoni/3.7
export PYTHONPATH=$HOME/TeNPy
MKL_NUM_THREADS = 8
export MKL_NUM_THREADS


python3 mf.py $g $L $U


echo \$?

date
" >$HOME/DMRG/MF/Long_run/Bash/addBash_GSs

sbatch <$HOME/DMRG/MF/Long_run/Bash/addBash_GSs

done
done
done

