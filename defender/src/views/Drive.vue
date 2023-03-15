<template>
  <container fluid>
    <v-list lines="two">
      <v-list-subheader inset>Sensitive</v-list-subheader>

      <v-list-item
        v-for="file in this.sensitiveFiles"
        :key="file.title"
        :title="file.id"
        :subtitle="file.date"
      >
        <template v-slot:prepend>
          <v-avatar color="grey-lighten-1">
            <v-icon color="white">mdi-file</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn
            color="grey-lighten-1"
            icon="mdi-information"
            variant="text"
          ></v-btn>
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-subheader inset>Files</v-list-subheader>

      <v-list-item
        v-for="file in publicFiles"
        :key="file.id"
        :title="file.title"
        :subtitle="file.date"
      >
        <template v-slot:prepend>
          <v-avatar :color="file.color">
            <v-icon color="white">mdi-file</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn
            color="grey-lighten-1"
            icon="mdi-information"
            variant="text"
          ></v-btn>
        </template>
      </v-list-item>
    </v-list>
  </container>
</template>

<script>
export default {
  data() {
    return {
      files: [
        {
          icon: "mdi-clipboard-text",
          title: "img.png",
          sensitive: true,
          date: "19 Dec 2024",
          id: 1,
        },
        {
          icon: "mdi-information",
          name: "img1.png",
          sensitive: true,
          date: "19 Dec 2024",
          id: 2,
        },
      ],
    };
  },

  computed: {
    publicFiles() {
      return this.files.filter((file) => !file.sensitive);
    },

    sensitiveFiles() {
      return this.files.filter((file) => file.sensitive);
    },
  },
};
</script>
