import { remote, OpenDialogOptions } from 'electron';
import * as React from 'react'
import * as ReactDOM from 'react-dom'
import {Component } from 'react'
import * as child_process from 'child_process'
import * as Path from "path";
import * as fs from "fs";
import * as ini from "ini";

import SectionContainer from "./SectionContainer"
import { InputVariation } from './ElementContainer';
import { fstat } from 'fs';
import { fileURLToPath } from 'url';
import { string } from 'prop-types';

const { dialog } = require( 'electron' ).remote

interface Settings {
    [key: string]: any
}

interface Props {
    rootDirectory   : string
}

interface State {
    settingsPath : string
    inputPath    : string
    outputPath   : string
    terminalOut  : JSX.Element[]
}

export default class MainContainer extends Component<Props, State> {
    public static instance: MainContainer = null

    private settings: Settings = {
        general: {
            Input                   : "",
            Output                  : "",
            LogLevel                : "casual",
            Seed                    : "" 
        },  
        digimon: {  
            Enabled                 : "no",
            DropItem                : "no",
            DropRate                : "no",
            ValuableItemCutoff      : "10000" 
        },  
        techs: {    
            Enabled                 : "no",
            Mode                    : "no",
            Power                   : "no",
            Cost                    : "no",
            Accuracy                : "no",
            Effect                  : "no",
            EffectChance            : "no"
        },  
        starter: {  
            Enabled                 : "no",
            UseWeakestTech          : "no"
        },  
        recruitment: {  
            Enabled                 : "no"
        },  
        chests: {   
            Enabled                 : "no",
            AllowEvo                : "no"
        },  
        tokomon: {  
            Enabled                 : "no",
            ConsumableOnly          : "no"
        },  
        techgifts: {    
            Enabled                 : "no"
        },  
        mapItems: { 
            Enabled                 : "no",
            FoodOnly                : "no",
            ValuableItemCutoff      : "10000"
        },  
        evolution: {    
            Enabled                 : "no",
            Requirements            : "no",
            SpecialEvos             : "no",
            ObtainAll               : "no"
        },
        patches: {
            FixEvoItemStatGain      : "no",
            AllowDropQuestItems     : "no",
            FixBrainTrainTierOne    : "no",
            FixGiromonJukeboxGlitch : "no",
            IncreaseTechLearnChance : "no",
            SetSpawnRate            : "",
            Woah                    : "no",
            Gabu                    : "no"
        }
    }

    private inProgress: boolean
    private terminal: any = null
    private scrollDown = false

    constructor( props: Readonly<Props> ) {
        super( props );
        this.state = {
            settingsPath: Path.join( props.rootDirectory, "TEMP__last_settings.ini" ),
            inputPath: "",
            outputPath: "Digimon World Rando.bin",
            terminalOut: []
        }
        this.inProgress = false

        if( !MainContainer.instance ) {
            MainContainer.instance = this
        }
    }
    
    /* select file to use for base ROM */
    private onMenuSelectROM(): void {
        let path = remote.dialog.showOpenDialog( {
                        title: "Select ROM file to randomize",
                        properties: [ 'openFile' ],
                        filters: [ { name: "ROM binary", extensions: [ "bin" ] } ],
                        defaultPath: this.props.rootDirectory 
                    } )[ 0 ];

        this.setState( { inputPath: path } )
    }

    /* select location to output randomized ROM */
    private onMenuSelectOutput(): void {
        let path = remote.dialog.showSaveDialog( {
                        title: "Select location to save randomized ROM",
                        filters: [ { name: "Settings File", extensions: [ "bin" ] } ],
                        defaultPath: this.props.rootDirectory 
                    } );

        this.setState( { outputPath: path } )
    }

    /* select file to save settings to */
    private onMenuSaveSettings(): void {
        let path = remote.dialog.showSaveDialog( {
                        title: "Select settings file to save",
                        filters: [ { name: "Settings File", extensions: [ "ini" ] } ],
                        defaultPath: this.props.rootDirectory 
                    } );

        let err = this.saveSettings( path )
        if( err ) {
            this.addToOutput( err.message, "error" )
        }
    }

    /* save current settings to specified file */
    private saveSettings( path: string ): Error {
        const settingsResult = this.calculateSettings()
        if( settingsResult ) {
            return settingsResult
        }

        let encodedSettings = ini.encode( this.settings, { section: undefined, whitespace: true } )
        let file = fs.openSync( path, 'w' )
        if( fs.writeSync( file, encodedSettings ) != encodedSettings.length ) {
            return Error( "ERR: unable to write settings to " + path )
        }
            
        return null
    }

    /* Load settings from menu */
    private onMenuLoadSettings(): void {
        let path = remote.dialog.showOpenDialog( {
                        title: "Select settings file to load",
                        properties: [ 'openFile' ],
                        filters: [ { name: "Settings File", extensions: [ "ini" ] } ],
                        defaultPath: this.props.rootDirectory 
                    } )[ 0 ];

        let err = this.loadSettings( path )
        if( err ) {
            this.addToOutput( err.message, "error" )
        }
    }

    /* load settings from specified file */
    private loadSettings( path: string ): Error {
        try {
            let file = fs.openSync( path, 'r' )
        }
        catch( e ) {
            return e
        }

        this.settings = ini.decode( fs.readFileSync( path, "utf-8" ) )

        this.applySettings()

        return null
    }

    /* snapshot current settings */
    private calculateSettings(): Error {
        /* get "checked" status of element with ID */
        function getCheckedOfInputById( id: string ): string {
            return ( document.getElementById( id ) as HTMLInputElement ).checked? "yes" : "no"
        }

        /* get "value" of element with ID */
        function getValueOfInputById( id: string ): string {
            return ( document.getElementById( id ) as HTMLInputElement ).value
        }

        /* get value (name) of checked radio button in group */
        function getValueOfRadioButtonByName( name: string ): string {
            let val: string = ""
            let list = document.getElementsByName( name ) as NodeListOf<HTMLInputElement>
            list.forEach( ( elem ) => {
                if( elem.checked )
                    val = elem.value
            })
            return val
        }

        /* general */  
        this.settings.general.Input                         = this.state.inputPath
        this.settings.general.Output                        = this.state.outputPath
        this.settings.general.LogLevel                      = getValueOfRadioButtonByName( "log" )
        this.settings.general.Seed                          = getValueOfInputById( "seed" ) 

        /* digimon */  
        this.settings.digimon.Enabled                       = getCheckedOfInputById( "digimondata" )
        this.settings.digimon.DropItem                      = getCheckedOfInputById( "digiDropItem" )
        this.settings.digimon.DropRate                      = getCheckedOfInputById( "digiDropRate" ) 

        if( getCheckedOfInputById( "digiEnableThreshold" ) == "yes" ) {
            this.settings.digimon.ValuableItemCutoff        = getValueOfInputById( "digiThreshold" )  
        }
        else {
            this.settings.digimon.ValuableItemCutoff        = "10000"
        }

        /* techs */  
        this.settings.techs.Enabled                         = getCheckedOfInputById( "techdata" )  
        this.settings.techs.Mode                            = getValueOfRadioButtonByName( "techModeName" )
        this.settings.techs.Power                           = getCheckedOfInputById( "techPower" )  
        this.settings.techs.Cost                            = getCheckedOfInputById( "techCost" )  
        this.settings.techs.Accuracy                        = getCheckedOfInputById( "techAccuracy" )  
        this.settings.techs.Effect                          = getCheckedOfInputById( "effect" )  
        this.settings.techs.EffectChance                    = getCheckedOfInputById( "effectChance" )

        
        /* starter */  
        this.settings.starter.Enabled                       = getCheckedOfInputById( "starter" )  
        this.settings.starter.UseWeakestTech                = getCheckedOfInputById( "useWeakest" ) 
        
        /* recruits */ 
        this.settings.recruitment.Enabled                   = getCheckedOfInputById( "recruit" )  
        
        /* chests */
        this.settings.chests.Enabled                        = getCheckedOfInputById( "chests" )  
        this.settings.chests.AllowEvo                       = getCheckedOfInputById( "allowEvo" )
        
        /* tokomon */
        this.settings.tokomon.Enabled                       = getCheckedOfInputById( "tokomon" )  
        this.settings.tokomon.ConsumableOnly                = getCheckedOfInputById( "consumableOnly" )

        /* tech gifts */
        this.settings.techgifts.Enabled                     = getCheckedOfInputById( "techgifts" )  
        
        /* spawns */
        this.settings.mapItems.Enabled                      = getCheckedOfInputById( "spawns" )  
        this.settings.mapItems.FoodOnly                     = getCheckedOfInputById( "foodOnly" )  

        if( getCheckedOfInputById( "spawnEnableThreshold" ) == "yes" ) {
            this.settings.mapItems.ValuableItemCutoff       = getValueOfInputById( "spawnThreshold" )  
        }
        else {
            this.settings.mapItems.ValuableItemCutoff       = "10000"
        }

        /* evolutions */
        this.settings.evolution.Enabled                     = getCheckedOfInputById( "digimonevos" )
        this.settings.evolution.Requirements                = getCheckedOfInputById( "requirements" )
        this.settings.evolution.SpecialEvos                 = getCheckedOfInputById( "specialEvos" )
        this.settings.evolution.ObtainAll                   = getCheckedOfInputById( "obtainAll" )

        /* patches */
        if( getCheckedOfInputById( "patches" ) == "yes" ) {
            this.settings.patches.FixEvoItemStatGain        = getCheckedOfInputById( "fixEvoItemStatGain" )  
            this.settings.patches.AllowDropQuestItems       = getCheckedOfInputById( "allowDropQuestItems" )  
            this.settings.patches.FixBrainTrainTierOne      = getCheckedOfInputById( "fixBrainTrainTierOne" )  
            this.settings.patches.FixGiromonJukeboxGlitch   = getCheckedOfInputById( "fixGiromonJukeboxGlitch" )
            this.settings.patches.IncreaseTechLearnChance   = getCheckedOfInputById( "increaseTechLearnChance" )  
            this.settings.patches.SetSpawnRate              = getValueOfInputById( "setSpawnRate" )  
            this.settings.patches.Woah                      = getCheckedOfInputById( "woah" )  
            this.settings.patches.Gabu                      = getCheckedOfInputById( "gabu" )  
        }
        else {
            this.settings.patches.FixEvoItemStatGain        = "no"
            this.settings.patches.AllowDropQuestItems       = "no"
            this.settings.patches.FixBrainTrainTierOne      = "no"
            this.settings.patches.FixGiromonJukeboxGlitch   = "no"
            this.settings.patches.IncreaseTechLearnChance   = "no"
            this.settings.patches.SetSpawnRate              = ""
            this.settings.patches.Woah                      = "no"
            this.settings.patches.Gabu                      = "no"
        }

        return null
    }

    private applySettings() {
        /* set "checked" status of element with ID */
        function setCheckedOfInputById( id: string, value: string ) {
            let elem = ( document.getElementById( id ) as HTMLInputElement )
            elem.checked = ( value == "yes" )? true : false

            /* send event to allow sections to be enabled correctly */
            elem.dispatchEvent( new Event( "loadSettings", { bubbles: true } ) )
        }

        /* set element with id to specified value */
        function setValueOfInputById( id: string, value: string ) {
            ( document.getElementById( id ) as HTMLInputElement ).value = value
        }

        /* set specified radio button to be checked */
        function setValueOfRadioButtonByName( name: string, value: string ) {
            let list = document.getElementsByName( name ) as NodeListOf<HTMLInputElement>
            list.forEach( ( elem ) => {
                if( elem.value == value ) {
                    elem.checked = true
                }
                else {
                    elem.checked = false
                }
            })
        }

        /* general */  
        this.setState( { inputPath: this.settings.general.Input,
                         outputPath: this.settings.general.Output } )
        setValueOfRadioButtonByName( "log", this.settings.general.LogLevel )
        setValueOfInputById( "seed", this.settings.general.Seed ) 

        /* digimon */  
        setCheckedOfInputById( "digimondata", this.settings.digimon.Enabled )
        setCheckedOfInputById( "digiDropItem", this.settings.digimon.DropItem )
        setCheckedOfInputById( "digiDropRate", this.settings.digimon.DropRate ) 
        setValueOfInputById( "digiThreshold", this.settings.digimon.ValuableItemCutoff )  
        if( this.settings.digimon.ValuableItemCutoff != "10000" ) {
            setCheckedOfInputById( "digiEnableThreshold", "yes" )
        }
        else {
            setCheckedOfInputById( "digiEnableThreshold", "no" )
        }

        /* techs */  
        setCheckedOfInputById( "techdata", this.settings.techs.Enabled )  

        setValueOfRadioButtonByName( "techModeName", this.settings.techs.Mode )
        setCheckedOfInputById( "techPower", this.settings.techs.Power )  
        setCheckedOfInputById( "techCost", this.settings.techs.Cost )  
        setCheckedOfInputById( "techAccuracy", this.settings.techs.Accuracy )  
        setCheckedOfInputById( "effect", this.settings.techs.Effect  )  
        setCheckedOfInputById( "effectChance", this.settings.techs.EffectChance )
        
        /* starter */  
        setCheckedOfInputById( "starter", this.settings.starter.Enabled )  
        setCheckedOfInputById( "useWeakest", this.settings.starter.UseWeakestTech ) 
        
        /* recruits */ 
        setCheckedOfInputById( "recruit", this.settings.recruitment.Enabled )  
        
        /* chests */
        setCheckedOfInputById( "chests", this.settings.chests.Enabled )  
        setCheckedOfInputById( "allowEvo", this.settings.chests.AllowEvo )
        
        /* tokomon */
        setCheckedOfInputById( "tokomon", this.settings.tokomon.Enabled )  
        setCheckedOfInputById( "consumableOnly", this.settings.tokomon.ConsumableOnly )

        /* tech gifts */
        setCheckedOfInputById( "techgifts", this.settings.techgifts.Enabled )  
        
        /* spawns */
        setCheckedOfInputById( "spawns", this.settings.mapItems.Enabled )  
        setCheckedOfInputById( "foodOnly", this.settings.mapItems.FoodOnly )  
        setValueOfInputById( "spawnThreshold", this.settings.mapItems.ValuableItemCutoff )  
        if( this.settings.mapItems.ValuableItemCutoff != "10000" ) {
            setCheckedOfInputById( "spawnEnableThreshold", "yes" )
        }
        else {
            setCheckedOfInputById( "spawnEnableThreshold", "no" )
        }

        /* evolutions */
        setCheckedOfInputById( "digimonevos", this.settings.evolution.Enabled )
        setCheckedOfInputById( "requirements", this.settings.evolution.Requirements )
        setCheckedOfInputById( "specialEvos", this.settings.evolution.SpecialEvos )
        setCheckedOfInputById( "obtainAll", this.settings.evolution.ObtainAll )

        /* patches */
        /* if any patches are turned on, set enabled to true */
        if( this.settings.patches.FixEvoItemStatGain == "yes"     
         || this.settings.patches.AllowDropQuestItems == "yes"    
         || this.settings.patches.FixBrainTrainTierOne == "yes"   
         || this.settings.patches.FixGiromonJukeboxGlitch == "yes"
         || this.settings.patches.IncreaseTechLearnChance == "yes"
         || this.settings.patches.SetSpawnRate != ""          
         || this.settings.patches.Woah == "yes"                   
         || this.settings.patches.Gabu == "yes" ) {
            setCheckedOfInputById( "patches", "yes" )
         }
        setCheckedOfInputById( "fixEvoItemStatGain", this.settings.patches.FixEvoItemStatGain )  
        setCheckedOfInputById( "allowDropQuestItems", this.settings.patches.AllowDropQuestItems )  
        setCheckedOfInputById( "fixBrainTrainTierOne", this.settings.patches.FixBrainTrainTierOne )  
        setCheckedOfInputById( "fixGiromonJukeboxGlitch", this.settings.patches.FixGiromonJukeboxGlitch )
        setCheckedOfInputById( "increaseTechLearnChance", this.settings.patches.IncreaseTechLearnChance )  
        setValueOfInputById( "setSpawnRate", this.settings.patches.SetSpawnRate )  
        setCheckedOfInputById( "woah", this.settings.patches.Woah )  
        setCheckedOfInputById( "gabu", this.settings.patches.Gabu )  
    }

    /* Handle capturing terminal output */
    private addToOutput( text: string, name?: string ) {
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
    private notifyDone() {
        const options = {
            title: "DONE",
            message: "Done.",
            detail: "Yes, it is really done."
        }
        this.inProgress = false
        dialog.showMessageBox( options )
    }

    /* Run the randomizer */
    private runRandomize() {
        this.setState( { terminalOut: [] } )
        const path = Path.join( this.props.rootDirectory, "digimon_randomize.exe" )
        const args = [ "-settings", this.state.settingsPath ]
        const env = Object.assign({}, process.env)
        const options = {
            detached: true,
            cwd: this.props.rootDirectory,
            env
        }

        let err = this.saveSettings( this.state.settingsPath )
        if( err ) {
            this.addToOutput( err.message, "error" )
            return
        }

        if( this.settings.general.Input == "" ) {
            this.addToOutput( "ERR: must select a ROM input file", "error" )
            return
        }

        if( !fs.existsSync( path ) ) {
            this.addToOutput( "'digimon_randomize.exe' does not exist in working directory", "error" )
            return
        }

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
        return ( <div className="window">
                    <div className="row">
                        <div id="fileOptions">
                            <div className="topColumnLeft" >
                                <div id="inputFileDiv"  className="fileSelect" >
                                    <button className="fileSelect"
                                            name="inputFileSelect" 
                                            id="inputFileSelect"
                                            onClick={this.onMenuSelectROM.bind(this)}
                                            disabled={this.inProgress}>Select ROM</button>
                                    <span className="fileName">{this.state.inputPath}</span>
                                    <br/>
                                </div>
                                <div id="outputFileDiv" className="fileSelect" >
                                    <button className="fileSelect"
                                            name="outputFileSelect" 
                                            id="outputFileSelect"
                                            onClick={this.onMenuSelectOutput.bind(this)}
                                            disabled={this.inProgress}>Select Output</button>
                                    <span className="fileName">{this.state.outputPath}</span>
                                    <br/>
                                </div>
                                <div id="logSeedDiv" className="inBlockAlign" > 
                                    <div id="logLevelDiv" className="category logSeedChild" >
                                        <h1 className="category">Logging: </h1>
                                        <input type="radio" 
                                            name="log" 
                                            value="full" 
                                            id="logFull"
                                            defaultChecked={true}
                                            disabled={this.inProgress} />
                                        <label htmlFor="log">Full</label>
                                        <input type="radio" 
                                            name="log" 
                                            value="casual" 
                                            id="logCasual"
                                            defaultChecked={false}
                                            disabled={this.inProgress} />
                                        <label htmlFor="log">Casual</label>
                                        <input type="radio" 
                                            name="log" 
                                            value="race" 
                                            id="logRace"
                                            defaultChecked={false}
                                            disabled={this.inProgress} />
                                        <label htmlFor="log">Race</label>
                                    </div>
                                    <div className="logSeedChild">
                                        <b>Seed: </b>
                                        <input type="number" 
                                            name="seed" 
                                            placeholder="Random" 
                                            id="seed"
                                            disabled={this.inProgress} />
                                    </div>
                                </div>
                            </div>
                            <div className="topColumnRight">
                                <button id="load" 
                                        disabled={this.inProgress} 
                                        onClick={this.onMenuLoadSettings.bind(this)}>
                                    Load Settings
                                </button><br/>
                                <button id="save" 
                                        disabled={this.inProgress} 
                                        onClick={this.onMenuSaveSettings.bind(this)}>
                                    Save Settings
                                </button><br/><br/>
                                <button id="randomize" 
                                        disabled={this.inProgress} 
                                        onClick={this.runRandomize.bind(this)}>
                                    {this.inProgress? "Randomizing..." : "Randomize"}
                                </button>
                            </div>
                        </div>

                        <hr/>
                        {/* leftmost column */}
                        <div className="column">
                            < SectionContainer 
                                id="starter" 
                                title="Starter" 
                                disabled= {this.inProgress}
                                tooltip={`Enable starter randomization.  This will select two random rookies to replace
                                        the starting partner digimon, Agumon and Gabumon.  They will each be assigned 
                                        a random starting tech from the new starter's pool of learnable techniques.`}
                                elements={[ { id: "useWeakest",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Use Weakest Tech",
                                            tooltip: `When this is enabled, the randomized starter will receive
                                                        the lowest tier damaging move that it can use.  NOTE: this
                                                        does not mean the WEAKEST tech, it means the first tech you
                                                        would learn from brain training (e.g. Spit Fire, Tear Drop).` }
                                        ]}
                            />
                            < SectionContainer 
                                id="digimondata" 
                                title="Digimon Data" 
                                disabled= {this.inProgress}
                                tooltip="Enable digimon data randomization."
                                elements={[ { id: "digiDropItem",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Item Dropped",
                                            tooltip: `Randomize the item dropped by a digimon when it is 
                                                        defeated.  Uses the "valuable item threshold" to 
                                                        exchange vanilla dropped items for similar-value 
                                                        random items` },
                                            { id: "digiDropRate",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Drop Rate",
                                            tooltip: `Randomize the chance that an enemy will drop an item. 
                                                        Tends to prefer small changes from vanilla values, but
                                                        will sometimes become much more frequent.  100% drop
                                                        rates will remain 100%` },
                                            { id: "digiEnableThreshold",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: true,
                                            label: "Match Valuable Drops",
                                            tooltip: `Randomize valuable drops to different valuable drops and
                                                        lower value drops to similar value.` },
                                            { id: "digiThreshold",
                                            inputType: InputVariation.Slider,
                                            defaultVal: "1000",
                                            sliderMin: "0",
                                            sliderMax: "10000",
                                            tooltip: `Set the threshold value for the cutoff between high and
                                                        and low value items.  Maximum and minimum vlues for this
                                                        field will behave the same as disabling this option.` }
                                        ]}
                            />
                            < SectionContainer 
                                id="techdata" 
                                title="Technique Data" 
                                disabled= {this.inProgress}
                                tooltip="Enable technique data randomization."
                                elements={[ { id: "techMode",
                                            inputType: InputVariation.Multiselect,
                                            defaultVal: false,
                                            label: "Randomization Mode",
                                            multiSelect: [ "shuffle", "random" ],
                                            multiSelectLabel: [ "Shuffle", "Random" ],
                                            tooltip: `Mode of randomization for technique data.  In general, 
                                                        "Shuffle" keeps the vanilla values and shuffles them around.
                                                        Meanwhile, "Random" generates all-new random values.  Hover
                                                        individual features to see how these options affect them.` },
                                            { id: "techPower",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Power",
                                            tooltip: `Randomize the power of each tech.  When mode is "Shuffle", 
                                                        the power of all techs will be shuffled amongst themselves.  
                                                        When mode is "Random", techs will be assigned a random power
                                                        ranging from 30% below the weakest vanilla tech and 999,
                                                        the max possible value.` },
                                            { id: "techCost",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "MP Cost",
                                            tooltip: `Randomize the MP cost of each tech.  When mode is "Shuffle",
                                                        the mp cost of all techs will be shuffled amongst themselves.
                                                        When mode is "Random", techs will be assigned a random cost
                                                        calculated from the power of the tech, ranging from 10% to 140% 
                                                        of the power.` },
                                            { id: "techAccuracy",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Accuracy",
                                            tooltip: `Randomize the accuracy of each tech.  When mode is "Shuffle",
                                                        the accuracy of all techs will be shuffled amongst themselves.
                                                        When mode is "Random", techs will be assigned a random accuracy
                                                        ranging from 33 to 100. The vast majority will fall between 
                                                        50 and 100, with just over 10% being 100% and just under 10%
                                                        being under 50.` },
                                            { id: "effect",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Status Effect",
                                            tooltip: `Randomize the status effect of each tech.  This will make about
                                                        50% off all techniques have some status effect, and they
                                                        will be roughly evenly distributed between Flat, Poison, 
                                                        Confusion, and Stun.  This option is not affect by the mode.` },
                                            { id: "effectChance",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Status Effect Chance",
                                            tooltip: `Randomize the chance of a status effect being inflicted for
                                                        each tech.  Techs will be assigned a random value between 
                                                        1% and 70%.  This option is not affected by the mode.` }
                                        ]}
                            />
                        </div>
                        {/* center column */}
                        <div className="column">
                        < SectionContainer 
                                id="digimonevos" 
                                title="Digivolutions" 
                                disabled= {this.inProgress}
                                tooltip={`Enable digivolution tree randomization.  Randomizes which digimon each
                                        digimon can randomize into.  Each fresh will get 1 target, each in-training
                                        will get 2 targets, each rookie gets 4-6 targets, and each champion
                                        gets 1-2 targets.  Unless "Obtain All" is set, not all playable digimon
                                        are guaranteed to be obtainable through natural digivolution.`}
                                elements={[ { id: "requirements",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Requirements",
                                            tooltip: `Randomize the requiremnts to digivolve to each digimon.
                                                        requirements will generally look fairly similar to vanilla
                                                        values, but totally random.  All digimon will have a stat
                                                        requirement, a care mistake required (min or max), a 
                                                        weight requirement (within 5 of), and a techs learned requirement.
                                                        Digimon may randomly have other bonus requirements, including
                                                        max/min battles fought, discipline, and happiness.` },
                                            { id: "specialEvos",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Special Digivolutions",
                                            tooltip: `Randomize the result of some special evolutions.  Specifically,
                                                        this currently includes death digivolutions (such as Bakemon and
                                                        Devimon), MetalMamemon's "upgrade" digivolutions, and the Toy Town
                                                        Monzemon suit.  To preserve completion, Toy Town will be accessible
                                                        by whatever the suit digivolves Numemon into, rather than by
                                                        Monzaemon.` },
                                            { id: "obtainAll",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: true,
                                            label: "Obtain All",
                                            tooltip: `When this option is enabled, randomized evolutions are guaranteed
                                                    to be organized in such a way that all natural evolution digimon
                                                    can still be obtained naturally through evolution.  That means
                                                    each in-training, rookie, champion, and ultimate level digimon
                                                    will have at least one digimon in the previous level that can
                                                    naturally digivolve to it.` }
                                        ]}
                            />
                            < SectionContainer 
                                id="chests" 
                                title="Chest Contents" 
                                disabled= {this.inProgress}
                                tooltip={`Enable item chest contents randomization.  This will randomize the item
                                        contained in each of the "computers".  Any item except digivolution items or
                                        quest items can be randomized into chests.  Quest items include, for example,
                                        the Mansion Key, the Gear, and the stone for the Leomon quest.`}
                                elements={[ { id: "allowEvo",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Digivolution Items",
                                            tooltip: `When this is enabled, digivolution items will be included in the
                                                    availalbe pool of items to be randomized into chests.` }
                                        ]}
                            />
                            < SectionContainer 
                                id="tokomon" 
                                title="Tokomon Items" 
                                disabled= {this.inProgress}
                                tooltip={`Randomize the items given by Tokomon at the start of the game.  This will by
                                        default include only consumable, non-quest items.  It also does not include
                                        digivolution items.  Tokomon will give 1-3 copies of 6 different items chosen
                                        at random, with less valuable items being more likely to come in larger quantities.`}
                                elements={[ { id: "consumableOnly",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: true,
                                            label: "Consumable Only",
                                            tooltip: `When this is enabled, only consumable items will be given.  This
                                                    disallows items like Enemy Repel, Training Manual, and similar.` }
                                        ]}
                            />
                            < SectionContainer 
                                id="spawns" 
                                title="Map Item Spawns" 
                                disabled= {this.inProgress}
                                tooltip={`Randomize items that spawn on maps (such as Digimushrooms).  Only non-quest 
                                        consumable items will be selected.  Does not allow digivolution items to spawn.
                                        Uses the "valuable item threshhold" to exchange vanilla map items for similar-
                                        value random items.  This helps preserve common items being typically less
                                        valuable than rare items.  This setting affects the items that spawn in 
                                        Centarumon's maze.`}
                                elements={[ { id: "foodOnly",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Food Items Only",
                                            tooltip: `Locks the randomly spawned items to be food only.  This will
                                                    only affect map spawns that are food in vanilla; thus,
                                                    the weird spawns in Centarumon's maze will not be forced to
                                                    be food with this setting.` },
                                            { id: "spawnEnableThreshold",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: true,
                                            label: "Match Rare Spawns",
                                            tooltip: `Randomize valuable spawns to different valuable drops and
                                                    lower value drops to similar value.  Helps preserve rare
                                                    item spawns being generally more valuable than common ones.` },
                                            { id: "spawnThreshold",
                                            inputType: InputVariation.Slider,
                                            defaultVal: "1000",
                                            sliderMin: "0",
                                            sliderMax: "10000",
                                            tooltip: `Set the threshold value for the cutoff between high and
                                                        and low value items.  Maximum and minimum vlues for this
                                                        field will behave the same as disabling this option.
                                                        Default value is 1000 -- this value seems to work most
                                                        effectively for preserving the rare/common split.` }
                                        ]}
                            />
                        </div>
                        {/* rightmost column */}
                        <div className="column">
                            < SectionContainer 
                                id="recruit" 
                                title="Recruitment" 
                                disabled= {this.inProgress}
                                tooltip={`Enable recruitment randomization.  Randomizes which recruit shows up in 
                                        town when you recruit one.  For example, it is possible to have Whamon 
                                        show up in town (thus opening the dock to Factorial Town) when Bakemon is
                                        recruited.  WARNING: this is an UNSTABLE feature, and with poor luck can
                                        currently create a seed that cannot be completed for 100PP!!  The
                                        following recruits are not randomized, but will be supported later:  Palmon,
                                        Vegiemon, Greymon, Birdramon, Centarumon, Angemon, and Monzaemon.  The 
                                        following cannot be randomize:  Agumon, Airdramon, and MetalGreymon.`}
                                elements={[ ]}
                            />
                            < SectionContainer 
                                id="techgifts" 
                                title="Technique Gifts" 
                                disabled= {this.inProgress}
                                tooltip={`Randomize the three techniques that Seadramon can teach you, as well
                                        the one that can be taught in Beetle Land (Bug, in vanilla).  They will
                                        still only be able to teach you a move that your current digimon can
                                        learn, so if you cannot learn the move then nothing will happen.  
                                        Seadramon will teach his three techs in order, so if you already know the
                                        first you will get the second, and so on.  If you know all three already,
                                        he will teach you nothing.`}
                                elements={[ ]}
                            />
                            < SectionContainer 
                                id="patches" 
                                title="Miscellaneous Patches" 
                                disabled= {this.inProgress}
                                tooltip={`Various patches to improve different aspects of the game.`}
                                elements={[ { id: "fixEvoItemStatGain",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Item Stat Gain",
                                            tooltip: `Enable this to cause digivolution items to actually grant
                                                    stats upon digivolution.  In vanilla, digivolving does not
                                                    grant any stats gain when it happens through an item.` },
                                            { id: "allowDropQuestItems",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Drop Quest Items",
                                            tooltip: `Enable this to allow dropping quest items (like the Mansion
                                                        Key) from your inventory.  In vanilla, these items cannot be dropped
                                                        and must be deposited in the bank to get them out of your inventory.` },
                                            { id: "fixBrainTrainTierOne",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Brain Train Learning",
                                            tooltip: `Enable this to fix the bug in vanilla that prevents learning
                                                    the lowest tier move for each specialty via brain training.  For 
                                                    example, in vanilla it is impossible to learn Spit Fire via brain
                                                    training.  This patch makes that possible and assigns the tier
                                                    one moves a 40% learn chance.` },
                                            { id: "fixGiromonJukeboxGlitch",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Giromon Glitch",
                                            tooltip: `Enable this to fix the crash that happens when viewing the jukebox
                                                    track list in the English version.` },
                                            { id: "increaseTechLearnChance",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Battle Learn Chance",
                                            tooltip: `Double the chance to learn techs after battle.  This makes some techs
                                                    learnable very quickly.  This setting is helpful for a race environment,
                                                    making it less likely to be long-term stuck with a terrible technique.` },
                                            { id: "woah",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Change Woah Text",
                                            tooltip: `Enable this to change the "Woah!" text when picking up an item to say
                                                    "Oh shit!" instead.  This has no real effect and is purely cosmetic.` },
                                            { id: "gabu",
                                            inputType: InputVariation.Checkbox,
                                            defaultVal: false,
                                            label: "Gabumon Mode",
                                            tooltip: `This makes Gabumon as powerfully as he was truly meant to be.  Not
                                                    for the faint-hearted.  Good luck.` },
                                            { id: "setSpawnRate",
                                            inputType: InputVariation.Value,
                                            defaultVal: "",
                                            sliderMin: "1",
                                            sliderMax: "100",
                                            label: "Recruit Spawn Rate",
                                            tooltip: `Enable this to set the chance for Mamemon, MetalMamemon, Piximon, and
                                                    Otamamon appearing on their respective maps to the specified %.  Leave
                                                    empty to make no changes to vanilla behavior.` }
                                        ]}
                            />
                        </div>
                    </div>
                    <div className="terminalOutput" >
                        <span className="terminalHeader">Execution Output</span><br/><br/>
                        <div className="terminalTextBox"
                         ref={terminal => { this.terminal = terminal } }>
                            {this.state.terminalOut}
                        </div>
                    </div>
                </div> )
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

    componentDidMount() {
        this.loadSettings( this.state.settingsPath )
    }
}