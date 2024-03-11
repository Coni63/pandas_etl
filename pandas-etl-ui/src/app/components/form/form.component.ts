import { Component } from '@angular/core';
import { DrawflowService } from 'src/app/service/drawflow.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.scss']
})
export class FormComponent {
  isOpen = true;
  params: any = {};
  selectedNode: any;
  formSubscription: any;
  validJson = true;

  constructor(private drawflowService: DrawflowService) { }

  ngOnInit() {
    this.formSubscription = this.drawflowService.form$.subscribe(state => {
      // this.isOpen = state.selectedNode !== '';
      this.selectedNode = state.selectedNode;
      this.params = JSON.stringify(state.data, null, 2);
    });
  }

  save() {
    this.drawflowService.setData(this.selectedNode, JSON.parse(this.params));
  }

  formatJson() {
    try {
      // Parse JSON to object to properly format it
      this.params = JSON.stringify(JSON.parse(this.params), null, 4);
      this.validJson = true;
    } catch (error) {
      this.validJson = false;
    }
  }
}
