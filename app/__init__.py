## NOTE!
## In python 3.3 and above, '__init__.py' is technically not required to create a package, as implicit namespace packages supported. However, it is still a good practice to include '__init__.py' for the reasons mention above, especially for better control and clarity in your codebase.

import logging
from .main import main
from .const import CONST
from .gui import gui

__all__ = ['main', 'CONST', 'Gui']

# Setup logging for the package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Initializing the app package")

# Package metadata
__version__ = '1.0.0'
__author__ = "Devalltect00; Rizky Purwanto Fernandes;"

def initialize():
  logger.info("Initializing the app package")

initialize()