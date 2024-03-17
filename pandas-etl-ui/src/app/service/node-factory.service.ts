import { Injectable } from '@angular/core';
import { AllActionsState, NodeSpecs } from '../interfaces/node-specs';
import { BehaviorSubject } from 'rxjs';
import { IconName, IconPrefix } from '@fortawesome/free-solid-svg-icons';
import { ApiService } from './api.service';

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
        icon: ['fas', 'user'],
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
        icon: ['fas', 'coffee'],
      },
       {
        key: 'join',
        name: 'Join',
        inputs: 2,
        outputs: 1,
        allow_multiple_input: true,
        classname: 'processor-node join-node',
        icon: ['far', 'bookmark'],
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
        icon: ['far', 'circle'],
      }
    ]
  }

  constructor(private apiService: ApiService) {
    this.apiService.getData().subscribe(data => {
      this.actionsSubject.next(data);
    });
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
            html: this.getDefaultHTML(action.name, action.icon),
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
      html: this.getDefaultHTML("N/A", null),
    }
  }

  private getDefaultHTML(name: string, icon: [IconPrefix, IconName] | null): string {
    let iconHtml = '';
    if (icon) {
      // not working because it's not controlled after by angular
      iconHtml = `<fa-icon [icon]="['${icon[0]}', '${icon[1]}']"></fa-icon>`;
    }
    return  `
    <div>
      <div class="title-box">
        ${iconHtml}&nbsp;${name}
      </div>
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
