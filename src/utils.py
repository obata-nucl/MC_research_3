from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import yaml

def load_config(filename: str | None = None) -> dict[str, Any]:
    """
    configs/common.yaml と 指定されたyamlファイルをロードしてマージする
    """

    project_root = Path(__file__).resolve().parent.parent
    config_dir = project_root / "configs"

    # 1. 共通設定をロード
    common_path = config_dir / "common.yaml"
    try:
        with open(common_path, 'r', encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load common config: {common_path}") from e
    
    # 2. 個別設定をロード
    if filename:
        specific_path = config_dir / filename
        try:
            with open(specific_path, 'r', encoding="utf-8") as f:
                specific_config = yaml.safe_load(f)
            if isinstance(specific_config, dict):
                config.update(specific_config)
            elif specific_config is None:
                pass
            else:
                raise ValueError(f"specific config must be a dict, got {type(specific_config)}")
        except Exception as e:
            raise RuntimeError(f"Failed to load specific config: {specific_path}") from e
    
    # 3. Path解決
    if "paths" in config:
        for key, rel_path in config["paths"].items():
            if isinstance(rel_path, str):
                path_obj = Path(rel_path)
                if path_obj.is_absolute():
                    config["paths"][key] = path_obj
                else:
                    config["paths"][key] = (project_root / rel_path).resolve()
    config["paths"]["project_root"] = project_root
    return config