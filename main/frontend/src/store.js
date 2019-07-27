import Vue from "vue";
import Vuex from "vuex";
import router from "./router";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo: null,
    allUsers: [
      { id: 1, name: "hoza", email: "hoza@gmail.com", password: "123456" },
      { id: 2, name: "lego", email: "lego@gmail.com", password: "123456" }
    ],
    isLogin: false,
    isLoginError: false
  },
  mutations: {
    loginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    },
    loginError(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    }
  },
  actions: {
    login({ commit }, loginObj) {
      // let selectedUser = null
      // state.allUsers.forEach(user =>{
      //     if (user.email === loginObj.email) selectedUser = user
      // })
      // if (selectedUser === null || selectedUser.password !== loginObj.password)
      //     commit("loginError")
      // else {
      //     commit("loginSuccess", selectedUser)
      //     router.push({name: 'home'})
      // }
      axios
        .post("https://reqres.in/api/login", loginObj)
        // loginObj = {email,password}
        .then(res => {
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        });
    },
    logout({ commit }) {
      commit("logout");
      router.push({ name: "home" });
    }
  }
});
