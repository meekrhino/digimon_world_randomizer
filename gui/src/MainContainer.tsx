import * as React from 'react'
import {Component } from 'react'
import * as path from "path";

import SectionContainer from "./SectionContainer"
import ElementContainer, { InputVariation } from './ElementContainer';

export default class MainContainer extends Component<object, object> {
    render() {
        return ( <div className="row">
                    <hr/>
                    {/* leftmost column */}
                    <div className="column">
                        < SectionContainer 
                            id="starter" 
                            title="Starter" 
                            tooltip={`Enable starter randomization.  This will select two random rookies to replace
                                    the starting partner digimon, Agumon and Gabumon.  They will each be assigned 
                                    a random starting tech from the new starter's pool of learnable techniques.`}
                            elements={[ { id: "useWeakest",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: false,
                                          label: "Use Weakest Tech",
                                          tooltip: `When this is enabled, the randomized starter will receive
                                                    the lowest tier damaging move that it can use.  NOTE: this
                                                    does not mean the WEAKEST tech, it means the first tech you
                                                    would learn from brain training (e.g. Spit Fire, Tear Drop).` }
                                    ]}
                        />
                        < SectionContainer 
                            id="digimondata" 
                            title="Digimon Data" 
                            tooltip="Enable digimon data randomization."
                            elements={[ { id: "digiDropItem",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: false,
                                          label: "Item Dropped",
                                          tooltip: `Randomize the item dropped by a digimon when it is 
                                                    defeated.  Uses the "valuable item threshold" to 
                                                    exchange vanilla dropped items for similar-value 
                                                    random items` },
                                        { id: "digiDropRate",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: false,
                                          label: "Drop Rate",
                                          tooltip: `Randomize the chance that an enemy will drop an item. 
                                                    Tends to prefer small changes from vanilla values, but
                                                    will sometimes become much more frequent.  100% drop
                                                    rates will remain 100%` },
                                        { id: "digiEnableThreshold",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: true,
                                          label: "Match Valuable Drops",
                                          tooltip: `Randomize valuable drops to different valuable drops and
                                                    lower value drops to similar value.` },
                                        { id: "digiThreshold",
                                          inputType: InputVariation.Slider,
                                          defaultVal: "1000",
                                          sliderMin: "0",
                                          sliderMax: "10000",
                                          tooltip: `Set the threshold value for the cutoff between high and
                                                    and low value items.  Maximum and minimum vlues for this
                                                    field will behave the same as disabling this option.` }
                                    ]}
                        />
                        < SectionContainer 
                            id="digimonevos" 
                            title="Digivolutions" 
                            tooltip={`Enable digivolution tree randomization.  Randomizes which digimon each
                                     digimon can randomize into.  Each fresh will get 1 target, each in-training
                                     will get 2 targets, each rookie gets 4-6 targets, and each champion
                                     gets 1-2 targets.  Unless "Obtain All" is set, not all playable digimon
                                     are guaranteed to be obtainable through natural digivolution.`}
                            elements={[ { id: "requirements",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: false,
                                          label: "Requirements",
                                          tooltip: `Randomize the requiremnts to digivolve to each digimon.
                                                    requirements will generally look fairly similar to vanilla
                                                    values, but totally random.  All digimon will have a stat
                                                    requirement, a care mistake required (min or max), a 
                                                    weight requirement (within 5 of), and a techs learned requirement.
                                                    Digimon may randomly have other bonus requirements, including
                                                    max/min battles fought, discipline, and happiness.` },
                                        { id: "specialEvos",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: false,
                                          label: "Special Digivolutions",
                                          tooltip: `Randomize the result of some special evolutions.  Specifically,
                                                    this currently includes death digivolutions (such as Bakemon and
                                                    Devimon), MetalMamemon's "upgrade" digivolutions, and the Toy Town
                                                    Monzemon suit.  To preserve completion, Toy Town will be accessible
                                                    by whatever the suit digivolves Numemon into, rather than by
                                                    Monzaemon.` },
                                        { id: "obtainAll",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: true,
                                        label: "Obtain All",
                                        tooltip: `When this option is enabled, randomized evolutions are guaranteed
                                                  to be organized in such a way that all natural evolution digimon
                                                  can still be obtained naturally through evolution.  That means
                                                  each in-training, rookie, champion, and ultimate level digimon
                                                  will have at least one digimon in the previous level that can
                                                  naturally digivolve to it.` }
                                    ]}
                        />
                    </div>
                    {/* center column */}
                    <div className="column">
                        < SectionContainer 
                            id="techdata" 
                            title="Technique Data" 
                            tooltip="Enable technique data randomization."
                            elements={[ { id: "techMode",
                                        inputType: InputVariation.Multiselect,
                                        defaultVal: false,
                                        label: "Randomization Mode",
                                        tooltip: `Mode of randomization for technique data.  In general, 
                                                    "shuffle" keeps the vanilla values by shuffles them around.
                                                    Meanwhile, "random" generates all-new random values.  Hover
                                                    individual options to see how these options affect them.` },
                                        { id: "techPower",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Power",
                                        tooltip: `Randomize the power of each tech.  When mode is "shuffle", 
                                                    the power of all techs will be shuffled amongst themselves.  
                                                    When mode is "random", techs will be assigned a random power
                                                    ranging from 30% below the weakest vanilla tech and 999,
                                                    the max possible value.` },
                                        { id: "techCost",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "MP Cost",
                                        tooltip: `Randomize the MP cost of each tech.  When mode is "shuffle",
                                                    the mp cost of all techs will be shuffled amongst themselves.
                                                    When mode is "random", techs will be assigned a random cost
                                                    calculated from the power of the tech, ranging from 10% to 140% 
                                                    of the power.` },
                                        { id: "techAccuracy",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Accuracy",
                                        tooltip: `Randomize the accuracy of each tech.  When mode is "shuffle",
                                                    the accuracy of all techs will be shuffled amongst themselves.
                                                    When mode is "random", techs will be assigned a random accuracy
                                                    ranging from 33 to 100. The vast majority will fall between 
                                                    50 and 100, with just over 10% being 100% and just under 10%
                                                    being under 50.` },
                                        { id: "effect",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Status Effect",
                                        tooltip: `Randomize the status effect of each tech.  This will make about
                                                    50% off all techniques have some status effect, and they
                                                    will be roughly evenly distributed between Flat, Poison, 
                                                    Confusion, and Stun.  This option is not affect by the mode.` },
                                        { id: "effectChance",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Status Effect Chance",
                                        tooltip: `Randomize the chance of a status effect being inflicted for
                                                    each tech.  Techs will be assigned a random value between 
                                                    1% and 70%.  This option is not affected by the mode.` }
                                    ]}
                        />
                        < SectionContainer 
                            id="chests" 
                            title="Chest Contents" 
                            tooltip={`Enable item chest contents randomization.  This will randomize the item
                                      contained in each of the "computers".  Any item except digivolution items or
                                      quest items can be randomized into chests.  Quest items include, for example,
                                      the Mansion Key, the Gear, and the stone for the Leomon quest.`}
                            elements={[ { id: "allowEvo",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Digivolution Items",
                                        tooltip: `When this is enabled, digivolution items will be included in the
                                                  availalbe pool of items to be randomized into chests.` }
                                    ]}
                        />
                        < SectionContainer 
                            id="tokomon" 
                            title="Tokomon Items" 
                            tooltip={`Randomize the items given by Tokomon at the start of the game.  This will by
                                      default include only consumable, non-quest items.  It also does not include
                                      digivolution items.  Tokomon will give 1-3 copies of 6 different items chosen
                                      at random, with less valuable items being more likely to come in larger quantities.`}
                            elements={[ { id: "consumableOnly",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: true,
                                        label: "Consumable Only",
                                        tooltip: `When this is enabled, only consumable items will be given.  This
                                                  disallows items like Enemy Repel, Training Manual, and similar.` }
                                    ]}
                        />
                        < SectionContainer 
                            id="spawns" 
                            title="Map Item Spawns" 
                            tooltip={`Randomize items that spawn on maps (such as Digimushrooms).  Only non-quest 
                                      consumable items will be selected.  Does not allow digivolution items to spawn.
                                      Uses the "valuable item threshhold" to exchange vanilla map items for similar-
                                      value random items.  This helps preserve common items being typically less
                                      valuable than rare items.  This setting affects the items that spawn in 
                                      Centarumon's maze.`}
                            elements={[ { id: "foodOnly",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Food Items Only",
                                        tooltip: `Locks the randomly spawned items to be food only.  This will
                                                  only affect map spawns that are food in vanilla; thus,
                                                  the weird spawns in Centarumon's maze will not be forced to
                                                  be food with this setting.` },
                                        { id: "spawnEnableThreshold",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: true,
                                        label: "Match Rare Spawns",
                                        tooltip: `Randomize valuable spawns to different valuable drops and
                                                  lower value drops to similar value.  Helps preserve rare
                                                  item spawns being generally more valuable than common ones.` },
                                        { id: "spawnThreshold",
                                        inputType: InputVariation.Slider,
                                        defaultVal: "1000",
                                        sliderMin: "0",
                                        sliderMax: "10000",
                                        tooltip: `Set the threshold value for the cutoff between high and
                                                    and low value items.  Maximum and minimum vlues for this
                                                    field will behave the same as disabling this option.
                                                    Default value is 1000 -- this value seems to work most
                                                    effectively for preserve the rare/common split.` }
                                    ]}
                        />
                    </div>
                    {/* rightmost column */}
                    <div className="column">
                        < SectionContainer 
                            id="recruit" 
                            title="Recruitment" 
                            tooltip={`Enable recruitment randomization.  Randomizes which recruit shows up in 
                                    town when you recruit one.  For example, it is possible to have Whamon 
                                    show up in town (thus opening the dock to Factorial Town) when Bakemon is
                                    recruited.  WARNING: this is an UNSTABLE feature, and with poor luck can
                                    currently create a seed that cannot be completed for 100PP!!  The
                                    following recruits are not randomized, but will be support later:  Palmon,
                                    Vegiemon, Greymon, Birdramon, Centarumon, Angemon, and Monzaemon.  The 
                                    following cannot be randomize:  Agumon, Airdramon, and MetalGreymon.`}
                            elements={[ ]}
                        />
                        < SectionContainer 
                            id="techgifts" 
                            title="Technique Gifts" 
                            tooltip={`Randomize the three techniques that Seadramon can teach you, as well
                                      the one that can be taught in Beetle Land (Bug, in vanilla).  They will
                                      still only be able to teach you a move that your current digimon can
                                      learn, so if you cannot learn the move then nothing will happen.  
                                      Seadramon will teach his three techs in order, so if you already know the
                                      first you will get the second, and so on.  If you know all three already,
                                      he will teach you nothing.`}
                            elements={[ ]}
                        />
                        < SectionContainer 
                            id="patches" 
                            title="Miscellaneous Patches" 
                            tooltip={`Various patches to improve different aspects of the game.`}
                            elements={[ { id: "fixEvoItemStatGain",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: false,
                                          label: "Item Stat Gain",
                                         tooltip: `Enable this to cause digivolution items to actually grant
                                                  stats upon digivolution.  In vanilla, digivolving does not
                                                  grant any stats gain when it happens through an item.` },
                                        { id: "allowDropQuestItems",
                                          inputType: InputVariation.Checkbox,
                                          defaultVal: false,
                                          label: "Drop Quest Items",
                                          tooltip: `Enable this to allow dropping quest items (like the Mansion
                                                    Key) from your inventory.  In vanilla, these items cannot be dropped
                                                    and must be deposited in the bank to get them out of your inventory.` },
                                        { id: "fixBrainTrainTierOne",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Brain Train Learning",
                                        tooltip: `Enable this to fix the bug in vanilla that prevents learning
                                                  the lowest tier move for each specialty via brain training.  For 
                                                  example, in vanilla it is impossible to learn Spit Fire via brain
                                                  training.  This patch makes that possible and assigns the tier
                                                  one moves a 40% learn chance.` },
                                        { id: "fixGiromonJukeboxGlitch",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Giromon Glitch",
                                        tooltip: `Enable this to fix the crash that happens when viewing the jukebox
                                                  track list in the English version.` },
                                        { id: "increaseTechLearnChance",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Battle Learn Chance",
                                        tooltip: `Double the chance to learn techs after battle.  This makes some techs
                                                  learnable very quickly.  This setting is helpful for a race environment,
                                                  making it less likely to be long-term stuck with a terrible technique.` },
                                        { id: "setSpawnRate",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Max Spawn Rate",
                                        tooltip: `Enable this to set the chance for Mamemon, MetalMamemon, Piximon, and
                                                  Otamamon appearing on their respective maps to 100%.` },
                                        { id: "woah",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Change Woah Text",
                                        tooltip: `Enable this to change the "Woah!" text when picking up an item to say
                                                  "Oh shit!" instead.  This has no real effect and is purely cosmetic.` },
                                        { id: "gabu",
                                        inputType: InputVariation.Checkbox,
                                        defaultVal: false,
                                        label: "Gabumon Mode",
                                        tooltip: `This makes Gabumon as powerfully as he was truly meant to be.  Not
                                                  for the faint-hearted.  Good luck.` }
                                    ]}
                        />
                    </div>
                </div> )
    }
}