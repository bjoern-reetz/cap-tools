## v2.3.0 (2024-05-14)

### Feat

- **cap_tools.models.Info**: add parameters_to_dict and parameters_from_dict methods
- **cap_tools.models.Info**: add event_codes_to_dict and event_codes_from_dict methods
- **cap_tools.models.Area**: add geocode_to_dict and geocode_from_dict methods

### Refactor

- **tests**: move quick tests to dedicated module

## v2.2.0 (2024-05-14)

### Feat

- **cap_tools.models.Area**: add geocodes_to_dict and geocodes_from_dict methods

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
