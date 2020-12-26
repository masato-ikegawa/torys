<template>
  <div>
    <h1>{{ theme }}</h1>
    <Loading class="loading" :class="{ disp: isDisp, nodisp: isNodisp }"></Loading>
    <TweetButton
      after="true"
      result="resultValue"
      class="tweet"
      :class="{ disp: isTweetDisp, nodisp: isTweetNodisp }"
    ></TweetButton>
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
      isDisp: false,
      isNodisp: true,
      theme: "ニコニコおみくじ",
      isTweetDisp: false,
      isTweetNodisp: true,
    };
  },
  methods: {
    loading() {
      this.isDisp = true;
      this.isNodisp = false;
      this.theme = "NowLoading...";
    },
    err() {
      this.isDisp = false;
      this.isNodisp = true;
      this.theme = "エラー…";
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 18px;
  margin-top: 20px;
  font-weight: bold;
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
