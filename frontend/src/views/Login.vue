<!-- 模板：写HTML结构，页面长什么样子 -->
<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 28px">实验室预约系统</h1>
      <div style="margin-top: 5px; margin-bottom: 20px">基于Agent智能预约系统</div>

      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item>
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入账号"
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
      <div>
        <el-button size="large" 
        type="primary" 
        style="width: 100%"
        @click="login"
        :loading="loadingValue"
        >登录</el-button>
        <div style="text-align: right; margin-top: 12px">
          还没有账号？请<a style="color: var(--el-color-primary)" href="/register">注册</a>
        </div>
      </div>
    </div>
  </div>
</template>

<!-- 脚本：写JS逻辑，数据，函数，导入 -->
<script setup>
import { reactive,ref } from 'vue'
import { useRouter } from 'vue-router'
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage, ElLoading } from 'element-plus'

const form = reactive({
  username: '',
  password: ''
})

const router = useRouter()

const loadingValue = ref(false) 

// 定义Login函数（箭头函数）
const login = () => {
  loadingValue.value = true // 把加载状态设置为true(按钮就开始转圈，防止)
  // 开启一个定时器，模拟等待（通常是发送请求给服务器）
  setTimeout(() => {
    loadingValue.value = false //2s之后，关闭加载状态（按钮恢复）
    ElMessage.success('登录成功') //弹出绿色的“登录成功”的界面
    router.push('/manager/home') // 跳转到/manafer/home界面，也就是后台首页
  }, 2000)
}


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
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  background-color: white;
}
</style>
