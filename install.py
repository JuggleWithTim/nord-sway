#!/usr/bin/env python3
"""Install Nord or switch between Nord and the previous desktop."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent / 'scripts/nord-theme'), run_name='__main__')
