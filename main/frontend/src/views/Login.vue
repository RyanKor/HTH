<template>
  <div class="login">
    <login-logo class="header" />
    <login-form class="footer" />
  </div>
</template>

<script>
// @ is an alias to /src
import LoginLogo from "../components/registerPage/LoginLogo.vue";
import LoginForm from "../components/registerPage/LoginForm.vue";

export default {
  name: "login",
  components: {
    LoginLogo,
    LoginForm
  }
};
</script>
<style scoped>
.login {
  width: 100%;
  height: 100vh;
  color: #fff;
  background: linear-gradient(-45deg, #0a4b8b, #35c3c0);
  /* background-size: 400% 400%; */
  /* -webkit-animation: Gradient 15s ease infinite;
  -moz-animation: Gradient 15s ease infinite;
  animation: Gradient 15s ease infinite; */
}
.header {
  width: 100%;
  height: 50%;
}
.footer {
  width: 100%;
  height: 50%;
}
/* @-webkit-keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

@-moz-keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

@keyframes Gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
} */
</style>
