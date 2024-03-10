import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import Drawflow from 'drawflow'
import { faLock, faLockOpen, faMagnifyingGlassPlus, faMagnifyingGlassMinus, faMagnifyingGlass, faEraser } from '@fortawesome/free-solid-svg-icons';
import { DrawflowService } from '../../service/drawflow.service';

@Component({
  selector: 'app-drawflow',
  templateUrl: './drawflow.component.html',
  styleUrls: ['./drawflow.component.scss']
})
export class DrawflowComponent implements OnInit {
  @ViewChild('drawflow', {static: true}) drawflowDiv!: ElementRef<HTMLDivElement>;

  zoom_in_icon = faMagnifyingGlassPlus;
  zoom_out_icon = faMagnifyingGlassMinus;
  zoom_reset_icon = faMagnifyingGlass;
  lock_icon = faLock
  unlock_icon = faLockOpen
  eraser_icon = faEraser

  lock = false;
  editor!: Drawflow;


  constructor(private drawflowService: DrawflowService) { }

  ngOnInit() {
    const id = this.drawflowDiv.nativeElement;
    this.drawflowService.initializeDrawflow(id);
  }

  toogleLock() {
    this.lock = !this.lock;
    this.drawflowService.setEditorMode(this.lock);
  }

  zoomIn() {
    this.drawflowService.zoomIn();
  }

  zoomOut() {
    this.drawflowService.zoomOut();
  }

  zoomReset() {
    this.drawflowService.zoomReset();
  }

  clear() {
    this.drawflowService.clear();
  }

  drop(event: DragEvent) {
    if (event.type === "drop") {
      let x = event.offsetX;
      let y = event.offsetY;
      const data = event.dataTransfer?.getData("text");

      if (data) {
        console.log(data);
        // addNodeToDrawFlow(mobile_item_selec, mobile_last_move.touches[0].clientX, mobile_last_move.touches[0].clientY);
        this.drawflowService.addNode(data, x, y);
      }
    }
  }

  allowDrop(event: DragEvent) {
    event.preventDefault();
  }

}
