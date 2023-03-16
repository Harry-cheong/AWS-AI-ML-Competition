<template>
  <container fluid>
    <v-list lines="two">
      <!-- <v-list-subheader inset>Sensitive</v-list-subheader>

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
      </v-list-item> -->

      <!-- <v-divider inset></v-divider> -->

      <v-list-subheader inset>Files</v-list-subheader>

      <v-list-item
        v-for="file in publicFiles"
        :key="file.id"
        :title="file.name"
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
    </v-list>
  </container>
</template>

<script>
import files from "../data/files.json";

export default {
  data() {
    return {
      files: files,
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
