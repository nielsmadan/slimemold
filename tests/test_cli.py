import pytest

from slimemold import __version__
from slimemold.cli import main


def test_version_prints_the_package_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])
    assert exit_info.value.code == 0
    assert capsys.readouterr().out == f"slimemold {__version__}\n"


def test_no_arguments_exits_cleanly() -> None:
    assert main([]) == 0
