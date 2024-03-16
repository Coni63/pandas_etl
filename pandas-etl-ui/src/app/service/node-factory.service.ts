import { Injectable } from '@angular/core';
import { AllActionsState, NodeSpecs } from '../interfaces/node-specs';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NodeFactoryService {

  private actionsSubject = new BehaviorSubject<AllActionsState>({
    "extractors":[],
    "processors": [],
    "loaders": []
  });
  actions$ = this.actionsSubject.asObservable();

  data: AllActionsState = {
    "extractors":[
      {
        key: 'facebook',
        name: 'ReadCSV',
        inputs: 0,
        outputs: 1,
        allow_multiple_input: false,
        classname: 'extractor-node',
      }
    ],
    "processors": [
      {
        key: 'log',
        name: 'Log',
        inputs: 1,
        outputs: 1,
        allow_multiple_input: true,
        classname: 'processor-node',
      },
       {
        key: 'join',
        name: 'Join',
        inputs: 2,
        outputs: 1,
        allow_multiple_input: true,
        classname: 'processor-node join-node',
      }
    ],
    "loaders": [
      {
        key: 'github',
        name: 'GithubStars',
        inputs: 1,
        outputs: 0,
        allow_multiple_input: false,
        classname: 'loader-node single-input',
      }
    ]
  }

  constructor() {
    this.getActions();
  }

  getActions() {
    this.actionsSubject.next(this.data);
  }

  getNodeData(nodeType: string, posx: number, posy: number): NodeSpecs {
    for (let type of ["extractors", "processors", "loaders"]) {
      let actions = this.data[type];
      for (let action of actions) {
        if (action.key === nodeType) {
          return {
            name: action.name,
            inputs: action.inputs,
            outputs: action.outputs,
            allow_multiple_input: action.allow_multiple_input,
            posx: posx,
            posy: posy,
            classname: action.classname,
            data: this.getDefaultData(),
            html: this.getDefaultHTML(action.name),
          }
        }

      }
    }
    return {
      name: "N/A",
      inputs: 0,
      outputs: 0,
      allow_multiple_input: false,
      posx: posx,
      posy: posy,
      classname: "simple-node",
      data: this.getDefaultData(),
      html: this.getDefaultHTML("N/A"),
    }
  }

  private getDefaultHTML(name: string): string {
    return  `
    <div>
      <div class="title-box"><i class="fab fa-github "></i> ${name}</div>
      <div class="box">
        <p class="box-key" df-description>Description</p>
      </div>
    </div>
    `;
  }

  private getDefaultData(): any {
    return {"description": "Description"};
  }
}
