from rest_framework.response import Response

class ResponseBuilder:
    def get_response(self, message, status):
        return Response(data={'message': message}, status=status)
    