import hypothesis
from hypothesis import (given,
                        settings,
                        )
from hypothesis.strategies import just

from pathlib import Path

from XChemDB.xchem_db import XChemDB


@settings(deadline=100000,
          suppress_health_check=[hypothesis.HealthCheck.too_slow],
          max_examples=1,
          )
@given(just(Path("/dls/labxchem/data")))
def test_from_file_tree(root: Path) -> None:
    db = XChemDB.from_file_tree(root)
    print(db.database)


if __name__ == "__main__":
    test_from_file_tree()

