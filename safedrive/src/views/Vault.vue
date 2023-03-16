<template>
  <verification-card
    v-if="!verified"
    @verify-success="verified = true"
  ></verification-card>
  <v-list v-else lines="two">
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
  </v-list>
</template>

<script>
import files from "../data/files.json";
import VerificationCard from "../components/VerificationCard";
export default {
  components: {
    VerificationCard,
  },

  computed: {
    sensitiveFiles() {
      return files.filter((file) => file.sensitive);
    },
  },

  data() {
    return {
      verified: false,
    };
  },
};
</script>
