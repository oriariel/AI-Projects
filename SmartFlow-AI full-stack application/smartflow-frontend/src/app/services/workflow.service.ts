import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface WorkflowStep {
  id: number;
  title: string;
  actor: string;
  description: string;
  next_step_ids: number[];
}

export interface WorkflowAnalysis {
  process_name: string;
  summary: string;
  steps: WorkflowStep[];
  potential_bottlenecks: string[];
  ai_automation_suggestions: string[];
}

@Injectable({
  providedIn: 'root'
})
export class WorkflowService {
  private apiUrl = 'http://127.0.0.1:8000/api/analyze-process'; // 👈 Using explicit 127.0.0.1 instead of localhost
  constructor(private http: HttpClient) {}

  analyzeProcess(description: string): Observable<WorkflowAnalysis> {
    return this.http.post<WorkflowAnalysis>(this.apiUrl, { description });
  }
}