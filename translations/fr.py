"""
This module contains the result sentences and intents for the French version
of the Keep quiet app.
"""

# Result sentences
RESULT_ENABLE_INTENT = "Ok, j'ai activé l'intention {}."
RESULT_DISABLE_INTENT = "Ok, j'ai désactivé l'intention {}."
RESULT_QUIET = "Ok, je vais rester silencieux."
RESULT_TALK = "Ok, je vais parler à nouveau."

# Intents
INTENT_ENABLE_INTENT = 'Sanlokii:ActiverIntention'
INTENT_DISABLE_INTENT = 'Sanlokii:DesactiverIntention'
INTENT_QUIET = 'Sanlokii:Silence'
INTENT_TALK = 'Sanlokii:Parle'

# Slot types
SLOT_TYPE_INTENT = 'Sanlokii/snips-intent'
