"""
This file is part of the The Sims 4 Mod Settings Menu licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import List, Any, Tuple, Iterator

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

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 's4msm_mod_settings_registry'

    def __init__(self) -> None:
        super().__init__()
        self._registered_menu_items: List[S4MSMMenuItem] = list()

    @classmethod
    def register_menu_item(cls, menu_item: S4MSMMenuItem):
        """register_menu_item(menu_item)

        :param menu_item: An instance of a menu item.
        :type menu_item: S4MSMMenuItem
        """
        cls()._register_menu_item(menu_item)

    def _register_menu_item(self, menu_item: S4MSMMenuItem):
        self._registered_menu_items.append(menu_item)

    def has_menu_items_available_for(self, source_sim_info: SimInfo, target: Any = None) -> bool:
        """has_menu_items_available_for(source_sim_info, target=target)

        Determine if menu items are available for a Target.

        :param source_sim_info: An instance of a Sim.
        :type source_sim_info: SimInfo
        :param target: An instance of an object. Default is None.
        :type target: Any, optional
        :return: True, if menu items are available for the Target. False, if not.
        :rtype: bool
        """
        self.log.format_with_message('Checking if any menu items are available for Sim and Target.', sim=source_sim_info, target=target)
        for _ in self._get_menu_items_available_for_gen(source_sim_info, target=target):
            return True
        self.log.format_with_message('No menu items are available for Sim and Target.', sim=source_sim_info, target=target)
        return False

    def get_menu_items_available_for(self, source_sim_info: SimInfo, target: Any = None) -> Tuple[S4MSMMenuItem]:
        """get_menu_items_available_for(source_sim_info, target=None)

        Retrieve the menu items available for the a Sim and a Target.

        :param source_sim_info: An instance of a Sim.
        :type source_sim_info: SimInfo
        :param target: An instance of an object. Default is None.
        :type target: Any, optional
        :return: A collection of menu items available for a Sim and a Target.
        :rtype: Tuple[S4MSMMenuItem]
        """
        self.log.format_with_message('Attempting to locate menu items available for Sim and Target.', sim=source_sim_info, target=target)
        return tuple(self._get_menu_items_available_for_gen(source_sim_info, target=target))

    def _get_menu_items_available_for_gen(self, source_sim_info: SimInfo, target: Any = None) -> Iterator[S4MSMMenuItem]:
        menu_items_count = 0
        for menu_item in self._registered_menu_items:
            self.log.format_with_message(f'Checking if menu item \'{menu_item.identifier}\' is available for the Sim and Target.')
            is_available_for_result = menu_item.is_available_for(source_sim_info, target=target)
            if not is_available_for_result:
                self.log.format_with_message('Menu Item is not Available.', menu_item=menu_item, is_available_for_result=is_available_for_result)
                continue
            menu_items_count += 1
            self.log.format_with_message('Menu Item is Available.', menu_item=menu_item)
            yield menu_item
        self.log.format_with_message(f'Located {menu_items_count} menu item(s( that were available for Sim and Target.', sim=source_sim_info, target=target)
