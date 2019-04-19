#!/usr/bin/env python3
"""
This module contains a Snips app that makes the Snips assistant be quiet.
"""

import importlib

from hermes_python.ontology.dialogue import DialogueConfiguration
from snipskit.apps import SnipsAppMixin
from snipskit.hermes.apps import HermesSnipsApp
from snipskit.hermes.decorators import intent
from snipskit.mqtt.client import publish_single

# Use the assistant's language.
i18n = importlib.import_module('translations.' + SnipsAppMixin().assistant['language'])

INJECTION_PERFORM = 'hermes/injection/perform'


class KeepQuiet(HermesSnipsApp):
    """
    This app lets you ask your assistant to stop replying to your voice
    commands until you ask it to talk to you again.
    """

    def initialize(self):
        """Initialize the app."""

        # Inject the names of the installed intents.

        intents = [intent['name'] for intent in self.assistant['intents']]
        injections = {'operations': [['add', {i18n.SLOT_TYPE_INTENT: intents}]]}
        publish_single(self.snips.mqtt, INJECTION_PERFORM, injections)

    @intent(i18n.INTENT_QUIET)
    def quiet(self, hermes, intent_message):
        """Handle the intent Quiet."""

        # Get all the intents from the assistant and remove the one to talk
        # again.
        intents = [intent['id'] for intent in self.assistant['intents']]
        intents.remove(i18n.INTENT_TALK)

        dialogue_conf = DialogueConfiguration().disable_intents(intents) \
                                               .enable_intent(i18n.INTENT_TALK)
        hermes.configure_dialogue(dialogue_conf)

        hermes.publish_end_session(intent_message.session_id,
                                   i18n.RESULT_QUIET)

    @intent(i18n.INTENT_TALK)
    def talk(self, hermes, intent_message):
        """Handle the intent Talk."""

        # Get all the intents from the assistant that are enabled by default.
        enabled_intents = [intent['id']
                           for intent in self.assistant['intents']
                           if intent['enabledByDefault']]

        # Get all the intents from the assistant that are disabled by default.
        disabled_intents = [intent['id']
                            for intent in self.assistant['intents']
                            if not intent['enabledByDefault']]

        dialogue_conf = DialogueConfiguration().enable_intents(enabled_intents) \
                                               .disable_intents(disabled_intents)
        hermes.configure_dialogue(dialogue_conf)

        hermes.publish_end_session(intent_message.session_id, i18n.RESULT_TALK)

    @intent(i18n.INTENT_ENABLE_INTENT)
    def enable_intent(self, hermes, intent_message):
        """Handle the intent EnableIntent."""
        intent = intent_message.slots.intent.first().value

        dialogue_conf = DialogueConfiguration().enable_intent(intent)
        hermes.configure_dialogue(dialogue_conf)

        hermes.publish_end_session(intent_message.session_id,
                                   i18n.RESULT_ENABLE_INTENT)

    @intent(i18n.INTENT_DISABLE_INTENT)
    def disable_intent(self, hermes, intent_message):
        """Handle the intent DisableIntent."""
        intent = intent_message.slots.intent.first().value

        dialogue_conf = DialogueConfiguration().disable_intent(intent)
        hermes.configure_dialogue(dialogue_conf)

        hermes.publish_end_session(intent_message.session_id,
                                   i18n.RESULT_DISABLE_INTENT)


if __name__ == "__main__":
    KeepQuiet()
