import { remote } from 'electron'
import * as React from 'react'
import * as ReactDOM from 'react-dom'
import { Component } from 'react'
import * as child_process from 'child_process'
import * as Path from "path"
import * as fs from "fs"

import SectionContainer from "./SectionContainer"
import { Button, Card, Elevation, Intent, RadioGroup, Radio, FileInput, NumericInput, Tabs, Tab, Label, InputGroup } from '@blueprintjs/core'
import * as Main from './MainModel'
import * as Constants from './constants'

interface Props {
    rootDirectory   : string
}

interface State {
    terminalOut : JSX.Element[]
    activeTab   : Page
}

enum Page {
    Digimon = "Digimon",
    Items = "Items",
    Progress = "Progression",
    Patches = "Misc. Patches"
}

export default class MainContainer extends Component<Props, State> {
    constructor( props: Readonly<Props> ) {
        super( props );
        this.state = {
            terminalOut: [],
            activeTab: Page.Digimon
        }
    }
    
    /* Private Variables */
    private data                    = new Main.MainModel()
    private inProgress  : boolean   = false
    private showTerminal: boolean   = false
    private terminal    : any       = null
    private scrollDown  : boolean   = false

    /* select file to use for base ROM */
    private onMenuSelectROM = ( e: React.FormEvent<HTMLInputElement> ): void => {
        let path = e.currentTarget.files?.[ 0 ]?.path

        if( path ) {
            this.data.General.InputFile = path
            this.forceUpdate()
        }
    }

    /* select location to output randomized ROM */
    private onMenuSelectOutput = ( e: React.FormEvent<HTMLInputElement> ): void => {
        let path = e.currentTarget.value

        this.data.General.OutputFile = path
        this.forceUpdate()
    }

    /* select location to output randomized ROM */
    private onMenuSelectSeed = ( e: React.FormEvent<HTMLInputElement> ): void => {
        let val = e.currentTarget.value

        this.data.General.Seed = val? `${val}` : undefined
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
        console.log( text )
        let output = this.state.terminalOut;
        let newDiv = <div key={output.length} 
                          className={"terminalText" + ( name? ( " " + name ) : "" )}>
                        {"> " + text}
                     </div>

        output.push( newDiv )

        this.scrollDown = true
        this.forceUpdate()
    }

    /* Notification callback for end of execution */
    private notifyDone = () => {
        this.inProgress = false

        this.addToOutput( `Settings (excluding input and output file names) were hashed to the following MD5 value:` )
        this.addToOutput( this.data.General.Hash )
        this.addToOutput( `If you're racing, compare this value to that of your race opponents to make sure you have the same ROM.` )
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
        this.showTerminal = true

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

        proc.stderr.on('data', (chunk) => {
            let textChunk = chunk.toString();
            this.addToOutput( textChunk, "error" )
        })
    }

    render() {
        let body: JSX.Element
        switch( this.state.activeTab ) {
            case Page.Digimon:
                body =  <div id="data-section">
                            <div className="column one-half">
                                <SectionContainer 
                                    title="Digimon Data" 
                                    disabled={this.inProgress}
                                    data={this.data.Digimon}
                                    tooltip={Constants.digimonDataTooltip}
                                    elements={Constants.digimomDataElements}/>
                                <SectionContainer 
                                    title="Digivolutions" 
                                    disabled={this.inProgress}
                                    data={this.data.Evolution}
                                    tooltip={Constants.evolutionTooltip}
                                    elements={Constants.evolutionElements}/>
                            </div>
                            <div className="column one-half">
                                <SectionContainer 
                                    title="Technique Data" 
                                    disabled={this.inProgress}
                                    data={this.data.Techs}
                                    tooltip={Constants.techDataTooltip}
                                    elements={Constants.techDataElements}/>
                            </div>
                        </div>
                break

            case Page.Items:
                body =  <div id="data-section">
                            <div className="column one-half">
                                <SectionContainer 
                                    title="Map Item Spawns" 
                                    disabled= {this.inProgress}
                                    data={this.data.MapItems}
                                    tooltip={Constants.mapItemTooltip}
                                    elements={Constants.mapItemElements}/>
                            </div>
                            <div className="column one-half">
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
                            </div>
                        </div>
                break
                    
            case Page.Progress:
                body =  <div id="data-section">
                            <div className="column one-half">
                                <SectionContainer
                                    title="Starter" 
                                    disabled={this.inProgress}
                                    data={this.data.Starter}
                                    tooltip={Constants.starterTooltip}
                                    elements={Constants.starterElements}/>
                            </div>
                            <div className="column one-half">
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
                            </div>
                        </div>
                break

            case Page.Patches:
                body =  <div id="data-section">
                            <SectionContainer 
                                title="Miscellaneous Patches" 
                                disabled= {this.inProgress}
                                data={this.data.Patches}
                                tooltip={Constants.patchTooltip}
                                wrapperID="misc-patches"
                                elements={Constants.patchElements}/>
                        </div>
                break

        }
        return  <div className="window">
                    {this.renderFileSection()}
                    {body}
                    <div 
                        className="terminalOutput"
                        hidden={!this.showTerminal}>
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
        return  <>
                    <Card id="file-section-wrapper" elevation={Elevation.TWO}>
                        <div id="file-section">
                            <div className="fill column two-thirds" >
                                <div id="input-file" className="file-select-row" >
                                    <Label>
                                        ROM:
                                    </Label>
                                    <FileInput
                                        className={`file-select ${this.data.General.InputFile? "" : "unselected"}`}
                                        id="input-file-select"
                                        disabled={this.inProgress}
                                        text={this.data.General.InputFile || "Select ROM file..."}
                                        fill={true}
                                        onInputChange={this.onMenuSelectROM}/>
                                </div>
                                <div id="output-file" className="file-select-row">
                                    <Label>
                                        Output:
                                    </Label>
                                    <InputGroup
                                        className="file-select"
                                        placeholder="Destination file name..."
                                        disabled={this.inProgress}
                                        value={this.data.General.OutputFile}
                                        onChange={this.onMenuSelectOutput}
                                        fill={true}/>
                                </div>
                                <div id="log-seed-section"> 
                                    <div className="seed-subsection">
                                        <Label id="seed">
                                            Seed: 
                                        </Label>
                                        <InputGroup
                                            placeholder="Random"
                                            disabled={this.inProgress}
                                            value={this.data.General.Seed}
                                            onChange={this.onMenuSelectSeed}/>
                                    </div>
                                    <RadioGroup
                                        className="log-subsection"
                                        label="Logging:"
                                        onChange={ ( e ) => {
                                            this.data.General.LogLevel = e.currentTarget.value as Main.LogType
                                            this.forceUpdate()
                                        }}
                                        selectedValue={this.data.General.LogLevel}
                                        inline={true}>
                                        <br/>
                                        <Radio 
                                            label="Full"
                                            value="full"
                                            id="logFull"
                                            inline={true}
                                            disabled={this.inProgress}/>
                                        <Radio
                                            label="Casual"
                                            value="casual"
                                            id="logCasual"
                                            inline={true}
                                            disabled={this.inProgress}/>
                                        <Radio
                                            label="Race"
                                            value="race"
                                            id="logRace"
                                            inline={true}
                                            disabled={this.inProgress}/>
                                    </RadioGroup>
                                </div>
                            </div>
                            <div id="topRightSection" className="column one-third">
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
                        <Tabs 
                            className="tab-group"
                            onChange={( newTab ) => { this.setState( { activeTab: newTab as Page } ) }}>
                            {Object.values( Page ).map( page =>
                                <Tab 
                                    key={`tab-${page.toLowerCase()}`} 
                                    id={page} 
                                    title={page}
                                    className="tab"/>
                            )}
                        </Tabs>
                    </Card>
        </>
    }
}