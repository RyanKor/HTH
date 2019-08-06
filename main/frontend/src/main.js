import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import "@babel/polyfill";
// footer.vue에 적용. mdb를 main.js에 적용해야 globl하게 적용 가능함.
// main.js에서 mdbvue라는 부트스트랩 모듈을 받아왔음. npm install --save mdbvue를 하고 나서 main.js에 라이브러리 호출!

// .components/surveyPage/example에 적용. 플러그인으로 사용하기 위해 .plugins에 vue-scrollactive plugin인 생성 후, main.js에서 플러그인 호출
import "./plugins/vue-scrollactive";
import router from "./router";
import store from "./store";
import axios from "axios";
Vue.prototype.$axios = axios;
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  // beforeCreate() {
  //   this.$store.dispatch("getMemberInfo");
  // },
  render: h => h(App)
}).$mount("#app");
