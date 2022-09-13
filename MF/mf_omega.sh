#for omega in 0.0100 0.0162 0.0264 0.0428 0.0695 0.1129 0.1833 0.2976 0.4833 0.7848 1.2743 2.0691 3.3598 5.4556 8.8587 14.3845 23.3572 37.9269 61.5848 100.0000
#for omega in 1
for omega in  0.1 0.14384499 0.20691381 0.29763514 0.42813324 0.61584821 0.88586679 1.27427499 1.83298071 2.6366509 3.79269019   5.45559478   7.8475997   11.28837892  16.23776739 23.35721469 33.59818286 48.32930239 69.51927962 100.
do
for L in   210
do
for chi in 500
do
#for U in 0 0.25 0.5 0.75 1 1.25 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4.0 1.99526231 2.45173589   3.0126409    3.70186906   4.54877795 5.58944158   6.86818691   8.43948197  10.37025591  12.74274986 15.65801995  19.24024183  23.64199987  29.05078651  35.69698847 43.86370006 53.89878153 66.22967617 81.38161719 100.
for U in 2.2
do


echo "#!/usr/local_rwth/bin/zsh




#SBATCH --job-name=GS_fast$L$g # The job name.
#SBATCH -c 6                # The number of cpu cores to use.
#SBATCH --time=47:59:00              # The time the job will take to run.
#SBATCH --mem-per-cpu=3200M        # The memory the job will use per cpu core.
###SBATCH --account=rwth0926
###SBATCH --account=theophysc
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


python3 mf_complete_omega.py $omega $L $chi $U 


echo \$?

date
" >$HOME/DMRG/MF/Bash/addBash_GSs

sbatch <$HOME/DMRG/MF/Bash/addBash_GSs

done
done
done
done


