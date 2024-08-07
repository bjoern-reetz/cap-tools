## v3.1.1 (2024-08-04)

### Fix

- **pyproject.toml**: improve project metadata

## v3.1.0 (2024-07-21)

### Feat

- **cap_tools.AlertState**: add new class AlertState
- **cap_tools.Reference**: add from_alert static method

### Refactor

- **tests**: refactor Hypothesis strategies, introducing strategies for Alert and Info

## v3.0.0 (2024-07-20)

### BREAKING CHANGE

- Alert.references_to_list and Alert.references_from_list now return/receive list[Reference] instead of list[str].
- The capability of uting keyword-arguments was removed.

### Feat

- **cap_tools**: introduce Reference NamedTuple

### Refactor

- **utils**: change split_and_remove_quotes and join_and_maybe_add_quotes to accept positional arguments only

## v2.5.1 (2024-05-29)

### Fix

- **cap_tools.models**: replace wrong type annotation MultiDict[str, str] -> MultiDict[str]

### Refactor

- **cap_tools**: add py.typed
- **tests**: add type hints for tests

## v2.5.0 (2024-05-27)

### Feat

- **cap_tools.models.Alert**: add *_to_list() and *_from_list() methods to split/join group listings

## v2.4.0 (2024-05-26)

### Feat

- **cap_tools.models**: *_to_dict() now return MultiDict, *_from_dict() now accept Mapping

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
