<template>
    <div class="bigBox">
        <div class="slot">
           <nav class="choices">
                <div>
                    <router-link to="/" class="btnWeather">HomePage</router-link>
                </div>
                <div>
                    <router-link to="/three-days" class="btnWeather">Weather</router-link>
                </div>
           </nav>
        </div>
        <div class="container">
            <div class="InformationBox">
                <div class="SearchBox">
                    <!-- 输入框和按钮 -->
                    <div class="input1">
                        <div class="first-div">
                            <p>FROM</p><input type="text" placeholder="Starting Station" v-model.lazy="place1" @blur="searchPlace1"/>
                        </div>
                        
                        <div class="second-div">
                            <p>TO</p><input type="text" placeholder="Destination Station" v-model.lazy="place2" @blur="searchPlace2"/>
                        </div>
                        
                    </div>
                
                    <div class="search">
                        <button @click="searchRoute">Search</button>
                    </div>
                    <div class="option1" v-if="checkStatus1">
                        <ul >
                            <li v-for="(option, index) in searchOptions1" :key="index" @click="selectOption(option, 1)">
                            {{ option.name }}
                            </li>
                        </ul>
                    </div>

                    <div class="option2" v-if="checkStatus2">
                        <ul >
                            <li v-for="(option, index) in searchOptions2" :key="index" @click="selectOption(option, 2)">
                            {{ option.name }}
                            </li>
                        </ul>
                    </div>
                    
                </div>
                <div class="information" v-if="showInformationBox">
                    <!-- 响应数据 -->
                    <div class="routePlan" v-for="(plan, index) in routes" :key="index">
                        <div class="icon">
                            <p>{{ index+1 }}</p>
                        </div>

                        <div class="data">
                            <p>Time Required: {{ plan.time }}</p>
                            <p>Total Distance: {{ plan.distance }}</p>
                            <p>Bus Route(s): {{ plan.route_name }}</p>
                        </div>
                        <br>
                        <div class="stations" v-for="(station, index) in plan.stations" :key="index">
                            <li>Station:{{ station.station_name }}<br>Information:{{ station.information }}<br>NextBus:{{ station.next_bus }}</li>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    data(){
        return{
            place1:"",  //用于储存第一个输入框的内容
            place2:"",   //用于储存第二个输入框的内容
            checkStatus1: false,   //查询地点的查询状态
            checkStatus2: false,
            searchOptions1: [],
            searchOptions2: [],
            selectedPlace1: {"name":"", "sign":""},
            selectedPlace2: {"name":"", "sign":""},
            routes: [],
            showInformationBox: false,
        }
    },

    methods:{
        searchPlace1() {
            if (this.checkStatus1 === true) {
                this.checkStatus1 = false;
            }
            if (this.place1 === "") {
                this.checkStatus1 = false;
            } else {
                axios.post("http://127.0.0.1:8000/api/bus/location"
                ,{"keywords":this.place1}
            )
                .then(response => {
                    // console.log(response.data);
                    if (response.data.error === null) {
                        this.checkStatus1 = true;
                    } else {
                        this.checkStatus1 = false;
                    }
                    this.searchOptions1 = response.data.results;
                })
                .catch(error => {
                    console.error(error);
                })
            } 
        },

        searchPlace2() {
            if (this.checkStatus2 === true) {
                this.checkStatus2 = false;
            }
            if (this.place2 === "") {
                this.checkStatus2 = false;
            } else {
                axios.post("http://127.0.0.1:8000/api/bus/location"
                ,{"keywords":this.place2}
            )
                .then(response => {
                    // console.log(response.data.places);
                    if (response.data.error === null) {
                        this.checkStatus2 = true;
                    } else {
                        this.checkStatus2 = false;
                    }
                    this.searchOptions2 = response.data.results;
                })
                .catch(error => {
                    console.error(error);
                })
            } 
        },

        selectOption(option, id) {
            console.log(option.sign);
            if (id === 1) {
                this.checkStatus1 = false;
                this.place1 = option.name;
                this.selectedPlace1.name = option.name;
                this.selectedPlace1.sign = option.sign;
            } 
            else if (id === 2) {
                this.checkStatus2 = false;
                this.place2 = option.name;
                this.selectedPlace2.name = option.name;
                this.selectedPlace2.sign = option.sign;
            }
        },

        searchRoute(){
            axios.post("http://127.0.0.1:8000/api/bus/route"
             , {"startPointName":this.selectedPlace1.name,"startPointSign":this.selectedPlace1.sign,
               "endPointName":this.selectedPlace2.name,"endPointSign":this.selectedPlace2.sign}
            )
            .then(response =>{
                this.routes = response.data.results;
                /* this.place1 = "";
                 this.place2 = "";
                this.selectedPlace1 = {"name":"", "sign":""};
                this.selectedPlace2 = {"name":"", "sign":""}; */
                this.showInformationBox = true; // 设置为 true，显示信息栏
            })
            .catch(error => {
                console.error(error);
            })
        }
    },

    mounted() {
        axios.post("https://01f7e045-eec1-4db7-a0bd-ce1d8a7dda5a.mock.pstmn.io//api/navigation/transport")
            .then(response =>{
                // console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            })
    }
}
</script>

<style>
@import '/public/static/checkup-style.css';
</style>
