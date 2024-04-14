from django.shortcuts import render
from pathlib import Path 
from django.conf import settings
from django.shortcuts import redirect
import NetworkVisualisationFrontEnd.settings as ns
import subprocess, os
import time

# Create your views here.
def home(request, empty_search):
    return render(request, "NetworkVisualisationToolWebsite/home.html", {'empty_search' : empty_search})

def about(request):
    return render(request, "NetworkVisualisationToolWebsite/about.html", {})

def howto(request):
    return render(request, "NetworkVisualisationToolWebsite/how-to.html", {})

def test(request):
    fC1 = ns.fC1 
    fP1 = ns.fP1 
    fC2 = ns.fC2 
    fP2 = ns.fP2
    fP1, fP2 = shorthandParameters(fP1, fP2)
    ns.fP1 = fP1
    ns.fP2 = fP2
    return render(request, "NetworkVisualisationToolWebsite/PythonNetworkVisualisation{}{}{}{}.html".format(fC1, fP1, fC2, fP2))

def shorthandParameters(fP1, fP2):
    match fP1:
       case "Computer Science":
           fP1 = "CS"
       case "Design Engineering and Innovation":
           fP1 = "DEAI"
       case "Electronic Engineering":
           fP1 = "EE"
       case "Social Care":
           fP1 = "SC"   
       case "University of Nottingham":
           fP1 = "UoN"
    match fP2:
       case "Computer Science":
           fP2 = "CS"
       case "Design Engineering and Innovation":
           fP2 = "DEAI"
       case "Electronic Engineering":
           fP2 = "EE"
       case "Social Care":
           fP2 = "SC"   
       case "University of Nottingham":
           fP2 = "UoN"
    return fP1, fP2

def applyFiltrationOptions(request, filterCategory1, filterParameter1, filterCategory2, filterParameter2):
    if request.method == "GET":
        filterCategory1 = request.GET.get('filterCategory1')
        filterParameter1 = request.GET.get('filterParameter1')
        filterCategory2 = request.GET.get('filterCategory2')
        filterParameter2 = request.GET.get('filterParameter2')
    ns.fC1 = filterCategory1
    ns.fP1 = filterParameter1
    ns.fC2 = filterCategory2
    ns.fP2 = filterParameter2
    networkVisualisationScript = "NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/NetworkVisualisationToolUpdated.py"
    process = subprocess.Popen(['Python', networkVisualisationScript, filterCategory1, filterParameter1, 
                      filterCategory2, filterParameter2])
    streamdata = process.communicate()[0]
    emptySearch = process.returncode
    time.sleep(2)
    if (emptySearch):
        return redirect('home', emptySearch)
    return redirect('home')

def resetFiltrationOptions(request): 
    ns.fC1 = ""
    ns.fP1 = ""
    ns.fC2 = ""
    ns.fP2 = ""
    return redirect('home')
 
    

