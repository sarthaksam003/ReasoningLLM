from datetime import datetime

with open("helloTestOutput.txt", "a") as f:
    f.write(f"✅ Pipeline test completed at {datetime.now()}\n")
