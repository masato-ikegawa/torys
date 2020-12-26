<template>
  <div class="image-container">
    <h4>顔写真を選んでください</h4>
    <input type="file" accept="image/*" @change="fileChange($event)" />
    <img :src="imageData" v-if="imageData" />
    <Button label="この画像にする" v-if="imageData" />
  </div>
</template>

<script>
import Button from "./Button.vue";

export default {
  name: "ImageButton",
  components:{
    Button,
  },
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
h4{
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
  h4{
    font-size: 17px;
    padding-top: 9px;
    margin-bottom: 18px;
  }
}
</style>
