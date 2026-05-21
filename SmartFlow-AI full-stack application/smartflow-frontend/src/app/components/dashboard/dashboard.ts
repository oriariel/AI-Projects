import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { WorkflowService, WorkflowAnalysis } from '../../services/workflow.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dashboard.html', // 👈 Links to your dashboard.html file
  styleUrl: './dashboard.css'     // 👈 Links to your dashboard.css file
})
export class DashboardComponent { // 👈 This MUST be exported exactly like this
  userInput: string = '';
  loading: boolean = false;
  analysisResult: WorkflowAnalysis | null = null;
  errorMessage: string = '';

  constructor(private workflowService: WorkflowService) {}

  submitProcess() {
    if (!this.userInput.trim()) return;

    this.loading = true;
    this.errorMessage = '';
    this.analysisResult = null;

    this.workflowService.analyzeProcess(this.userInput).subscribe({
      next: (data) => {
        this.analysisResult = data;
        this.loading = false;
      },
      error: (err) => {
        this.errorMessage = 'Failed to analyze process. Please try again.';
        this.loading = false;
        console.error(err);
      }
    });
  }
}