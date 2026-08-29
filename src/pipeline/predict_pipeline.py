import os
import sys
import pandas as pd

from flask import request
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.constant import TARGET_COLUMN
from src.utils.main_utils import MainUtils


@dataclass
class PredictionFileDetail:
    prediction_output_dirname: str = "predictions"
    prediction_file_name: str = "predicted_file.csv"

    prediction_file_path: str = os.path.join(
        prediction_output_dirname,
        prediction_file_name
    )


class PredictionPipeline:

    def __init__(self, request: request):
        self.request = request
        self.utils = MainUtils()
        self.prediction_file_detail = PredictionFileDetail()

    # ---------------------------------------------------------
    # STEP 1: SAVE UPLOADED CSV
    # ---------------------------------------------------------
    def save_input_files(self) -> str:

        try:

            prediction_artifacts_dir = "prediction_artifacts"

            os.makedirs(
                prediction_artifacts_dir,
                exist_ok=True
            )

            # Check whether a file was received
            if "file" not in self.request.files:
                raise Exception(
                    "No file received. Please select a CSV file."
                )

            input_csv_file = self.request.files["file"]

            # Check filename
            if not input_csv_file.filename:
                raise Exception(
                    "No filename received. Please select a CSV file."
                )

            # Check CSV extension
            if not input_csv_file.filename.lower().endswith(".csv"):
                raise Exception(
                    "Please upload a CSV file."
                )

            # Create path for uploaded file
            input_file_path = os.path.join(
                prediction_artifacts_dir,
                input_csv_file.filename
            )

            # Save uploaded file
            input_csv_file.save(input_file_path)

            logging.info(
                f"Input file saved successfully: {input_file_path}"
            )

            return input_file_path

        except Exception as e:

            raise CustomException(e, sys) from e

    # ---------------------------------------------------------
    # STEP 2: LOAD LOCAL MODEL AND PREDICT
    # ---------------------------------------------------------
    def predict(self, features):

        try:

            # Get project root directory
            project_root = os.getcwd()

            # Local model path
            model_path = os.path.join(
                project_root,
                "model.pkl"
            )

            # Check model exists
            if not os.path.exists(model_path):

                raise Exception(
                    f"model.pkl not found at: {model_path}"
                )

            logging.info(
                f"Loading local model from: {model_path}"
            )

            # Load local model
            model = self.utils.load_object(
                file_path=model_path
            )

            logging.info(
                "Local model loaded successfully."
            )

            # Make predictions
            predictions = model.predict(features)

            logging.info(
                "Predictions generated successfully."
            )

            return predictions

        except Exception as e:

            raise CustomException(e, sys) from e

    # ---------------------------------------------------------
    # STEP 3: READ CSV -> PREDICT -> CREATE OUTPUT CSV
    # ---------------------------------------------------------
    def get_predicted_dataframe(
        self,
        input_dataframe_path: str
    ):

        try:

            # Read uploaded CSV
            input_dataframe = pd.read_csv(
                input_dataframe_path
            )

            logging.info(
                "Input CSV loaded successfully."
            )

            logging.info(
                f"Input CSV shape: {input_dataframe.shape}"
            )

            logging.info(
                f"Input CSV columns: "
                f"{list(input_dataframe.columns)}"
            )

            # -------------------------------------------------
            # IMPORTANT:
            # Remove Result column before prediction.
            #
            # The model was trained WITHOUT Result.
            # -------------------------------------------------

            features = input_dataframe.drop(
                columns=[TARGET_COLUMN],
                errors="ignore"
            )

            logging.info(
                f"Features used for prediction: "
                f"{list(features.columns)}"
            )

            # Generate predictions
            predictions = self.predict(
                features
            )

            # -------------------------------------------------
            # Add predictions to original dataframe
            # -------------------------------------------------

            input_dataframe[TARGET_COLUMN] = predictions

            # Convert 0/1 predictions into labels
            target_column_mapping = {
                0: "phising",
                1: "safe"
            }

            input_dataframe[TARGET_COLUMN] = (
                input_dataframe[TARGET_COLUMN]
                .map(target_column_mapping)
            )

            # -------------------------------------------------
            # Create predictions directory
            # -------------------------------------------------

            os.makedirs(
                self.prediction_file_detail.prediction_output_dirname,
                exist_ok=True
            )

            # -------------------------------------------------
            # Save final prediction CSV
            # -------------------------------------------------

            input_dataframe.to_csv(
                self.prediction_file_detail.prediction_file_path,
                index=False
            )

            logging.info(
                "Prediction completed successfully."
            )

            logging.info(
                f"Prediction file created at: "
                f"{self.prediction_file_detail.prediction_file_path}"
            )

        except Exception as e:

            raise CustomException(e, sys) from e

    # ---------------------------------------------------------
    # STEP 4: RUN COMPLETE PREDICTION PIPELINE
    # ---------------------------------------------------------
    def run_pipeline(self):

        try:

            # Save uploaded CSV
            input_csv_path = self.save_input_files()

            # Generate predictions
            self.get_predicted_dataframe(
                input_csv_path
            )

            # Return prediction file details
            return self.prediction_file_detail

        except Exception as e:

            raise CustomException(e, sys) from e