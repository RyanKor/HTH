import Vue from "vue";
import Vuex from "vuex";
import router from "./router";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo: null,
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
    login({ dispatch }, loginObj) {
      // login --> 토큰 반환
      axios
        .post("http://127.0.0.1:8000/api/rest-auth/login/", loginObj)
        // loginObj = {email,password}
        .then(res => {
          // 접근 성공시, 토큰 값이 반환된다. (실제로는 토큰과 함께 유저 id를 받아온다.)
          // 토큰을 헤더 정보에 포함시켜서 유저 정보를 요청
          let token = res.data.token;
          //토큰을 로컬 스토리지에 저장
          localStorage.setItem("access_token", token);
          // this.dispatch("getMemberInfo");
          router.push({ name: "home" });
          console.log(res);
        })
        .catch(() => {
          alert("이메일과 비밀번호를 확인하세요.");
        });
    },
    logout({ commit }) {
      commit("logout");
      router.push({ name: "home" });
    },
    signup({ dispatch }, loginObj) {
      // login --> 토큰 반환
      axios
        .post("http://127.0.0.1:8000/api/rest-auth/registration/", loginObj)
        // loginObj = {email,password}
        .then(res => {
          alert("회원가입이 성공적으로 이뤄졌습니다.");
          router.push({ name: "login" });
          console.log(res);
        })
        .catch(() => {
          alert("이메일과 비밀번호를 확인하세요.");
        });
    }
    // getMemberInfo({ commit }) {
    //   //로컬 스토리지에 저장된 토큰을 저장한다.
    //   let token = localStorage.getItem("access_token");
    //   let config = {
    //     headers: {
    //       "access-token": token
    //     }
    //   };
    //   //토큰 -> 멤버 정보 반환
    //   //새로고침 --> 토큰만 갖고 멤버 정보 요청가능
    //   axios
    //     .get("https://127.0.0.1:8000/api/user/", config)
    //     .then(response => {
    //       let userInfo = {
    //         pk: response.data.data.pk,
    //         username: response.data.data.username,
    //         email: response.data.data.email
    //       };
    //       commit("loginSuccess", userInfo);
    //     })
    //     .catch(err => {
    //       alert("이메일과 비밀번호를 확인하세요.");
    //     });
    // }
  }
});
