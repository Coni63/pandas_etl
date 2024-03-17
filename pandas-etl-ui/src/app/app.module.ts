import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DrawflowComponent } from './components/drawflow/drawflow.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { HeaderComponent } from './components/header/header.component';
import { TabsComponent } from './components/tabs/tabs.component';
import { DrawflowService } from './service/drawflow.service';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { MainpageComponent } from './components/mainpage/mainpage.component';
import { FormComponent } from './components/form/form.component';
import { FormsModule } from '@angular/forms';
import { StateService } from './service/state.service';

@NgModule({
  declarations: [
    AppComponent,
    DrawflowComponent,
    HeaderComponent,
    TabsComponent,
    SidebarComponent,
    MainpageComponent,
    FormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    DrawflowService,
    StateService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
