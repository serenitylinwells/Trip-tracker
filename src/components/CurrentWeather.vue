<template>
    <header>
        <i class='bx bx-cloud'></i>
        <h2 class="logo">Foshan Weather Forecast</h2>
        <nav>
            <div>
                <router-link to="/three-days" class="link">Three Days</router-link>
                <router-link to="/hours" class="link">Hours</router-link>
                <router-link to="/now" class="three-link">Now</router-link>
                <router-link to="/checkup" class="btnCheckUp">Checkup</router-link>
            </div>
        </nav>
    </header>
    <div class="weather-container">
        <div v-if="weatherData" class="weather-detail">
            <h1>Live Weather</h1>
            <p>Temperature: {{ weatherData.now.temp }}°C</p >
            <p>Feels Like: {{ weatherData.now.feelsLike }}°C</p >
            <p>Wind Direction: {{ weatherData.now.windDir }}</p >
            <p>Wind Scale: {{ weatherData.now.windScale }}</p >
            <p>Relative Humidity: {{ weatherData.now.humidity }}%</p >
        </div>
        <div v-if="weatherData" class="weather-detail">
            <h1>More Information</h1>
            <p>Pressure: {{ weatherData.now.pressure }} hPa</p >
            <p>Precipitation: {{ weatherData.now.precip }} mm</p >
            <p>Visibility: {{ weatherData.now.vis }} km</p >
            <p>Cloud Cover: {{ weatherData.now.cloud }}%</p >
            <p>Dew Point: {{ weatherData.now.dew }}°C</p >
        </div>
        <!-- 如果有错误信息，则显示错误 -->
        <div v-else-if="error">
            <p>{{ error }}</p >
        </div>
        <!-- 在加载数据时显示加载中... -->
        <div v-else>
            <p>Loading...</p >
        </div>
    </div>
</template>

<script>
export default {
    name: 'RealTimeWeather',
    data() {
        return {
            weatherData: null// 存储天气数据的变量
        };
    },
    methods: {
        fetchWeatherData() {
            const location = "101280800"; // 佛山的位置代码
            const key = "5941238cf4b94075ad752b01506ec007"; // 和风天气API密钥
            // 和风天气API的URL
            const url = `https://devapi.qweather.com/v7/weather/now?location=${location}&key=${key}`;

            // 发送网络请求获取天气数据
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (data.code === "200") {
                        this.weatherData = data;// 请求成功，存储天气预报数据
                    } else {
                        console.error("Error,please check api");// 请求失败的错误处理
                    }
                })
                .catch(error => {
                    console.error("Error during fetch:", error);// 网络或其他错误处理
                });
        }    
    },
    // 组件挂载后立即获取天气数据
    mounted() {
        this.fetchWeatherData();
    }
};
</script>

<style scoped>
    @import url('https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css');

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
.weather-container {
    min-width: 600px;
    width: 700px;
    margin: 20px auto; 
    padding: 40px; 
    background: rgba(201, 201, 201, 0.4);
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(5px);
    display: flex;
    flex-direction: row;
    justify-content: space-between; 
    align-items: center;
    transition: transform 0.3s, box-shadow 0.3s; 
}

.weather-container:hover {
    transform: translateY(-5px); 
    box-shadow: 0 12px 20px rgba(0, 0, 0, 0.3);
}

.weather-detail {
    width: 48%; 
}

.weather-detail:first-child {
    border-right: 2px solid rgba(0, 0, 0, 0.1);
    padding-right: 20px; 
}

.weather-detail:last-child {
    padding-left: 20px; 
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