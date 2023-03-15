<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :rail="rail"
      permanent
      @click="rail = !rail"
    >
      <v-list-item
        prepend-avatar="https://images.unsplash.com/photo-1594003715326-f6030861574e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c2NlbmVyeSUyMHdhbGxwYXBlcnxlbnwwfHwwfHw%3D&w=1000&q=80"
        title="Harry"
        nav
      >
        <template v-slot:append>
          <v-btn
            variant="text"
            icon="mdi-chevron-left"
            @click.stop="rail = !rail"
          ></v-btn>
        </template>
      </v-list-item>

      <v-divider></v-divider>

      <v-list density="compact">
        <v-list-item
          v-for="item in items"
          :prepend-icon="item.icon"
          :title="item.title"
          :value="item.value"
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar>
      <v-toolbar-title class="center-align" dark>SafeDrive</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Vue from "vue";

export default {
  data() {
    return {
      drawer: true,
      rail: true,
      items: [
        { title: "Home", icon: "mdi-home-city", value: "home" },
        { title: "Drive", icon: "mdi-account", value: "drive" },
      ],
    };
  },

  methods: {},
};
</script>
