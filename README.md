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

Public Beta 0.8.0
@New Features
    *When random recruitment is enabled, change the "Xmon joins the city!" message
     to reflect the random recruitment.

Public Beta 0.7.2
@Bug Fixes
    *Randomly recruited digimon will now consistently appear in town (and the "actual"
     recruits will not show up)
    *All map item spawns now randomized (a handful were missed initially)
    *Whamon recruit can no longer be swapped to a Factorial Town digimon
    *Devimon will gain stats when randomly assigned to a natural evolution (requires
     random evolutions and random special evolutions)
    *Logging for random recruitment no longer inverted


Public Beta 0.7.1
@New Features
    *Patch to fix the Giromon/jukebox glitch
    *Improve random recruitment logging (log now tells what each recruit should give you)

@Bug Fixes
    *Getting Ogremon early in random recruits will no longer break the Drimogemon fight
    *Seadramon will now properly be able to teach 3 random techs (when enabled)
    *Devimon is now an option for natural evolution when random requirements is enabled
    *Properly use 2nd starter starting stats when 2nd starter is assigned


Public Beta 0.7.0
@New Features
    *random mode for tech data -- instead of just shuffling the existing values, generates true
                                  random values.  Power ranges from 30% below vanilla lowest to
                                  30% above vanilla highest (cap 999).  MP cost ranges from 10%
                                  to 140% of power value.  This means less complete garbage
                                  moves while still having the occasional amazing move.
    *randomize evolution requirements

@Bug Fixes
    *Random special evolutions can now correctly include Panjyamon, MetalEtemon, and Gigadramon
    *Seed is now printed out at the end of the log
    *Fix text color glitch


Public Beta 0.6.0
@New Features
    *ObtainAll option for random evolutions is finally supported.  Enabling this ensures that
     all natural evolution digimon are still obtainable through natural evolution after the
     evolutions are randomized.
    *patch to increase battle learn chance for techs

@Bug Fixes
    *Toy Town can now properly be opened by the digimon the suit evolves to (when special
     evolutions are randomized)
    *Ninjamon will no longer continue to fight forever if random recruits is enabled.  Also
     prevents the eternal battle with ghost Ninjamon.


Public Beta 0.5.0
@New Features
    *randomize recruitments (recruit A, B joins your town)
        --All recruitments except: Agumon, Airdramon, MetalGreymon, Palmon, Vegiemon,
                                   Greymon, Birdramon, Centarumon, Angemon, Monzaemon
        --This feature is largely untested and has lots of bugs, probably.  You may
          want to leave it off for now.
    *randomize the following special evolutions:
        --Monzaemon (and match the Toy Town trigger to the new one)
        --MetalMamemon
        --Giromon
        --Bakemon
        --Devimon
        --Phoenixmon
        --SkullGreymon
        --Triggers remain the same, just the resulting digimon is changed
    *customizable high/low price cutoff for map items and enemy drops
    *patch brain training to allow learning first tier move if you do not have it.  40% chance

@Bug Fixes
    *Moon Mirror and Electro Ring will no longer be randomized in (gamebreaking)
    *Starter will never randomize to itself (Agumon will never become Agumon)
    *Alternate Dynamite Kick and Horizontal Kick will be randomized as they should
    *Self targeting moves like War Cry will never be assigned a status effect


Public Beta 0.4.0
    *Cleanup for first public release!


Closed Beta 0.3.1
@Bug Fixes
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
@Bug Fixes
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