from functools import wraps

from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response


def with_serializer(serializerClass, success_code=status.HTTP_201_CREATED,
                    dataGetter=lambda request: request.data,
                    **kwargs):
    def dec(func):
        @wraps(func)
        def c(*a, **k):

            if len(a) == 2:
                self, request = a[:2]
            elif len(a) == 1:
                self, request = None, a[0]
            else:
                raise AssertionError("Incorrect argument count")

            serializer = serializerClass(data=dataGetter(request), context={
                "request": request,
                "view": self
            }, **kwargs)

            if serializer.is_valid():
                a += (serializer, )
                out = func(*a, **k)

                if not isinstance(out, HttpResponse):
                    return Response(out, status=success_code)
                return out
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return c
    return dec
