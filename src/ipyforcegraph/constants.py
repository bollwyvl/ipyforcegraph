try:
    from importlib.metadata import version
except:
    from importlib_metadata import version

NAME = "ipyforcegraph"

__version__ = version(NAME)

EXTENSION_NAME = "@jupyrdf/jupyter-forcegraph"
EXTENSION_SPEC_VERSION = (
    __version__.replace("a", "-alpha").replace("b", "-beta").replace("rc", "-rc")
)

__all__ = ["__version__", "EXTENSION_NAME", "EXTENSION_SPEC_VERSION"]
