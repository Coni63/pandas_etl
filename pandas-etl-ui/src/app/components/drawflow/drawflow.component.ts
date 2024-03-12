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
        this.drawflowService.addNode(data, x, y);

        document.querySelectorAll('.open-modal').forEach((element: Element) => {
          let elem = element as HTMLElement;

          elem.removeEventListener('click', () => {});

          elem.addEventListener('click', () => {
            console.log('open modal');
            // Add your modal opening logic here
          });
        });
      }
    }
  }

  allowDrop(event: DragEvent) {
    event.preventDefault();
  }

}
