<template>
    <header>
        <i class='bx bx-cloud'></i>
        <h2 class="logo">Foshan Weather Forecast</h2>
        <nav>
            <div>
                <router-link to="/three-days" class="link">Three Days</router-link>
                <router-link to="/hours" class="three-link">Hours</router-link>
                <router-link to="/now" class="link">Now</router-link>
                <router-link to="/checkup" class="btnCheckUp">Checkup</router-link>
            </div>
        </nav>
    </header>
    <div id="weather" class="weather-forecast">
        <!-- 使用v-for指令循环每个小时的天气数据 -->
        <div v-for="hour in limitedForecast" :key="hour.fxTime" class="weather-hour">
            <!-- 天气图标 -->
            <div class="weather-icon"><i :class="`qi-${hour.icon}`"></i></div>
            <h3>Time: {{ formatHour(hour.fxTime) }}</h3>
            <p>Temperature: {{ hour.temp }}°C</p >
            <p>Weather: {{ hour.text }}</p >
            <p>Wind Direction: {{ hour.windDir }}</p >
            <p>Wind Strength: {{ hour.windScale }}</p >
            <p>Wind Speed: {{ hour.windSpeed }}km/h</p >
            <p>Humidity: {{ hour.humidity }}%</p >
        </div>
    </div>
</template>

<script>
export default {
    name: "HourlyWeatherForecast",
    data() {
        return {
            hourlyForecast: []// 预报数据数组
        };
    },
    computed: {
        limitedForecast() {
            return this.hourlyForecast.slice(0, 6); // 只显示未来6小时的天气
        }
    },
    methods: {
        fetchWeather() {
            const location = "101280800"; // 佛山的位置代码
            const key = "5941238cf4b94075ad752b01506ec007";// 和风天气API密钥
            // 和风天气API的URL
            const url = `https://devapi.qweather.com/v7/weather/24h?location=${location}&key=${key}`;

            // 发送网络请求获取天气数据
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (data.code === "200") {
                        this.hourlyForecast = data.hourly;// 请求成功，存储天气预报数据
                    } else {
                        console.error("Error,please check api");// 请求失败的错误处理
                    }
                })
                .catch(error => {
                    console.error("Error during fetch:", error);// 网络或其他错误处理
                });
        },
        formatHour(fxTime) {
            const date = new Date(fxTime);
            return `${date.getHours()}时`;
        }
    },
    // 组件挂载后立即获取天气数据
    mounted() {
        this.fetchWeather();
    }
};
</script>

<style scoped>
    @import url('https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css');
    @import url('https://cdn.jsdelivr.net/npm/qweather-icons@1.3.0/font/qweather-icons.css');

header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 1.3rem 8%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
    background-color: rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(1.9rem);
}

header::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, #dddddd4d, transparent);
    transition: 0.4s;
    pointer-events: none;
}

header i {
    font-size: 4rem;
    color: #fff;
    margin-right: 60px;
}

header:hover::after {
    left: 40%;
}

.link,
.three-link {
    position: relative;
    font-size: 1.2rem;
    color: #fff;
    text-decoration: none;
    font-weight: 500;
    margin-left: 2.5rem;
}

.link::after,
.three-link::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -0.5rem;
    width: 100%;
    height: 0.19rem;
    background: #fff;
    border-radius: 0.3rem;
    transform: scaleX(0);
    transform-origin: left;
    transition: transform .4s;
}

.link:hover::after,
.three-link::after {
    transform: scaleX(1);
}

.btnCheckUp {
    margin-left: 0;
    width: 8rem;
    height: 3rem;
    line-height: 2.45rem;
    text-align: center;
    background: transparent;
    border: 0.13rem solid #fff;
    outline: none;
    border-radius: 1.5rem;
    cursor: pointer;
    font-size: 1.3rem;
    color: #fff;
    font-weight: 500;
    margin-left: 3rem;
    transition: .5s;
    text-decoration: none;
    display: inline-block;
}

.btnCheckUp:hover {
    background: #fff;
    color: #162938;
}

body {
    user-select: none;
    cursor: default;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: url(../back.jpg) no-repeat;
    background-size: cover;
    background-position: center;
}

.weather-forecast {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    padding: 20px;
    background-color: rgba(202, 202, 202, 0.4);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    gap: 20px;
}

.weather-day {
    border: 1px solid rgba(224, 224, 224, 0.3);
    padding: 20px;
    margin: 10px;
    border-radius: 15px;
    background-color: rgba(241, 241, 241, 0.2);
    backdrop-filter: blur(5px);
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    min-width: 200px;
    width: 250px;
}

.weather-day:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}

.weather-icon {
    font-size: 64px;
    color: white;
}

h3,
p {
    color: white;
    font-size: 18px;
    margin-bottom: 8px;
}

h1 {
    color: white;
    font-size: 24px;
    text-align: center;
    margin-bottom: 30px;
}

h2 {
    color: white;
    font-size: 32px;
}
</style>