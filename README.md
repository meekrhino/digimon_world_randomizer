# digimon_world_randomizer
Digimon World 1 (PS1) data randomizer.  Create a unique, brand new experience for the classic game!

To use, open settings.ini and adjust all settings according to preference.  In [general], set Input as the relative path to your Digimon World .bin file, then set Output to the filename where you would like the modified .bin file to be placed.

i.e. if your DW binary file is called Digimon World.bin and is in the same folder as digimon_randomize.exe or digimon_randomize.py:
Input = Digimon World.bin
Output = Digimon World Rando.bin

Note:
For most sections of the settings file, there is an "Enabled" field that must be set to yes before any of the other options will be used.

After you have the settings you want, run digimon_randomize.py or digimon_randomize.exe.  The seed used (whether you set it manually or left it blank) will be printed out to the console.
If you are doing a race, have your racing opponent(s) put that seed value in their settings.ini file (and make sure they have the same settings selected!)

Steps to settings this up for the first time:
    1. Download the latest release of digimon_randomizer.zip
    2. Unzip to wherever
    3. Open "settings.ini" and fill out the file paths for "Input" and "Output"
        *Paths can be absolute or relative, and should point to the .bin file
    4. Change the other settings to your liking
    5. Run "digimon_randomize.exe"
    6. Load the .bin file at the "Output" location into your emulator

Recommended steps to setting up a race:
    1. Follow 1-4 above
    2. Set "LogLevel" to "race"
    3. Set the seed to any number, or simply run the randomizer and copy the random seed produced
    4. Once "Seed" in "settings.ini" is set to the value you want, send your "settings.ini" file to your race opponents
    5. All race participants should update "Input"/"Output" in "settings.ini" to their own paths
    6. All race participants should run "digimon_randomize.exe"
    7. If everyone's settings matched, including the seed, an identical ROM will be produced for everyone.


Version log:

Public Beta 0.4.0
    *Cleanup for first public release!

Closed Beta 0.3.1
@Bug fixes
    *Quests items will no longer appear in chests when the randomizer is run twice on the same file

Closed Beta 0.3.0
@New Features
    *randomize techs taught by Seadramon + Beetle Land
    *randomize tech data
        --random power option
        --random MP cost option
        --random accuracy option
        --random effect option
        --random effect chance option
    *patch evo items to give stats/lifetime
    *patch to make quest items dropable

Closed Beta 0.2.0
@New Features
    *randomize digimon data
        --random drop item option
        --random drop rate option

Closed Beta 0.1.1
@Bug fixes
    *exclude myotismon steak from randomizing (breaks that quest if not)

Closed Beta 0.1.0
@New Features
    *random rookie starter
        --random or weakest tech option
    *random chest items
        --evo item ban option
    *random Tokomon items
        --consumable only option
    *random map spawn items
        --food replaces other food option
    *random evolutions