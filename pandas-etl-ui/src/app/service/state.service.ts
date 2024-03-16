import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StateService {

  constructor() { }

  saveState(data: any) {
    localStorage.setItem('cacheState', JSON.stringify(data));
  }

  loadState(): any {
    const data = localStorage.getItem('cacheState');
    return data ? JSON.parse(data) : null;
  }
}
