import os
import importlib

current_dir = os.path.dirname(__file__)

for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    if os.path.isdir(item_path) and item.startswith("day_"):
        module = importlib.import_module(f".{item}", package=__name__)
        globals()[item] = module