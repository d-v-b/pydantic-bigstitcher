import re

import pydantic_bigstitcher


def test_version_is_exposed() -> None:
    assert isinstance(pydantic_bigstitcher.__version__, str)
    # PEP 440-ish: at least N.N.N, possibly with a dev/local suffix
    assert re.match(r"^\d+\.\d+\.\d+", pydantic_bigstitcher.__version__)
