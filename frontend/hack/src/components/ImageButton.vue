<template>
  <div class="image-container">
    <h4>顔写真を選んでください</h4>
    <input type="file" accept="image/*" @change="fileChange($event)" />
    <img :src="imageData" v-if="imageData" />
    <button @click="tappedPostButton()" v-if="imageData">この画像に決定</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ImageButton",
  components: {},
  data() {
    return {
      imageData: "",
      data: {
        bpi: null,
      },
    };
  },
  mounted: function () {
    axios
      .get("https://api.coindesk.com/v1/bpi/currentprice.json")
      .then(
        function (response) {
          //デバッグ用にconsoleに出力
          console.log(response.data.bpi);
          this.bpi = response.data.bpi;
        }.bind(this)
      )
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    tappedPostButton() {
      return axios.post("localhost:8080", { チンポ: String });
    },
    // ファイル読み込み
    fileChange(e) {
      const files = e.target.files;
      // ファイルが選択されたかチェック
      if (files.length > 0) {
        const file = files[0];
        // ファイルリーダーを使って画像を読み込み
        const reader = new FileReader();
        reader.onload = (e) => {
          // imageDataに格納
          this.imageData = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
  },
};
</script>

<style scoped>
.image-container {
  width: 100%;
  height: 300px;
  padding: 0;
}

h4 {
  font-size: 15px;
  padding-top: 6px;
  margin-bottom: 12px;
}

img {
  display: block;
  width: 200px;
  height: auto;
  max-height: 500px;
  margin: 0 auto;
}

@media screen and (min-width: 900px) {
  img {
    width: 250px;
    height: auto;
    max-height: 500px;
  }

  h4 {
    font-size: 17px;
    padding-top: 9px;
    margin-bottom: 18px;
  }
}
</style>
