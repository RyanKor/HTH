<template>
  <div class="container2">
    <div class="cont2-txt">
      <div class="cont2-txt-head">
        <span class="span1">언제 어디서든</span> 간편한 설문으로
        <br />건강을 관리하세요.
      </div>
    </div>
    <div class="cont2-icons">
      <div class="icon-box">
        <img class="icon" src="../../assets/survey.png" />
        <p class="icon-head">
          모바일
          <br />사전설문으로
        </p>
        <p class="icon-main"></p>
      </div>
      <div class="icon-box">
        <img class="icon" src="../../assets/thumbs.png" />
        <p class="icon-head">
          진료의
          <br />질은 높이고!
        </p>
        <p class="icon-main"></p>
      </div>
      <div class="icon-box">
        <img class="icon" src="../../assets/patient.png" />
        <p class="icon-head">
          소통의
          <br />불편함은 줄이고!
        </p>
        <p class="icon-main"></p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  }
};
</script>
<style scoped>
.container2 {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  background-color: #ffffff;
  width: 100%;
  height: 51vh;
}
.cont2-txt-head {
  color: rgb(48, 48, 48);
  text-align: center;
  font-weight: 400;
  font-size: 1.5rem;
  padding-top: 4%;
}
.span1 {
  color: #0e4f8f;
  font-weight: 800;
}
.cont2-txt-main {
  font-size: 0.8rem;
}
.cont2-icons {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20rem;
  height: auto;
  padding-bottom: 2%;
}
.icon-box {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  width: 34%;
  height: 20%;
  font-weight: 400;
  padding-bottom: 2%;
}
.icon {
  width: 75px;
  height: 75px;
}
.icon-head {
  margin-top: 1rem;
  text-align: center;
  font-size: 0.85rem;
}
</style>
