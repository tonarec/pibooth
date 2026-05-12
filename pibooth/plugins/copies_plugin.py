# -*- coding: utf-8 -*-

import pibooth
from pibooth.utils import LOGGER


class CopiesPlugin(object):

    """Plugin to manage the copies selection.
    """

    name = 'pibooth-core:copies'

    def __init__(self, plugin_manager):
        self._pm = plugin_manager

    @pibooth.hookimpl
    def state_copies_enter(self, cfg, app):
        app.copies_to_print = cfg.getint('PRINTER', 'default_copies')

    @pibooth.hookimpl
    def state_copies_do(self, cfg, app, win, events):
        if app.find_capture_event(events):
            LOGGER.debug(">>> Capture button selected!")
            max_copies = cfg.getint('PRINTER', 'max_copies')
            if app.copies_to_print >= max_copies:
                LOGGER.warning("Maximum number of copies reached (%s max)",
                               app.copies_to_print)
                return

            # TODO: Implement decrease number
            app.copies_to_print += 1
            app.copies_to_print = max(app.copies_to_print, max_copies)
            LOGGER.debug(">>> New copies number: %d", app.copies_to_print)

            win.set_copies_number(app.copies_to_print)
