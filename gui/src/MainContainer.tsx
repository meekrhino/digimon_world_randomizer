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
                    </div>
                </div> )
    }
}