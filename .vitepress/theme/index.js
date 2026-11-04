import PrimaryTheme from 'primary-vitepress'
import DonateLayout from './DonateLayout.vue'
import './override.css'

export default {
  ...PrimaryTheme,
  // Use your wrapper layout that includes both primary-vitepress and the donation modal
  Layout: DonateLayout,
  enhanceApp(ctx) {
    // If primary-vitepress has its own enhanceApp function, call it so you don't break its functionality
    if (PrimaryTheme.enhanceApp) {
      PrimaryTheme.enhanceApp(ctx)
    }
  }
}
