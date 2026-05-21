import 'zone.js';
import { BootstrapContext, bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component'; // 👈 Fixed import path and class name
import { config } from './app/app.config.server';

const bootstrap = (context: BootstrapContext) =>
    bootstrapApplication(AppComponent, config, context); // 👈 Fixed reference to AppComponent

export default bootstrap;