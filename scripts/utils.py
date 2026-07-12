"""
utils.py

Common utility functions used throughout the multilingual LLM safety benchmark.

Author: Shriya Patil
Project: Multilingual LLM Safety Benchmark
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from datetime import datetime

import pandas as pd


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

def load_config(config_path: str = "config/config.json") -> dict:
    """
    Load the experiment configuration.

    Parameters
    ----------
    config_path : str
        Path to config.json.

    Returns
    -------
    dict
        Configuration dictionary.
    """

    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------

def load_dataset(dataset_path: str) -> pd.DataFrame:
    """
    Load the benchmark dataset.

    Parameters
    ----------
    dataset_path : str

    Returns
    -------
    pandas.DataFrame
    """

    path = Path(dataset_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}"
        )

    return pd.read_csv(path, encoding="utf-8")


# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

def ensure_directory(directory: str) -> Path:
    """
    Create a directory if it doesn't exist.

    Returns
    -------
    pathlib.Path
    """

    path = Path(directory)

    path.mkdir(parents=True, exist_ok=True)

    return path


# ---------------------------------------------------------------------
# Timestamp
# ---------------------------------------------------------------------

def get_timestamp() -> str:
    """
    Return current timestamp.

    Example
    -------
    2026-07-10_21-45-32
    """

    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# ---------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------

def setup_logger(
    log_directory: str = "logs",
    logger_name: str = "experiment"
) -> logging.Logger:
    """
    Create experiment logger.

    Returns
    -------
    logging.Logger
    """

    ensure_directory(log_directory)

    log_file = (
        Path(log_directory)
        / f"{logger_name}_{get_timestamp()}.log"
    )

    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


# ---------------------------------------------------------------------
# CSV
# ---------------------------------------------------------------------

def save_dataframe(
    df: pd.DataFrame,
    output_path: str
) -> None:
    """
    Save DataFrame to CSV.
    """

    output = Path(output_path)

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output,
        index=False,
        encoding="utf-8-sig"
    )