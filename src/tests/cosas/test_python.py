import pytest


@pytest.mark.usefixtures("list_data")
def test_all(list_data):
    print(list_data)

    assert isinstance(list_data, list)



@pytest.mark.usefixtures("model_data")
def test_model(model_data):
    print(model_data)

    assert isinstance(model_data, dict)