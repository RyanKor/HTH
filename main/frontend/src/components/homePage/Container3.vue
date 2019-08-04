<template>
  <div class="cont3">
    <div class="cont3-txt-head">
      <span>60데시벨</span> 이렇게 사용하세요!
    </div>
    <img class="mockup" src="../../assets/White_mockup.png" />
    <div class="cont3-txt-main">
      설문조사를 완료하면
      <span>
        실제 의료차트와
        <br />유사한 형식
      </span>으로 응답 결과가 출력됩니다.
      <br />현장 진료 시, 환자는 출력된 페이지를 제출하고
      <br />의사는 환자의 상태를 한눈에 확인할 수 있습니다!
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
span {
  color: #0d4d8d;
  font-weight: 700;
}
.cont3 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 75vh;
  padding: 7% 0;
  background-color: #fafafa;
}
.cont3-txt-head {
  color: #202020;
  font-size: 1.6rem;
  font-weight: 500;
}
.mockup {
  width: 13rem;
  height: 16rem;
  margin: 1rem 0;
}
.cont3-txt-main {
  padding: 0 2rem;
  color: #363636;
  font-size: 0.8rem;
  font-weight: 400;
  text-align: center;
  line-height: 1.1rem;
}
</style>
