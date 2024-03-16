import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { DrawflowService } from '../../service/drawflow.service';
import { TabState } from '../../interfaces/tab-state';
import { faTimes, faPlus } from '@fortawesome/free-solid-svg-icons';


@Component({
  selector: 'app-tabs',
  templateUrl: './tabs.component.html',
  styleUrls: ['./tabs.component.scss']
})
export class TabsComponent {
  tabs: TabState = { selectedTab: '', tabs: [] };
  private tabsSubscription!: Subscription;
  remove_icon = faTimes
  add_icon = faPlus;

  constructor(private drawflowService: DrawflowService) { }

  ngOnInit() {
    this.tabsSubscription = this.drawflowService.tabs$.subscribe(tabs => {
      this.tabs = tabs;
    });
  }

  ngOnDestroy() {
    this.tabsSubscription.unsubscribe();
  }

  changeTab(tab: string) {
    this.drawflowService.changeModule(tab);
  }

  addTab() {
    let name = prompt('Enter the name of the new module');
    if (name) {
      if (this.tabs.tabs.includes(name)) {
        alert('Module name already exists');
        return;
      }
      this.drawflowService.addModule(name);
    }
  }

  removeTab() {
    let confirm = window.confirm('Are you sure you want to delete this module?');
    if (confirm) {
      this.drawflowService.removeModule(this.tabs.selectedTab);
    }
  }
}
