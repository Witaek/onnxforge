from onnxforge_shared import __version__


def test_shared_version_exists():
    assert isinstance(__version__, str)