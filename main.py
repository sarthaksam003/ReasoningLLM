from datetime import datetime
import os

# Get the dynamic filename from environment variable
# This will be something like "output_20250716_121530.txt"
output_filename = os.environ.get('OUTPUT_FILENAME', 'default_output.txt')

with open(output_filename, "a") as f:
    f.write(f"Pipeline test conducted at exactly @ {datetime.now()}.\n")