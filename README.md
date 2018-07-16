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




Version log:

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