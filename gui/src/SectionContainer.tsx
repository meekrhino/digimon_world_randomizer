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
        return ( <div id={this.props.id} className="category">
                    <h1 className="category">{this.props.title}</h1>
                    <label><input type="checkbox" id="enable" value="Enabled" onClick = { this.handleToggle } /> 
                        <span><div className="tooltip">
                            Enabled
                            <span className="tooltiptext">{this.props.tooltip}</span>
                        </div></span>
                    </label> <br/>
                    {this.props.elements? this.props.elements.map( ( elem, index ) => 
                        < ElementContainer
                            key={index}
                            id={elem.id}
                            inputType={elem.inputType}
                            defaultVal={elem.defaultVal}
                            sliderMin={elem.sliderMin}
                            sliderMax={elem.sliderMax}
                            enabled={this.state.enabled}
                            label={elem.label}
                            tooltip={elem.tooltip}
                        /> ) : <div></div> }
                </div> )
    }
}

const toggleEnabled = ( state: State) => ({ enabled: !state.enabled })