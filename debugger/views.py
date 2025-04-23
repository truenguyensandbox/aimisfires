from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
import sys
import traceback

def index(request):
    return render(request, 'debugger/index.html')

@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        blocked = ["import os", "import sys", "open(", "eval(", "exec(", "while True", "__"]

        if any(bad in code for bad in blocked):
            return JsonResponse({'output': '❌ Unsafe code detected. Please avoid restricted keywords.'})

        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()

        try:
            exec(code, {})
            output = redirected_output.getvalue()
        except Exception:
            output = traceback.format_exc()
        finally:
            sys.stdout = old_stdout

        return JsonResponse({'output': output})

    return JsonResponse({'output': 'Invalid request method'})
from django.shortcuts import render

def about(request):
    return render(request, 'debugger/about.html')
