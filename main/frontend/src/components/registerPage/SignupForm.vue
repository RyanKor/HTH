<template>
  <div class="formContainer">
    <a class="bold">&nbsp;&nbsp;회원가입</a>
    <form class="login-box">
      <p>아이디</p>
      <input type="text" v-model="username" name="username" label="가입할 ID를 입력하세요" />
      <p>이메일</p>
      <input type="text" v-model="email" name="email" label="가입할 이메일을 입력하세요" />
      <p>비밀번호</p>
      <input type="password" v-model="password1" name="userpassword1" label="비밀번호를 입력하세요" />
      <p>비밀번호 확인</p>
      <input type="password" v-model="password2" name="userpassword2" label="비밀번호 확인을 위해 다시 한 번 입력해주세요" />
      <br />
    </form>
    <div class="login-btn">
      <input
        type="submit"
        class="button"
        name="submit"
        @click="signup({username, email,password1, password2})"
        value="회원가입"
      />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null
    };
  },
  methods: {
    ...mapActions(["signup"])
  }
};
</script>


<style scoped>
.formContainer {
  width: 100%;
  padding-top: 0.5rem;
  padding: auto;
}
.login-box {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 17rem;
  margin: auto;
}
.login-box p {
  margin: 0;
  padding: 0;
  font-size: 0.85rem;
  font-weight: 500;
}
.login-box input {
  width: 100%;
  margin-bottom: 1rem;
}
.login-box input[type="text"],
input[type="password"] {
  border: none;
  border-bottom: 1.5px solid #fff;
  background: transparent;
  outline: none;
  height: 30px;
}
.login-btn {
  display: flex;
  flex-direction: column;
}
.button {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 5px 5px 0px rgba(0, 0, 0, 0.308);
  outline-color: rgb(32, 114, 207);
  width: 14rem;
  height: 3rem;
  margin: auto;
  margin-top: 0.2rem;
  color: rgb(54, 54, 54);
  font-size: 0.9rem;
  font-weight: 700;
  transition: 0.5s;
}
.button:hover {
  box-shadow: 5px 7px 10px 2px rgba(0, 0, 0, 0.308);
}
.login-btn-txt {
  display: flex;
  justify-content: center;
  margin-top: 1.3rem;
  font-size: 0.85rem;
}
.bold {
  color: rgb(248, 215, 26);
  font-weight: 700;
}
</style>