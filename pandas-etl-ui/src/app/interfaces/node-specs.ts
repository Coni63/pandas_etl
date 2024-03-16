export interface NodeSpecs {
    name: string;
    inputs: number;
    outputs: number;
    allow_multiple_input: boolean;
    posx: number;
    posy: number;
    classname: string;
    data: any;
    html: string;
}


export interface ActionState {
    key: string;
    name: string;
    inputs: number;
    outputs: number;
    allow_multiple_input: boolean;
    classname: string;
}

export interface AllActionsState {
    [key: string]: ActionState[];
}