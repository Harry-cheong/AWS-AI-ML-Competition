import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import "@mdi/font/css/materialdesignicons.css";

import App from "./App.vue";
import Drive from "./views/Drive";
import Vault from "./views/Vault";
import Upload from "./views/Upload";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/drive" },
    { path: "/drive", component: Drive },
    { path: "/vault", component: Vault },
    { path: "/upload", component: Upload },
  ],

  scrollBehaviour(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }
    return { left: 0, top: 0 };
  },
});

const vuetify = createVuetify({
  components,
  directives,
});
const app = createApp(App);

app.use(router);
app.use(vuetify);
app.mount("#app");
