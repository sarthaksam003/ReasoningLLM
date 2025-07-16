from datetime import datetime
import os
output_path = os.path.join("outputs", "testHelloOutput.txt")

with open(output_path, "a") as f:
    f.write(f"Pipeline test kara at {datetime.now()}\n")
