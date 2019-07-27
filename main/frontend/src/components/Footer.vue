<template>
  <!-- Footer -->
  <mdb-footer color="unique-color-dark" class="page-footer font-small pt-0">
    
    <div class="footer-copyright text-center py-3">
      <mdb-container fluid>
          <div class="company">
        <span>&copy; 2019 Copyright 60 dB</span>
        <span>회사 주소 : 성북구 안암로 7가 고려대학교</span>
        <span>문의사항 : cs60db@60db.com</span>
          </div>

      </mdb-container>
    </div>
  </mdb-footer>
  <!-- Footer -->
</template>
<script>
// main.js에서 mdbvue라는 부트스트랩 모듈을 받아왔음. npm install --save mdbvue를 하고 나서 main.js에 관련 라이브러리 호출 코드를 넣을 것! main.js 참고
  import { mdbFooter, mdbContainer, mdbRow, mdbCol } from 'mdbvue';
  export default {
    name: 'FooterPage',
    components: {
      mdbFooter,
      mdbContainer,
      mdbRow,
      mdbCol
    }
  }
</script>

<style scoped>
.company{
    display: flex;
    justify-content: space-around;
}
</style>
