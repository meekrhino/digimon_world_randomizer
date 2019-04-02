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
    label       : string
    tooltip     : string
    sliderMin?  : number
    sliderMax?  : number
    multiSelect?: string[]
}

interface Props { 
    id          : string
    inputType   : InputVariation
    defaultVal  : any
    enabled     : boolean
    label       : string
    tooltip     : string
    sliderMin?  : number
    sliderMax?  : number
    multiSelect?: string[]
}


export default class ElementContainer extends Component<Props, object> {
    constructor( props: Props ) {
        super( props )
    }

    render() {
        switch( this.props.inputType ) {
            case InputVariation.Checkbox:
                return ( <div className="category">
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

            case InputVariation.Multiselect:
                break
            case InputVariation.Slider:
                break
        }
    }   
}