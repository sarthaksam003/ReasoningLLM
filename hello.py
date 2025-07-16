from datetime import datetime
import os
output_path = os.path.join("outputs", "testHelloOutput.txt")

with open(output_path, "a") as f:
    f.write(f"Pipeline test conducted at exactly @ {datetime.now()} or 11:41 am at 16 July 2025 after coming from tea break\n")
