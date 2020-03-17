import { remote } from 'electron'
import * as React from 'react'
import * as ReactDOM from 'react-dom'
import { Component } from 'react'
import * as child_process from 'child_process'
import * as Path from "path"
import * as fs from "fs"

import SectionContainer from "./SectionContainer"
import { Button, Card, Elevation, Intent, RadioGroup, Radio, FileInput, NumericInput } from '@blueprintjs/core'
import * as Main from './MainModel'
import * as Constants from './constants'

interface Props {
    rootDirectory   : string
}

interface State {
    terminalOut  : JSX.Element[]
}

export default class MainContainer extends Component<Props, State> {
    constructor( props: Readonly<Props> ) {
        super( props );
        this.state = {
            terminalOut: []
        }
    }
    
    /* Private Variables */
    private data                    = new Main.MainModel()
    private inProgress  : boolean   = false
    private terminal    : any       = null
    private scrollDown  : boolean   = false

    /* select file to use for base ROM */
    private onMenuSelectROM = ( e: React.FormEvent<HTMLInputElement> ): void => {
        let path = e.currentTarget.files[ 0 ].path

        this.data.General.InputFile = path
    }

    /* select location to output randomized ROM */
    private onMenuSelectOutput = ( e: React.FormEvent<HTMLInputElement> ): void => {
        let path = e.currentTarget.files[ 0 ].path

        this.data.General.OutputFile = path
    }

    /* select file to save settings to */
    private onMenuSaveSettings = (): void => {
        let path = remote.dialog.showSaveDialog( {
                        title: "Select settings file to save",
                        filters: [ { name: "Settings File", extensions: [ "json" ] } ],
                        defaultPath: this.props.rootDirectory 
                    } );

        let err = this.saveSettings( path )
        if( err ) {
            this.addToOutput( err.message, "error" )
        }
    }

    /* save current settings to specified file */
    private saveSettings = ( path: string ) => {
        let file: number
        try {
            file = fs.openSync( path, 'w' )
        }
        catch( e ) {
            return e
        }
        const settings = this.data.toJSON()
        if( fs.writeSync( file, settings ) != settings.length ) {
            return Error( "ERR: unable to write settings to " + path )
        }
    }

    /* Load settings from menu */
    private onMenuLoadSettings = (): void => {
        let path = remote.dialog.showOpenDialog( {
                        title: "Select settings file to load",
                        properties: [ 'openFile' ],
                        filters: [ { name: "Settings File", extensions: [ "json" ] } ],
                        defaultPath: this.props.rootDirectory
                    } )?.[ 0 ];

        let err = this.loadSettings( path )
        if( err ) {
            console.log( err )
            this.addToOutput( err.message, "error" )
        }
        this.forceUpdate()
    }

    /* load settings from specified file */
    private loadSettings = ( path: string ): Error | undefined => {
        try {
            let file = fs.openSync( path, 'r' )
        }
        catch( e ) {
            return e
        }

        this.data.fromJSON( fs.readFileSync( path, "utf-8" ) )
    }

    /* Handle capturing terminal output */
    private addToOutput = ( text: string, name?: string ) => {
        let output = this.state.terminalOut;
        let newDiv = <div key={output.length} 
                          className={"terminalText" + ( name? ( " " + name ) : "" )}>
                        {"> " + text}
                     </div>

        output.push( newDiv )

        this.setState( { terminalOut: output } )
        this.scrollDown = true
    }

    /* Notification callback for end of execution */
    private notifyDone = () => {
        this.inProgress = false

        this.addToOutput( `Settings (excluding input and output file names) were hashed
                           to the following MD5 value:` )
        this.addToOutput( this.data.General.Hash )
        this.addToOutput( `If you're racing, compare this value to that of your race
                           opponents to make sure you have the same ROM.` )
        this.forceUpdate()
    }

    /* Run the randomizer */
    private runRandomize = () => {
        this.setState( { terminalOut: [] } )
        const path = Path.join( this.props.rootDirectory, "digimon_randomize.exe" )
        const args = [ "-settings", this.data.toJSON() ]
        const env = Object.assign({}, process.env)
        const options = {
            detached: true,
            cwd: this.props.rootDirectory,
            env
        }

        if( this.data.General.InputFile == "" ) {
            this.addToOutput( "ERR: must select a ROM input file", "error" )
            return
        }

        if( !fs.existsSync( path ) ) {
            this.addToOutput( "'digimon_randomize.exe' does not exist in working directory", "error" )
            return
        }

        this.addToOutput( "Initiating randomizer..." )

        this.inProgress = true
        let spawn = child_process.execFile;
        let proc = spawn( path, args, options )
        
        proc.on( 'exit', this.notifyDone.bind( this ) )

        proc.stdout.on('data', (chunk) => {
            let textChunk = chunk.toString();
            this.addToOutput( textChunk )
        })
    }

    render() {
        return  <div className="window">
                    {this.renderFileSection()}
                    <div id="data-section">
                        {/* leftmost column */}
                        <div className="column one-third">
                            <SectionContainer
                                title="Starter" 
                                disabled={this.inProgress}
                                data={this.data.Starter}
                                tooltip={Constants.starterTooltip}
                                elements={Constants.starterElements}/>
                            <SectionContainer 
                                title="Digimon Data" 
                                disabled={this.inProgress}
                                data={this.data.Digimon}
                                tooltip={Constants.digimonDataTooltip}
                                elements={Constants.digimomDataElements}/>
                            <SectionContainer 
                                title="Technique Data" 
                                disabled={this.inProgress}
                                data={this.data.Techs}
                                tooltip={Constants.techDataTooltip}
                                elements={Constants.techDataElements}/>
                        </div>
                        {/* center column */}
                        <div className="column one-third">
                            <SectionContainer 
                                title="Digivolutions" 
                                disabled={this.inProgress}
                                data={this.data.Evolution}
                                tooltip={Constants.evolutionTooltip}
                                elements={Constants.evolutionElements}/>
                            <SectionContainer 
                                title="Chest Contents" 
                                disabled={this.inProgress}
                                data={this.data.Chests}
                                tooltip={Constants.chestsTooltip}
                                elements={Constants.chestsElements}/>
                            <SectionContainer 
                                title="Tokomon Items" 
                                disabled= {this.inProgress}
                                data={this.data.Tokomon}
                                tooltip={Constants.tokomonTooltip}
                                elements={Constants.tokomonElements}/>
                            <SectionContainer 
                                title="Map Item Spawns" 
                                disabled= {this.inProgress}
                                data={this.data.MapItems}
                                tooltip={Constants.mapItemTooltip}
                                elements={Constants.mapItemElements}/>
                        </div>
                        {/* rightmost column */}
                        <div className="column one-third">
                        <SectionContainer 
                            title="Recruitment" 
                            disabled= {this.inProgress}
                            data={this.data.Recruitment}
                            tooltip={Constants.recruitTooltip}/>
                        <SectionContainer 
                            title="Technique Gifts" 
                            disabled= {this.inProgress}
                            data={this.data.TechGifts}
                            tooltip={Constants.techGiftTooltip}/>
                        <SectionContainer 
                            title="Miscellaneous Patches" 
                            disabled= {this.inProgress}
                            data={this.data.Patches}
                            tooltip={Constants.patchTooltip}
                            elements={Constants.patchElements}/>
                    </div>
                </div>
                <div 
                    className="terminalOutput"
                    hidden={!this.inProgress}>
                    <span className="terminalHeader">
                        Execution Output
                    </span>
                    <div className="terminalTextBox"
                        ref={terminal => { this.terminal = terminal } }>
                        {this.state.terminalOut}
                    </div>
                </div>
            </div>
    }

    componentDidUpdate( prevProps: Props, prevState: State ) {
        if ( this.scrollDown ) {
            const elem = ReactDOM.findDOMNode( this.terminal );
            if ( elem instanceof Element ) {
                elem.scrollTop = elem.scrollHeight;
                this.scrollDown = false;
            }
        }
    }

    /* Private Functions */
    private renderFileSection = () => {
        return  <Card id="file-section" elevation={Elevation.TWO}>
                    <div className="column two-thirds" >
                        <div id="input-file"  className="fileSelect" >
                            <FileInput
                                className="file-select"
                                id="input-file-select"
                                disabled={this.inProgress}
                                text={this.data.General.InputFile || "Select ROM file..."}
                                fill={true}
                                onInputChange={this.onMenuSelectROM}/>
                        </div>
                        <div id="output-file" className="fileSelect">
                            <FileInput
                                className="file-select"
                                id="output-file-select"
                                disabled={this.inProgress}
                                text={this.data.General.InputFile || "Select destination..."}
                                fill={true}
                                onInputChange={this.onMenuSelectOutput}/>
                        </div>
                        <div id="log-seed-section"> 
                            <div id="seed">
                                <b>
                                    Seed: 
                                </b>
                                <NumericInput
                                    placeholder="Random"
                                    disabled={this.inProgress}
                                    buttonPosition={"none"}
                                    allowNumericCharactersOnly={true}
                                    value={this.data.General.Seed}
                                    onValueChange={val => this.data.General.Seed = val}/>
                            </div>
                            <RadioGroup
                                onChange={e => {this.data.General.LogLevel = e.currentTarget.value as Main.LogType}}
                                selectedValue={this.data.General.LogLevel}
                                inline={true}>
                                <Radio 
                                    label="Full"
                                    value="full"
                                    id="logFull"
                                    disabled={this.inProgress}/>
                                <Radio
                                    label="Casual"
                                    value="casual"
                                    id="logCasual"
                                    disabled={this.inProgress}/>
                                <Radio
                                    label="Race"
                                    value="race"
                                    id="logRace"
                                    disabled={this.inProgress}/>
                            </RadioGroup>
                        </div>
                    </div>
                    <div className="column one-third">
                        <div id="topRightSection" >
                            <Button id="load" 
                                    disabled={this.inProgress} 
                                    onClick={this.onMenuLoadSettings}>
                                Load Settings
                            </Button>
                            <Button id="save" 
                                    disabled={this.inProgress} 
                                    onClick={this.onMenuSaveSettings}>
                                Save Settings
                            </Button>
                            <Button 
                                id="randomize" 
                                intent={Intent.SUCCESS}
                                disabled={this.inProgress} 
                                onClick={this.runRandomize}>
                                {this.inProgress? "Randomizing..." : "Randomize"}
                            </Button>
                        </div>
                    </div>
                </Card>
    }
}