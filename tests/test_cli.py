from click.testing import CliRunner
import pytest
from minicmlpy import cli

@pytest.fixture
def runner():
    return CliRunner()

def test_hello(runner):
    result = runner.invoke(cli.main)
    assert result.output == 'Hello World!\n'