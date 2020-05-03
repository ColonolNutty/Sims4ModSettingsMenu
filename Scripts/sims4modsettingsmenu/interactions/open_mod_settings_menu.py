"""
This file is part of the The Sims 4 Mod Settings Menu licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import Any

from sims4modsettingsmenu.dialogs.mod_settings_menu_dialog import S4ModSettingsMenu
from sims4modsettingsmenu.modinfo import ModInfo
from event_testing.results import TestResult
from interactions.context import InteractionContext
from sims.sim import Sim
from sims4communitylib.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from sims4communitylib.mod_support.mod_identity import CommonModIdentity
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4modsettingsmenu.registration.mod_settings_registry import S4MSMModSettingsRegistry


class S4MSMOpenModSettingsMenuInteraction(CommonImmediateSuperInteraction):
    """S4MSMOpenModSettingsMenuInteraction(*_, **__)

    Open the Mod Settings Menu.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._mod_settings_menu = S4ModSettingsMenu()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 's4msm_open_mod_settings_menu'

    @classmethod
    def get_mod_settings_registry(cls) -> S4MSMModSettingsRegistry:
        """get_mod_settings_registry()

        Retrieve an instance of the mod settings registry.

        :return: An instance of the mod settings registry.
        :rtype: S4MSMModSettingsRegistry
        """
        return S4MSMModSettingsRegistry()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> TestResult:
        cls.get_log().format_with_message(
            'Running \'{}\' on_test.'.format(cls.__name__),
            interaction_sim=interaction_sim,
            interaction_target=interaction_target,
            interaction_context=interaction_context,
            kwargles=kwargs
        )
        source_sim_info = CommonSimUtils.get_sim_info(interaction_sim)
        if not cls.get_mod_settings_registry().has_menu_items_available_for(source_sim_info, target=interaction_target):
            cls.get_log().debug('No menu items were available for \'{}\''.format(interaction_target))
            return TestResult.NONE
        cls.get_log().debug('Success, can open mod settings.')
        return TestResult.TRUE

    # noinspection PyMissingOrEmptyDocstring
    def on_started(self, interaction_sim: Sim, interaction_target: Sim) -> bool:
        self.log.format_with_message(
            'Running \'{}\' on_started.'.format(self.__class__.__name__),
            interaction_sim=interaction_sim,
            interaction_target=interaction_target
        )
        source_sim_info = CommonSimUtils.get_sim_info(interaction_sim)
        self._mod_settings_menu.open(source_sim_info, target=interaction_target)
        return True
