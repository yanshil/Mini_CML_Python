from click.testing import CliRunner

@pytest.fixture
def runner():
    return CliRunner()

def test_hello(runner):
    result = runner.invoke(cli.main)
    assert 'Hello' in result.output
    pass