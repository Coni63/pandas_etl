import { Component, OnInit } from '@angular/core';
import { faLockOpen } from '@fortawesome/free-solid-svg-icons';
import { Subscription } from 'rxjs';
import { NodeFactoryService } from 'src/app/service/node-factory.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  unlock_icon = faLockOpen;
  actionsSubscription!: Subscription;
  items: any = {}

  constructor(private nodeFactoryService: NodeFactoryService) {  }

  ngOnInit() {
    this.actionsSubscription = this.nodeFactoryService.actions$.subscribe(data => {
      this.items = data;
      console.log(this.items);
    });
  }

  drag(event: DragEvent, dataNode: string) {
    event.dataTransfer!.clearData();
    event.dataTransfer!.setData("text/plain", dataNode);
  }
}
