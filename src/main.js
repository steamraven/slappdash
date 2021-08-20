import {createApp} from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config'
import  InputText from  'primevue/inputtext';
import Button from 'primevue/button';
import 'primevue/resources/themes/mdc-light-indigo/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';



const app = createApp(App);
app.use(PrimeVue);
app.component("InputText", InputText);
app.component("Button", Button);
app.mount("#app")
