from pandas import DataFrame
import pytest

@pytest.mark.usefixtures("read_df")
def test_df(read_df):
    print(read_df)

    assert isinstance(read_df, DataFrame)