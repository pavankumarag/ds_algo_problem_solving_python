assert __name__ != "__main__", "This module should NOT be executed."

import os
import sys

# Include the path to the parent directory
print os.path.dirname(__file__)
sys.path.insert(0, os.path.dirname(__file__))
