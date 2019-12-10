assert __name__ != "__main__", "This module should NOT be executed."

import os
import sys

# Include the path to the parent directory
PATH = os.path.join(os.path.dirname(__file__), "../")
print PATH
sys.path.insert(0, PATH)
