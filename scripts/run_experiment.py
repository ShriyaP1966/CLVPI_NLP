"""
run_experiment.py

Main experiment runner for the Multilingual LLM Safety Benchmark.

This script:
1. Loads configuration
2. Validates the dataset
3. Creates a new experiment directory
4. Initializes the selected provider
5. Runs the benchmark
"""

from pathlib import Path
from datetime import datetime
import json

from utils import (
    load_config,
    setup_logger,
)

from validate_dataset import validate_dataset
from dataset_loader import DatasetLoader
from result_writer import ResultWriter

# Temporary provider
from providers.provider_factory import ProviderFactory

class ExperimentRunner:
    """
    Main experiment controller.
    """

    def __init__(self):

        self.config = load_config()

        self.logger = setup_logger(
            logger_name="experiment"
        )

        provider_name = self.config["provider"]

        self.provider = ProviderFactory.create_provider(
            provider_name
        )
        self.experiment_path = None

    def create_experiment_directory(self):
        """
        Create a unique experiment folder.
        """

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        self.experiment_path = (
            Path("experiments")
            / f"EXP_{timestamp}"
        )

        self.experiment_path.mkdir(
            parents=True,
            exist_ok=True
        )

        print("Experiment Folder:")
        print(self.experiment_path)

        self.logger.info(
            f"Experiment Folder: {self.experiment_path}"
        )

    def save_metadata(self):
        """
        Save experiment metadata.
        """

        metadata = {

            "experiment_time": datetime.now().isoformat(),

            "model": self.provider.__class__.__name__,

            "dataset": self.config["dataset"]["path"],

            "status": "initialized"

        }

        with open(
            self.experiment_path / "metadata.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4
            )

    def execute_tasks(self, tasks):
        """
        Execute benchmark tasks using the selected provider.
        """

        responses = []

        total = len(tasks)

        print()
        print("Running benchmark...")
        print()

        for index, task in enumerate(tasks, start=1):

            response = self.provider.generate_response(
                task["prompt"]
            )

            task_result = {

                "attack_id": task["attack_id"],

                "variation_id": task["variation_id"],

                "attack_category": task["attack_category"],

                "language": task["language"],

                "prompt": task["prompt"],

                "response": response,

                "provider": self.provider.__class__.__name__,

            }

            responses.append(task_result)

            print(f"[{index}/{total}] Completed")

        return responses

    def run(self):

        print("=" * 60)
        print("MULTILINGUAL SAFETY BENCHMARK")
        print("=" * 60)

        print("\nValidating dataset...\n")

        if not validate_dataset():

            print("\nDataset validation failed.")

            return

        print("\nDataset validation passed.\n")

        loader = DatasetLoader()

        tasks = loader.load_tasks()

        print(f"Loaded {len(tasks)} benchmark tasks.")

        responses = self.execute_tasks(tasks)

        print()

        print(f"Generated {len(responses)} responses.")

        writer = ResultWriter()

        output_path = writer.save_results(responses)
        self.create_experiment_directory()

        self.save_metadata()

        print()

        print("=" * 60)
        print("EXECUTION SUMMARY")
        print("=" * 60)

        print(f"Provider          : {self.provider.__class__.__name__}")

        print(f"Benchmark Tasks   : {len(tasks)}")

        print(f"Responses Created : {len(responses)}")

        print(f"Output File       : {output_path}")

        print(f"Experiment Folder : {self.experiment_path}")

        print()
        print("STATUS : SUCCESS")

        print("=" * 60)

        self.logger.info(
            "Framework initialized."
        )


if __name__ == "__main__":

    runner = ExperimentRunner()

    runner.run()