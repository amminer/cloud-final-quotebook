from lib.config_helper import config


if config.model == 'sqlite3':
    from .model_sqlite3 import Model
elif config.model == 'datastore':
    from .model_datastore import Model
else:
    raise ValueError(f'invalid configuration: "model": "{config.model}"')


def get_model():
    return Model()
