<template>
  <div class="image-container">
    <h4>顔写真を選んでください</h4>
    <input type="file" accept="image/*" @change="fileChange($event)" />
    <button class="post-btn" @click="tappedPostButton()" v-if="imageData">
      この画像に決定
    </button>
    <img :src="imageData" v-if="imageData" />
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
  methods: {
    imageToBase64() {
      if (this.imageData) {
        return this.imageData;
      } else {
        return null;
      }
    },
    tappedPostButton() {
      const data = this.imageToBase64();
      axios.post(
        "http://localhost:5000/upload",
        { img: data },
        { headers: { "Content-Type": "application/json" } }
      );
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

.post-btn {
  display: inline-block;
  height: auto;
  width: 120px;
  cursor: pointer;
}

img {
  display: block;
  width: 200px;
  height: auto;
  max-height: 500px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 20px;
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
