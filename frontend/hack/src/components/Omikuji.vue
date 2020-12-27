<template>
  <div>
    <h1>{{ theme }}</h1>
    <p>{{ time }}</p>
    <Loading class="loading" :class="{ disp: isDisp, nodisp: isNodisp }"></Loading>
    <ul :class="{ flex: isListDisp, nodisp: isListNodisp }">
      <li v-for="(dog, index) in dogs" :key="index">
        <img class="dogImg" src="../assets/dog_corgi.png" alt="犬の画像" />
      </li>
    </ul>
    <img class="resultImg" :src="imageData" v-if="imageData" alt="結果の画像" />
    <TweetButton
      ref="twetbtn"
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
      resultValue: "",
      isDisp: false,
      isNodisp: true,
      theme: "ニコニコおみくじ",
      isTweetDisp: false,
      isTweetNodisp: true,
      imageData: "",
      dogs: [],
      time: "",
      timeId: 0,
      isListDisp: true,
      isListNodisp: false,
    };
  },
  methods: {
    loading() {
      this.isDisp = true;
      this.isNodisp = false;
      this.theme = "Now Loading...(1秒に1匹犬が増えます)";
      var count = 0;
      var dogCount = 0;
      var startTime = Date.now();
      var elapsedTime = 0;
      this.time = "00:00:0(5分くらいかかるよ！)";
      this.dogs.push(dogCount);
      this.timeId = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        var m = Math.floor(elapsedTime / 60000);
        var s = Math.floor((elapsedTime % 60000) / 1000);
        var ms = elapsedTime % 1000;
        if (s >= 30) m = ("0" + m).slice(-2);
        s = ("0" + s).slice(-2);
        ms = ("0" + ms).slice(-1);
        this.time = m + ":" + s + ":" + ms + "(5分くらいかかるよ！)";
        count++;
        if (count % 10 === 0) {
          dogCount++;
          this.dogs.push(dogCount);
        }
      }, 100);
    },
    err() {
      this.isListDisp = false;
      this.isListNodisp = true;
      clearInterval(this.timeId);
      this.time = "";
      this.isDisp = false;
      this.isNodisp = true;
      this.theme = "エラー…";
    },
    success(resultText, resultImgData) {
      this.isListDisp = false;
      this.isListNodisp = true;
      clearInterval(this.timeId);
      this.time = "";
      this.isDisp = false;
      this.isNodisp = true;
      if (resultImgData === "") {
        this.theme = resultText + "(画像が表示できないよ)";
      } else {
        this.theme = resultText;
        this.imageData = "data:image/jpg;base64," + resultImgData;
        console.log("src:", this.imageData);
      }
      this.isTweetDisp = true;
      this.isTweetNodisp = false;
      this.$refs.twetbtn.resultChange(resultText);
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 14px;
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

.flex {
  display: flex;
}

ul {
  padding-inline-start: 0px;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  align-items: center;
  list-style: none;
}

.dogImg {
  width: 30px;
  height: auto;
}

.resultImg {
  display: block;
  width: 100px;
  height: auto;
  max-height: 200px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 10px;
  margin-bottom: 20px;
}

@media screen and (min-width: 400px) {
  h1 {
    font-size: 14px;
  }
}

@media screen and (min-width: 600px) {
  h1 {
    font-size: 18px;
  }
}

@media screen and (min-width: 900px) {
  h1 {
    font-size: 21px;
  }

  .resultImg {
    width: 125px;
    height: auto;
    max-height: 250px;
  }
}

@media screen and (min-width: 1200px) {
  h1 {
    font-size: 24px;
  }
}
</style>
