from pathlib import Path

import pytest

from cdt import config


@pytest.mark.config
def test_create_config():
    conf = config.Config('user')

    if conf.config_path is isinstance(conf.config_path, Path):
        assert conf.config_path.exists()

    assert Path(conf.config_path).exists()