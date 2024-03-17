import { Component } from '@angular/core';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import { faDownload, faPlay, faUpload } from '@fortawesome/free-solid-svg-icons';
import { ApiService } from 'src/app/service/api.service';
import { DrawflowService } from 'src/app/service/drawflow.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent {
  github_icon = faGithub;
  export_icon = faDownload;
  import_icon = faUpload;
  run_icon = faPlay;
  title = "Pandas ETL UI"
  github_url = "https://github.com/Coni63/pandas_etl"

  constructor(private drawflowService: DrawflowService, private apiService: ApiService) { }

  exportPlan() {
    let filename = prompt("Enter the filename", "data.json");
    if (filename == null || filename == "") {
      console.log("User cancelled the prompt.")
      return;
    }

    if (!filename.endsWith(".json")) {
      filename += ".json";
    }

    console.log("exporting plan")
    let plan = this.drawflowService.exportPlan();
    const jsonData = JSON.stringify(plan);
    const blob = new Blob([jsonData], { type: 'application/json' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'data.json';
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
  }

  importPlan(event: any) {
    console.log("importing plan")
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e: any) => {
      const jsonData = JSON.parse(e.target.result);
      this.drawflowService.loadPlan(jsonData);
    };
    reader.readAsText(file);
  }

  runPlan() {
    console.log("running plan")
    console.log(this.drawflowService.getCurrentModulePlan());
    this.apiService.sendPlan(this.drawflowService.getCurrentModulePlan()).subscribe(response => {
      console.log(response);
    });
  }
}
