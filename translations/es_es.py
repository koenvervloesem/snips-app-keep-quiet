"""
This module contains the result sentences and intents for the English version
of the Keep quiet app.
"""

# Result sentences
RESULT_ENABLE_INTENT = "Ok, he activado la intención {}."
RESULT_DISABLE_INTENT = "Ok, he desactivado la intención {}."
RESULT_QUIET = "Ok, permanezco en silencio."
RESULT_TALK = "Ok, ya hablo otra vez."

# Intents
INTENT_ENABLE_INTENT = 'koan:EnableIntent'
INTENT_DISABLE_INTENT = 'koan:DisableIntent'
INTENT_QUIET = 'koan:Quiet'
INTENT_TALK = 'koan:Talk'

# Slot types
SLOT_TYPE_INTENT = 'koan/snips-intent'
