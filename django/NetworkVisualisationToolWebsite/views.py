from django.shortcuts import render
from pathlib import Path 
from django.conf import settings
from django.shortcuts import redirect
import NetworkVisualisationFrontEnd.settings as ns
import subprocess, os, time
from constantly import ValueConstant, Values

class Discipline(Values):
   """
   Constants representing various specialties across the EMERGENCE network. 
   """
   COMPUTER_SCIENCE = ValueConstant("Computer Science")
   COMPUTER_SCIENCE_SHORTHAND = ValueConstant("CS")
   ROBOTICS = ValueConstant("Robotics")
   HEALTHCARE = ValueConstant("Healthcare")
   DESIGN_ENGINEERING_INNOVATION = ValueConstant("Design Engineering and Innovation")
   DESIGN_ENGINEERING_INNOVATION_SHORTHAND = ValueConstant("DEAI")
   ELECTRONIC_ENGINEERING = ValueConstant("Electronic Engineering")
   ELECTRONIC_ENGINEERING_SHORTHAND = ValueConstant("EE")
   SOCIAL_CARE = ValueConstant("Social Care")
   SOCIAL_CARE_SHORTHAND = ValueConstant("SC")
   PHYSIOTHERAPY = ValueConstant("Physiotherapy")
   INCLUDE_LEGEND_NODES = ValueConstant("include-legend-nodes")
   INCLUDE_CENTRAL_NODE = ValueConstant("include-central-nodes")

class Institution(Values):
    """
    Constants representing the Institutions within the network 
    """
    UNIVERSITY_OF_NOTTINGHAM = ValueConstant("University of Nottingham")
    UNIVERSITY_OF_NOTTINGHAM_SHORTHAND = ValueConstant("UoN")
    ASTRALINE_TECH = ValueConstant("Astraline TEC Ltd a Johnnie Johnson business")
    ATSTRALINE_SHORTHAND = ValueConstant("Astraline")
    ANGLIA_RUSKIN = ValueConstant("Anglia Ruskin University")
    ANGLIA_RUSKIN_SHORTHAND = ValueConstant("ARU")
    BOW = ValueConstant("BOW(Fomerly Cyberselves)")
    BOW_SHORTHAND = ValueConstant("Bow")
    BLACKWOOD = ValueConstant("Blackwood Homes and Care")
    BLACKWOOD_SHORTHAND = ValueConstant("Blackwood")
    BRISTOL_ROBOTICS_UWE = ValueConstant("Bristol Robotics University, UWE")
    BRISTOL_ROBOTICS_UWE_SHORTHAND = ValueConstant("BRU")
    CARDIFF_UNIVERSITY = ValueConstant("Cardiff University")
    CARDIFF_UNIVERSITY_SHORTHAND = ValueConstant("CU")
    EDINBURGH_ROBOTICS = ValueConstant("Edinburgh Centre for Robotics")
    EDINBURGH_ROBOTICS_SHORTHAND = ValueConstant("ECFR")
    HERIOT_WATT_UNIVERSITY = ValueConstant("Heriot-Watt University")
    HERIOT_WATT_UNIVERSITY_SHORTHAND = ValueConstant("HWU")
    IBM_UK_LTD = ValueConstant("IBM UK Ltd")
    IBM_UK_LTD_SHORTHAND = ValueConstant("IBM")
    KINGS_COLLEGE_LONDON = ValueConstant("King's College London")
    KINGS_COLLEGE_LONDON_SHORTHAND = ValueConstant("KCL")
    KONPANION = ValueConstant("Konpanion (BOROBO ltd)")
    KONPANION_SHORTHAND = ValueConstant("Konpanion")
    LOUGHBOROUGH = ValueConstant("Loughborough University")
    LOUGHBOROUGH_SHORTHAND = ValueConstant("LBU")
    NOTTINGHAM_TRENT = ValueConstant("Nottingham Trent University")
    NOTTINGHAM_TRENT_SHORTHAND = ValueConstant("NTU")
    ORBIT_RRI = ValueConstant("ORBIT RRI")
    ORBIT_RRI_SHORTHAND = ValueConstant("ORRI")
    OVAL_DESIGN = ValueConstant("Oval Design")
    OVAL_DESIGN_SHORTHAND = ValueConstant("OD")
    PIRG_HERTS_LTD = ValueConstant("PIRg Herts Ltd")
    PIRG_HERTS_LTD_SHORTHAND = ValueConstant("PIRgHLtd")
    QUEEN_MARY_UNIVERSITY_OF_LONDON = ValueConstant("Queen Mary University of London")
    QUEEN_MARY_SHORTHAND = ValueConstant("QMUL")
    SIMPLICARE_LTD = ValueConstant("Simplicare Ltd")
    SIMPLICARE_LTD_SHORTHAND = ValueConstant("Simplicare")
    SKILLS_FOR_CARE = ValueConstant("Skills for Care")
    SKILLS_FOR_CARE_SHORTHAND = ValueConstant("SFC")
    SWANSEA_UNIVERSITY = ValueConstant("Swansea University")
    SWANSEA_UNIVERSITY_SHORTHAND = ValueConstant("SWU")
    SCOTTISH_CARE = ValueConstant("Scottish Care")
    SCOTTISH_CARE_SHORTHAND = ValueConstant("ScotCare")
    SHEFFIELD_HALLAM_UNIVERSITY = ValueConstant("Sheffield Hallam University")
    SHEFFIELD_HALLAM_UNIVERSITY_SHORTHAND = ValueConstant("SHU")
    TRINITY_COLLEGE_DUBLIN = ValueConstant("Trinity College Dublin")
    TRINITY_COLLEGE_DUBLIN_SHORTHAND = ValueConstant("TCD")
    UWE_BRISTOL = ValueConstant("UWE Bristol")
    UWE_BRISTOL_SHORTHAND = ValueConstant("UWEB")
    UNIVERSITY_OF_ABERDEEN = ValueConstant("University of Aberdeen")
    UNIVERSITY_OF_ABERDEEN_SHORTHAND = ValueConstant("UoA")
    UNIVERSITY_OF_EDINBURGH = ValueConstant("University of Edinburgh")
    UNIVERSITY_OF_EDINBURGH_SHORTHAND = ValueConstant("UoE")
    UNIVERSITY_OF_GLASGOW = ValueConstant("University of Glasgow")
    UNIVERSITY_OF_GLASGOW_SHORTHAND = ValueConstant("UoG")
    UNIVERSITY_OF_HERTFORDSHIRE = ValueConstant("University of Herfordshire")
    UNIVERSITY_OF_HERTFORDSHIRE_SHORTHAND = ValueConstant("UoH")
    UNIVERSITY_OF_LINCOLN = ValueConstant("University of Licoln")
    UNIVERSITY_OF_LINCOLN_SHORTHAND = ValueConstant("UoL")
    UNIVERSITY_OF_PLYMOUTH = ValueConstant("University of Plymouth")
    UNIVERSITY_OF_PLYMOUTH_SHORTHAND = ValueConstant("UoP")
    UNIVERSITY_OF_SHEFFIELD = ValueConstant("University of Sheffield")
    UNIVERSITY_OF_SHEFFIELD_SHORTHAND = ValueConstant("UoSh")
    UNIVERSITY_OF_SOUTHAMPTON = ValueConstant("University of Southampton")
    UNIVERSITY_OF_SOUTHAMPTION_SHORTHAND = ValueConstant("UoS")
    UNIVERSITY_OF_YORK = ValueConstant("University of York")
    UNIVERSITY_OF_YORK_SHORTHAND = ValueConstant("UoY")
    UNIVERSITY_OF_WEST_OF_ENGLAND = ValueConstant("University of West of England")
    UNIVERSITY_OF_WEST_OF_ENGLAND_SHORTHAND = ValueConstant("UoWoE")

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

def shorthandParameters(filterParameter1, filterParameter2):
    """
    Function that converts the longhand form of a paramter to its appropriate shorthand i.e. "Computer Science" -> "CS"
    """
    match filterParameter1:
       case Discipline.COMPUTER_SCIENCE.value:
           filterParameter1 = Discipline.COMPUTER_SCIENCE_SHORTHAND.value
       case Discipline.DESIGN_ENGINEERING_INNOVATION.value:
           filterParameter1 = Discipline.DESIGN_ENGINEERING_INNOVATION_SHORTHAND.value
       case Discipline.ELECTRONIC_ENGINEERING.value:
           filterParameter1 = Discipline.ELECTRONIC_ENGINEERING_SHORTHAND.value
       case Discipline.SOCIAL_CARE.value:
           filterParameter1 = Discipline.SOCIAL_CARE_SHORTHAND.value   
       case Institution.UNIVERSITY_OF_NOTTINGHAM.value:
           filterParameter1 = Institution.UNIVERSITY_OF_NOTTINGHAM_SHORTHAND.value 
       case Institution.ASTRALINE_TECH.value:
          filterParameter1 = Institution.ATSTRALINE_SHORTHAND.value
       case Institution.UNIVERSITY_OF_ABERDEEN.value:
          filterParameter1 = Institution.UNIVERSITY_OF_ABERDEEN_SHORTHAND.value
       case Institution.UNIVERSITY_OF_EDINBURGH.value:
          filterParameter1 = Institution.UNIVERSITY_OF_EDINBURGH_SHORTHAND.value
       case Institution.UNIVERSITY_OF_GLASGOW.value:
          filterParameter1 = Institution.UNIVERSITY_OF_GLASGOW_SHORTHAND.value
       case Institution.UNIVERSITY_OF_HERTFORDSHIRE.value:
          filterParameter1 = Institution.UNIVERSITY_OF_HERTFORDSHIRE_SHORTHAND.value 
       case Institution.UNIVERSITY_OF_LINCOLN.value:
          filterParameter1 = Institution.UNIVERSITY_OF_LINCOLN_SHORTHAND
       case Institution.BOW.value: 
          filterParameter1 = Institution.BOW_SHORTHAND.value 
       case Institution.BLACKWOOD.value:
          filterParameter1 = Institution.BLACKWOOD_SHORTHAND.value
       case Institution.BRISTOL_ROBOTICS_UWE.value:
          filterParameter1 = Institution.BRISTOL_ROBOTICS_UWE_SHORTHAND.value
       case Institution.UWE_BRISTOL.value:
          filterParameter1 = Institution.UWE_BRISTOL_SHORTHAND.value
       case Institution.CARDIFF_UNIVERSITY.value:
          filterParameter1 = Institution.CARDIFF_UNIVERSITY_SHORTHAND.value
       case Institution.KINGS_COLLEGE_LONDON.value:
          filterParameter1 = Institution.KINGS_COLLEGE_LONDON_SHORTHAND.value
       case Institution.TRINITY_COLLEGE_DUBLIN.value:
          filterParameter1 = Institution.TRINITY_COLLEGE_DUBLIN_SHORTHAND.value
       case Institution.SCOTTISH_CARE.value:
          filterParameter1 = Institution.SCOTTISH_CARE_SHORTHAND.value
       case Institution.SKILLS_FOR_CARE.value:
          filterParameter1 = Institution.SKILLS_FOR_CARE_SHORTHAND.value
       case Institution.OVAL_DESIGN.value:
          filterParameter1 = Institution.OVAL_DESIGN_SHORTHAND.value
       case Institution.EDINBURGH_ROBOTICS.value:
          filterParameter1 = Institution.EDINBURGH_ROBOTICS_SHORTHAND.value
       case Institution.UNIVERSITY_OF_WEST_OF_ENGLAND.value:
          filterParameter1 = Institution.UNIVERSITY_OF_WEST_OF_ENGLAND_SHORTHAND.value
       case Institution.UNIVERSITY_OF_GLASGOW.value:
          filterParameter1 = Institution.UNIVERSITY_OF_GLASGOW_SHORTHAND.value
       case Institution.HERIOT_WATT_UNIVERSITY.value:
          filterParameter1 = Institution.HERIOT_WATT_UNIVERSITY_SHORTHAND.value
       case Institution.PIRG_HERTS_LTD.value:
          filterParameter1 = Institution.PIRG_HERTS_LTD_SHORTHAND.value 
       case Institution.SHEFFIELD_HALLAM_UNIVERSITY.value:
          filterParameter1 = Institution.SHEFFIELD_HALLAM_UNIVERSITY_SHORTHAND.value 
       case Institution.UNIVERSITY_OF_HERTFORDSHIRE.value:
          filterParameter1 = Institution.UNIVERSITY_OF_HERTFORDSHIRE_SHORTHAND.value
       case Institution.IBM_UK_LTD.value:
          filterParameter1 = Institution.IBM_UK_LTD_SHORTHAND.value
       case Institution.KONPANION.value:
          filterParameter1 = Institution.KONPANION_SHORTHAND.value
       case Institution.ANGLIA_RUSKIN.value:
          filterParameter1 = Institution.ANGLIA_RUSKIN_SHORTHAND.value
       case Institution.LOUGHBOROUGH.value:
          filterParameter1 = Institution.LOUGHBOROUGH_SHORTHAND.value
       case Institution.ORBIT_RRI.value:
          filterParameter1 = Institution.ORBIT_RRI_SHORTHAND.value
       case Institution.PIRG_HERTS_LTD.value:
          filterParameter1 = Institution.PIRG_HERTS_LTD_SHORTHAND.value
       case Institution.QUEEN_MARY_UNIVERSITY_OF_LONDON.value:
          filterParameter1 = Institution.QUEEN_MARY_SHORTHAND.value
       case Institution.SIMPLICARE_LTD.value:
          filterParameter1 = Institution.SIMPLICARE_LTD_SHORTHAND.value
       case Institution.SWANSEA_UNIVERSITY.value:
          filterParameter1 = Institution.SWANSEA_UNIVERSITY_SHORTHAND.value 
       case Institution.NOTTINGHAM_TRENT.value: 
          filterParameter1 = Institution.NOTTINGHAM_TRENT_SHORTHAND.value
       case Institution.UNIVERSITY_OF_SHEFFIELD.value:
          filterParameter1 = Institution.UNIVERSITY_OF_SHEFFIELD_SHORTHAND.value
       case Institution.UNIVERSITY_OF_SOUTHAMPTON.value: 
          filterParameter1 = Institution.UNIVERSITY_OF_SOUTHAMPTION_SHORTHAND.value 
       case Institution.UNIVERSITY_OF_YORK.value:
          filterParameter1 = Institution.UNIVERSITY_OF_YORK_SHORTHAND.value
    match filterParameter2: 
       case Discipline.COMPUTER_SCIENCE.value:
           filterParameter2 = Discipline.COMPUTER_SCIENCE_SHORTHAND.value
       case Discipline.DESIGN_ENGINEERING_INNOVATION.value:
           filterParameter2 = Discipline.DESIGN_ENGINEERING_INNOVATION_SHORTHAND.value
       case Discipline.ELECTRONIC_ENGINEERING.value:
           filterParameter2 = Discipline.ELECTRONIC_ENGINEERING_SHORTHAND.value
       case Discipline.SOCIAL_CARE.value:
           filterParameter2 = Discipline.SOCIAL_CARE_SHORTHAND.value 
       case Institution.UNIVERSITY_OF_NOTTINGHAM.value:
           filterParameter2 = Institution.UNIVERSITY_OF_NOTTINGHAM_SHORTHAND.value
       case Institution.ASTRALINE_TECH.value:
          filterParameter2 = Institution.ATSTRALINE_SHORTHAND.value
       case Institution.UNIVERSITY_OF_ABERDEEN.value:
          filterParameter2 = Institution.UNIVERSITY_OF_ABERDEEN_SHORTHAND.value
       case Institution.UNIVERSITY_OF_EDINBURGH.value:
          filterParameter2 = Institution.UNIVERSITY_OF_EDINBURGH_SHORTHAND.value
       case Institution.UNIVERSITY_OF_GLASGOW.value:
          filterParameter2 = Institution.UNIVERSITY_OF_GLASGOW_SHORTHAND.value
       case Institution.UNIVERSITY_OF_HERTFORDSHIRE.value:
          filterParameter2 = Institution.UNIVERSITY_OF_HERTFORDSHIRE_SHORTHAND.value 
       case Institution.UNIVERSITY_OF_LINCOLN.value:
          filterParameter2 = Institution.UNIVERSITY_OF_LINCOLN_SHORTHAND
       case Institution.BOW.value: 
          filterParameter2 = Institution.BOW_SHORTHAND.value 
       case Institution.BLACKWOOD.value:
          filterParameter2 = Institution.BLACKWOOD_SHORTHAND.value
       case Institution.BRISTOL_ROBOTICS_UWE.value:
          filterParameter2 = Institution.BRISTOL_ROBOTICS_UWE_SHORTHAND.value
       case Institution.UWE_BRISTOL.value:
          filterParameter2 = Institution.UWE_BRISTOL_SHORTHAND.value
       case Institution.CARDIFF_UNIVERSITY.value:
          filterParameter2 = Institution.CARDIFF_UNIVERSITY_SHORTHAND.value
       case Institution.KINGS_COLLEGE_LONDON.value:
          filterParameter2 = Institution.KINGS_COLLEGE_LONDON_SHORTHAND.value
       case Institution.TRINITY_COLLEGE_DUBLIN.value:
          filterParameter2 = Institution.TRINITY_COLLEGE_DUBLIN_SHORTHAND.value
       case Institution.SCOTTISH_CARE.value:
          filterParameter2 = Institution.SCOTTISH_CARE_SHORTHAND.value
       case Institution.SKILLS_FOR_CARE.value:
          filterParameter2 = Institution.SKILLS_FOR_CARE_SHORTHAND.value
       case Institution.OVAL_DESIGN.value:
          filterParameter2 = Institution.OVAL_DESIGN_SHORTHAND.value
       case Institution.EDINBURGH_ROBOTICS.value:
          filterParameter2 = Institution.EDINBURGH_ROBOTICS_SHORTHAND.value
       case Institution.UNIVERSITY_OF_WEST_OF_ENGLAND.value:
          filterParameter2 = Institution.UNIVERSITY_OF_WEST_OF_ENGLAND_SHORTHAND.value
       case Institution.UNIVERSITY_OF_GLASGOW.value:
          filterParameter2 = Institution.UNIVERSITY_OF_GLASGOW_SHORTHAND.value
       case Institution.HERIOT_WATT_UNIVERSITY.value:
          filterParameter2 = Institution.HERIOT_WATT_UNIVERSITY_SHORTHAND.value
       case Institution.PIRG_HERTS_LTD.value:
          filterParameter2 = Institution.PIRG_HERTS_LTD_SHORTHAND.value 
       case Institution.SHEFFIELD_HALLAM_UNIVERSITY.value:
          filterParameter2 = Institution.SHEFFIELD_HALLAM_UNIVERSITY_SHORTHAND.value 
       case Institution.UNIVERSITY_OF_HERTFORDSHIRE.value:
          filterParameter2 = Institution.UNIVERSITY_OF_HERTFORDSHIRE_SHORTHAND.value
       case Institution.IBM_UK_LTD.value:
          filterParameter2 = Institution.IBM_UK_LTD_SHORTHAND.value
       case Institution.KONPANION.value:
          filterParameter2 = Institution.KONPANION_SHORTHAND.value
       case Institution.LOUGHBOROUGH.value:
          filterParameter2 = Institution.LOUGHBOROUGH_SHORTHAND.value
       case Institution.ORBIT_RRI.value:
          filterParameter2 = Institution.ORBIT_RRI_SHORTHAND.value
       case Institution.PIRG_HERTS_LTD.value:
          filterParameter2 = Institution.PIRG_HERTS_LTD_SHORTHAND.value
       case Institution.QUEEN_MARY_UNIVERSITY_OF_LONDON.value:
          filterParameter2 = Institution.QUEEN_MARY_SHORTHAND.value
       case Institution.SIMPLICARE_LTD.value:
          filterParameter2 = Institution.SIMPLICARE_LTD_SHORTHAND.value
       case Institution.SWANSEA_UNIVERSITY.value:
          filterParameter2 = Institution.SWANSEA_UNIVERSITY_SHORTHAND.value 
       case Institution.NOTTINGHAM_TRENT.value: 
          filterParameter2 = Institution.NOTTINGHAM_TRENT_SHORTHAND.value
       case Institution.UNIVERSITY_OF_SHEFFIELD.value:
          filterParameter2 = Institution.UNIVERSITY_OF_SHEFFIELD_SHORTHAND.value
       case Institution.UNIVERSITY_OF_SOUTHAMPTON.value: 
          filterParameter2 = Institution.UNIVERSITY_OF_SOUTHAMPTION_SHORTHAND.value 
       case Institution.UNIVERSITY_OF_YORK.value:
          filterParameter2 = Institution.UNIVERSITY_OF_YORK_SHORTHAND.value
       case Institution.ANGLIA_RUSKIN.value:
          filterParameter2 = Institution.ANGLIA_RUSKIN_SHORTHAND.value
    return filterParameter1, filterParameter2

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
 
    

