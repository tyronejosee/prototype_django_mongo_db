"""Views for Utils App."""

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from mongoengine.connection import get_connection


class MongoHealthCheckView(APIView):
    """View for MongoDB health check."""

    def get(self, request: Request) -> Response:
        try:
            # Ping the MongoDB server
            conn = get_connection()
            conn.admin.command("ping")
            return Response(
                {"status": "ok", "mongo": "connected"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"status": "error", "mongo": "unreachable", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
