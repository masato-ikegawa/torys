<template>
  <div class="image-container">
    <h4>顔写真を選んでください</h4>
    <label for="file_upload">
      ファイルを選択して下さい
      <input type="file" id="file_upload" accept="image/*" @change="fileChange($event)" />
    </label>
    <img :src="imageData" v-if="imageData" />
  </div>
</template>

<script>
export default {
  name: "ImagePost",
  data() {
    return {
      imageData: "",
    };
  },
  methods: {
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
          // 画像を受け取ったのでApp.vueの決定ボタンを有効にしてもらう
          this.passApp();
          // 画像を受け取ったのでApp.vueにimgDataを送信
          this.sendImgData();
        };
        reader.readAsDataURL(file);
      }
    },
    passApp() {
      this.$emit("passImageStatus");
    },
    sendImgData() {
      this.$emit("catchImgData", this.imageData);
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
  width: 100px;
  height: auto;
  max-height: 200px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 10px;
  margin-bottom: 20px;
}

label > input {
  display: none;
}

label {
  width: 180px;
  height: 30px;
  line-height: 30px;
  display: block;
  cursor: pointer;
  background: rgb(50, 150, 220);
  border: solid 1px #aaa;
  border-radius: 5px;
  font-size: 13px;
  color: #fff;
  font-weight: bold;
  text-align: center;
  margin: 0 auto;
}

label:hover {
  opacity: 0.8;
}

@media screen and (min-width: 900px) {
  img {
    width: 125px;
    height: auto;
    max-height: 250px;
  }

  h4 {
    font-size: 17px;
    padding-top: 9px;
    margin-bottom: 18px;
  }

  label {
    width: 200px;
    height: 32px;
    font-size: 14px;
  }
}
</style>
