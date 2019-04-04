import * as React from 'react'
import {Component } from 'react'
import * as path from "path";

export enum InputVariation {
    Checkbox,
    Slider,
    Multiselect,
    Value
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
                return( <div className="tooltip" >
                            {this.props.multiSelect.map( ( opt, index ) =>
                                <div key={index}>
                                    <input type="radio"
                                        disabled={!this.props.enabled}
                                        name={this.props.id + "Name"}
                                        value={opt}
                                        id={this.props.id + opt} />
                                    <label htmlFor={this.props.id + opt}>{opt}</label>
                                    <span className="tooltiptext">{this.props.tooltip}</span><br/>
                                </div>
                            )}
                        </div> )

            case InputVariation.Value:
                return ( <div>
                            <label><input type="number" 
                                          disabled={!this.props.enabled} 
                                          defaultValue={this.props.defaultVal as string}
                                          min={this.props.sliderMin}
                                          max={this.props.sliderMax}
                                          id={this.props.id} /> 
                                <span className="inputNum"><div className="tooltip">
                                    {this.props.label}
                                    <span className="tooltiptext">{this.props.tooltip}</span>
                                </div></span>
                            </label> <br/>
                        </div> )
        }
    }   
}