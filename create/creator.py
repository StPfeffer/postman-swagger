__all__ = ['Creator']

from .component import *
from .info import *
from .path import *
from .server import *
from .tag import *


class Creator(Component, Info, Path, Server, Tag):

    def __init__(self, populate: bool):
        self.populate = populate

        Component.__init__(self)
        Info.__init__(self)
        Path.__init__(self)
        Server.__init__(self)
        Tag.__init__(self)
