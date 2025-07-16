from datetime import datetime
import os
output_path = os.path.join("outputs", "testHelloOutput.txt")

with open(output_path, "a") as f:
    f.write(f"Pipeline test conducted at exactly @ {datetime.now()} or 10:57 am at 16 July 2025 before going for tea break\n")
