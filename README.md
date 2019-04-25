# Keep quiet app for Snips

[![Build status](https://api.travis-ci.com/koenvervloesem/snips-app-keep-quiet.svg?branch=master)](https://travis-ci.com/koenvervloesem/snips-app-keep-quiet) [![Maintainability](https://api.codeclimate.com/v1/badges/3b028b9d7db9ffa2e760/maintainability)](https://codeclimate.com/github/koenvervloesem/snips-app-keep-quiet/maintainability) [![Code quality](https://api.codacy.com/project/badge/Grade/b244c94ff16447fc8ee3af07d03eb92e)](https://www.codacy.com/app/koenvervloesem/snips-app-keep-quiet) [![Python versions](https://img.shields.io/badge/python-3.5|3.6|3.7-blue.svg)](https://www.python.org) [![GitHub license](https://img.shields.io/github/license/koenvervloesem/snips-app-keep-quiet.svg)](https://github.com/koenvervloesem/snips-app-keep-quiet/blob/master/LICENSE) [![Languages](https://img.shields.io/badge/i18n-en|de|fr-brown.svg)](https://github.com/koenvervloesem/snips-app-keep-quiet/tree/master/translations) [![Snips App Store](https://img.shields.io/badge/snips-app-blue.svg)](https://console.snips.ai/store/en/skill_134O6Yb4K6b)

With this [Snips](https://snips.ai/) app, you can ask your assistant to stop replying to your voice commands until you ask it to talk to you again. 

## Installation

The easiest way to install this app is by adding the corresponding Snips app to your assistant in the [Snips Console](https://console.snips.ai):

*   English: [Keep quiet](https://console.snips.ai/store/en/skill_134O6Yb4K6b)
*   French: [Mode silencieux](https://console.snips.ai/store/fr/skill_8lyE0KYQ1zr)
*   German: [Auszeit!](https://console.snips.ai/store/de/skill_zmmENzQnqaQ)

To be able to use this app, you need Snips 1.1.2 (0.62.3).

For disabling and enabling intents, the `snips-injection` service should be running, because the names of the installed intents are injected in the vocabulary of Snips.

## Usage

This app recognizes the following intents:

*   DisableIntent - You ask your assistant to disable an intent.
*   EnableIntent - You ask your assistant to enable an intent.
*   Quiet - You ask your assistant to stop replying to your voice commands. 
*   Talk - You ask your assistant to talk again. 

## Copyright

This app is provided by [Koen Vervloesem](mailto:koen@vervloesem.eu) as open source software. See LICENSE for more information.
