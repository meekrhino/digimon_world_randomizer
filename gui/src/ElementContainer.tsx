import * as React from 'react'
import {Component } from 'react'
import * as path from "path";

export enum InputVariation {
    Checkbox,
    Slider,
    Multiselect
}

export interface SectionElement {
    id          : string
    inputType   : InputVariation
    defaultVal  : any
    label?      : string
    tooltip     : string
    sliderMin?  : string
    sliderMax?  : string
    multiSelect?: string[]
}

interface Props { 
    id          : string
    inputType   : InputVariation
    defaultVal  : any
    enabled     : boolean
    label?      : string
    tooltip     : string
    sliderMin?  : string
    sliderMax?  : string
    multiSelect?: string[]
}


export default class ElementContainer extends Component<Props, object> {
    constructor( props: Props ) {
        super( props )
    }

    render() {
        switch( this.props.inputType ) {
            case InputVariation.Checkbox:
                return ( <div>
                            <label><input type="checkbox" 
                                          disabled={!this.props.enabled} 
                                          defaultChecked={this.props.defaultVal as boolean}
                                          id={this.props.id} /> 
                                <span><div className="tooltip">
                                    {this.props.label}
                                    <span className="tooltiptext">{this.props.tooltip}</span>
                                </div></span>
                            </label> <br/>
                        </div> )

            case InputVariation.Slider:
                return ( <div className="slidecontainer tooltip" >
                            <input type="range"
                                   disabled={!this.props.enabled}
                                   defaultValue={this.props.defaultVal as string}
                                   min={this.props.sliderMin}
                                   max={this.props.sliderMax}
                                   id={this.props.id} />
                                <span className="tooltiptext">{this.props.tooltip}</span><br/>
                        </div> )

            case InputVariation.Multiselect:
                    return( <div></div>)
        }
    }   
}