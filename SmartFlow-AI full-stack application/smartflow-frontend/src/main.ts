import 'zone.js';
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component'; // 👈 Fixed import path and class name

bootstrapApplication(AppComponent, appConfig) // 👈 Bootstrapping AppComponent instead of App
  .catch((err) => console.error(err));