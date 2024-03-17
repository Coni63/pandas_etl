import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AllActionsState } from '../interfaces/node-specs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) { }

  getData(): Observable<AllActionsState> {
    return this.http.get<AllActionsState>(`${this.baseUrl}/actions`);
  }

  // Example method to send data to FastAPI backend
  sendPlan(data: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/start`, data);
  }
}
