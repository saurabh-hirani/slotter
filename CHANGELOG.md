## CHANGELOG

### v0.0.1

- First cut

### v0.0.2

- Bumping up the version to verify if package can be uploaded to pypi
- No logic changes

### v0.0.3

- Breaking change - items should be tuples instead of single values.
- Instead of s.add_item(5) do s.add_item('x', 5) because the user needs to refer a name against a slot.
