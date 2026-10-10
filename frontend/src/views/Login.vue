<template>
  <div style="height: 100vh; display: flex; justify-content: center; align-items: center">
    <div style="width: 380px; padding: 24px; border-radius: 8px; box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1)">
      <h1 style="text-align: center; font-size: 24px">实验室预约系统</h1>
      <el-form @submit.prevent="handleSubmit">
        <el-form-item label="用户名">
          <el-input v-model="form.username" autocomplete="username" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" autocomplete="current-password" show-password />
        </el-form-item>
        <el-button type="primary" native-type="submit" style="width: 100%">登录</el-button>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { ElMessage } from 'element-plus'

const form = reactive({
  username: '',
  password: ''
})

function handleSubmit() {
  if (!form.username || !form.password) {
    ElMessage.warning('请输入用户名和密码')
    return
  }

  ElMessage.success('登录信息已提交')
}
</script>
