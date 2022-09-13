for L in  50
do
for g in 0.2 1 2
do


echo "#!/usr/local_rwth/bin/zsh




#SBATCH --job-name=GS_fast$L$g # The job name.
#SBATCH -c 10                # The number of cpu cores to use.
#SBATCH --time=47:59:00              # The time the job will take to run.
#SBATCH --mem-per-cpu=3200M        # The memory the job will use per cpu core.
#SBATCH --account=rwth0722
#SBATCH --mail-type=NONE
#SBATCH --mail-user=passetti@physik.rwth-aachen.de


#SBATCH --output=$HOME/output/cori
#

### Change to the work directory
cd $HOME/DMRG/MF/Data_complete_MF
### Execute your application

MKL_NUM_THREADS = 10
export MKL_NUM_THREADS


module load pythoni/3.7
export PYTHONPATH=$HOME/TeNPy
MKL_NUM_THREADS = 10
export MKL_NUM_THREADS


python3 mf.py $g $L


echo \$?

date
" >$HOME/DMRG/MF/Data_complete_MF/Bash/addBash_GSs

sbatch <$HOME/DMRG/MF/Data_complete_MF/Bash/addBash_GSs

done
done


