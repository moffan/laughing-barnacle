# MoFF FM alfa scout zero

## Create custom roles

Create a `settings` folder and create a `json` file for each role with the following format.

```json
{
  "Attribute name": "weight value"
}
```

### Example:

For a `"Imported full back - support"` create a file named `inverted-fullback-support.json`

```json
{
  "Corners": "0",
  "Crossing": "0",
  "Dribbling": "0",
  "Finishing": "0",
  "First Touch": "0",
  "Free Kick Taking": "0",
  "Heading": "0",
  "Long Shots": "0",
  "Long Throws": "0",
  "Marking": "0",
  "Passing": "0",
  "Penalty Taking": "0",
  "Tackling": "0",
  "Technique": "0",

  "Aggression": "0",
  "Anticipation": "0",
  "Bravery": "0",
  "Composure": "0",
  "Concentration": "0",
  "Decisions": "0",
  "Determination": "0",
  "Flair": "0",
  "Leadership": "0",
  "Off The Ball": "0",
  "Positioning": "0",
  "Teamwork": "0",
  "Vision": "0",
  "Work Rate": "0",

  "Acceleration": "0",
  "Agility": "0",
  "Balance": "0",
  "Jumping Reach": "0",
  "Natural Fitness": "0",
  "Pace": "0",
  "Stamina": "0",
  "Strength": "0"
}
```

> Note! the name of the attributes must match the names in game and the attribute names in the exports.

## Python

This was made with `Python@3.12`

### Pip

```bash
## install package and add to "requirements"
pip install SomePackage
pip freeze > requirements.txt

## Restore packages from "requirements.txt"
pip install -r requirements.txt

```

### Distribution

```bash
pyinstaller --onefile ./alfa_scout_zero
```
