<template>
  <div class="container">
    <input type="file" accept="image/*" @change="fileChange($event)"/>
  </div>
</template>

<script>
export default {
  name: "ImageButton",
  data: {
    imageData: "",
  },
  methods: { 
    // ファイル読み込み
    fileChange(e){
      const files = e.target.files;
      // ファイルが
      if (files.length > 0){
        const file = files[0];
        const reader =  new FileReader();
        reader.onload = (e) =>{
          this.imageData = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    }
  },
};
</script>
