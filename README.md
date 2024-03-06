# ODPy

![Banner](images/image.png "OpenDoctoratePy")

- ~~It's a pity that DoctoratePy is no longer maintained. Therefore, this repo aims to continue the support of this project for newer versions of the game.~~

- Python server implementation of a certain anime tower defense game. This repo is for the CN TapTap Version.

- This project is for educational purposes only. Do not sell this or I will eat your liver.
	- [Discord Server](https://discord.com/invite/SmuB88RR5W)

- That guy from Reddit is wrong. You need a brain to run this.

- Please don't make unauthorized redistribution.
    - I really mean it. It is not funny and could lead me into unnecessary legal troubles.

## Prerequisities

- [PowerShell](https://github.com/PowerShell/PowerShell/releases/) (Required.)
- [Scoop](https://scoop.sh/) and/or [WinGet](https://github.com/microsoft/winget-cli). (Not required but highly recommended.)
    - **[Python](https://www.python.org/) 3.12 or above. (Must be installed to $PATH)**
        - **[UV](https://github.com/astral-sh/uv) [REQUIRED].**
    - [Nushell](https://github.com/nushell/nushell). (Required.)
    - ***A functional text editor or an IDE, like ([VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/)/ Et cetera.) (Not required but highly recommended.)***
    - **[Git](https://git-scm.com/). (Preferrably latest.) (Required to use the update script.)**

## How to apply update

- First of all, acquire the `.patch` file, once you have it, you can use the following command:

```nu
    git apply /path/to/some-changes.patch
```

- Then run:

```nu
    nu update.nu
```

## Currently tested emulator to be working

- MuMu Player X / MuMu Player 12 (**Recommended**)

- ~~LDPlayer9~~ (Deprecated.) (***If you use this, you are on your own.***)

## Usage guide

- **The guide will assume you have setup all the prerequisities softwares.**

### MuMu Player X (aka MuMu Player 12)

- *[System Requirements](https://www.mumuglobal.com/faq/system-requirement-mumu-player-x.html)*

- **[Download](https://a11.gdl.netease.com/MuMuInstaller_12.0.0.6_12beta-gw-offline_all_1666787400.exe)**

    - Enable root permission in MuMu Player's settings (ADB connection should be enabled by default, therefore no need to enable it manually).
    - Start MuMu Player X (aka MuMu Player 12).
    - Run `setup.bat`, and success can be indicated from `Press enter to exit...`. (Only required for the first time.)
    - Run `start.bat`.

### In-game

- **By default you can use any usernames and passwords to login.**

## Changing Contengency Contract Battleplan Season

- Change the value of key `selectedCrisisV2` in `config\config.json` to whatever you want. The available seasons are under `data\crisisV2`.

- Currently the only way to play old CC seasons is to rollback your Arknights game installation to an older version.

## Customizing indivual operators level, potentials, skill ranks and others

- Customize each operator indivually by adding new info in `customUnitInfo` key in `config\config.json`. You can find <char_id> from [here](https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json). By default, all characters will have max level, max potentials, max mastery.

    - `favorPoint` - Trust points (25570 is 200% Trust) [link to exact point to %](https://gamepress.gg/arknights/core-gameplay/arknights-guide-operator-trust)
    - `mainSkillLvl` - Skill Rank (Put Masteries at 0 if this is lower than 7)
    - `potentialRank` - Potential Rank
        - `0 ~ 5`
    - `evolvePhase` - Promotion

        ```txt
        0 -> E0
        1 -> E1
        2 -> E2
        ```

    - `skills` - Mastery level for each skill starting from S1.

```json
"<char_id>": {
    "favorPoint": 25570,
    "mainSkillLvl": 7,
    "potentialRank": 2,
    "level": 50,
    "evolvePhase": 1,
    "skills": [1, 0]
}
```

## Duplicating characters

- Duplicating characters. Just add the [Character ID](https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json) to key `duplicateUnits` in `config\config.json`.

```json
"duplicateUnits": [
    "char_4064_mlynar",
    "char_4064_mlynar",
    "char_350_surtr",
    "char_350_surtr",
    "char_350_surtr"
]
```

## Customizing support unit

- Customize the support unit list by changing the unit info in `assistUnit` key in `config\config.json`. All characters info can be found [here](https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json).

	- `charId` - key of the character
	- `skinId` - skinId of the character (Skin list can be found [here](https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/skin_table.json))
	- `skillIndex` - Skill Index of the support unit (Index starts from 0).

<u>Note:</u> Characters stats and skill masteries are based on the above parameters.

```json
	{
		"charId": "char_350_surtr",
		"skinId": "char_350_surtr@it#1",
		"skillIndex": 2
	}
```

## TODO

- [ ] Add Gacha
