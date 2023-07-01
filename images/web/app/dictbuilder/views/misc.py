import json
from django.http import JsonResponse
from django.views import View
import inspect
from django.shortcuts import render


class DynamicArgsView(View):
    def get(self, request, *args, **kwargs):
        function_namespace = kwargs.get("function_namespace", None)

        # Split the namespace by dots
        modules = function_namespace.split(".")

        # Import the module
        module = __import__(modules[0])

        for mod in modules[1:-1]:
            module = getattr(module, mod)

        func_name = modules[-1]

        # Get the function from the module
        function = getattr(module, func_name)

        # Get the function arguments
        argspec = inspect.getfullargspec(function)

        # # Prepare the arguments from the request
        # func_args = {
        #     arg: request.GET.get(arg, None) for arg in argspec.args if arg != "self"
        # }

        # Call the function with the prepared arguments
        # response = function(**func_args)

        return JsonResponse({"response": argspec.args})
