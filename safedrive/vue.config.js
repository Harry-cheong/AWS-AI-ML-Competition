const { defineConfig } = require("@vue/cli-service");
const fs = require("fs");
module.exports = defineConfig({
  transpileDependencies: true,
});

module.exports = {
  transpileDependencies: ["vuetify"],
};
