from app.dtos import Killers
from app.utils import generate_xml_by_list
from config import configuration


class SoapMethods:

    @staticmethod
    def create_killer_team(team_id: int, team_name: str, team_size: int, start_cave_id: int,
                           killers: Killers) -> str:
        killers_list = generate_xml_by_list("<service:killers>", killers.killers, "</service:killers>")

        body = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:service="{configuration.SOAP_SERVICE_URL}">
    <soap:Header/>
    <soap:Body>
        <service:CreateKillerTeamRequest>
            <service:teamId>{team_id}</service:teamId>
            <service:teamName>{team_name}</service:teamName>
            <service:teamSize>{team_size}</service:teamSize>
            <service:startCaveId>{start_cave_id}</service:startCaveId>
            {killers_list}
        </service:CreateKillerTeamRequest>
    </soap:Body>
</soap:Envelope>
                """

        return body

    @staticmethod
    def move_killer_team_to_cave(team_id: int, cave_id: int) -> str:
        body = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:service="{configuration.SOAP_SERVICE_URL}">
    <soap:Header/>
    <soap:Body>
        <service:MoveKillerTeamToCaveRequest>
            <service:teamId>{team_id}</service:teamId>
            <service:caveId>{cave_id}</service:caveId>
        </service:MoveKillerTeamToCaveRequest>
    </soap:Body>
</soap:Envelope>
                """

        return body

    @staticmethod
    def get_dragons_killed_by_killer_find_by_id(killer_id: int):
        body = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:service="{configuration.SOAP_SERVICE_URL}">
    <soap:Header/>
    <soap:Body>
        <service:GetDragonsKilledByKillerFindByIdRequest>
            <service:id>{killer_id}</service:id>
        </service:GetDragonsKilledByKillerFindByIdRequest>
    </soap:Body>
</soap:Envelope>
                """

        return body
