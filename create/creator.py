__all__ = ['Creator']

from .info import *
from .server import *
from .tag import *
from .path import *
from .component import *


class Creator(Component, Info, Path, Server, Tag):

    def __init__(self, populate: bool):
        Component.__init__(self, populate)
        Info.__init__(self, populate)
        Path.__init__(self, populate)
        Server.__init__(self, populate)
        Tag.__init__(self, populate)
