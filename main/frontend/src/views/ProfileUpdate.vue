<template>
  <div class="form">
    <form method="put" enctype="multipart/form-data">
      <label>사진을 업로드해주세요</label>
      <img class="thumb" :src="avatar" />
      <input type="text" v-model="gender" />
      <input type="text" v-model="birth" />
      <input type="text" v-model="height" />
      <input type="text" v-model="weight" />
      <input type="text" v-model="name" />
      <input type="text" v-model="checkup" />
      <input type="text" v-model="checkupTrue" />
      <input type="text" v-model="diagnosedDisease" />
      <input type="text" v-model="takingMedicine" />
      <input type="text" v-model="whatMedicine" />
      <input type="text" v-model="familyHistory" />
      <input type="text" v-model="drinking" />
      <input type="text" v-model="drinkingPerWeek" />
      <input type="text" v-model="smoking" />
      <input type="text" v-model="howLongSmoking" />
      <input type="text" v-model="howMuchSmoking" />
      <input type="text" v-model="job" />
      <input type="text" v-model="relevantData" />
    </form>
    <input
      type="submit"
      class="button"
      name="submit"
      @click="update({avatar, gender,birth, height, weight, name, checkup, checkupTrue, diagnosedDisease, takingMedicine, whatMedicine, familyHistory, drinking, drinkingPerWeek,
        smoking,howLongSmoking, howMuchSmoking, job, relevantData})"
      value="프로필 업데이트"
    />
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
</style>
