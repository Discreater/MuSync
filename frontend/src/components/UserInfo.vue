<template>
  <div>
    <p>User info</p>
    <el-form
      ref="form"
      :model="user"
      style="max-width: 500px; margin: 0 auto"
      label-width="80px"
      :rules="form_rules"
    >
      <el-form-item label="用户名" prop="name">
        <el-input v-model="user.name" clearable placeholder="3-20个字符"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input id="email" clearable v-model="user.email" placeholder="正确邮箱格式"></el-input>
      </el-form-item>
      <el-form-item label="性别">
        <el-radio v-model="user.gender" label="man">男</el-radio>
        <el-radio v-model="user.gender" label="woman">女</el-radio>
        <el-radio v-model="user.gender" label="secret">保密</el-radio>
      </el-form-item>
      <el-form-item label="手机">
        <el-input v-model="user.phone" clearable></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'

export default {
  name: 'UserInfo',
  data () {
    var checkEmail = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('邮箱不能为空'))
      } else {
        // eslint-disable-next-line
        let re = /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
        if (!re.test(String(value))) {
          callback(new Error('请输入正确的邮箱'))
        } else {
          callback()
        }
      }
    }
    return {
      user: {},
      password: '',
      form_rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, message: '用户名太短', trigger: 'blur' },
          { max: 20, message: '用户名太长', trigger: 'blur' }
        ],
        email: [
          { validator: checkEmail, trigger: 'blur' },
          { required: true, message: '请输入邮箱', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onCancel () {
      this.$router.go(-1)
    },
    onSubmit () {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          if (localStorage.user_id) {
            let k = {}
            k.id = this.user.id
            k.name = this.user.name
            k.email = this.user.email
            k.gender = this.user.gender
            k.phone = this.user.phone
            axios.post(this.COMMON.httpURL + 'user/change-info', Qs.stringify(k))
              .then(response => {
                this.$message({
                  showClose: true,
                  message: '修改成功',
                  type: 'success',
                  duration: 1500
                })
                localStorage.name = this.user.name
                this.$router.go(-1)
              })
              .catch(error => {
                if (error.response) {
                  this.$message({
                    showClose: true,
                    message: error.response.data.error,
                    type: 'error',
                    duration: 2000
                  })
                } else {
                  this.$message({
                    showClose: true,
                    message: '未知错误',
                    type: 'error',
                    duration: 2000
                  })
                  console.log(error)
                }
              })
          }
        } else {
          return false
        }
      })
    },
    fetchUserInfo: function () {
      let userId = localStorage.user_id
      axios.get(this.COMMON.httpURL + 'user/' + userId + '/fetch-info')
        .then(response => {
          this.user = response.data.info
        })
        .catch(error => {
          if (error.response) {
            this.$message({
              showClose: true,
              message: error.response.data.error,
              type: 'error',
              duration: 2000
            })
          } else {
            this.$message({
              showClose: true,
              message: '未知错误',
              type: 'error',
              duration: 2000
            })
            console.log(error)
          }
        })
    }
  },
  created () {
    this.fetchUserInfo()
  },
  watch: {
    '$route': 'fetchUserInfo'
  }
}
</script>
