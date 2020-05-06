"""
This file is part of the The Sims 4 Mod Settings Menu licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import Any

from sims.sim_info import SimInfo
from sims4communitylib.dialogs.option_dialogs.common_choose_object_option_dialog import CommonChooseObjectOptionDialog
from sims4communitylib.dialogs.option_dialogs.options.common_dialog_option_context import CommonDialogOptionContext
from sims4communitylib.dialogs.option_dialogs.options.objects.common_dialog_select_option import \
    CommonDialogSelectOption
from sims4communitylib.logging.has_log import HasLog
from sims4communitylib.mod_support.mod_identity import CommonModIdentity
from sims4communitylib.utils.sims.common_sim_name_utils import CommonSimNameUtils
from sims4modsettingsmenu.enums.string_ids import S4MSMStringId
from sims4modsettingsmenu.modinfo import ModInfo
from sims4modsettingsmenu.registration.mod_settings_menu_item import S4MSMMenuItem
from sims4modsettingsmenu.registration.mod_settings_registry import S4MSMModSettingsRegistry


class S4ModSettingsMenu(HasLog):
    """S4MSMDialog()

    The dialog shown when the Open Mod Settings interaction is used.

    """
    def __init__(self) -> None:
        super().__init__()
        self._menu_item_registry = S4MSMModSettingsRegistry()

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_identity(self) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @property
    def log_identifier(self) -> str:
        return 's4msm_mod_settings_dialog'

    def open(self, source_sim_info: SimInfo, target: Any=None, page: int=1) -> None:
        """open(source_sim_info, target=None, page=1)

        Open the mod settings menu.

        :param source_sim_info: An instance of the Sim opening the dialog.
        :type source_sim_info: SimInfo
        :param target: An instance of an object. Default is None.
        :type target: Any, optional
        :param page: The page to open at. Default is 1.
        :type page: int, optional
        """
        self.log.debug('Opening Mod Settings Menu.')

        def _on_close(*_, **__) -> None:
            self.log.debug('MSM closed.')

        option_dialog = CommonChooseObjectOptionDialog(
            S4MSMStringId.MOD_SETTINGS_MENU,
            S4MSMStringId.CHOOSE_SETTINGS_TO_MODIFY,
            on_close=_on_close,
            mod_identity=self.mod_identity
        )

        def _open_dialog(*_, **__) -> None:
            self.log.debug('Reopening MSM.')
            self.open(source_sim_info, target=target, page=page)

        available_menu_items = self._menu_item_registry.get_menu_items_available_for(source_sim_info, target=target)

        sorted_available_menu_items = sorted(available_menu_items, key=lambda mi: mi.identifier)

        def _on_chosen(_: str, chosen_menu_item: S4MSMMenuItem):
            return chosen_menu_item.show(source_sim_info, target=target, on_close=_open_dialog)

        self.log.debug('Adding menu items.')
        for menu_item in sorted_available_menu_items:
            option_dialog.add_option(
                CommonDialogSelectOption(
                    menu_item.identifier,
                    menu_item,
                    CommonDialogOptionContext(
                        S4MSMStringId.MOD_SETTINGS,
                        S4MSMStringId.ALL_SETTINGS_RELATED_TO_MOD,
                        title_tokens=(menu_item.mod_name,),
                        description_tokens=(menu_item.mod_name,),
                        tooltip_text_identifier=menu_item.description
                    ),
                    on_chosen=_on_chosen
                )
            )

        if not option_dialog.has_options():
            self.log.debug('No menu items were available for \'{}\' and \'{}\'.'.format(CommonSimNameUtils.get_full_name(source_sim_info), target))
            return

        option_dialog.show(
            sim_info=source_sim_info,
            page=page
        )
