<template>
  <div class="head-bar">
    <div class="head-icon test">
      <img src="/static/logo.png" style="height: 80px; width: 80px">
    </div>
    <div class="head-search test">
      <div class="search-frame test">
        <el-input placeholder="请输入内容" v-model="search_input"></el-input>
      </div>
      <div class="search-button test">
        <el-button class="el-icon-search" circle type="warning" @click="search"></el-button>
      </div>
    </div>
    <div class="head-user-info test">
      <div v-if="is_logined" class="logined">
        <el-dropdown>
          <span class="el-drop-down-link">
            <b-img v-bind="user_icon_props" rounded="circle" height="40"></b-img>
            <i class="el-icon-arrow-down" style="z-index:100; margin-left: 5px"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>个人信息</el-dropdown-item>
            <el-dropdown-item>
              <p @click="logout">注销</p>
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div v-else class="unlogined">
        <el-popover placement="bottom" trigger="manual" v-model="login_form_visible" title="登录">
          <div>
            <el-form ref="login_form" :model="login_form" label-width="70px" :rules="login_rules">
              <el-form-item label="用户名" prop="name">
                <el-input v-model="login_form.name" clearable></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input show-password v-model="login_form.password" clearable></el-input>
              </el-form-item>
              <el-form-item>
                <el-button
                  :disabled="logining"
                  v-loading="logining"
                  type="primary"
                  @click="onLoginSubmit"
                >确认</el-button>
                <el-button @click="login_form_visible = false">取消</el-button>
              </el-form-item>
            </el-form>
          </div>
          <el-button type="primary" slot="reference" @click="onLoginButton">登录</el-button>
        </el-popover>
        <el-popover placement="bottom" trigger="manual" v-model="register_form_visible" title="注册">
          <el-form
            ref="register_form"
            :model="register_form"
            label-width="70px"
            :rules="register_rules"
            status-icon
          >
            <el-form-item label="邮箱" prop="email">
              <el-input id="email" clearable v-model="register_form.email" placeholder="正确邮箱格式"></el-input>
            </el-form-item>
            <el-form-item label="用户名" prop="name">
              <el-input v-model="register_form.name" clearable placeholder="3-20个字符"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input
                show-password
                v-model="register_form.password"
                clearable
                placeholder="6个以上字符"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button
                :disabled="registering"
                v-loading="registering"
                type="primary"
                @click="onRegisterSubmit"
              >提交</el-button>
              <el-button @click="register_form_visible = false">取消</el-button>
            </el-form-item>
          </el-form>
          <el-button type="success" slot="reference" @click="onRegisterButton">注册</el-button>
        </el-popover>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

function errorMessage (vm, msg) {
  vm.$message({
    showClose: true,
    message: msg,
    type: 'error',
    duration: 2000
  })
}

export default {
  name: 'HeadBar',
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
      user_icon_props: {
        blank: true,
        blankColor: '#cc9'
      },
      search_input: '',
      login_form_visible: false,
      register_form_visible: false,
      login_form: {
        name: '',
        password: ''
      },
      register_form: {
        name: '',
        password: '',
        email: ''
      },
      logining: false,
      registering: false,
      errors: [],
      login_rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      },
      register_rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, message: '用户名太短', trigger: 'blur' },
          { max: 20, message: '用户名太长', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, message: '密码太短', trigger: 'blur' },
          { max: 200, message: '密码太长', trigger: 'blur' }
        ],
        email: [
          { validator: checkEmail, trigger: 'blur' },
          { required: true, message: '请输入邮箱', trigger: 'blur' }
        ]
      }
    }
  },
  computed: {
    is_logined () {
      return this.$store.state.is_logined
    }
  },
  methods: {
    search: function () {
      // TODO axios GET
      this.$router.push('/search')
    },
    onLoginButton: function () {
      this.login_form_visible = !this.login_form_visible
      this.register_form_visible = false
    },
    onRegisterButton: function () {
      this.login_form_visible = false
      this.register_form_visible = !this.register_form_visible
    },
    onLoginSubmit: function () {
      this.logining = true
      // 前端验证
      this.$refs['login_form'].validate((valid) => {
        if (valid) {
          // api请求登录
          axios.post(this.COMMON.httpURL + 'user/login', this.login_form)
            .then(response => {
              localStorage.user_id = response.data.user_id
              localStorage.name = this.login_form.name
              localStorage.password = this.login_form.password
              this.$store.commit('login')
              this.$message({
                showClose: true,
                message: '登录成功',
                type: 'success',
                duration: 1500
              })
              this.logining = false
              this.login_form_visible = false
            })
            .catch(error => {
              if (error.response) {
                switch (error.response.data.error) {
                  case 'name':
                    errorMessage(this, '用户名不存在')
                    break
                  case 'method':
                    errorMessage(this, '方法错误')
                    break
                  case 'parameter':
                    errorMessage(this, '请求参数非法')
                    break
                  case 'password':
                    errorMessage(this, '密码错误')
                    break
                  default:
                    errorMessage(this, '未知错误')
                    break
                }
              } else {
                errorMessage(this, '状态异常')
              }
              this.logining = false
            })
        } else {
          this.logining = false
          return false
        }
      })
    },
    onRegisterSubmit: function () {
      this.registering = true
      // 前端验证
      this.$refs['register_form'].validate((valid) => {
        if (valid) {
          // api请求注册
          axios.post(this.COMMON.httpURL + 'register', this.register_form)
            .then(response => {
              localStorage.user_id = response.data.user_id
              localStorage.name = this.register_form.name
              localStorage.password = this.register_form.password
              this.$store.commit('login')
              this.$message({
                showClose: true,
                message: '注册成功',
                type: 'success',
                duration: 1500
              })
              this.registering = false
              this.register_form_visible = false
            })
            .catch(error => {
              if (error.response) {
                switch (error.response.data.error) {
                  case 'name_dupli':
                    errorMessage(this, '用户名已被占用')
                    break
                  case 'name':
                    errorMessage(this, '用户名出错')
                    break
                  case 'method':
                    errorMessage(this, '方法错误')
                    break
                  case 'parameter':
                    errorMessage(this, '请求参数非法')
                    break
                  case 'password':
                    errorMessage(this, '密码出错')
                    break
                  case 'email':
                    errorMessage(this, '邮箱格式出错')
                    break
                  default:
                    errorMessage(this, '未知错误')
                    break
                }
              } else {
                errorMessage(this, '状态异常')
              }
              this.registering = false
            })
        } else {
          this.registering = false
          return false
        }
      })
    },
    logout: function () {
      localStorage.removeItem('user_id')
      localStorage.removeItem('name')
      localStorage.removeItem('password')
      this.login_form.password = ''
      this.register_form.email = ''
      this.register_form.password = ''
      this.$store.commit('logout')
      this.$message({
        showClose: true,
        message: '注销成功',
        type: 'success',
        duration: 1500
      })
      axios.delete(this.COMMON.httpURL + 'user/logout')
    }
  },
  created: function () {
    if (localStorage.user_id) {
      if (localStorage.name && localStorage.password) {
        axios.post(this.COMMON.httpURL + 'user/login', { name: localStorage.name, password: localStorage.password })
          .then(response => {
            localStorage.user_id = response.data.user_id
            this.$store.commit('login')
          })
      }
    }
  }
}
</script>

<style scoped>
.head-bar {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.head-bar .head-icon {
  flex-grow: 4;
  order: 1;
}
.head-bar .head-search {
  flex-grow: 17;
  order: 2;
  display: flex;
  align-items: center;
  justify-content: center;
}
.head-search .search-frame {
  flex-grow: 6;
  order: 1;
}
.search-frame .el-input {
  width: 50%;
  left: 20%;
}
.head-search .search-button {
  flex-grow: 2;
  order: 2;
}
.search-button .el-button {
  position: relative;
  float: left;
}
.head-bar .head-user-info {
  flex-grow: 5;
  order: 3;
}
.test {
  border-block-color: #ffffff;
  border-block-width: 0px;
}
</style>
