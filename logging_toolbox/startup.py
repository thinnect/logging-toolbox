"""
Utilities related to logging for the nozzle daemon.
"""
import logging
from importlib import import_module
from itertools import chain

logger = logging.getLogger(__name__)


def startup_log(args, critical_modules=(), cleaners=None):
    """
    Logs the configuration and dependency versions.

    Note: Logging should be already set up at this point.

    :param argparse.Namespace args: The arguments this program was
        launched with. Should contain all the configuration this
        program receives.
    :param list[str] critical_modules: The modules that will have their
        version information dumped.
    :param dict[str, types.FunctionType] cleaners: A dictionary
        containing functions to clean configuration values. Usually done
        to hide passwords or other sensitive information.
    :rtype: None
    """

    if cleaners is None:
        cleaners = {}

    configuration = vars(args)

    if configuration or critical_modules:

        max_width = max(len(i) for i in chain(configuration.keys(),
                                              critical_modules)) + 1

        total_width = max_width + 25

        logger.info('CONFIG'.center(total_width, '='))
        if critical_modules:
            logger.info('Versions'.center(total_width, '-'))
            for module_name in critical_modules:
                try:
                    module = import_module(module_name)
                except ImportError:
                    logger.info('%-*s: DOES NOT EXIST',
                                max_width,
                                module_name)
                else:
                    logger.info('%-*s: %s',
                                max_width,
                                module_name,
                                _get_version(module))

        if configuration:
            logger.info('Arguments'.center(total_width, '-'))
            for name, value in configuration.items():
                sanitized = cleaners.get(name, lambda v: v)(value)
                logger.info('%-*s: %s', max_width, name, sanitized)
        logger.info('=' * total_width)


def _get_version(module):
    """Returns a module's version or UNKNOWN if no version is available"""
    # Attempt to use the __version__ attribute first
    if hasattr(module, '__version__'):
        return module.__version__
    # Then try pkg_resources
    try:
        import pkg_resources
    except ImportError:
        pass
    else:
        return pkg_resources.get_distribution(module.__name__).version

    return 'UNKNOWN'
