<template>
  <div>
    <v-row no-gutters justify="center" align="center">
      <v-col cols="8">
        <v-file-input
          show-size
          label="File input"
          @change="selectFile"
        ></v-file-input>
      </v-col>

      <v-col cols="4" class="pl-2">
        <v-btn color="success" dark small @click="upload">
          Upload
          <v-icon right dark>mdi-cloud-upload</v-icon>
        </v-btn>
      </v-col>
    </v-row>

    <v-alert v-if="message" border="left" color="blue-grey" dark>
      {{ message }}
    </v-alert>

    <!-- <v-card v-if="fileInfos.length > 0" class="mx-auto">
      <v-list>
        <v-subheader>List of Files</v-subheader>
        <v-list-item-group color="primary">
          <v-list-item v-for="(file, index) in fileInfos" :key="index">
            <a :href="file.url">{{ file.name }}</a>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card> -->
  </div>

  <v-divider></v-divider>

  <v-card v-if="currentFile" class="ma-4">
    <v-card-title class="text-center">File Status</v-card-title>
    <v-divider incest></v-divider>
    <div v-if="currentFile" class="pa-3">
      <div class="text-center">
        <div v-if="!uploaded">
          <p3>
            Uploading Files...
            <v-progress-circular
              indeterminate
              color="blue"
            ></v-progress-circular>
            <v-btn @click="uploaded = true">Resolve</v-btn>
          </p3>
        </div>

        <div v-else class="align-center">
          <p3> Uploaded <v-icon icon="mdi-check" color="green"></v-icon></p3>
        </div>

        <div v-if="uploaded && !malwareCheck">
          <p3>
            Checking for Malware...
            <v-progress-circular
              indeterminate
              color="blue"
            ></v-progress-circular>
            <div>
              <v-btn @click="malwareCheck = true">Resolve</v-btn>
            </div>
          </p3>
        </div>
        <div v-else-if="malwareCheck" class="align-center">
          <p3> File Secure <v-icon icon="mdi-check" color="green"></v-icon></p3>
        </div>

        <div v-if="malwareCheck && !sensitiveCheck">
          <p3>
            Checking for Malware...
            <v-progress-circular
              indeterminate
              color="blue"
            ></v-progress-circular>
            <v-btn
              @click="
                sensitiveCheck = true;
                reset();
              "
              >Resolve</v-btn
            >
          </p3>
        </div>
        <div v-else-if="sensitiveCheck" class="align-center">
          <p3> PII Removed <v-icon icon="mdi-check" color="green"></v-icon></p3>
        </div>
      </div>
    </div>
  </v-card>
</template>

<script>
import AWS from "aws-sdk";
import axios from "axios";

export default {
  name: "upload-files",
  data() {
    return {
      currentFile: undefined,
      message: "",

      // File status
      uploaded: false,
      malwareCheck: false,
      sensitiveCheck: false,
    };
  },

  methods: {
    selectFile(file) {
      this.progress = 0;
      this.currentFile = file;
    },

    upload() {
      if (!this.currentFile) {
        this.message = "Please select a file!";
        return;
      }

      this.message = "";

      //   const formData = new FormData();

      //   formData.append("file", this.currentFile);

      //   axios
      //     .post(
      //       "https://vue-http-demo-5801a-default-rtdb.asia-southeast1.firebasedatabase.app/",
      //       formData,
      //       {
      //         headers: {
      //           "Content-Type": "multipart/form-data",
      //         },
      //       }
      //     )
      //     .then((response) => {
      //       console.log(response.data);
      //       if (response.ok) {
      //         this.uploaded = true;
      //       }
      //     })
      //     .catch((error) => {
      //       console.log(error);
      //     });
    },

    reset() {
      setTimeout(() => {
        this.currentFile = undefined;
        this.uploaded = this.malwareCheck = this.sensitiveCheck = false;
      }, 2000);
    },
  },
};
</script>
