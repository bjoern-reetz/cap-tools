## v2.1.0 (2024-05-13)

### Feat

- **cap_tools.models.Info**: add get_language and set_language methods

## v2.0.0 (2024-05-11)

### BREAKING CHANGE

- It is very unlikely that this change will affect you. This default value is only relevant when using the Python API to create Alerts, where it now throws an error when omitting a value.

### Refactor

- remove default="" from value attributes of ValueName and Value

## v1.1.0 (2024-05-11)

### Feat

- remove kw_only=True from dataclasses with 2 or less attributes

## v1.0.0 (2024-05-09)
