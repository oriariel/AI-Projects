import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, DashboardComponent], 
  templateUrl: './app.html', // 👈 Verify it points to ./app.html
  styleUrl: './app.css'      // 👈 Verify it points to ./app.css
})
export class AppComponent {
  title = 'smartflow-frontend';
}