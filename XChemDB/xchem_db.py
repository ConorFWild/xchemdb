from typing import NamedTuple
from pathlib import Path
import re

import pandas as pd


# class Record(NamedTuple):
#     year: str
#     system: str
#     intial_models_path: Path


def initial_model_path_to_system(path: Path) -> str:
    datasets = path.glob("*")
    first_dataset = next(datasets)
    match = re.search("[^-]+", first_dataset.name)
    return match[0]


def get_initial_models_dataframe(root: Path) -> pd.DataFrame:
    initial_model_paths = get_initial_model_paths(root)

    records = []
    for path in initial_model_paths:
        try:
            record = {"year": path.parent.parent.parent.parent.name,
                      "system": initial_model_path_to_system(path),
                      "initial_model_path": str(path),
                      }
            records.append(record)
        except:
            continue
    
    return pd.DataFrame(records)


def get_initial_model_paths(root: Path):
    return root.glob("*/*/processing/analysis/initial_model")


class XChemDB:
    # year : system : path_to_initial_models
    database: pd.DataFrame

    def __init__(self, df):
        self.database = df

    @staticmethod
    def from_file_tree(root: Path):
        
        df = get_initial_models_dataframe(root)
        
        return XChemDB(df)

