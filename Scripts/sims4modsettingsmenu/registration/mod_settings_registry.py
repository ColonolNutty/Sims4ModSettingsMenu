"""
This file is part of the The Sims 4 Mod Settings Menu licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import List, Any, Tuple

from sims.sim_info import SimInfo
from sims4communitylib.logging.has_class_log import HasClassLog
from sims4communitylib.mod_support.mod_identity import CommonModIdentity
from sims4communitylib.services.common_service import CommonService
from sims4modsettingsmenu.modinfo import ModInfo
from sims4modsettingsmenu.registration.mod_settings_menu_item import S4MSMMenuItem


class S4MSMModSettingsRegistry(CommonService, HasClassLog):
    """S4MSMModSettingsRegistry()

    A registry containing registered setting menus.

    """

    def __init__(self) -> None:
        super().__init__()
        self._registered_menu_items: List[S4MSMMenuItem] = list()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 's4msm_mod_settings_registry'

    @classmethod
    def register_menu_item(cls, menu_item: S4MSMMenuItem):
        """register_menu_item(menu_item)

        :param menu_item: An instance of a menu item.
        :type menu_item: S4MSMMenuItem
        """
        cls()._register_menu_item(menu_item)

    def _register_menu_item(self, menu_item: S4MSMMenuItem):
        self._registered_menu_items.append(menu_item)

    def has_menu_items_available_for(self, source_sim_info: SimInfo, target: Any=None) -> bool:
        """has_menu_items_available_for(source_sim_info, target=target)

        Determine if menu items are available for a Target.

        :param source_sim_info: An instance of a Sim.
        :type source_sim_info: SimInfo
        :param target: An instance of an object. Default is None.
        :type target: Any, optional
        :return: True, if menu items are available for the Target. False, if not.
        :rtype: bool
        """
        self.log.debug('Determining if any menu items are available for {}.'.format(target))
        for menu_item in self._registered_menu_items:
            if menu_item.is_available_for(source_sim_info, target=target):
                self.log.debug('Menu items are available for the Target.')
                return True
        self.log.debug('No menu items are available for the Target.')
        return False

    def get_menu_items_available_for(self, source_sim_info: SimInfo, target: Any=None) -> Tuple[S4MSMMenuItem]:
        """get_menu_items_available_for(source_sim_info, target=None)

        Retrieve the menu items available for the specified Target.

        :param source_sim_info: An instance of a Sim.
        :type source_sim_info: SimInfo
        :param target: An instance of an object. Default is None.
        :type target: Any, optional
        :return: A collection of menu items available for a Target.
        :rtype: Tuple[S4MSMMenuItem]
        """
        self.log.debug('Attempting to locate menu items available for {}.'.format(target))
        available_menu_items: List[S4MSMMenuItem] = list()
        for menu_item in self._registered_menu_items:
            self.log.debug('Checking if menu item \'{}\' is available for the Target.'.format(menu_item.identifier))
            if not menu_item.is_available_for(source_sim_info, target=target):
                self.log.debug('Available.')
                continue
            self.log.debug('Not Available.')
            available_menu_items.append(menu_item)
        self.log.debug('Located {} menu items available for Target.'.format(len(available_menu_items)))
        return tuple(available_menu_items)
