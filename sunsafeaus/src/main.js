import './assets/main.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from "./router";

const app = createApp(App);

// Set the default browser tab title
document.title = "SunSafeAus"; // Change this to your desired title

// Dynamically set the favicon from the assets folder
const link = document.createElement("link");
link.rel = "icon";
link.type = "image/png";  // Ensure it's a PNG format
link.href = new URL('./assets/logo.png', import.meta.url).href; // Correct path resolution for Vite
document.head.appendChild(link);

app.use(router);
app.mount('#app'); 