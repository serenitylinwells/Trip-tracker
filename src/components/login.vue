<template>
    <header>
        <i class='bx bx-bus'></i>
        <h2 class="logo">Real-time Bus Location Information System</h2>
        <nav class="navigation">
            <div class="links">
                <a href="#" class="home-link">Home</a>
                <a href="#">Service</a>
                <a href="#">About</a>
                <a href="#">Source</a>
            </div>
            <div class="buttons">
                <button class="btnLogin-popup" @click="resetLogin">Login</button>
                <button class="btnRegister-popup" @click="resetLogin">Sign Up</button>
            </div>
        </nav>
    </header>

    <div class="wrapper">
        <span class="bg-animate"></span>
        <span class="bg-animate2"></span>
        <div class="form-box login">
            <h2 class="animation" style="--i:0;--j:21;">Login</h2>
            <form action="#" @submit.prevent="login_check">
                <!-- 阻止默认事件 -->
                <div class="input-box animation" style="--i:1;--j:22;">
                    <input type="text" required v-model="Account.username">
                    <!-- username赋值 -->
                    <label>Username</label>
                    <i class='bx bxs-user'></i>
                </div>
                <div class="input-box animation" style="--i:2;--j:23;">
                    <input type="password" required v-model="Account.password">
                    <!-- pasword赋值 -->
                    <label>Password</label>
                    <i class='bx bxs-lock-alt'></i>
                </div>
                <p v-if="login_error" style="color: rgb(217, 25, 25);text-align: center;">Wrong Account or Password！</p>
                <button type="submit" class="btn animation" style="--i:3;--j:24;">Login</button>
                <!-- 发送请求， 晚点补充@submit.prevent -->
                <div class="logreg-link animation" style="--i:4;--j:25;">
                    <p>Don't you have an account? <a href="#" class="register-link" @click="resetLogin">Sign Up</a></p>
                </div>
            </form>
        </div>
        <div class="info-text login">
            <h2 class="animation" style="--i:0;--j:20;">Bus-Trip Tracker</h2>
            <p class="animation" style="--i:1;--j:21;">Navigate Your Journey with Precision and Ease.</p>
        </div>

        <div class="form-box register">
            <h2 class="animation" style="--i:17;--j:0;">Sign Up</h2>
            <form action="#" @submit.prevent="register">
                <!-- 阻止默认事件 -->
                <div class="input-box animation" style="--i:18;--j:1;">
                    <input type="text" required v-model="newAccount.username">
                    <!-- username赋值 -->
                    <label>Username</label>
                    <i class='bx bxs-user'></i>
                </div>
                <div class="input-box animation" style="--i:19;--j:2;">
                    <input type="text" required v-model="newAccount.mail">
                    <!-- email赋值 -->
                    <label>Email</label>
                    <i class='bx bxs-envelope'></i>
                </div>
                <div class="input-box animation" style="--i:20;--j:3;">
                    <input type="password" required v-model="newAccount.password">
                    <!-- password赋值 -->
                    <label>Password</label>
                    <i class='bx bxs-lock-alt'></i>
                    <p v-if="register_succeed" style="color: white;text-align: center;">Registration Succeessful</p>
                    <p v-if="register_error" style="color: rgb(217, 25, 25);text-align: center;">Account already existed</p>
                </div>
                <button type="submit" class="btn animation" style="--i:21;--j:4;" @click="resetLogin">Sign Up</button>
                <!-- 发送请求， 晚点补充@submit.prevent -->
                <div class="logreg-link animation" style="--i:22;--j:5;">
                    <p>Already have an account? <a href="#" class="login-link" @click="resetLogin">Login</a></p>
                </div>
            </form>
        </div>

        <div class="info-text register">
            <h2 class="animation" style="--i:17; --j:0;">Bus-Trip Tracker</h2>
            <p class="animation" style="--i:18; --j:1;">Navigate Your Journey with Precision and Ease.</p>
        </div>
    </div>
</template>

<script>
import { setupEventListeners } from '/public/static/eventListeners.js';
import axios from 'axios';
import { defineEmits } from 'vue';

export default {
    emits: ['login-status'],

    data(){
        return{
            Account: {
                username: "",
                password: ""
        },
            newAccount: {
                username: "",
                password: "",
                mail: "",
        },

        login_error: false,
        register_succeed: false,
        register_error: false
    }
},

    methods:{

        login_check(){   
            axios.post("http://127.0.0.1:8000/api/user/login"
                ,this.Account
                )
            .then(response =>{
                console.log(this.Account);
                console.log(response.data);
                this.$emit('login-status', response.data.status);//向App组件发送status
                if (response.data.status === "ERROR") {
                    this.login_error = true;
                    this.Account.username = "";
                    this.Account.password = "";
                } else {
                this.$router.push('/checkup');

                }
            })
            .catch(error => {
                console.error(error);
            })
        },
    
        register() {
            axios.post("http://127.0.0.1:8000/api/user/register"
                ,this.newAccount
            )
            .then(response =>{
                if (response.data.status === "SUCCEED"){
                    this.newAccount.password = "";
                    this.newAccount.mail = "";
                    this.newAccount.username = "";
                    this.register_succeed = true;
                } else {
                    this.register_error = true;
                }
                

            })
            .catch(error => {
                console.error(error);
            })
        },

        resetLogin() {
            this.login_error = false;
            this.register_error = false;
            this.register_succeed = false;
        }
    },

        

    mounted() {
        setupEventListeners();
    }
}

</script>

<style>
@import '/public/static/log-style.css';
@import url('https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css');

.buttons{
    margin-top: 20px;
}
</style>