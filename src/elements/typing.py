"""
Copyright 2021 Janrey "CodexLink" Licas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import NewType as _N

ActivityDictName = _N("ActivityDictName", str)
BadgeElements = _N("BadgeElements", str)
BadgeStructure = _N("BadgeStructure", str)
Base64Bytes = _N("Base64Bytes", bytes)
Base64String = _N("Base64String", str)
ColorHEX = _N("ColorHEX", str)
HttpsURL = _N("HttpsURL", str)
RegExp = _N("RegExp", str)
READMERawContent = _N("READMERawContent", bytes)
READMEContent = _N("READMEContent", str)
READMEIntegritySHA = _N("READMEIntegritySHA", str)
