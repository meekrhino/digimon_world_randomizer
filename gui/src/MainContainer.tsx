import { app, BrowserWindow, Menu } from "electron";
import * as React from 'react'
import {Component } from 'react'
import * as path from "path";


const initialState = { enabled: true }
type State = Readonly<typeof initialState>

export default class MainContainer extends Component<object, State> {
    readonly state: State = initialState
    
    render() {
        const { enabled } = this.state
        return ( <div>
                    <button onClick = { this.handleToggle }>Enable</button>
                    The button is {enabled? "enabled" : "disabled"}!
                 </div> )
    }
    
    private handleToggle = () => this.setState( toggleEnabled )
}

const toggleEnabled = ( state: State) => ({ enabled: !state.enabled })