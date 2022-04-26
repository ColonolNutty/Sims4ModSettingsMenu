"""
This file is part of the The Sims 4 Mod Settings Menu licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
# noinspection PyUnresolvedReferences
import _resourceman
from typing import Callable, Any, Union
from protocolbuffers.Localization_pb2 import LocalizedString
from sims.sim_info import SimInfo
from sims4communitylib.logging.has_log import HasLog
from sims4communitylib.mod_support.mod_identity import CommonModIdentity
from sims4communitylib.utils.common_function_utils import CommonFunctionUtils
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4modsettingsmenu.enums.string_ids import S4MSMStringId


class S4MSMMenuItem(HasLog):
    """S4MSMMenuItem()

    A menu item that will display in the Mod Settings Menu. When selected, it will display a dialog containing settings.
    """

    def __init__(self) -> None:
        super().__init__()
        self._default_title = CommonLocalizationUtils.create_localized_string(S4MSMStringId.MOD_SETTINGS, tokens=(self.mod_name,))
        self._default_description = CommonLocalizationUtils.create_localized_string(S4MSMStringId.ALL_SETTINGS_RELATED_TO_MOD, tokens=(self.mod_name,))

    @property
    def identifier(self) -> str:
        """
        An identifier used to sort alphabetically.

        :return: A text identifier.
        :rtype: str
        """
        return self.mod_identity.base_namespace

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_name(self) -> Union[int, str, LocalizedString]:
        """
        The name of the mod the menu item belongs to. It will display within the MSM dialog.

        :return: A localized string, decimal identifier, or text representing the name of the mod owning this menu item.
        :rtype: Union[int, str, LocalizedString]
        """
        return self.mod_identity.name

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_version(self) -> Union[int, str, LocalizedString]:
        """
        The version of the mod the menu item belongs to. It will display within the MSM dialog.

        :return: A localized string, decimal identifier, or text representing the version of the mod owning this menu item.
        :rtype: Union[int, str, LocalizedString]
        """
        return self.mod_identity.version

    @property
    def title(self) -> Union[int, str, LocalizedString, None]:
        """
        The title of the menu item to display in the MSM dialog.

        :return: A localized string, decimal identifier, or text representing the title of this menu item.
        :rtype: Union[int, str, LocalizedString, None]
        """
        return self._default_title

    @property
    def description(self) -> Union[int, str, LocalizedString, None]:
        """
        The description of the menu item to display in the MSM dialog.

        :return: A localized string, decimal identifier, or text representing the description of this menu item.
        :rtype: Union[int, str, LocalizedString, None]
        """
        return self._default_description

    @property
    def icon(self) -> _resourceman.Key:
        """
        An icon that will replace the default select icon for the mod in the MSM dialog.

        An Icon may be loaded in the following example.


        .. highlight:: python
        .. code-block:: python

            CommonResourceUtils.get_resource_key(Types.PNG, CommonIconId.S4CLIB_ARROW_RIGHT_ICON)

        .. note:: _resourceman has issues being resolved, but it does in fact exist! -> import _resourceman

        :return: The resource key of the icon to display for this menu item.
        :rtype: _resourceman.Key
        """
        return None

    @property
    def tooltip_text(self) -> Union[LocalizedString, None]:
        """
        A description of the menu item. It will display as a tooltip within the MSM dialog.

        :return: A localized string representing the description of this menu item.
        :rtype: LocalizedString
        """
        return None

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_identity(self) -> CommonModIdentity:
        raise NotImplementedError(f'Missing \'{self.__class__.__name__}.mod_identity\'.')

    # noinspection PyMissingOrEmptyDocstring
    @property
    def log_identifier(self) -> str:
        return 's4msm_menu_item'

    def is_available_for(self, source_sim_info: SimInfo, target: Any=None) -> bool:
        """is_available_for(source_sim_info, target=None)

        Determine if these settings are available for the Target.

        .. note:: If the settings are not available for the target, the menu item itself will not be included in the MSM dialog.

        :param source_sim_info: An instance of a Sim.
        :type source_sim_info: SimInfo
        :param target: An instance of an object. Default is None.
        :type target: Any, optional
        :return: True, if these settings are available for the Target. False, if not.
        :rtype: bool
        """
        raise NotImplementedError(f'Missing \'{self.__class__.__name__}.is_available_for\'.')

    def show(
        self,
        source_sim_info: SimInfo,
        *args,
        target: Any=None,
        on_close: Callable[..., Any]=CommonFunctionUtils.noop,
        **kwargs
    ):
        """show(\
            source_sim_info,\
            *args,\
            target=None,\
            on_close=CommonFunctionUtils.noop,\
            **kwargs\
        )

        Show the settings dialog.

        :param source_sim_info: An instance of a Sim.
        :type source_sim_info: SimInfo
        :param target: An instance of an object. Default is None.
        :type target: Any, optional
        :param on_close: The action to take upon the settings being closed. Default is CommonFunctionUtils.noop.
        :type on_close: Callable[..., Any], optional
        """
        raise NotImplementedError(f'Missing \'{self.__class__.__name__}.show\'.')
