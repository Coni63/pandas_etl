import { ElementRef, Injectable } from '@angular/core';
import Drawflow from 'drawflow';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { TabState } from '../interfaces/tab-state';
import { FormState } from '../interfaces/form-state';

@Injectable({
  providedIn: 'root'
})
export class DrawflowService {
  editor!: Drawflow;

  private tabsSubject = new BehaviorSubject<TabState>({ selectedTab: '', tabs: [] });
  tabs$ = this.tabsSubject.asObservable();

  private formSubject = new BehaviorSubject<FormState>({ selectedNode: '', data: {} });
  form$ = this.formSubject.asObservable();

  private selectedNode: string | number = '';
  private selectedModule: string = '';


  data = {"drawflow":{"Home":{"data":{"1":{"id":1,"name":"welcome","data":{},"class":"welcome","html":"\n    <div>\n      <div class=\"title-box\">👏 Welcome!!</div>\n      <div class=\"box\">\n        <p>Simple flow library <b>demo</b>\n        <a href=\"https://github.com/jerosoler/Drawflow\" target=\"_blank\">Drawflow</a> by <b>Jero Soler</b></p><br>\n\n        <p>Multiple input / outputs<br>\n           Data sync nodes<br>\n           Import / export<br>\n           Modules support<br>\n           Simple use<br>\n           Type: Fixed or Edit<br>\n           Events: view console<br>\n           Pure Javascript<br>\n        </p>\n        <br>\n        <p><b><u>Shortkeys:</u></b></p>\n        <p>🎹 <b>Delete</b> for remove selected<br>\n        💠 Mouse Left Click == Move<br>\n        ❌ Mouse Right == Delete Option<br>\n        🔍 Ctrl + Wheel == Zoom<br>\n        📱 Mobile support<br>\n        ...</p>\n      </div>\n    </div>\n    ","typenode": false, "inputs":{},"outputs":{},"pos_x":50,"pos_y":50},"2":{"id":2,"name":"slack","data":{},"class":"slack","html":"\n          <div>\n            <div class=\"title-box\"><i class=\"fab fa-slack\"></i> Slack chat message</div>\n          </div>\n          ","typenode": false, "inputs":{"input_1":{"connections":[{"node":"7","input":"output_1"}]}},"outputs":{},"pos_x":1028,"pos_y":87},"3":{"id":3,"name":"telegram","data":{"channel":"channel_2"},"class":"telegram","html":"\n          <div>\n            <div class=\"title-box\"><i class=\"fab fa-telegram-plane\"></i> Telegram bot</div>\n            <div class=\"box\">\n              <p>Send to telegram</p>\n              <p>select channel</p>\n              <select df-channel>\n                <option value=\"channel_1\">Channel 1</option>\n                <option value=\"channel_2\">Channel 2</option>\n                <option value=\"channel_3\">Channel 3</option>\n                <option value=\"channel_4\">Channel 4</option>\n              </select>\n            </div>\n          </div>\n          ","typenode": false, "inputs":{"input_1":{"connections":[{"node":"7","input":"output_1"}]}},"outputs":{},"pos_x":1032,"pos_y":184},"4":{"id":4,"name":"email","data":{},"class":"email","html":"\n            <div>\n              <div class=\"title-box\"><i class=\"fas fa-at\"></i> Send Email </div>\n            </div>\n            ","typenode": false, "inputs":{"input_1":{"connections":[{"node":"5","input":"output_1"}]}},"outputs":{},"pos_x":1033,"pos_y":439},"5":{"id":5,"name":"template","data":{"template":"Write your template"},"class":"template","html":"\n            <div>\n              <div class=\"title-box\"><i class=\"fas fa-code\"></i> Template</div>\n              <div class=\"box\">\n                Ger Vars\n                <textarea df-template></textarea>\n                Output template with vars\n              </div>\n            </div>\n            ","typenode": false, "inputs":{"input_1":{"connections":[{"node":"6","input":"output_1"}]}},"outputs":{"output_1":{"connections":[{"node":"4","output":"input_1"},{"node":"11","output":"input_1"}]}},"pos_x":607,"pos_y":304},"6":{"id":6,"name":"github","data":{"name":"https://github.com/jerosoler/Drawflow"},"class":"github","html":"\n          <div>\n            <div class=\"title-box\"><i class=\"fab fa-github \"></i> Github Stars</div>\n            <div class=\"box\">\n              <p>Enter repository url</p>\n            <input type=\"text\" df-name>\n            </div>\n          </div>\n          ","typenode": false, "inputs":{},"outputs":{"output_1":{"connections":[{"node":"5","output":"input_1"}]}},"pos_x":341,"pos_y":191},"7":{"id":7,"name":"facebook","data":{},"class":"facebook","html":"\n        <div>\n          <div class=\"title-box\"><i class=\"fab fa-facebook\"></i> Facebook Message</div>\n        </div>\n        ","typenode": false, "inputs":{},"outputs":{"output_1":{"connections":[{"node":"2","output":"input_1"},{"node":"3","output":"input_1"},{"node":"11","output":"input_1"}]}},"pos_x":347,"pos_y":87},"11":{"id":11,"name":"log","data":{},"class":"log","html":"\n            <div>\n              <div class=\"title-box\"><i class=\"fas fa-file-signature\"></i> Save log file </div>\n            </div>\n            ","typenode": false, "inputs":{"input_1":{"connections":[{"node":"5","input":"output_1"},{"node":"7","input":"output_1"}]}},"outputs":{},"pos_x":1031,"pos_y":363}}},"Other":{"data":{"8":{"id":8,"name":"personalized","data":{},"class":"personalized","html":"\n            <div>\n              Personalized\n            </div>\n            ","typenode": false, "inputs":{"input_1":{"connections":[{"node":"12","input":"output_1"},{"node":"12","input":"output_2"},{"node":"12","input":"output_3"},{"node":"12","input":"output_4"}]}},"outputs":{"output_1":{"connections":[{"node":"9","output":"input_1"}]}},"pos_x":764,"pos_y":227},"9":{"id":9,"name":"dbclick","data":{"name":"Hello World!!"},"class":"dbclick","html":"\n            <div>\n            <div class=\"title-box\"><i class=\"fas fa-mouse\"></i> Db Click</div>\n              <div class=\"box dbclickbox\" ondblclick=\"showpopup(event)\">\n                Db Click here\n                <div class=\"modal\" style=\"display:none\">\n                  <div class=\"modal-content\">\n                    <span class=\"close\" onclick=\"closemodal(event)\">&times;</span>\n                    Change your variable {name} !\n                    <input type=\"text\" df-name>\n                  </div>\n\n                </div>\n              </div>\n            </div>\n            ","typenode": false, "inputs":{"input_1":{"connections":[{"node":"8","input":"output_1"}]}},"outputs":{"output_1":{"connections":[{"node":"12","output":"input_2"}]}},"pos_x":209,"pos_y":38},"12":{"id":12,"name":"multiple","data":{},"class":"multiple","html":"\n            <div>\n              <div class=\"box\">\n                Multiple!\n              </div>\n            </div>\n            ","typenode": false, "inputs":{"input_1":{"connections":[]},"input_2":{"connections":[{"node":"9","input":"output_1"}]},"input_3":{"connections":[]}},"outputs":{"output_1":{"connections":[{"node":"8","output":"input_1"}]},"output_2":{"connections":[{"node":"8","output":"input_1"}]},"output_3":{"connections":[{"node":"8","output":"input_1"}]},"output_4":{"connections":[{"node":"8","output":"input_1"}]}},"pos_x":179,"pos_y":272}}}}}

  constructor() { }

  initializeDrawflow(element: HTMLDivElement) {
    this.editor = new Drawflow(element);

    this.addCallbakNodes();
    this.addCallbackConnections();
    this.addCallbackModules();
    this.addCallbackReroute();
    this.addOtherCallbacks();

    this.editor.start();
    this.editor.import(this.data);

  }

  getEditor(): Drawflow {
    return this.editor;
  }

  private updateModulesList() {
    let data = this.editor.export();
    this.selectedModule = this.editor.module;
    let state = { selectedTab: this.selectedModule, tabs: Object.keys(data.drawflow) } as TabState;
    this.tabsSubject.next(state);
    console.log(state);
  }

  addModule(name: string) {
    let data = this.editor.export();
    this.editor.addModule(name);
    this.selectedModule = this.editor.module;
    let state = { selectedTab: this.selectedModule, tabs: Object.keys(data.drawflow) } as TabState;
    this.tabsSubject.next(state);
  }

  changeModule(name: string) {
    this.editor.changeModule(name);
    this.updateModulesList();
  }

  setData(id: string | number, data: any) {
    let currentModule = this.editor.module;
    this.editor.drawflow.drawflow[currentModule].data[id].data = data;
  }

  zoomIn() {
    this.editor.zoom_in();
  }

  zoomOut() {
    this.editor.zoom_out();
  }

  zoomReset() {
    this.editor.zoom_reset();
  }

  clear() {
    this.editor.clearModuleSelected();
  }

  setEditorMode(locked: boolean) {
    this.editor.editor_mode = locked ? 'fixed' : 'edit';
  }

  addNode(data: string, x: number, y: number) {
    let html = `
    <div>
      <div class="title-box"><i class="fab fa-github "></i> Github Stars</div>
      <div class="box">
        <p class="box-key">Description:</p>
        <p class="box-value"><input type="text" df-description></p>
        <p class="box-btn"><button class="open-modal"></p>
      </div>
    </div>
    `;
    html = '<app-foo>sdf</app-foo>'
    this.editor.addNode("node", 1, 1, x, y, "class", {}, html, false);
  }

  addCallbakNodes() {
    this.editor.on('nodeCreated', (id) => {
      console.log("Node created " + id);
    });

    this.editor.on('nodeRemoved', (id) => {
      console.log("Node removed " + id);
      this.selectedNode = '';
    });

    this.editor.on("nodeDataChanged", (data) => {
      console.log("Edit Data");
      console.log(this.selectedNode, data);
    });

    this.editor.on('nodeSelected', (id) => {
      console.log("Node selected " + id);
      this.selectedNode = id;
      this.formSubject.next({ selectedNode: id, data: this.editor.getNodeFromId(id).data});
    });

    this.editor.on('nodeUnselected', (id) => {
      console.log("Node unselected " + id);
      this.selectedNode = '';
      this.formSubject.next({ selectedNode: '', data: {}});
    });

    this.editor.on('nodeMoved', (id) => {
      console.log("Node moved " + id);
      this.selectedNode = id;
    });
  }

  addCallbackConnections() {
    this.editor.on('connectionCreated', (connection) => {
      console.log('Connection created');
      console.log(connection);
    });

    this.editor.on('connectionRemoved', (connection) => {
      console.log('Connection removed');
      console.log(connection);
    });
  }

  addCallbackModules() {
    this.editor.on('moduleCreated', (name) => {
      console.log("Module Created " + name);
      this.updateModulesList();
    });

    this.editor.on('moduleChanged', (name) => {
      console.log("Module Changed " + name);

    });

    this.editor.on('moduleRemoved', (name) => {
      console.log('Module Removed ' + name);
    });
  }

  addCallbackReroute() {
    this.editor.on('addReroute', (id) => {
      console.log("Reroute added " + id);
    });

    this.editor.on('removeReroute', (id) => {
      console.log("Reroute removed " + id);
    });
  }

  addOtherCallbacks() {
    this.editor.on('mouseMove', (position) => {
      // console.log('Position mouse x:' + position.x + ' y:'+ position.y);
    });


    this.editor.on('zoom', (zoom) => {
      console.log('Zoom level ' + zoom);
    });

    this.editor.on('translate', (position) => {
      // console.log('Translate x:' + position.x + ' y:'+ position.y);
    });


    this.editor.on('import', () => {
      console.log("Import");
      this.updateModulesList();
    });

    this.editor.on('export', () => {
      // console.log("Export");
    });
  }


}
