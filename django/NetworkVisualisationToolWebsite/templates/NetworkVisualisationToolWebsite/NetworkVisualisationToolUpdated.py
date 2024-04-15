from constantly import ValueConstant, Values
from textwrap3 import wrap
import gravis as gv, networkx as nx, openpyxl, random, sys

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

class Colour(Values):
   """
   Constants representing the various colours of the nodes within the network visualisation
   """
   RED = ValueConstant("red")
   BLUE = ValueConstant("blue")
   GREEN = ValueConstant("green")
   YELLOW = ValueConstant("yellow")
   ORANGE = ValueConstant("orange")
   MAGENTA = ValueConstant("magenta")
   PURPLE = ValueConstant("purple")

class Misc(Values):
   """
   Constants representing miscellaneous values used within the program.  
   """
   ORIGIN = ValueConstant('origin')
   REMOTE = ValueConstant('remote')
   ERROR_MESSAGE = ValueConstant('Some error occured while pushing the code')
   PATH_OF_GIT_REPO = ValueConstant(r'')
   COMMIT_MESSAGE = ValueConstant('New members added to the dataset')
   EXCEL_FILE = ValueConstant("NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/NetworkVisualisationData/EMERGENCECollatedData.xlsx")
   ZERO = ValueConstant(0)
   ONE = ValueConstant(1)
   TWO = ValueConstant(2)
   THREE = ValueConstant(3)
   FOUR = ValueConstant(4)
   FIVE = ValueConstant(5)
   SIX = ValueConstant(6)
   SEVEN = ValueConstant(7)
   EIGHT = ValueConstant(8)
   NINE = ValueConstant(9)
   TEN = ValueConstant(10)
   ELEVEN = ValueConstant(11)
   TWELVE = ValueConstant(12)
   THIRTEEN = ValueConstant(13)
   WIDTH_RESOLUTION_VISUALISATION = ValueConstant(1000)
   HEIGHT_RESOLUTION_VISUALISATION = ValueConstant(1000) 
   STREAMLIT_TITLE = ValueConstant("EMERGENCE Network Visualisation Tool")
   STREAMLIT_TEXT = ValueConstant("Refer to the EMERGENCE website for instructions on how to use")
   LEGEND_TITLE = ValueConstant("Legend Node: ")
   ONE_HUNDRED = ValueConstant(100)
   FOUR_HUNDRED = ValueConstant(400)
   LEGEND_X_VALUE = ValueConstant(-1500)
   LEGEND_Y_VALUE = ValueConstant(-1250)
   LEGEND_NODE_SIZE = ValueConstant(75)
   LEGEND_SHAPE = ValueConstant("box")
   LEGEND_WIDTH_CONSTRAINT = ValueConstant(150)
   LEGEND_FONT_SIZE = ValueConstant(20)
   CENTRAL_NODE_ID = ValueConstant("Central Node")
   CENTRAL_NODE_LABEL = ValueConstant("Emergence Network")
   CENRAL_NODE_COLOUR = ValueConstant("black")
   READ_MODE = ValueConstant("r")
   ENCODING = ValueConstant("utf-8")
   HTML_FILE_NAME = ValueConstant("network_visualisation.html")
   NAME = ValueConstant("Name: ")
   INSTITUTION = ValueConstant("\nInstitution: ")
   JOB_TITLE = ValueConstant("\nJob Title: ")
   DISCIPLINE = ValueConstant("\nDiscipline: ")
   LOCATION_SECTION = ValueConstant("\nLocation: ")
   RESEARCH_THEMES = ValueConstant("\nResearch themes of interest: ")
   TRUE = ValueConstant(True)
   FALSE = ValueConstant(False)
   NEWLINE = ValueConstant("\n")
   VALUE = ValueConstant("value")
   ID = ValueConstant("id")
   TITLE = ValueConstant("title")
   ALPHABET = ValueConstant("alphabet")
   ALPHABETICAL = ValueConstant("Alphabetical")
   GROUP = ValueConstant("group")
   LABEL = ValueConstant("label")
   SIZE = ValueConstant("size")
   FIXED = ValueConstant("fixed")
   X = ValueConstant("x")
   Y = ValueConstant("y")
   PHYSICS = ValueConstant("physics")
   SHAPE = ValueConstant("shape")
   TMP = ValueConstant('tmp')
   WIDTH_CONSTRAINT = ValueConstant("widthConstraint")
   FONT = ValueConstant("font")
   DISCIPLINE_WORD = ValueConstant("Discipline")
   INSTITUTION_WORD = ValueConstant("Institution")
   SIZE = ValueConstant("size")
   LOCATION = ValueConstant("Location")
   PX = ValueConstant('{fpixels}px')
   HEIGHT = ValueConstant("1080px")
   WIDTH = ValueConstant("100%")
   BGCOLOUR = ValueConstant("#fffff")
   HTML_FILES = ValueConstant("html_files")
   FORMATTED_HTML_FILE_NAME = ValueConstant("{path_label}\\network_visualisation.html")
   PAGE_LAYOUT = ValueConstant("wide")
   ALL = ValueConstant("All") 
   EMPTY_STRING = ValueConstant("")
   NONE = ValueConstant("None")
   SCALE = ValueConstant(1000)
   FNAME = ValueConstant("NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/PythonNetworkVisualisation{}{}{}{}.html")
   SIZE = ValueConstant("size")
   HOVER = ValueConstant("hover")
   SEVENTYFIVE = ValueConstant(75)
   FIFTY = ValueConstant(50)
   COLOR = ValueConstant("color")
   SEVENFIFTY = ValueConstant(750)


class Legend(Values):
   """
   Constants representing the numerical values for the Legend nodes
   """
   ONETHREESIX = ValueConstant(136)
   ONETHREESEVEN = ValueConstant(137)
   ONETHREEEIGHT = ValueConstant(138)
   ONETHREENINE = ValueConstant(139)
   ONEFOURTY = ValueConstant(140)
   ONEFOURONE = ValueConstant(141)
   ONEFOURTWO = ValueConstant(142)
   ONEFOURTHREE = ValueConstant(143)
   ONEFOURFOUR = ValueConstant(144)

class LegendCoordinates(Values):
   """
   Constants representing the coordinates for the legend nodes
   """
   POINT_ONE = ValueConstant((250,750))
   POINT_TWO = ValueConstant((750,1250))
   POINT_THREE = ValueConstant((750,250))
   POINT_FOUR = ValueConstant((500,-750))
   POINT_FIVE = ValueConstant((150,-750))
   POINT_SIX = ValueConstant((-500,-750))
   POINT_SEVEN = ValueConstant((-750,250))
   MIN_RANGE = ValueConstant(-1001)
   MAX_RANGE = ValueConstant(1001)

class VisualisationSettings(Values):
   ZOOM_FACTOR = ValueConstant(0.45)
   NODE_LABEL_FONT = ValueConstant("Archivo Black")
   GRAPH_HEIGHT = ValueConstant(900)
   LAYOUT_ALGORITHM = ValueConstant("barnesHut")


def setMemberColour(specialty):
   """
   Returns a specific node-colour based on the member's specialty.  
   """
   #Colours nodes a unique colour according to the specialty
   if (specialty == Discipline.COMPUTER_SCIENCE.value):
      #All Computer Scientists are coloured as red
      return Colour.RED.value
   elif (specialty == Discipline.ROBOTICS.value):
      #All Roboticists are coloured as blue
      return Colour.BLUE.value
   elif (specialty == Discipline.DESIGN_ENGINEERING_INNOVATION.value):
      #All Design Engineers are coloured Green
      return Colour.GREEN.value
   elif (specialty == Discipline.HEALTHCARE.value):
      #All Healthcare professionals are coloured yellow
      return Colour.YELLOW.value
   elif (specialty == Discipline.PHYSIOTHERAPY.value):
      #All Physiotherapsists are coloured orange
      return Colour.ORANGE.value
   elif (specialty == Discipline.ELECTRONIC_ENGINEERING.value):
      #All Electronic Engineers are coloured magenta
      return Colour.MAGENTA.value
   elif (specialty == Discipline.SOCIAL_CARE.value):
      #All Electronic Engineers are coloured purple
      return Colour.PURPLE.value

def format_motivation_text(motivationText, charLimit):
   """
   formats the passed in 'motivationText' to abide by the line character limit
   charLimit.
   """
   splitText = wrap(motivationText, charLimit)
   #formats 'motivationText' in to charLimit character blocks
   #each of these blocks are stored in the list splitText
   formattedMessage=Misc.NEWLINE.value + Misc.NEWLINE.value
   #Creates a two-line gap between the title and the text
   for i in range(len(splitText)):
      #Iterates through the 'splitText' array and concatenates charLimit
      #characters before a newline
      formattedMessage += splitText[i] + Misc.NEWLINE.value
   #returns a formattedMessage once this is complete
   return formattedMessage  

def filterByTwoDifferentFactors(factor1, factor2, filterParameter1, filterParameter2, name):
     """
     Function that filters the graph by two different filters, i.e. Discipline 'Computer Science' Institution 'University of Nottingham'
     """
     if ((factor1 == filterParameter1) and (factor2 == filterParameter2)):
         filterGraph1.append(name)

def filterByTwoSameFactors(factor1, factor2, filterParameter1, filterParameter2, name):
    """
    Function that filters the graph by the same factor with different parameters, i.e. Discipline 'Computer Science' Discipline 'Robotics'
    """
    if ((factor1 == filterParameter1) or (factor2 == filterParameter2)):
         filterGraph1.append(name)

def filterBySingleFactor(factor1, filterParameter1, name):
    """
    Function that filters the graph by a single factor, i.e. Discipline 'Computer Science'
    """
    if ((factor1 == filterParameter1)):
        filterGraph1.append(name)

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
       case Institution.ANGLIA_RUSKIN.value:
          filterParameter1 = Institution.ANGLIA_RUSKIN_SHORTHAND.value
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

nodesFiltered = Misc.FALSE.value
loadAllDisciplines = Misc.FALSE.value
filterCategory1 = Misc.EMPTY_STRING.value
filterParameter1 = Misc.EMPTY_STRING.value
filterCategory2 = Misc.EMPTY_STRING.value
filterParameter2 =Misc.EMPTY_STRING.value
threeDimensional = Misc.FALSE.value
if (len(sys.argv) == Misc.THREE.value):
   nodesFiltered = Misc.TRUE.value
   filterCategory1 = sys.argv[Misc.ONE.value]
   filterParameter1 = sys.argv[Misc.TWO.value]
elif (len(sys.argv) > Misc.THREE.value):
   nodesFiltered = Misc.TRUE.value
   filterCategory1 = sys.argv[Misc.ONE.value]
   filterParameter1 = sys.argv[Misc.TWO.value]
   filterCategory2 = sys.argv[Misc.THREE.value]
   filterParameter2 = sys.argv[Misc.FOUR.value]

def setFilterByAll(value):
   """
   Function that filters by all disciplines/locations 
   """
   global loadAllDisciplines
   loadAllDisciplines = value

if ((filterParameter1 == Misc.ALL.value) or (filterParameter2 == Misc.ALL.value)):
  setFilterByAll(Misc.TRUE.value)
elif ((filterCategory1 != Misc.DISCIPLINE_WORD.value) and (filterCategory2 != Misc.DISCIPLINE_WORD.value)):
  setFilterByAll(Misc.TRUE.value)

def setNodesFiltered(value):
   """
   Function that sets the global nodesFiltered boolean to the value passed in
   """
   global nodesFiltered
   nodesFiltered = value
   

def filterNodesByCategories(filterCategory1, filterParameter1, filterCategory2, filterParameter2, member_name, member_institution, member_location, member_discipline): 
   """
   Function that applies the filtration to the graph based on the values passed in by the user.
   """
   match filterCategory1:
               case Misc.DISCIPLINE_WORD.value:
                  if (filterParameter1 == Misc.ALL.value):
                     match filterCategory2:
                        case Misc.LOCATION.value:
                           if (filterParameter2 == Misc.ALL.value):
                              setNodesFiltered(Misc.FALSE.value)
                           else:
                              filterBySingleFactor(member_location, filterParameter2, member_name)
                        case Misc.DISCIPLINE_WORD.value:
                           setNodesFiltered(Misc.FALSE.value)
                        case Misc.ALPHABETICAL.value:
                           filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter2, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterBySingleFactor(member_institution, filterParameter2, member_name)
                        case Misc.EMPTY_STRING.value:
                           setNodesFiltered(Misc.FALSE.value)
                  else:
                     match filterCategory2:
                        case Misc.LOCATION.value:
                           if (filterParameter2 == Misc.ALL.value):
                              filterBySingleFactor(member_discipline, filterParameter1, member_name)
                           else:
                              filterByTwoDifferentFactors(member_discipline, member_location, filterParameter1, filterParameter2, member_name)
                        case Misc.DISCIPLINE_WORD.value:
                           if (filterParameter2 == Misc.ALL.value):
                              setNodesFiltered(Misc.FALSE.value)
                           else:
                              filterByTwoSameFactors(member_discipline, member_discipline, filterParameter1, filterParameter2, member_name)
                        case Misc.ALPHABETICAL.value:
                           filterByTwoDifferentFactors(member_discipline, member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterByTwoDifferentFactors(member_discipline, member_institution, filterParameter1, filterParameter2, member_name)
                        case Misc.EMPTY_STRING.value:
                           filterBySingleFactor(member_discipline, filterParameter1, member_name)

               case Misc.LOCATION.value:
                  if (filterParameter1 == Misc.ALL.value):
                     match filterCategory2:
                        case Misc.DISCIPLINE_WORD.value:
                           if (filterParameter2 == Misc.ALL.value):
                              setNodesFiltered(Misc.FALSE.value)
                           else:
                              filterBySingleFactor(member_discipline, filterParameter2, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterBySingleFactor(member_institution, filterParameter2, member_name)
                        case Misc.LOCATION.value:
                           setNodesFiltered(Misc.FALSE.value)
                        case Misc.ALPHABETICAL.value: 
                           filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter2, member_name)
                        case Misc.EMPTY_STRING.value:
                           setNodesFiltered(Misc.FALSE.value)
                  else:
                     match filterCategory2:
                        case Misc.DISCIPLINE_WORD.value:
                           if (filterParameter2 == Misc.ALL.value):
                              filterBySingleFactor(member_location, filterParameter1, member_name)
                           else:
                              filterByTwoDifferentFactors(member_location, member_discipline, filterParameter1, filterParameter2, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterByTwoDifferentFactors(member_location, member_institution, filterParameter1, filterParameter2, member_name)
                        case Misc.LOCATION.value:
                           if (filterParameter2 == Misc.ALL.value):
                              setNodesFiltered(Misc.FALSE.value)
                           else:
                              filterByTwoSameFactors(member_location, member_location, filterParameter1, filterParameter2, member_name)
                        case Misc.ALPHABETICAL.value: 
                           filterByTwoDifferentFactors(member_location, member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                        case Misc.EMPTY_STRING.value:
                           filterBySingleFactor(member_location, filterParameter1, member_name)
               case Misc.INSTITUTION_WORD.value: 
                  match filterCategory2:
                     case Misc.DISCIPLINE_WORD.value: 
                        filterByTwoDifferentFactors(member_institution, member_discipline, filterParameter1, filterParameter2, member_name)
                     case Misc.LOCATION.value: 
                        filterByTwoDifferentFactors(member_institution, member_location, filterParameter1, filterParameter2, member_name)
                     case Misc.INSTITUTION_WORD.value: 
                        filterByTwoSameFactors(member_institution, member_institution, filterParameter1, filterParameter2, member_name)
                     case Misc.ALPHABETICAL.value: 
                        filterByTwoDifferentFactors(member_institution, member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                     case Misc.EMPTY_STRING.value:
                        filterBySingleFactor(member_institution, filterParameter1, member_name)
               case Misc.ALPHABETICAL.value: 
                  match filterCategory2:
                     case Misc.DISCIPLINE_WORD.value:
                        filterByTwoDifferentFactors(member_name[Misc.ZERO.value], member_discipline, filterParameter1, filterParameter2, member_name)
                     case Misc.LOCATION.value: 
                        filterByTwoDifferentFactors(member_name[Misc.ZERO.value], member_location, filterParameter1, filterParameter2, member_name)
                     case Misc.INSTITUTION_WORD.value:
                        filterByTwoDifferentFactors(member_name[Misc.ZERO.value], member_institution, filterParameter1, filterParameter2, member_name)
                     case Misc.ALPHABETICAL.value: 
                        filterByTwoSameFactors(member_name[Misc.ZERO.value], member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                     case Misc.EMPTY_STRING.value:
                        filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter1, member_name)
               case Misc.EMPTY_STRING.value:
                  match filterCategory2:
                     case Misc.DISCIPLINE_WORD.value:
                        filterBySingleFactor(member_discipline, filterParameter2, member_name)
                     case Misc.LOCATION.value: 
                        filterBySingleFactor(member_location, filterParameter2, member_name)
                     case Misc.INSTITUTION_WORD.value:
                        filterBySingleFactor(member_institution, filterParameter2, member_name)
                     case Misc.ALPHABETICAL.value: 
                        filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter2, member_name)
    
filterGraph1 = []
filterGraph2 = []
emptySearch = False
#List containing the names of all the members in the network 
emergenceMemberNames = []
#Initialises a networkX graph for the legend nodes
emergenceMemberMotivations = []

emergenceMemberLocations = set()
emergenceMemberInstitutions = set()

nx_graph = nx.Graph()
#Reference to the excel file containing the member details 
emergenceExcelWorkbook = openpyxl.load_workbook(Misc.EXCEL_FILE.value)
#Reference to the first sheet in the excel file
emergenceExcelWorkbookSheet = emergenceExcelWorkbook.worksheets[Misc.ZERO.value]

#Stores the number of actual nodes & the number of nodes in the legend
num_actual_nodes = emergenceExcelWorkbookSheet.max_row-Misc.ONE.value
num_legend_nodes = Misc.SEVEN.value

#The Step value represents the spacing between each of the legend nodes
step = Misc.ONE_HUNDRED.value
#The x value represents the x position of the legend 
x = Misc.LEGEND_X_VALUE.value
#The y value represents the y position of the legend
y = Misc.LEGEND_Y_VALUE.value
#A list of all of the labels for the legend nodes
legend_labels = [Discipline.ROBOTICS.value, Discipline.HEALTHCARE.value, Discipline.COMPUTER_SCIENCE.value, Discipline.DESIGN_ENGINEERING_INNOVATION.value,
                 Discipline.ELECTRONIC_ENGINEERING.value, Discipline.SOCIAL_CARE.value, Discipline.PHYSIOTHERAPY.value]

#A list of tuples containing all of the legend nodes
legend_nodes = [
    (
        num_actual_nodes + legend_node, #Node ID set to the sum of the current numbher of nodes  
                                                                # + the index of the legend node
        {
            Misc.GROUP.value: legend_node, #Adds the new legend node to the group
            Misc.LABEL.value: legend_labels[legend_node],#Indexes the legend_labels list to return the appropriate label for the node
            Misc.SIZE.value: Misc.LEGEND_NODE_SIZE.value,#Defines the size of the legend nodes
            Misc.FIXED.value: Misc.TRUE.value,#Sets the legend position to fixed
            Misc.PHYSICS.value: Misc.FALSE.value, #Sets the legend to have no physics mechanics
            Misc.X.value: x, #Sets the x-value of the legend
            Misc.Y.value: Misc.PX.value.format(fpixels=y+legend_node*step), #Sets the y-value of the legend
            Misc.SHAPE.value: Misc.LEGEND_SHAPE.value, #Sets the shape of the legend nodes
            Misc.WIDTH_CONSTRAINT.value: Misc.LEGEND_WIDTH_CONSTRAINT.value, #Sets the width contraints for the legend
            Misc.FONT.value: {Misc.SIZE.value: Misc.LEGEND_FONT_SIZE.value}, #Sets the font size for the legend
            Misc.DISCIPLINE_WORD.value: Discipline.INCLUDE_LEGEND_NODES.value, #Sets the speciality attribute for the legend 'include-legend-nodes'
            Misc.INSTITUTION_WORD.value: Discipline.INCLUDE_LEGEND_NODES.value,#Sets the institution attribute for the legend 'include-legend-nodes'
            Misc.ALPHABET.value: Discipline.INCLUDE_LEGEND_NODES.value, #Sets the alphabet attribute for the legend 'include-legend-nodes'
            Misc.TITLE.value: Misc.LEGEND_TITLE.value + legend_labels[legend_node], #Sets the title attribute for the legend 'include-legend-nodes'
            Misc.LOCATION.value: Discipline.INCLUDE_LEGEND_NODES.value#Sets the location attribute to the 'include_legend_nodes' value
        }
      
    )
    for legend_node in range(num_legend_nodes)#Creates 'num_legend_nodes' legend nodes and specifies an attribute for all of them
]

nx_graph.add_nodes_from(legend_nodes) #Adds all of the legend nodes to the graph

nx_graph.add_node(Misc.CENTRAL_NODE_ID.value, label=Misc.CENTRAL_NODE_LABEL.value, title=Misc.CENTRAL_NODE_ID.value, physics=Misc.TRUE.value, color=Misc.CENRAL_NODE_COLOUR.value, location= Discipline.INCLUDE_CENTRAL_NODE.value, institution=Discipline.INCLUDE_CENTRAL_NODE.value, Discipline=Discipline.INCLUDE_CENTRAL_NODE.value, alphabet=Discipline.INCLUDE_CENTRAL_NODE.value, x=1000, y=1000)    
#Adds in the central node of the network visualisation which is labeled "EMERGENCE_Network"

for row_index in range(Misc.TWO.value, emergenceExcelWorkbookSheet.max_row+Misc.ONE.value):
     #Iterates through all of the rows in the excel document
          #if the row is not the title row 
          member_name = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.SIX.value).value)
          #The member_name variable is extracted from the fifth column of the sheet
          member_institution = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.SEVEN.value).value)
          #The member_institution variable is extracted from the sixth column of the sheet
          member_location = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.EIGHT.value).value)
          emergenceMemberLocations.add(member_location)
          #The member_location variable is extracted from the seventh column of the sheet
          member_job_title = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.NINE.value).value)
          #The member_job_title variable is extracted from the eighth column of the sheet
          member_discipline = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.TEN.value).value)
          #The member_specialty variable is extracted from the ninth column of the sheet
          member_colour = setMemberColour(member_discipline)
          #The member_name variable is assigned the result of the setMemberColour function
          member_network_motivation = format_motivation_text(str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.THIRTEEN.value).value), Misc.ONE_HUNDRED.value)
          #The member_network_motivation variable is assigned the result of the format_motivation_text function
          member_alphabet = member_name[Misc.ZERO.value]
          #The member_specialty variable is extracted from the ninth column of the sheet
          member_title = Misc.NAME.value + member_name + Misc.INSTITUTION.value + member_institution + Misc.JOB_TITLE.value + member_job_title + Misc.DISCIPLINE.value + member_discipline + Misc.LOCATION_SECTION.value + member_location + Misc.RESEARCH_THEMES.value + member_network_motivation
          #The member_title variable displays all of the member attributes when the node is hovered over
          nx_graph.add_node(member_name, label=member_name, title=member_title, physics=Misc.TRUE.value,  institution=member_institution, Discipline=member_discipline, alphabet=member_alphabet, color=member_colour, location=member_location)
          #Creates a new node for each of the EMERGENCE members with all of the relevant attributes
          emergenceMemberNames.append(member_name)
          #Appends each member to the member_names array
          if (member_network_motivation != format_motivation_text(Misc.NONE.value, Misc.ONE_HUNDRED.value)):
            emergenceMemberMotivations.append(member_network_motivation)
          if (nodesFiltered):
            filterNodesByCategories(filterCategory1,filterParameter1, filterCategory2, filterParameter2, 
                                    member_name, member_institution, member_location, member_discipline)

# Calculate layout
pos = nx.drawing.layout.spring_layout(nx_graph, scale=Misc.SCALE.value)

legend_node_names = [Legend.ONETHREESIX.value, Legend.ONETHREESEVEN.value, Legend.ONETHREEEIGHT.value, 
                     Legend.ONETHREENINE.value, Legend.ONEFOURTY.value,Legend.ONEFOURONE.value, Legend.ONEFOURTWO.value]

legend_node_dict_mapping = [{Legend.ONETHREESIX.value:Discipline.ROBOTICS.value}, {Legend.ONETHREESEVEN.value : Discipline.HEALTHCARE.value}, 
                             {Legend.ONETHREEEIGHT.value:Discipline.COMPUTER_SCIENCE.value}, {Legend.ONETHREENINE.value: Discipline.DESIGN_ENGINEERING_INNOVATION.value},
                             {Legend.ONEFOURTY.value:Discipline.ELECTRONIC_ENGINEERING.value}, {Legend.ONEFOURONE.value:Discipline.SOCIAL_CARE.value}, {Legend.ONEFOURTWO.value:Discipline.PHYSIOTHERAPY.value } ]

legend_node_colour_mapping = {Discipline.ROBOTICS.value : setMemberColour(Discipline.ROBOTICS.value), 
                             Discipline.HEALTHCARE.value : setMemberColour(Discipline.HEALTHCARE.value),
                             Discipline.COMPUTER_SCIENCE.value : setMemberColour(Discipline.COMPUTER_SCIENCE.value),
                             Discipline.DESIGN_ENGINEERING_INNOVATION.value : setMemberColour(Discipline.DESIGN_ENGINEERING_INNOVATION.value),
                             Discipline.ELECTRONIC_ENGINEERING.value : setMemberColour(Discipline.ELECTRONIC_ENGINEERING.value),
                             Discipline.SOCIAL_CARE.value : setMemberColour(Discipline.SOCIAL_CARE.value),
                             Discipline.PHYSIOTHERAPY.value : setMemberColour(Discipline.PHYSIOTHERAPY.value)}

legend_node_count = Misc.ZERO.value
# Add coordinates as node annotations that are recognized by gravis
general_node_count = Misc.ZERO.value

legend_node_coordinates = [LegendCoordinates.POINT_ONE.value, LegendCoordinates.POINT_TWO.value, LegendCoordinates.POINT_THREE.value, 
                           LegendCoordinates.POINT_FOUR.value, LegendCoordinates.POINT_FIVE.value, LegendCoordinates.POINT_SIX.value, 
                           LegendCoordinates.POINT_SEVEN.value]

for name, (x, y) in pos.items():
    node = nx_graph.nodes[name]
    if name == Misc.CENTRAL_NODE_ID.value:
        node[Misc.X.value] = Misc.ZERO.value
        node[Misc.Y.value] = Misc.ZERO.value
        nx.set_node_attributes(nx_graph, {name : Misc.SEVENTYFIVE.value}, name=Misc.SIZE.value)
        node[Misc.HOVER.value] = name
    elif name in legend_node_names:
        legendDict = legend_node_dict_mapping[legend_node_count]
        nx_graph = nx.relabel_nodes(nx_graph, legendDict)
        print(name)
        name = legendDict[name]
        node = nx_graph.nodes[name]
        legend_node_coordinate = legend_node_coordinates[legend_node_count]
        node[Misc.X.value] = legend_node_coordinate[Misc.ZERO.value]
        node[Misc.Y.value] = legend_node_coordinate[Misc.ONE.value]
        nx.set_node_attributes(nx_graph, {name : Misc.FIFTY.value}, name=Misc.SIZE.value)
        hoverText = nx.get_node_attributes(nx_graph, Misc.TITLE.value)
        node[Misc.HOVER.value] = name
        legend_node_count += Misc.ONE.value
    else:
        node[Misc.X.value] = random.randint(LegendCoordinates.MIN_RANGE.value, LegendCoordinates.MAX_RANGE.value)
        node[Misc.Y.value] = random.randint(LegendCoordinates.MIN_RANGE.value, LegendCoordinates.MAX_RANGE.value)
        nx.set_node_attributes(nx_graph, {name : Misc.FIFTY.value}, name=Misc.SIZE.value)
        hoverText = nx.get_node_attributes(nx_graph, Misc.TITLE.value)
        node[Misc.HOVER.value] =  hoverText[name]
        general_node_count += Misc.ONE.value

nx.set_node_attributes(nx_graph, legend_node_colour_mapping, name=Misc.COLOR.value)

for i in range(Misc.ZERO.value, len(legend_labels)):
   #Iterates through the member_names array
   nx_graph.add_edge(Misc.CENTRAL_NODE_ID.value, legend_labels[i]) #Creates an edge between the central node and the legend nodes

for i in range(Misc.ZERO.value, len(legend_labels)):
   for node in nx_graph.nodes():
       selectedNode = nx_graph.nodes[node]
       if ((selectedNode not in legend_labels) and len(selectedNode) != 0):
         if (legend_labels[i] == selectedNode[Misc.DISCIPLINE_WORD.value]):
            legendPoint = legend_node_coordinates[i]
            selectedNode[Misc.X.value] = random.randint(legendPoint[Misc.ZERO.value] - Misc.SEVENFIFTY.value,legendPoint[Misc.ZERO.value] + Misc.SEVENFIFTY.value)
            selectedNode[Misc.Y.value] = legendPoint[Misc.ONE.value] + random.randint(Misc.FIFTY.value, Misc.FOUR_HUNDRED.value)
            nx_graph.add_edge(legend_labels[i], selectedNode[Misc.LABEL.value])

if (nodesFiltered):
   if (len(filterGraph1) == Misc.ZERO.value):
      emptySearch = Misc.TRUE.value
   filterGraph1.append(Misc.CENTRAL_NODE_ID.value)
   if (not loadAllDisciplines):
      filterGraph1.append(filterParameter1)
      filterGraph1.append(filterParameter2)
   elif (loadAllDisciplines):
      for i in range(len(legend_labels)):
         filterGraph1.append(legend_labels[i])
   filteredView = nx_graph.subgraph(filterGraph1)
   figGravis = gv.vis(filteredView, zoom_factor=VisualisationSettings.ZOOM_FACTOR.value, layout_algorithm_active=Misc.TRUE.value, graph_height=VisualisationSettings.GRAPH_HEIGHT.value,layout_algorithm=VisualisationSettings.LAYOUT_ALGORITHM.value, node_label_font=VisualisationSettings.NODE_LABEL_FONT.value)
else:
   figGravis = gv.vis(nx_graph, zoom_factor=VisualisationSettings.ZOOM_FACTOR.value, graph_height=VisualisationSettings.GRAPH_HEIGHT.value, node_drag_fix=Misc.TRUE.value, node_hover_tooltip=Misc.TRUE.value, layout_algorithm=VisualisationSettings.LAYOUT_ALGORITHM.value, node_label_font= VisualisationSettings.NODE_LABEL_FONT.value)

filterParameter1, filterParameter2 = shorthandParameters(filterParameter1, filterParameter2)

fname = (Misc.FNAME.value).format(filterCategory1, filterParameter1,
                                 filterCategory2, filterParameter2)

figGravis.export_html(fname, Misc.TRUE.value)
figGravis.display()
if (emptySearch):
   sys.exit(Misc.ONE.value)
sys.exit(Misc.ZERO.value)





