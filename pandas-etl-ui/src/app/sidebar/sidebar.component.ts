import { Component } from '@angular/core';
import { faLockOpen } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent {
  unlock_icon = faLockOpen;

  drag(event: DragEvent, dataNode: string) {
    event.dataTransfer!.clearData();
    event.dataTransfer!.setData("text/plain", dataNode);
  }
}
