import requests
from fastapi import APIRouter

from app.dtos import Killers
from app.soap_utils.soap_methods import SoapMethods
from config import configuration
import xmltodict
import json

killers_router = APIRouter()


@killers_router.post("/teams/create/{teamId}/{teamName}/{teamSize}/{startCaveId}")
async def create_team(teamId: int, teamName: str, teamSize: int, startCaveId: int, killers: Killers):
    body_xml = SoapMethods.create_killer_team(teamId, teamName, teamSize, startCaveId, killers)
    response = requests.post(url=configuration.SOAP_SERVICE_URL, data=body_xml)

    if response.status_code == 200:
        dict_data = xmltodict.parse(response.text)
        team_data = dict_data.get("SOAP-ENV:Envelope", {}).get("SOAP-ENV:Body", {}).get("teamResponse", {}).get("ns3:team", {})
        json_data = json.dumps(team_data, ensure_ascii=False, indent=4)
        response = json.loads(json_data)
        return response
    else:
        dict_data = xmltodict.parse(response.text)
        error_text = dict_data.get("SOAP-ENV:Envelope", {}).get("SOAP-ENV:Body", {}).get("SOAP-ENV:Fault", {}).get("faultstring", {}).get("#text", str(response.text))
        return error_text


@killers_router.post("/team/{teamId}/move-to-cave/{caveId}")
async def move_team(teamId: int, caveId: int):
    body_xml = SoapMethods.move_killer_team_to_cave(teamId, caveId)
    response = requests.post(url=configuration.SOAP_SERVICE_URL, data=body_xml)


    if response.status_code == 200:
        dict_data = xmltodict.parse(response.text)
        team_data = dict_data.get("SOAP-ENV:Envelope", {}).get("SOAP-ENV:Body", {}).get("teamResponse", {}).get("ns3:team", {})
        json_data = json.dumps(team_data, ensure_ascii=False, indent=4)
        response = json.loads(json_data)
        return response
    else:
        dict_data = xmltodict.parse(response.text)
        error_text = dict_data.get("SOAP-ENV:Envelope", {}).get("SOAP-ENV:Body", {}).get("SOAP-ENV:Fault", {}).get("faultstring", {}).get("#text", str(response.text))
        return error_text

@killers_router.post("/{killerId}/killed-dragons")
async def move_team(killerId: int):
    body_xml = SoapMethods.get_dragons_killed_by_killer_find_by_id(killerId)
    response = requests.post(url=configuration.SOAP_SERVICE_URL, data=body_xml)


    if response.status_code == 200:
        dict_data = xmltodict.parse(response.text)
        json_string = dict_data.get("SOAP-ENV:Envelope", {}).get("SOAP-ENV:Body", {}).get("DragonListResponse", {}).get("ns3:dragons", [])

        return json_string
    else:
        dict_data = xmltodict.parse(response.text)
        error_text = dict_data.get("SOAP-ENV:Envelope", {}).get("SOAP-ENV:Body", {}).get("SOAP-ENV:Fault", {}).get("faultstring", {}).get("#text", str(response.text))
        return error_text
