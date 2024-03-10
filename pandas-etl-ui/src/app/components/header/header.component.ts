import { Component } from '@angular/core';
import { faGithub } from '@fortawesome/free-brands-svg-icons';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent {
  github_icon = faGithub;
  title = "Pandas ETL UI"
  github_url = "https://github.com/Coni63/pandas_etl"
}
