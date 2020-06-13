import * as React from 'react'
import { Component } from 'react'

import ElementContainer, { SectionElement } from "./ElementContainer"
import { Checkbox, Tooltip, Card } from '@blueprintjs/core'
import { Toggleable } from './MainModel'

export interface SectionProps<T> {
    title           : string
    tooltip         : string
    disabled        : boolean
    data            : T
    wrapperID?      : string
    elements?       : SectionElement<T>[]
}

export default class SectionContainer<T extends Toggleable> extends Component<SectionProps<T>, any> {    
    constructor( props: SectionProps<T> ) {
        super( props )
    }

    render() {
        return <Card id={this.props.title + "Container"} className="category">
                    <h1 className="category">
                        {this.props.title}
                    </h1>
                    <Tooltip 
                        popoverClassName="tooltip-popover"
                        content={this.props.tooltip}
                        hoverOpenDelay={750}>
                        <Checkbox
                            label="Enabled"
                            checked={this.props.data.Enabled}
                            disabled={this.props.disabled}
                            onClick={() => {
                                this.props.data.Enabled = !this.props.data.Enabled
                                this.forceUpdate()
                            }}/>
                    </Tooltip>
                    <div 
                        className={`flex`}
                        id={this.props.wrapperID || this.props.title}>
                        {this.props.elements?.map( ( elem, index ) => 
                            <ElementContainer
                                key={index}
                                inputType={elem.inputType}
                                value={this.props.data[ elem.attribute ]}
                                setValue={( value: any ) => {
                                    this.props.data[ elem.attribute ] = value
                                    this.forceUpdate()
                                }}
                                minVal={elem.minVal}
                                maxVal={elem.maxVal}
                                enabled={this.props.data.Enabled && !this.props.disabled}
                                label={elem.label}
                                tooltip={elem.tooltip}
                                multiSelect={elem.multiSelect}
                                multiSelectLabel={elem.multiSelectLabel}
                                dropdownPlaceholder={elem.dropdownPlaceholder}
                                dropdownOptions={elem.dropdownOptions}/>
                        )}
                    </div>
                </Card>
    }
}
