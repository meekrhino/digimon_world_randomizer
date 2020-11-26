import { InputVariation, SectionElement } from "./ElementContainer"
import * as Main from "./MainModel"

/* Levels */
export enum Level {
    Fresh = 1,
    InTraining,   
    Rookie,     
    Champion,
    Ultimate,
}

/* Digimon Names */
export const digimonNames = [
    "Botamon",
    "Koromon",
    "Agumon",
    "Betamon",
    "Greymon",
    "Devimon",
    "Airdramon",
    "Tyrannomon",
    "Meramon",
    "Seadramon",
    "Numemon",
    "MetalGreymon",
    "Mamemon",
    "Monzaemon",
    "Punimon",
    "Tsunomon",
    "Gabumon",
    "Elecmon",
    "Kabuterimon",
    "Angemon",
    "Birdramon",
    "Garurumon",
    "Frigimon",
    "Whamon",
    "Vegiemon",
    "SkullGreymon",
    "MetalMamemon",
    "Vademon",
    "Poyomon",
    "Tokomon",
    "Patamon",
    "Kunemon",
    "Unimon",
    "Ogremon",
    "Shellmon",
    "Centarumon",
    "Bakemon",
    "Drimogemon",
    "Sukamon",
    "Andromon",
    "Giromon",
    "Etemon",
    "Yuramon",
    "Tanemon",
    "Biyomon",
    "Palmon",
    "Monochromon",
    "Leomon",
    "Coelamon",
    "Kokatorimon",
    "Kuwagamon",
    "Mojyamon",
    "Nanimon",
    "Megadramon",
    "Piximon",
    "Digitamamon",
    "Penguinmon",
    "Ninjamon",
    "Phoenixmon",
    "H-Kabuterimon",
    "MegaSeadramon",
    "WereGarurumon",
    "Panjyamon",
    "Gigadramon",
    "MetalEtemon",
]

/* Starter */
export const starterTooltip: string = 
   `Enable starter randomization.  This will select two random rookies to replace
    the starting partner digimon, Agumon and Gabumon.  They will each be assigned 
    a random starting tech from the new starter's pool of learnable techniques.`

export const starterElements: SectionElement<Main.StarterSettings>[] = [
  { attribute: "UseWeakestTech",
    inputType: InputVariation.Checkbox,
    label: "Use Weakest Tech",
    tooltip: 
       `When this is enabled, the randomized starter will receive
        the lowest tier damaging move that it can use.  NOTE: this
        does not mean the WEAKEST tech, it means the first tech you
        would learn from brain training (e.g. Spit Fire, Tear Drop).` },
  { attribute: "Digimon",
    inputType: InputVariation.Dropdown,
    dropdownPlaceholder: "Select Starter Digimon",
    dropdownOptions: [ "Random" ].concat( digimonNames ),
    tooltip: 
       `Set starter digimon.  Leave unchanged or select "Random"
        to randomize from the selected levels.  This will only
        set the DAY starter -- the NIGHT starter will be 
        randomized according to other selections.` },
  { attribute: "Fresh",
    inputType: InputVariation.Checkbox,
    label: "Include Fresh",
    tooltip: 
       `Include Fresh digimon in starter options.  If no
        options are selected, only rookies will be included.` },
  { attribute: "InTraining",
    inputType: InputVariation.Checkbox,
    label: "Include In-Training",
    tooltip: 
       `Include In-Training digimon in starter options.  If no
        options are selected, only rookies will be included.` },
  { attribute: "Rookie",
    inputType: InputVariation.Checkbox,
    label: "Include Rookie",
    tooltip: 
       `Include Rookie digimon in starter options.  If no
        options are selected, only rookies will be included.` },
  { attribute: "Champion",
    inputType: InputVariation.Checkbox,
    label: "Include Champion",
    tooltip: 
       `Include Champion digimon in starter options.  If no
        options are selected, only rookies will be included.` },
  { attribute: "Ultimate",
    inputType: InputVariation.Checkbox,
    label: "Include Ultimate",
    tooltip: 
       `Include Ultimate digimon in starter options.  If no
        options are selected, only rookies will be included.` }
]

/* Digimon Data */
export const digimonDataTooltip = "Enable digimon data randomization."

export const digimomDataElements: SectionElement<Main.DigimonSettings>[] = [ 
  { attribute: "DroppedItem",
    inputType: InputVariation.Checkbox,
    label: "Item Dropped",
    tooltip: 
       `Randomize the item dropped by a digimon when it is 
        defeated.  Uses the "valuable item threshold" to 
        exchange vanilla dropped items for similar-value 
        random items` },
  { attribute: "DropRate",
    inputType: InputVariation.Checkbox,
    label: "Drop Rate",
    tooltip: 
       `Randomize the chance that an enemy will drop an item. 
        Tends to prefer small changes from vanilla values, but
        will sometimes become much more frequent.  100% drop
        rates will remain 100%` },
  { attribute: "MatchValue",
    inputType: InputVariation.Checkbox,
    label: "Match Valuable Drops",
    tooltip: 
       `Randomize valuable drops to different valuable drops and
        lower value drops to similar value.` },
  { attribute: "ValuableItemCutoff",
    inputType: InputVariation.Slider,
    minVal: Main.ItemValueMin,
    maxVal: Main.ItemValueMax,
    tooltip: 
       `Set the threshold value for the cutoff between high and
        and low value items.  Maximum and minimum vlues for this
        field will behave the same as disabling this option.` }
]

/* Tech Data */
export const techDataTooltip = "Enable technique data randomization."

export const techDataElements: SectionElement<Main.TechSettings>[] = [ 
  { attribute: "RandomizationMode",
    inputType: InputVariation.Multiselect,
    label: "Randomization Mode",
    multiSelect: [ "shuffle", "random" ],
    multiSelectLabel: [ "Shuffle", "Random" ],
    tooltip: 
       `Mode of randomization for technique data.  In general, 
        "Shuffle" keeps the vanilla values and shuffles them around.
        Meanwhile, "Random" generates all-new random values.  Hover
        individual features to see how these options affect them.` },
  { attribute: "Power",
    inputType: InputVariation.Checkbox,
    label: "Power",
    tooltip: 
       `Randomize the power of each tech.  When mode is "Shuffle", 
        the power of all techs will be shuffled amongst themselves.  
        When mode is "Random", techs will be assigned a random power
        ranging from 30% below the weakest vanilla tech and 999,
        the max possible value.` },
  { attribute: "Cost",
    inputType: InputVariation.Checkbox,
    label: "MP Cost",
    tooltip: 
       `Randomize the MP cost of each tech.  When mode is "Shuffle",
        the mp cost of all techs will be shuffled amongst themselves.
        When mode is "Random", techs will be assigned a random cost
        calculated from the power of the tech, ranging from 10% to 140% 
        of the power.` },
  { attribute: "Accuracy",
    inputType: InputVariation.Checkbox,
    label: "Accuracy",
    tooltip: 
       `Randomize the accuracy of each tech.  When mode is "Shuffle",
        the accuracy of all techs will be shuffled amongst themselves.
        When mode is "Random", techs will be assigned a random accuracy
        ranging from 33 to 100. The vast majority will fall between 
        50 and 100, with just over 10% being 100% and just under 10%
        being under 50.` },
  { attribute: "Effect",
    inputType: InputVariation.Checkbox,
    label: "Status Effect",
    tooltip: 
       `Randomize the status effect of each tech.  This will make about
        50% off all techniques have some status effect, and they
        will be roughly evenly distributed between Flat, Poison, 
        Confusion, and Stun.  This option is not affect by the mode.` },
  { attribute: "EffectChance",
    inputType: InputVariation.Checkbox,
    label: "Status Effect Chance",
    tooltip: 
       `Randomize the chance of a status effect being inflicted for
        each tech.  Techs will be assigned a random value between 
        1% and 70%.  This option is not affected by the mode.` },
  { attribute: "TypeEffectiveness",
    inputType: InputVariation.Checkbox,
    label: "Type Effectiveness",
    tooltip: `Randomizes the type effectiveness of different attributes.
              The values will be between 2 and 20, as in vanilla.`}
]

/* Evolution */
export const evolutionTooltip =
   `Enable digivolution tree randomization.  Randomizes which digimon each
    digimon can randomize into.  Each fresh will get 1 target, each in-training
    will get 2 targets, each rookie gets 4-6 targets, and each champion
    gets 1-2 targets.  Unless "Obtain All" is set, not all playable digimon
    are guaranteed to be obtainable through natural digivolution.`

export const evolutionElements: SectionElement<Main.EvolutionSettings>[] = [ {
    attribute: "Requirements",
    inputType: InputVariation.Checkbox,
    label: "Requirements",
    tooltip: 
       `Randomize the requiremnts to digivolve to each digimon.
        Requirements will generally look fairly similar to vanilla
        values, but totally random.  All digimon will have a stat
        requirement, a care mistake required (min or max), a 
        weight requirement (within 5 of), and a techs learned requirement.
        Digimon may randomly have other bonus requirements, including
        max/min battles fought, discipline, and happiness.` },
  { attribute: "SpecialEvolutions",
    inputType: InputVariation.Checkbox,
    label: "Special Digivolutions",
    tooltip: 
       `Randomize the result of some special evolutions.  Specifically,
        this currently includes death digivolutions (such as Bakemon and
        Devimon), MetalMamemon's "upgrade" digivolutions, and the Toy Town
        Monzemon suit.  To preserve completion, Toy Town will be accessible
        by whatever the suit digivolves Numemon into, rather than by
        Monzaemon.` },
  { attribute: "ObtainAllMode",
    inputType: InputVariation.Checkbox,
    label: "Obtain All",
    tooltip: 
       `When this option is enabled, randomized evolutions are guaranteed
        to be organized in such a way that all natural evolution digimon
        can still be obtained naturally through evolution.  That means
        each in-training, rookie, champion, and ultimate level digimon
        will have at least one digimon in the previous level that can
        naturally digivolve to it.` }
]

/* Chests */
export const chestsTooltip = 
   `Enable item chest contents randomization.  This will randomize the item
    contained in each of the "computers".  Any item except digivolution items or
    quest items can be randomized into chests.  Quest items include, for example,
    the Mansion Key, the Gear, and the stone for the Leomon quest.`

export const chestsElements: SectionElement<Main.ChestSettings>[] = [ 
  { attribute: "AllowEvolutionItems",
    inputType: InputVariation.Checkbox,
    label: "Digivolution Items",
    tooltip: 
       `When this is enabled, digivolution items will be included in the
        availalbe pool of items to be randomized into chests.` }
]

/* Tokomon */
export const tokomonTooltip = 
   `Randomize the items given by Tokomon at the start of the game.  This will by
    default include only consumable, non-quest items.  It also does not include
    digivolution items.  Tokomon will give 1-3 copies of 6 different items chosen
    at random, with less valuable items being more likely to come in larger quantities.`

export const tokomonElements: SectionElement<Main.TokomonSettings>[] = [ 
  { attribute: "ConsumableOnly",
    inputType: InputVariation.Checkbox,
    label: "Consumable Only",
    tooltip: 
       `When this is enabled, only consumable items will be given.  This
        disallows items like Enemy Repel, Training Manual, and similar.` }
]

/* Map Items */
export const mapItemTooltip =
   `Randomize items that spawn on maps (such as Digimushrooms).  Only non-quest 
    consumable items will be selected.  Does not allow digivolution items to spawn.
    Uses the "valuable item threshhold" to exchange vanilla map items for similar-
    value random items.  This helps preserve common items being typically less
    valuable than rare items.  This setting affects the items that spawn in 
    Centarumon's maze.`

export const mapItemElements: SectionElement<Main.MapItemSettings>[] = [ 
  { attribute: "FoodOnly",
    inputType: InputVariation.Checkbox,
    label: "Food Items Only",
    tooltip: 
       `Locks the randomly spawned items to be food only.  This will
        only affect map spawns that are food in vanilla; thus,
        the weird spawns in Centarumon's maze will not be forced to
        be food with this setting.` },
  { attribute: "MatchValue",
    inputType: InputVariation.Checkbox,
    label: "Match Rare Spawns",
    tooltip: 
       `Randomize valuable spawns to different valuable drops and
        lower value drops to similar value.  Helps preserve rare
        item spawns being generally more valuable than common ones.` },
  { attribute: "ValuableItemCutoff",
    inputType: InputVariation.Slider,
    minVal: Main.ItemValueMin,
    maxVal: Main.ItemValueMax,
    tooltip: 
       `Set the threshold value for the cutoff between high and
        and low value items.  Maximum and minimum vlues for this
        field will behave the same as disabling this option.
        Default value is 1000 -- this value seems to work most
        effectively for preserving the rare/common split.` }
]

/* Recruitment */
export const recruitTooltip = 
   `Enable recruitment randomization.  Randomizes which recruit shows up in 
    town when you recruit one.  For example, it is possible to have Whamon 
    show up in town (thus opening the dock to Factorial Town) when Bakemon is
    recruited.  WARNING: poor luck can currently create a seed that cannot be 
    completed for 100PP!!  The following recruits are not randomized, but will 
    be supported later:  Palmon, Vegiemon, Greymon, Birdramon, Centarumon, Angemon, 
    and Monzaemon.  The following cannot be randomized:  Agumon, Airdramon, and
    MetalGreymon.`

/* Tech Gifts */
export const techGiftTooltip = 
   `Randomize the three techniques that Seadramon can teach you, as well
    the one that can be taught in Beetle Land (Bug, in vanilla).  They will
    still only be able to teach you a move that your current digimon can
    learn, so if you cannot learn the move then nothing will happen.  
    Seadramon will teach his three techs in order, so if you already know the
    first you will get the second, and so on.  If you know all three already,
    he will teach you nothing.`

/* Patches */
export const patchTooltip = "Various patches to improve different aspects of the game."

export const patchElements: SectionElement<Main.PatchSettings>[] = [ 
  { attribute: "EvoItemStatGain",
    inputType: InputVariation.Checkbox,
    label: "Item Stat Gain",
    tooltip: 
       `Enable this to cause digivolution items to actually grant
            stats upon digivolution.  In vanilla, digivolving does not
            grant any stats gain when it happens through an item.` },
  { attribute: "QuestItemsDroppable",
    inputType: InputVariation.Checkbox,
    label: "Drop Quest Items",
    tooltip: 
       `Enable this to allow dropping quest items (like the Mansion
        Key) from your inventory.  In vanilla, these items cannot be dropped
        and must be deposited in the bank to get them out of your inventory.` },
  { attribute: "BrainTrainTierOne",
    inputType: InputVariation.Checkbox,
    label: "Brain Train Learning",
    tooltip: 
       `Enable this to fix the bug in vanilla that prevents learning
        the lowest tier move for each specialty via brain training.  For 
        example, in vanilla it is impossible to learn Spit Fire via brain
        training.  This patch makes that possible and assigns the tier
        one moves a 30% learn chance.` },
  { attribute: "JukeboxGlitch",
    inputType: InputVariation.Checkbox,
    label: "Giromon Glitch",
    tooltip: 
       `Enable this to fix the crash that happens when viewing the jukebox
        track list in the English version.` },
  { attribute: "IncreaseLearnChance",
    inputType: InputVariation.Checkbox,
    label: "Battle Learn Chance",
    tooltip: 
       `Double the chance to learn techs after battle.  This makes some techs
        learnable very quickly.  This setting is helpful for a race environment,
        making it less likely to be long-term stuck with a terrible technique.` },
  { attribute: "Woah",
    inputType: InputVariation.Checkbox,
    label: "Change Woah Text",
    tooltip: 
       `Enable this to change the "Woah!" text when picking up an item to say
        "Oh shit!" instead.  This has no real effect and is purely cosmetic.` },
  { attribute: "Gabu",
    inputType: InputVariation.Checkbox,
    label: "Gabumon Mode",
    tooltip: 
       `This makes Gabumon as powerful as he was truly meant to be.  Not
        for the faint of heart.  Good luck.` },
  { attribute: "ShowHashIntro",
    inputType: InputVariation.Checkbox,
    label: "Display Settings",
    tooltip: 
       `Show a hash of the settings used on the Jijimon intro screen when
        creating a new game.  This is useful for on-the-fly verification
        that each race participant is using the same settings (and seed).` },
  { attribute: "SkipIntro",
    inputType: InputVariation.Checkbox,
    label: "Skip Intro",
    tooltip: 
       `Enable this to cut out the majority (as much as possible) of the 
        intro dialogue when creating a new game.  Does not conflict with
        "Display Settings" option.` },
  { attribute: "UnlockAreas",
    inputType: InputVariation.Checkbox,
    label: "Unlock Areas",
    tooltip: 
       `Remove digimon type (Vaccine, Data, Virus, Monzaemon) entry
        barriers to Greylord's Mansion, Ice Sanctuary and Toy Town,
        allowing any digimon to enter. This option helps alleviate
        the difficulty of getting a partiulcar type of digimon when
        digivolution is random. for instance.` },
  { attribute: "UnrigSlots",
    inputType: InputVariation.Checkbox,
    label: "Fair Bonus Try",
    tooltip: 
       `In Digimon World, the bonus try slots are not fair.  When you start
        up the slots, the game has already decided whether or not you will be
        allowed to win, no matter how perfect you time it (though it still
        won't do everything for you, even if it is planning to let you win).
        This option removes that 'feature' and makes the bonus try slots
        fair and purely skill-based.` },
  { attribute: "SpawnRateEnabled",
    inputType: InputVariation.Checkbox,
    label: "Recruit Spawn Rate",
    tooltip: 
       `Enable this to set the chance for Mamemon, MetalMamemon, Piximon, and
        Otamamon appearing on their respective maps` },
  { attribute: "SpawnRate",
    inputType: InputVariation.Slider,
    minVal: Main.SpawnRateMin,
    maxVal: Main.SpawnRateMax,
    label: "Recruit Spawn Rate",
    tooltip: 
       `The percentage chance for the digimon to spawn.  Disable to use vanilla
        behavior.` },
  { attribute: "Softlock",
    inputType: InputVariation.Checkbox,
    label: "Fix Softlocks",
    tooltip: `This fixes some movement related softlocks.` },
  { attribute: "LearnMoveAndCommand",
    inputType: InputVariation.Checkbox,
    label: "Fix Brains Learning",
    tooltip: 
        `This patch disables the text for learning new commands, allowing you
         to learn a command and a technique at the same session.
         This mainly helps if you're doing Bonus Tries to obtain new moves.` },
  { attribute: "FixDVChips",
  inputType: InputVariation.Checkbox,
  label: "Fix DV Chip descriptions",
  tooltip: 
      `Fixes DV Chip descriptions, to actually tell you what they do` },
  { attribute: "HappyVending",
    inputType: InputVariation.Checkbox,
    label: "Happymushroom Vending",
    tooltip: 
        `Replaces Meat trade with a Happymushroom trade at the vending machine
         at Dragon Eye Lake's top area.` },
]
