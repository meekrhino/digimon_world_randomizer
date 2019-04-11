import * as React from 'react'
import * as ReactDOM from 'react-dom'
import {Component } from 'react'

export enum InputVariation {
    Checkbox,
    Slider,
    Multiselect,
    Value
}

export interface SectionElement {
    id                  : string
    inputType           : InputVariation
    defaultVal          : any
    label?              : string
    tooltip             : string
    sliderMin?          : string
    sliderMax?          : string
    multiSelect?        : string[]
    multiSelectLabel?   : string[]
}

interface Props { 
    id                  : string
    inputType           : InputVariation
    defaultVal          : any
    enabled             : boolean
    label?              : string
    tooltip             : string
    sliderMin?          : string
    sliderMax?          : string
    multiSelect?        : string[]
    multiSelectLabel?   : string[]
}

interface State {   
    sliderVal?          : string
}


export default class ElementContainer extends Component<Props, State> {
    private input: any = null
    private out: any = null

    constructor( props: Props ) {
        super( props )

        if( props.inputType == InputVariation.Slider ) {
            this.state = { sliderVal: props.defaultVal }
        }
    }

    private onSliderDrag() {
        const elem = ReactDOM.findDOMNode( this.input );
        if ( elem instanceof HTMLInputElement ) {
            this.setState( { sliderVal: elem.value } )
        }
    }

    render() {
        switch( this.props.inputType ) {
            case InputVariation.Checkbox:
                return ( <div>
                            <label><input type="checkbox" 
                                          disabled={!this.props.enabled} 
                                          defaultChecked={this.props.defaultVal as boolean}
                                          id={this.props.id}
                                          ref={input => { this.input = input } } /> 
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
                                   id={this.props.id}
                                   ref={input => { this.input = input } }
                                   onInput={ this.onSliderDrag.bind(this) } />
                            <span className="slidervalue" 
                                  id={this.props.id + "Span"}
                                  ref={out => { this.out = out } } >{this.state.sliderVal}</span>
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
                                        defaultChecked={index? false : true}
                                        id={this.props.id + opt}
                                        ref={input => { this.input = input } } />
                                    <label htmlFor={this.props.id + opt}>{this.props.multiSelectLabel[ index ]}</label>
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
                                          id={this.props.id}
                                          ref={input => { this.input = input } } /> 
                                <span className="inputNum"><div className="tooltip">
                                    {this.props.label}
                                    <span className="tooltiptext">{this.props.tooltip}</span>
                                </div></span>
                            </label> <br/>
                        </div> )
        }
    }   

    componentDidMount() {
        if( this.out ) {
            this.out.addEventListener( "loadSettings", this.onSliderDrag.bind(this) )
        }
    }
}