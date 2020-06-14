# Digimon World Randomizer
##### Digimon World 1 (PSX) data randomizer.  Create a unique, brand new experience for the classic game!

To use, open settings.ini and adjust all settings according to preference.  In `[general]`, set `Input` as the relative path to your Digimon World `.bin` file, then set `Output` to the filename where you would like the modified `.bin` file to be placed.

i.e. if your DW binary file is called `Digimon World.bin` and is in the same folder as `digimon_randomize.exe` or `digimon_randomize.py`:
`Input = Digimon World.bin`
`Output = Digimon World Rando.bin`

###### Note:  For most sections of the settings file, there is an `Enabled` field that must be set to yes before any of the other options will be used.
&nbsp;
After you have the settings you want, run `digimon_randomize.py` or `digimon_randomize.exe`.  The random seed will be printed out to the console. If you did not manually set a seed via `Seed`, one will be randomly generated.
See race instructions below for creating identical race ROMs.

##### Steps for first time setup:
1. Download the latest release of `digimon_randomizer.zip`
2. Unzip to wherever
3. Open `settings.ini` and fill out the file paths for `Input` and `Output`
    * Paths can be absolute or relative, and should point to the `.bin` file
4. Change the other settings to your liking
5. Run `digimon_randomize.exe`
6. Load the `.bin` file at the `Output` location into your emulator of choice

##### Recommended race setup:
1. Follow 1-4 above
2. Set `LogLevel` to `race`
3. Set the seed to any number, or simply run the randomizer and copy the random seed produced
4. Once `Seed` in `settings.ini` is set to the value you want, send your `settings.ini` file to your race opponents
5. All race participants should update `Input`/`Output` in `settings.ini` to their own paths
6. All race participants should run `digimon_randomize.exe`
7. If everyone's settings matched, including the seed, an identical ROM will be produced for everyone.


### Version log:

##### Release 1.1.1
###### Bug Fixes
    - Fix random seed crashing the script
    - Fix log file not having seed in name when it was random

##### Release 1.1.0
###### New Features
    - Complete re-design of the GUI
        -- Tabbed view to allow far more room for adding new features
        -- Tie all data directly into UI for easier expansion
    - Integrate all of Syd's features from the forked branch
        -- Fix softlocks patches
        -- Fix PP calculation 
        -- Unlock Toy Town as part of "Unlock Areas" patch
        -- Various other fixes
    - Options to allow starter to be any level (fresh to ultimate)
    - Option to specify exact starting digimon
    - Make race/casual always produce different results for same seed
    - Include seed value in log file filename

###### Bug Fixes
    - Too many to try to list here -- mostly patch improvement and UI improvement.  Stability significantly up

##### Release 1.0.0
###### New Features
    - Graphical User Interface
        -- Select files, save, load and edit settings with an easy-to-use graphical interface.  No more manual `ini` file editing!
    - Patch to insert a hash of the configured settings into the Jijimon intro dialogue (for verifying race integrity)
    - Patch to skip the majority of the introductory dialogue ("Welcome to Digimon World" etc)
    - Patch to unrig bonus try training -- the slots will no longer force you to lose most of the time.  They are
                                           now entirely based on skill: no RNG at all.
    - Patch to remove the virus/vaccine type locks on Greylord's Mansion and Ice Sanctuary.
    - Additionally randomize the following special evolutions:
        -- Airdramon
        -- Ninjamon
        -- Monochromon
        -- Kunemon
        -- Coelamon
        -- Nanimon
        -- Vademon
        -- Sukamon
        -- NOT Numemon (for the sake of preserving the Toy Town access)
    - Increase tech learn chance patch now applies to brain training as well
        
###### Bug Fixes
    - Fixed certain enemy digimon drop rates being lower than intended
    - Fixed PP calculation with random recruits.  PP will now match that of the received recruit, rather than the one you spoke to/fought.


##### Public Beta 0.8.2
###### Bug Fixes
    - Fixed hardware crash caused by invalid targeting during confusion status.
    

##### Public Beta 0.8.1
###### New Features
    - Configurable option to change spawn rate of Mamemon, Piximon, MetalMamemon, and Otamamon to a specific value.

###### Bug Fixes
    - Recruitment messages should now properly match random recruit.
    - Counter will never be assigned as the starting tech


##### Public Beta 0.8.0
###### New Features
    - When random recruitment is enabled, change the "Xmon joins the city!" message to reflect 
      the random recruitment.


##### Public Beta 0.7.2
###### Bug Fixes
    - Randomly recruited digimon will now consistently appear in town (and the "actual" recruits will not show up)
    - All map item spawns now randomized (a handful were missed initially)
    - Whamon recruit can no longer be swapped to a Factorial Town digimon
    - Devimon will gain stats when randomly assigned to a natural evolution (requires random evolutions and random special evolutions)
    - Logging for random recruitment no longer inverted


##### Public Beta 0.7.1
###### New Features
    - Patch to fix the Giromon/jukebox glitch
    - Improve random recruitment logging (log now tells what each recruit should give you)

###### Bug Fixes
    - Getting Ogremon early in random recruits will no longer break the Drimogemon fight
    - Seadramon will now properly be able to teach 3 random techs (when enabled)
    - Devimon is now an option for natural evolution when random requirements is enabled
    - Properly use 2nd starter starting stats when 2nd starter is assigned


##### Public Beta 0.7.0
###### New Features
    - random mode for tech data -- instead of just shuffling the existing values, generates true
                                   random values.  Power ranges from 30% below vanilla lowest to
                                   30% above vanilla highest (cap 999).  MP cost ranges from 10%
                                   to 140% of power value.  This means less complete garbage
                                   moves while still having the occasional amazing move.
    - randomize evolution requirements

###### Bug Fixes
    - Random special evolutions can now correctly include Panjyamon, MetalEtemon, and Gigadramon
    - Seed is now printed out at the end of the log
    - Fix text color glitch


##### Public Beta 0.6.0
###### New Features
    - ObtainAll option for random evolutions is finally supported.  
      Enabling this ensures that all natural evolution digimon are still 
      obtainable through natural evolution after the evolutions are randomized.
    - patch to increase battle learn chance for techs

###### Bug Fixes
    - Toy Town can now properly be opened by the digimon the suit evolves to (when special
      evolutions are randomized)
    - Ninjamon will no longer continue to fight forever if random recruits is enabled.  Also
      prevents the eternal battle with ghost Ninjamon.


##### Public Beta 0.5.0
###### New Features
    - randomize recruitments (recruit A, B joins your town)
        -- All recruitments except: Agumon, Airdramon, MetalGreymon, Palmon, Vegiemon,
                                    Greymon, Birdramon, Centarumon, Angemon, Monzaemon
        -- This feature is largely untested and has lots of bugs, probably.  You may
           want to leave it off for now.
    - randomize the following special evolutions:
        -- Monzaemon (and match the Toy Town trigger to the new one)
        -- MetalMamemon
        -- Giromon
        -- Bakemon
        -- Devimon
        -- Phoenixmon
        -- SkullGreymon
        -- Triggers remain the same, just the resulting digimon is changed
    - customizable high/low price cutoff for map items and enemy drops
    - patch brain training to allow learning first tier move if you do not have it.  40% chance

###### Bug Fixes
    - Moon Mirror and Electro Ring will no longer be randomized in (gamebreaking)
    - Starter will never randomize to itself (Agumon will never become Agumon)
    - Alternate Dynamite Kick and Horizontal Kick will be randomized as they should
    - Self targeting moves like War Cry will never be assigned a status effect


##### Public Beta 0.4.0
    *Cleanup for first public release!


##### Closed Beta 0.3.1
###### Bug Fixes
    - Quests items will no longer appear in chests when the randomizer is run twice on the same file


##### Closed Beta 0.3.0
###### New Features
    - randomize techs taught by Seadramon + Beetle Land
    - randomize tech data
        -- random power option
        -- random MP cost option
        -- random accuracy option
        -- random effect option
        -- random effect chance option
    - patch evo items to give stats/lifetime
    - patch to make quest items dropable


##### Closed Beta 0.2.0
###### New Features
    - randomize digimon data
        -- random drop item option
        -- random drop rate option


##### Closed Beta 0.1.1
###### Bug Fixes
    - exclude myotismon steak from randomizing (breaks that quest if not)


##### Closed Beta 0.1.0
###### New Features
    - random rookie starter
        -- random or weakest tech option
    - random chest items
        -- evo item ban option
    - random Tokomon items
        -- consumable only option
    - random map spawn items
        -- food replaces other food option
    - random evolutions