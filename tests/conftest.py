import os
import sys
from pathlib import Path

# Set path to parent directory to import target package
sys.path.append(str(Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).joinpath("src")))