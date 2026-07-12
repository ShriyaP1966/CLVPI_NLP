"""
result_writer.py

Writes benchmark responses to CSV files.

Author: Shriya Patil
"""

import pandas as pd
from pathlib import Path

from utils import (
    load_config,
    ensure_directory,
    save_dataframe,
)


class ResultWriter:
    """
    Saves benchmark results.
    """

    def __init__(self):

        config = load_config()

        self.output_directory = config["outputs"]["raw"]

        ensure_directory(self.output_directory)

    def save_results(
        self,
        responses,
        filename="mock_results.csv"
    ):
        """
        Save responses to CSV.

        Parameters
        ----------
        responses : list[dict]

        filename : str
        """

        df = pd.DataFrame(responses)

        output_path = (
            Path(self.output_directory)
            / filename
        )

        save_dataframe(
            df,
            str(output_path)
        )

        print()
        print("Results saved successfully.")
        return output_path