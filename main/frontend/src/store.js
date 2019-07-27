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
    },
    logout(state) {
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
          // 접근 성공시, 토큰 값이 반환된다. (실제로는 토큰과 함께 유저 id를 받아온다.)
          // 토큰을 헤더 정보에 포함시켜서 유저 정보를 요청
          let token = res.data.token;
          let config = {
            headers: {
              "access-token": token
            }
          };
          axios
            .get("https://reqres.in/api/users/2", config)
            .then(response => {
              let userInfo = {
                id: response.data.data.id,
                first_name: response.data.data.first_name,
                last_name: response.data.data.last_name,
                avatar: response.data.data.avatar
              };
              commit("loginSuccess", userInfo);
            })
            .catch(() => {
              alert("이메일과 비밀번호를 확인하세요.");
            });
        })
        .catch(err => {
          alert("이메일과 비밀번호를 확인하세요.");
        });
    },
    logout({ commit }) {
      commit("logout");
      router.push({ name: "home" });
    }
  }
});
