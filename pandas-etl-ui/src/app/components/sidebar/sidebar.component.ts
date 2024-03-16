import { Component, OnInit } from '@angular/core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { Subscription } from 'rxjs';
import { NodeFactoryService } from 'src/app/service/node-factory.service';
import { FontAwesomeModule, FaIconLibrary } from '@fortawesome/angular-fontawesome'

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  actionsSubscription!: Subscription;
  items: any = {}

  constructor(private nodeFactoryService: NodeFactoryService, private library: FaIconLibrary) {
    library.addIconPacks(fas, far);
  }

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
