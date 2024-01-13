import requests
from typing import Dict, Any

DefaultHTTPGetAddress = "https://checkip.amazonaws.com"

class APIGatewayProxyRequest:
    def __init__(self, **kwargs: Any):
        self.__dict__ = kwargs

class APIGatewayProxyResponse:
    def __init__(self, headers: Dict[str, str], body: str, statusCode: int):
        self.headers = headers
        self.body = body
        self.statusCode = statusCode

def handler(request: APIGatewayProxyRequest) -> APIGatewayProxyResponse:
    try:
        resp = requests.get(DefaultHTTPGetAddress)
        resp.raise_for_status()

        if resp.status_code != 200:
            raise Exception("Non 200 Response found")

        ip = resp.text.strip()
        if not ip:
            raise Exception("No IP in HTTP response")

        return APIGatewayProxyResponse(
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
            },
            body='{"count": "2"}',
            statusCode=200
        )

    except Exception as e:
        return APIGatewayProxyResponse(headers={}, body=str(e), statusCode=500)

def main():
    # For testing locally, you can create a dummy APIGatewayProxyRequest
    request = APIGatewayProxyRequest()
    response = handler(request)
    print(response.__dict__)

if __name__ == "__main__":
    main()