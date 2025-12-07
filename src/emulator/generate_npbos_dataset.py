from __future__ import annotations

import subprocess
from pathlib import Path

import numpy as np
import pandas as pd

from src.utils import load_config

def parse_npbos_output(output: str) -> dict[str, float]:
    """
    NPBOSの実行結果から主要なエネルギー準位を抽出
    """
    levels = {}

    targets = {
        "2  +  ( 1)": "E2_1",
        "4  +  ( 1)": "E4_1",
        "6  +  ( 1)": "E6_1",
        "0  +  ( 2)": "E0_2",
    }

    lines = output.splitlines()

    for line in lines:
        for key, label in targets.items():
            if key in line:
                try:
                    parts = line.split()
                    if not parts:
                        raise ValueError("No parts found in line")
                    energy = float(parts[-3])
                    levels[label] = energy
                except ValueError:
                    continue
    if len(levels) != len(targets):
        raise ValueError("Not all target energy levels were found")
    return levels
