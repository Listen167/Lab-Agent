<!-- 模板：写HTML结构，页面长什么样子 -->
<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 24px">实验室预约系统</h1>
      <div style="margin-top: 5px; margin-bottom: 30px">基于Agent智能预约系统</div>

      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item>
          <el-input v-model="form.username" 
          placeholder="请输入账号" 
          size="large"
          :prefix-icon="User" 
          />
        </el-form-item>

        <el-form-item>
          <el-input
            v-model="form.password"
            placeholder="请输入密码"
            size="large"
            :prefix-icon="Lock"
            type="password"
            show-password
          />
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<!-- 脚本：写JS逻辑，数据，函数，导入 -->
<script setup>
import { reactive } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'

const form = reactive({
  username: '',
  password: ''
})
</script>

<!-- 样式：写css，页面好不好看 -->
<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-box {
  width: 380px;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  background-color: white;
}
</style>
