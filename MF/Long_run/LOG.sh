for L in  50
do
for g in 0.2 1 2
do
for U in 5.01187234  6.98947321  9.74740226  13.59356391  18.95735652  26.43761186  36.86945065  51.41751828  71.7060097  100
do

echo "#!/usr/local_rwth/bin/zsh




#SBATCH --job-name=GS_fast$L$g # The job name.
#SBATCH -c 8                # The number of cpu cores to use.
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


python3 log.py $g $L $U


echo \$?

date
" >$HOME/DMRG/MF/Long_run/Bash/addBash_GSs

sbatch <$HOME/DMRG/MF/Long_run/Bash/addBash_GSs

done
done
done

