import * as hash from "object-hash"
import * as path from "path"

/* Local Types */
interface RawSettings {
    general          : GeneralSettings & { Hash: string }
    digimon          : DigimonSettings
    techs            : TechSettings
    starter          : StarterSettings
    recruitment      : RecruitmentSettings
    chests           : ChestSettings
    tokomon          : TokomonSettings
    techGifts        : TechGiftSettings
    mapItems         : MapItemSettings
    evolution        : EvolutionSettings
    patches          : PatchSettings
}

/* Public Types */
export type LogType = "full" | "casual" | "race"

export interface Toggleable {
    Enabled             : boolean
}

export interface GeneralSettings {
    InputFile           : string
    OutputFile          : string
    LogLevel            : LogType
    Seed                : string
    Hash                : string
}

export interface DigimonSettings extends Toggleable {
    DroppedItem         : boolean
    DropRate            : boolean
    MatchValue          : boolean
    ValuableItemCutoff  : number
}

export interface TechSettings extends Toggleable {
    RandomizationMode   : string
    Power               : boolean
    Cost                : boolean
    Accuracy            : boolean
    Effect              : boolean
    EffectChance        : boolean
    TypeEffectiveness   : boolean
}

export interface StarterSettings extends Toggleable {
    UseWeakestTech      : boolean
    Fresh               : boolean
    InTraining          : boolean
    Rookie              : boolean
    Champion            : boolean
    Ultimate            : boolean
    Digimon             : string
}

export interface RecruitmentSettings extends Toggleable {
}

export interface ChestSettings extends Toggleable {
    AllowEvolutionItems : boolean
}

export interface TokomonSettings extends Toggleable {
    ConsumableOnly      : boolean
}

export interface TechGiftSettings extends Toggleable {
}

export interface MapItemSettings extends Toggleable {
    FoodOnly            : boolean
    MatchValue          : boolean
    ValuableItemCutoff  : number
}

export interface EvolutionSettings extends Toggleable {
    Requirements        : boolean
    SpecialEvolutions   : boolean
    ObtainAllMode       : boolean
}

export interface PatchSettings extends Toggleable {
    EvoItemStatGain     : boolean
    QuestItemsDroppable : boolean
    BrainTrainTierOne   : boolean
    JukeboxGlitch       : boolean
    IncreaseLearnChance : boolean
    SpawnRateEnabled    : boolean
    SpawnRate           : number
    ShowHashIntro       : boolean
    SkipIntro           : boolean
    Woah                : boolean
    Gabu                : boolean
    Softlock            : boolean
    UnlockAreas         : boolean
    UnrigSlots          : boolean
    LearnMoveAndCommand : boolean
    FixDVChips          : boolean
    HappyVending        : boolean
}

/* Public Constants */
export const ItemValueMax = 10000
export const ItemValueMin = 0
export const SpawnRateMax = 100
export const SpawnRateMin = 1
export const SpawnRateDefault = 3

export class MainModel {
    constructor( raw?: string ) {
        this.General = {
            InputFile           : "",
            OutputFile          : "",
            LogLevel            : "casual",
            Seed                : undefined,
            Hash                : undefined
        }

        this.Digimon = {
            Enabled             : false,
            DroppedItem         : false,
            DropRate            : false,
            MatchValue          : false,
            ValuableItemCutoff  : 1000
        }

        this.Techs = {
            Enabled             : false,
            RandomizationMode   : "random",
            Power               : false,
            Cost                : false,
            Accuracy            : false,
            Effect              : false,
            EffectChance        : false,
            TypeEffectiveness   : false,
        }

        this.Starter = {
            Enabled             : false,
            UseWeakestTech      : false,
            Digimon             : "Random",
            Fresh               : false,
            InTraining          : false,
            Rookie              : true,
            Champion            : false,
            Ultimate            : false
        }

        this.Recruitment = {
            Enabled             : false
        }

        this.Chests = {
            Enabled             : false,
            AllowEvolutionItems : false
        }

        this.Tokomon = {
            Enabled             : false,
            ConsumableOnly      : false
        }

        this.TechGifts = {
            Enabled             : false
        }

        this.MapItems = {
            Enabled             : false,
            FoodOnly            : false,
            MatchValue          : false,
            ValuableItemCutoff  : 1000
        }

        this.Evolution = {
            Enabled             : false,
            Requirements        : false,
            SpecialEvolutions   : false,
            ObtainAllMode       : false
        }

        this.Patches = {
            Enabled             : false,
            EvoItemStatGain     : false,
            QuestItemsDroppable : false,
            BrainTrainTierOne   : false,
            JukeboxGlitch       : false,
            IncreaseLearnChance : false,
            SpawnRateEnabled    : false,
            SpawnRate           : SpawnRateDefault,
            ShowHashIntro       : false,
            SkipIntro           : false,
            Woah                : false,
            Gabu                : false,
            Softlock            : false,
            UnlockAreas         : false,
            UnrigSlots          : false,
            LearnMoveAndCommand : false,
            FixDVChips          : false,
            HappyVending        : false,
        }

        if( raw ) {
            this.fromJSON( raw )
        }
    }

    /* Public Variables */
    public General          : GeneralSettings
    public Digimon          : DigimonSettings
    public Techs            : TechSettings
    public Starter          : StarterSettings
    public Recruitment      : RecruitmentSettings
    public Chests           : ChestSettings
    public Tokomon          : TokomonSettings
    public TechGifts        : TechGiftSettings
    public MapItems         : MapItemSettings
    public Evolution        : EvolutionSettings
    public Patches          : PatchSettings

    fromJSON = ( json: string ) => {
        const data = JSON.parse( json ) as RawSettings

        this.General        = { 
            ...data.general, 
            OutputFile: path.parse( data.general.OutputFile ).base
        }
        this.Digimon        = data.digimon
        this.Techs          = data.techs      
        this.Starter        = data.starter
        this.Recruitment    = data.recruitment
        this.Chests         = data.chests     
        this.Tokomon        = data.tokomon    
        this.TechGifts      = data.techGifts  
        this.MapItems       = data.mapItems   
        this.Evolution      = data.evolution  
        this.Patches        = data.patches

        if( !this.Starter.Digimon ) {
            this.Starter.Digimon = "Random"
        }
    }

    toJSON = (): string => {
        let outPath = path.join( path.parse( this.General.InputFile ).dir, this.General.OutputFile )
        if( path.parse( outPath ).ext !== ".bin" ) {
            outPath = outPath + ".bin"
        }

        let raw: RawSettings = {
            general         : {
                ...this.General,
                OutputFile: outPath
            },
            digimon         : this.Digimon,
            techs           : this.Techs,      
            starter         : this.Starter,    
            recruitment     : this.Recruitment,
            chests          : this.Chests,     
            tokomon         : this.Tokomon,    
            techGifts       : this.TechGifts,  
            mapItems        : this.MapItems,   
            evolution       : this.Evolution,  
            patches         : this.Patches
        }

        if( !raw.starter.Digimon ) {
            raw.starter.Digimon = "Random"
        }

        if( !this.Starter.Fresh
         && !this.Starter.InTraining
         && !this.Starter.Rookie
         && !this.Starter.Champion
         && !this.Starter.Ultimate ) {
             raw.starter.Rookie = true
         }

        raw.general.Hash = hash( raw, { algorithm: "md5", excludeKeys: ( key: any ) => {
            if( key == "InputFile" || key == "OutputFile" || key == "Hash" ) {
                return true
            }
            return false
        } } )

        this.General.Hash = raw.general.Hash

        return JSON.stringify( raw, null, '\t' )
    }
}
