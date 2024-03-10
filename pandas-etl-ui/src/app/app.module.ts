import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DrawflowComponent } from './components/drawflow/drawflow.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { HeaderComponent } from './components/header/header.component';
import { TabsComponent } from './components/tabs/tabs.component';
import { DrawflowService } from './service/drawflow.service';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { MainpageComponent } from './components/mainpage/mainpage.component';

@NgModule({
  declarations: [
    AppComponent,
    DrawflowComponent,
    HeaderComponent,
    TabsComponent,
    SidebarComponent,
    MainpageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule
  ],
  providers: [
    DrawflowService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
