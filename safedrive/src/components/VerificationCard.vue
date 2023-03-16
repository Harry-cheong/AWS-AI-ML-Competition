<template>
  <v-container fluid>
    <v-card class="pa-2 ma-2" width="300px">
      <v-card-title class="text--primary text-center"
        >Verify to proceed</v-card-title
      >

      <v-img
        width="300"
        :aspect-ratio="1"
        src="data:image/png;base64,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"
      ></v-img>

      <div>
        <v-text-field
          :value="passwordHidden"
          v-model="password"
          label="Password"
        ></v-text-field>
      </div>

      <div class="d-flex justify-space-around align-center">
        <v-btn @click="checkPwd">Confirm</v-btn>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import pwd from "../data/pwd.json";

export default {
  inject: {
    username: {
      default: "default",
    },
  },
  emits: ["verify-success"],

  data() {
    return {
      password: "",
    };
  },

  computed: {
    passwordHidden() {
      return this.password.replace(/./g, "*");
    },
  },

  methods: {
    checkPwd() {
      const verifyPassword = pwd.find(
        (user) => user.user === this.username.toLowerCase()
      )?.vaultpwd;
      // console.log(verifyPassword);
      if (this.password === verifyPassword) {
        console.log("Verification Success");
        this.$emit("verify-success");
      } else {
        this.password = "";
      }
    },
  },
};
</script>
