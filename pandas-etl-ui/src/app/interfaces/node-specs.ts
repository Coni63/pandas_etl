import { IconPrefix, IconName } from '@fortawesome/fontawesome-svg-core';


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
    icon: [IconPrefix, IconName];
}

export interface AllActionsState {
    [key: string]: ActionState[];
}