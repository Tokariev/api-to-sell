# Run all tests

import os
import subprocess
def run_tests():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    result = subprocess.run(['pytest', test_dir], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Some tests failed:")
        print(result.stderr)
    else:
        print("All tests passed successfully.")

if __name__ == "__main__":
    run_tests()