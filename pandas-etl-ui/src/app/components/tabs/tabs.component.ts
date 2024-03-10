import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { DrawflowService } from '../../service/drawflow.service';
import { TabState } from '../../interfaces/tab-state';

@Component({
  selector: 'app-tabs',
  templateUrl: './tabs.component.html',
  styleUrls: ['./tabs.component.scss']
})
export class TabsComponent {
  tabs: TabState = { selectedTab: '', tabs: [] };
  private tabsSubscription!: Subscription;

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
}
