from pandas import DataFrame
import pytest
import pandas as pd

@pytest.fixture
def read_df() -> pd.DataFrame:

    return pd.read_csv("customer_data.csv")