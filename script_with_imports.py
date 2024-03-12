import sys

from dir_for_imports.a import func_from_a

sys.path.append("dir_for_imports/dir_b")
from file_b import func_from_b

