import * as React from 'react'
import {Component } from 'react'
import * as path from "path";

import SectionContainer from "./SectionContainer"
import ElementContainer, { InputVariation } from './ElementContainer';

export default class MainContainer extends Component<object, object> {
    render() {
        return ( <div>
                    < SectionContainer 
                        id="digimonData" 
                        title="Digimon Data" 
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
                                    { id: "digiEnableThresh",
                                      inputType: InputVariation.Checkbox,
                                      defaultVal: true,
                                      label: "Match Valuable Drops",
                                      tooltip: `Randomize valuable drops to different valuable drops and
                                                lower value drops to similar value.` }

                                 ]}
                    />
                </div> )
    }
}