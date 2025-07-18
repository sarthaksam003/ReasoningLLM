#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:05:00
#SBATCH --job-name=job_20250718_093725
#SBATCH --output=/home/sarthaks/InternWork/logs/job_20250718_093725.out
#SBATCH --error=/home/sarthaks/InternWork/logs/job_20250718_093725.err
#SBATCH --partition=standard
cd /home/sarthaks/InternWork/intern_repos
source /home/sarthaks/miniconda3/etc/profile.d/conda.sh
conda activate mor_env
export OUTPUT_FILENAME="output_20250718_093725.txt"
echo "=== Starting Python execution ==="
if [ -f "main.py" ]; then
  echo "Running main.py -> $OUTPUT_FILENAME"
  python main.py
elif [ -f "hello.py" ]; then
  echo "Running hello.py -> $OUTPUT_FILENAME"
  python hello.py
else
  echo "Error: No main.py or hello.py found!"
  exit 1
fi
echo "=== Python execution completed ==="
