<template>
  <div>
    <h1>{{ theme }}</h1>
    <p>{{ time }}</p>
    <Loading class="loading" :class="{ disp: isDisp, nodisp: isNodisp }"></Loading>
    <ul>
      <li v-for="(dog, index) in dogs" :key="index">
        <img src="../assets/dog_corgi.png" />
      </li>
    </ul>

    <img :src="imageData" v-if="imageData" />
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
      imageData: "",
      dogs: [],
      time: "",
      timeId: 0,
    };
  },
  methods: {
    loading() {
      this.isDisp = true;
      this.isNodisp = false;
      this.theme = "NowLoading...(30秒に1匹犬が増えます)";
      var dogCount = 0;
      var startTime = Date.now();
      var elapsedTime = 0;
      this.timeId = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        var m = Math.floor(elapsedTime / 60000);
        var s = Math.floor((elapsedTime % 60000) / 1000);
        var ms = elapsedTime % 1000;
        m = ("0" + m).slice(-2);
        s = ("0" + s).slice(-2);
        ms = ("0" + ms).slice(-2);
        this.time = m + ":" + s + ":" + ms;
      }, 10);
    },
    err() {
      clearInterval(this.timeId);
      this.time = "";
      this.isDisp = false;
      this.isNodisp = true;
      this.theme = "エラー…";
    },
    success(resultText, resultImgData) {
      clearInterval(this.timeId);
      this.time = "";
      this.isDisp = false;
      this.isNodisp = true;
      if (resultImgData === "") {
        this.theme = resultText + "(画像表示できないよ)";
      }
      this.theme = resultText;
      this.imageData = resultImgData;
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

p {
  color: black;
  font-size: 12px;
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

ul {
  list-style: none;
}
</style>
