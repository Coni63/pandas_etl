import { ElementRef, Injectable } from '@angular/core';
import Drawflow from 'drawflow';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { TabState } from '../interfaces/tab-state';
import { FormState } from '../interfaces/form-state';
import { NodeFactoryService } from './node-factory.service';

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

  constructor(private nodeFactoryService: NodeFactoryService) { }

  initializeDrawflow(element: HTMLDivElement) {
    this.editor = new Drawflow(element);

    this.addCallbakNodes();
    this.addCallbackConnections();
    this.addCallbackModules();
    this.addCallbackReroute();
    this.addOtherCallbacks();

    this.editor.start();
  }

  getEditor(): Drawflow {
    return this.editor;
  }

  loadPlan(plan: any) {
    let backup = this.editor.export();
    try {
      this.editor.import(plan);
    } catch (error) {
      console.error("Error importing plan", error);
      this.editor.import(backup);
    }
  }

  exportPlan() {
    return this.editor.export();
  }

  getCurrentModulePlan(): any {
    let curr_module = this.editor.module;
    return this.editor.drawflow.drawflow[curr_module].data;
  }

  private updateModulesList() {
    let tabs = Object.keys(this.editor.drawflow.drawflow);
    this.selectedModule = this.editor.module;
    let state = { selectedTab: this.selectedModule, tabs: tabs } as TabState;
    this.tabsSubject.next(state);
    console.log(state);
  }

  addModule(name: string) {
    this.editor.addModule(name);
    this.updateModulesList();
  }

  changeModule(name: string) {
    this.editor.changeModule(name);
    this.updateModulesList();
  }

  removeModule(name: string) {
    this.editor.removeModule(name);
    this.updateModulesList();
  }

  setData(id: string | number, data: any) {
    let currentModule = this.editor.module;
    this.editor.drawflow.drawflow[currentModule].data[id].data = data;

    // Update the node description
    if ("description" in data) {
      let nodeid = "#node-" + id;
      var elem = document.querySelector(nodeid)?.querySelector('[df-description]');
      if (elem) {
        elem.innerHTML = data.description;
      }
    }
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
    let specs = this.nodeFactoryService.getNodeData(data, x, y);
    this.editor.addNode(specs.name, specs.inputs, specs.outputs, specs.posx, specs.posy, specs.classname, specs.data, specs.html, false);
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

      let node = this.editor.getNodeFromId(connection.input_id);
      if (node.class.includes("single-input")) {
        let conns = node.inputs[connection.input_class].connections;
        if (conns.length > 1) {
          this.editor.removeSingleConnection(connection.output_id, connection.input_id, connection.output_class, connection.input_class);
        }
      }
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
