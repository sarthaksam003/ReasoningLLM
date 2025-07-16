#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:05:00
#SBATCH --job-name=job_20250716_102638
#SBATCH --output=/home/sarthaks/InternWork/logs/job_20250716_102638.out
#SBATCH --error=/home/sarthaks/InternWork/logs/job_20250716_102638.err
#SBATCH --partition=standard
cd /home/sarthaks/InternWork/github-runner/_work/ReasoningLLM/ReasoningLLM
source /home/sarthaks/miniconda3/etc/profile.d/conda.sh
conda activate mor_env
python /home/sarthaks/InternWork/github-runner/_work/ReasoningLLM/ReasoningLLM/hello.py
