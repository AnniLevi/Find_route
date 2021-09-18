from .settings_prod import *

try:
    from .settings_local import *
except ImportError:
    pass
