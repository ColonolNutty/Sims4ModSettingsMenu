"""
This file is part of the The Sims 4 Mod Settings Menu licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import Tuple

from objects.script_object import ScriptObject
from sims4communitylib.enums.affordance_list_ids import CommonAffordanceListId
from sims4communitylib.services.resources.common_instance_manager_modification_registry import \
    CommonInstanceManagerModificationRegistry
from sims4communitylib.services.resources.modification_handlers.common_add_interactions_to_affordance_lists_handler import \
    CommonAddInteractionsToAffordanceListsModificationHandler
from sims4modsettingsmenu.enums.interaction_ids import S4MSMInteractionId
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, \
    CommonInteractionType, CommonScriptObjectInteractionHandler, CommonInteractionHandler


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_TERRAIN_LOAD)
class _S4MSMTerrainInteractionHandler(CommonInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[int]:
        result: Tuple[int] = (
            S4MSMInteractionId.OPEN_MOD_SETTINGS_MENU,
        )
        return result


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_OCEAN_LOAD)
class _S4MSMOceanInteractionHandler(CommonInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[int]:
        result: Tuple[int] = (
            S4MSMInteractionId.OPEN_MOD_SETTINGS_MENU,
        )
        return result


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _S4MSMSimInteractionHandler(CommonScriptObjectInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[int]:
        result: Tuple[int] = (
            S4MSMInteractionId.OPEN_MOD_SETTINGS_MENU,
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True


@CommonInstanceManagerModificationRegistry.register_modification_handler()
class _S4MSMAddToAffordanceWhitelist(CommonAddInteractionsToAffordanceListsModificationHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interaction_ids(self) -> Tuple[int]:
        result: Tuple[int] = (
            S4MSMInteractionId.OPEN_MOD_SETTINGS_MENU,
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    @property
    def affordance_list_ids(self) -> Tuple[int]:
        result: Tuple[int] = (
            CommonAffordanceListId.DEBUG_AFFORDANCES,
        )
        return result
