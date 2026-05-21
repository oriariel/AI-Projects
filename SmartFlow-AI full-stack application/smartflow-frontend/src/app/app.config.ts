import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { provideZoneChangeDetection as provideZone } from '@angular/core'; // 👈 Import zone provider explicitly

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    // Change your zone provider line to use explicit zone-based change detection:
    provideZoneChangeDetection({ eventCoalescing: true }), 
    provideRouter(routes),
    provideHttpClient(withFetch())
  ]
};