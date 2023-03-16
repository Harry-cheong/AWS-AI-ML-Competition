<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :rail="rail"
      permanent
      @click="rail = false"
    >
      <v-list-item
        class="pa-2"
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
          :title="item.title"
          :value="item.value"
          :to="item.routeName"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>
        </v-list-item>
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
export default {
  provide() {
    return {
      username: "Harry",
    };
  },

  data() {
    return {
      drawer: true,
      rail: true,
      items: [
        {
          title: "Upload",
          icon: "mdi-plus",
          value: "upload",
          routeName: "upload",
        },
        {
          title: "Drive",
          icon: "mdi-cloud",
          value: "drive",
          routeName: "drive",
        },
        {
          title: "Vault",
          icon: "mdi-lock-outline",
          value: "vault",
          routeName: "vault",
        },
      ],
      user: "Harry",
    };
  },

  methods: {},
};
</script>
