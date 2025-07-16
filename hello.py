from datetime import datetime
import os

# Get the dynamic filename from environment variable set by SLURM job
# If not set, fallback to the old filename
output_filename = os.environ.get('OUTPUT_FILENAME', 'testHelloOutput.txt')

with open(output_filename, "a") as f:
    f.write(f"Pipeline test conducted at exactly @ {datetime.now()} or 12:05 pm at 16 July 2025 after coming from tea break\n")