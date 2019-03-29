#!/usr/bin/env python3
"""
This module contains a Snips app that makes the Snips assistant be quiet.
"""

import importlib
from pathlib import Path

from hermes_python.ontology.dialogue import DialogueConfiguration
from snipskit.config import AssistantConfig
from snipskit.hermes.apps import HermesSnipsApp
from snipskit.hermes.decorators import intent

# Use the assistant's language.
i18n = importlib.import_module('translations.' + AssistantConfig()['language'])


class KeepQuiet(HermesSnipsApp):
    """
    This app lets you ask your assistant to stop replying to your voice
    commands until you ask it to talk to you again.
    """

    @intent(i18n.INTENT_QUIET)
    def quiet(self, hermes, intent_message):
        """Handle the intent Quiet."""

        intents = [intent['id'] for intent in self.assistant['intents']]
        intents.remove(i18n.INTENT_TALK)

        dialogue_conf = DialogueConfiguration().disable_intents(intents).enable_intent(i18n.INTENT_TALK)
        hermes.configure_dialogue(dialogue_conf)

        hermes.publish_end_session(intent_message.session_id, i18n.RESULT_QUIET)

    @intent(i18n.INTENT_TALK)
    def talk(self, hermes, intent_message):
        """Handle the intent Talk."""

        intents = [intent['id'] for intent in self.assistant['intents']]

        dialogue_conf = DialogueConfiguration().enable_intents(intents)
        hermes.configure_dialogue(dialogue_conf)

        hermes.publish_end_session(intent_message.session_id, i18n.RESULT_TALK)

if __name__ == "__main__":
    KeepQuiet()
