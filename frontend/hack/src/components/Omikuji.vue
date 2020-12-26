<template>
  <div>
    <h1>ニコニコおみくじ</h1>
    <Loading class="loading nodisp"></Loading>
    <TweetButton after="true" :result="resultValue" class="tweet nodisp"></TweetButton>
  </div>
</template>

<script>
import Loading from "./Loading.vue";
import TweetButton from "./TweetButton.vue";

export default {
  name: "Omikuji",
  components: {
    Loading,
    TweetButton,
  },
  data() {
    return {
      result: Number,
      resultText: String,
    };
  },
};
</script>

<style scoped>
h1 {
  font-size: 18px;
  margin-top: 0;
  padding-top: 60px;
}

.loading {
  display: none;
}

.tweet {
  margin-top: 30px;
  margin-right: auto;
  margin-left: auto;
}

.disp {
  display: block !important;
}

.nodisp {
  display: none !important;
}
</style>
