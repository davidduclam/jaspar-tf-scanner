import pytest
import requests
from modules import jaspar_api
from unittest.mock import patch, Mock

@patch("modules.jaspar_api.requests.get")
def test_search_jaspar(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"results": [{"id": "MA0001.1"}]}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = jaspar_api.search_jaspar("TP53")
    assert result == [{"id": "MA0001.1"}]

@patch("modules.jaspar_api.requests.get")
def test_search_jaspar_error(mock_get):
    mock_get.side_effect = requests.RequestException("API error")
    result = jaspar_api.search_jaspar("TP53")
    assert result is None

@patch("modules.jaspar_api.requests.get")
def test_fetch_jaspar_motif(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"name": "ABF1"}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = jaspar_api.fetch_jaspar_motif("MA0265.1")
    assert result == {"name": "ABF1"}

@patch("modules.jaspar_api.requests.get")
def test_fetch_jaspar_motif_error(mock_get):
    mock_get.side_effect = requests.RequestException("API error")
    result = jaspar_api.fetch_jaspar_motif("MA0265.1")
    assert result is None
