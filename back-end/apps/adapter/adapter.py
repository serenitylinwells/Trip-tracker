import hashlib
import requests
from fastapi import APIRouter
from .settings import *
from ..orm.models import *

adapterApi = APIRouter()  # Create a router for this module


@adapterApi.post("/location")  # Location query interface
async def location(site: Site):
    # Build query parameters
    url = "http://api.wxbus163.cn/z_busapi/BusApi.php"
    data = {
        "optype": "tfrone",
        "uname": uname,
        "keySecret": hashlib.md5((uname + key + "tfrone").encode(encoding="UTF-8")).hexdigest(),
        "cityname": "佛山",  # City name
        "keywords": site.keywords
    }

    # Get data
    try:
        response = requests.post(url, data=data)
    except:
        # Request failed, possibly due to network issues
        return {"error": "Post failed", "results": None}

    # Format the data
    try:
        formatted_data = f_location(response.json()["returl_list"])
    except:
        # Unable to format the data, possibly due to abnormal source data
        return {"error": "Abnormal data returned", "results": None}
    return {"error": None, "results": formatted_data}


@adapterApi.post("/route")  # Route planning query interface
async def route(routeinfo: RouteInfo):
    # Build query parameters
    url = "http://api.wxbus163.cn/z_busapi/BusApi.php"
    data = {
        "optype": "tfrtwo",
        "uname": uname,
        "keySecret": hashlib.md5((uname + key + "tfrtwo").encode(encoding="UTF-8")).hexdigest(),
        "stasta": routeinfo.startPointName,
        "staimlgn": routeinfo.startPointSign,
        "endsta": routeinfo.endPointName,
        "endimlgn": routeinfo.endPointSign
    }

    # Get data
    try:
        response = requests.post(url, data=data)
    except:
        # Request failed, possibly due to network issues
        return {"error": "Post failed", "results": None}

    # Check if the route exists
    if response.json()["return_code"] == "error":
        # No matching route found
        return {"error": "The route does not exist", "results": None}

    # Format the data
    formatted_data = []
    try:
        for item in response.json()["returl_list"]:
            formatted_data.append({
                "time": item["xydurtime"],
                "distance": item["xcdist"],
                "route_name": item["xytitle"],
                "stations": f_route(item["lineinfo"])
            })
    except:
        # Unable to format the data, possibly due to abnormal source data
        return {"error": "Abnormal data returned", "results": None}
    return {"error": None, "results": formatted_data}


def f_location(data: list) -> list:  # Subroutine to format location data
    formatted_data = []
    for item in data:
        formatted_data.append({
            "name": item["xyname"],
            "address": item["xyaddress"],
            "sign": item["imlgn"]
        })
    return formatted_data


def f_route(data: list) -> list:  # Subroutine to format route data
    formatted_data = []
    for d in data:
        formatted_d = {}
        if d["stype"] == 1:
            formatted_d["type"] = 1
            formatted_d["station_name"] = d.get("staname")
            formatted_d["next_bus"] = d.get("hcbus")
            formatted_d["information"] = d.get("msg")
        elif d["stype"] == 2:
            formatted_d["type"] = 2
            formatted_d["station_name"] = None
            formatted_d["next_bus"] = None
            formatted_d["information"] = d.get("msg")
        elif d["stype"] == 3:
            formatted_d["type"] = 3
            formatted_d["station_name"] = d.get("staname")
            formatted_d["next_bus"] = None
            formatted_d["information"] = d.get("msg")
        elif d["stype"] == 4:
            formatted_d["type"] = 4
            formatted_d["station_name"] = d.get("staname")
            formatted_d["next_bus"] = None
            formatted_d["information"] = d.get("msg")
        formatted_data.append(formatted_d)
    return formatted_data
