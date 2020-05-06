"""
This file is part of the The Sims 4 Mod Settings Menu licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import Callable, Any, Union
from protocolbuffers.Localization_pb2 import LocalizedString
from sims.sim_info import SimInfo
from sims4communitylib.logging.has_log import HasLog
from sims4communitylib.mod_support.mod_identity import CommonModIdentity
from sims4communitylib.utils.common_function_utils import CommonFunctionUtils


class S4MSMMenuItem(HasLog):
    """S4MSMMenuItem()

    A menu item that will display in the Mod Settings Menu. When selected, it will display a dialog containing settings.
    """

    @property
    def identifier(self) -> str:
        """
        An identifier used to sort alphabetically.
        """
        return self.mod_identity.base_namespace

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_name(self) -> Union[int, str, LocalizedString]:
        """
        The name of the mod the menu item belongs to. It will display within the MSM dialog.

        :return: A localized string, decimal identifier, or test representing the name of the mod owning this menu item.
        :rtype: Union[int, str, LocalizedString]
        """
        return self.mod_identity.name

    # noinspection PyMissingOrEmptyDocstring
    @property
    def description(self) -> LocalizedString:
        """
        A description of the menu item. It will display as a tooltip within the MSM dialog.

        :return: A localized string representing the description of this menu item.
        :rtype: LocalizedString
        """
        raise NotImplementedError('Missing \'{}.description\'.'.format(self.__class__.__name__))

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_identity(self) -> CommonModIdentity:
        raise NotImplementedError('Missing \'{}.mod_identity\'.'.format(self.__class__.__name__))

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
        raise NotImplementedError('Missing \'{}.is_available_for\'.'.format(self.__class__.__name__))

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
        raise NotImplementedError('Missing \'{}.show\'.'.format(self.__class__.__name__))
