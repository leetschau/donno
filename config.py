import json
from pathlib import Path
from typing import Dict, Union

DEFAULT_CONF_PATH = Path.home() / '.config/donno/config.json'
BASE_DIR = Path.home() / ".donno"
DEFAULT_CONF = {
    'app_home': str(BASE_DIR),
    'repo': str(BASE_DIR / 'repo'),
    'editor': 'nvim',
    'viewer': 'nvim -R',
    'default_notebook': '/Diary',
    'editor_envs': {
        'XDG_CONFIG_HOME': '$HOME/.config',
    },
}


def load_configs() -> Dict[str, Union[str, Path, dict]]:
    if not DEFAULT_CONF_PATH.exists():
        DEFAULT_CONF_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(DEFAULT_CONF_PATH, 'w') as f:
            json.dump(DEFAULT_CONF, f, indent=4)
        return DEFAULT_CONF
    with open(DEFAULT_CONF_PATH) as f:
        configs = json.load(f)
    return configs
