from datetime import datetime
import os
output_path = os.path.join("outputs", "testHelloOutput.txt")

with open(output_path, "a") as f:
    f.write(f"Pipeline test conducted at exactly @ {datetime.now()} while listening to 'Daddy Cool' by Boney M\n")
