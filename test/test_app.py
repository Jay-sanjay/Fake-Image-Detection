from app import index
import sys

sys.path.append("./app.py")
def test_index():
    assert index() == "Project is running"