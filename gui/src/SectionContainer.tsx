import * as React from 'react'
import {Component } from 'react'
import * as path from "path";

import ElementContainer, { SectionElement } from "./ElementContainer"

const initialState = { enabled: false }
type State = Readonly<typeof initialState>

interface Props { 
    id              : string
    title           : string
    tooltip         : string
    disabled        : boolean
    elements?       : SectionElement[]
}


export default class SectionContainer extends Component<Props, State> {
    readonly state: State = initialState
    
    private handleToggle = () => this.setState( toggleEnabled )
    
    constructor( props: Props ) {
        super( props )
    }

    render() {
        const { enabled } = this.state
        return ( <div id={this.props.id + "Container"} className="category">
                    <h1 className="category">{this.props.title}</h1>
                    <label><input type="checkbox" 
                                  id={this.props.id}
                                  value="Enabled" 
                                  disabled={this.props.disabled} 
                                  onChange={this.handleToggle} /> 
                        <span><div className="tooltip">
                            Enabled
                            <span className="tooltiptext">{this.props.tooltip}</span>
                        </div></span>
                    </label> <br/>
                    {this.props.elements.map( ( elem, index ) => 
                        < ElementContainer
                            key={index}
                            id={elem.id}
                            inputType={elem.inputType}
                            defaultVal={elem.defaultVal}
                            sliderMin={elem.sliderMin}
                            sliderMax={elem.sliderMax}
                            enabled={this.state.enabled && !this.props.disabled}
                            label={elem.label}
                            tooltip={elem.tooltip}
                            multiSelect={elem.multiSelect}
                            multiSelectLabel={elem.multiSelectLabel}
                        /> )}
                </div> )
    }
}

const toggleEnabled = ( state: State) => { console.log("change eventtriggered" ); return { enabled: !state.enabled }}