import { Injectable } from '@angular/core';
import { NodeSpecs } from '../interfaces/node-specs';

@Injectable({
  providedIn: 'root'
})
export class NodeFactoryService {

  constructor() { }

  getNodeData(nodeType: string, posx: number, posy: number): NodeSpecs {
    switch (nodeType) {
      case 'facebook':
        return {
          name: 'ReadCSV',
          inputs: 0,
          outputs: 1,
          allow_multiple_input: false,
          posx: posx,
          posy: posy,
          classname: 'extractor-node',
          data: this.getDefaultData(),
          html: this.getDefaultHTML(),
        };
      case 'log':
        return {
          name: 'Log',
          inputs: 1,
          outputs: 1,
          allow_multiple_input: true,
          posx: posx,
          posy: posy,
          classname: 'processor-node',
          data: this.getDefaultData(),
          html: this.getDefaultHTML(),
        };
      case 'join':
        return {
          name: 'Join',
          inputs: 2,
          outputs: 1,
          allow_multiple_input: true,
          posx: posx,
          posy: posy,
          classname: 'processor-node join-node',
          data: this.getDefaultData(),
          html: this.getDefaultHTML(),
        };
      default: {
        return {
          name: 'GithubStars',
          inputs: 1,
          outputs: 0,
          allow_multiple_input: false,
          posx: posx,
          posy: posy,
          classname: 'loader-node single-input',
          data: this.getDefaultData(),
          html: this.getDefaultHTML(),
        };
      }
    }
  }

  private getDefaultHTML(): string {
    return  `
    <div>
      <div class="title-box"><i class="fab fa-github "></i> Github Stars</div>
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
