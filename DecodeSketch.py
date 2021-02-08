
import adsk.core, adsk.fusion, adsk.cam, traceback, math
from .lib.TurtleUtils import TurtleUtils
from .lib.TurtleCommand import TurtleCommand
from .lib.SketchEncoder import SketchEncoder
from .lib.SketchDecoder import SketchDecoder
from .lib.data.SketchData import SketchData


# lib link:
# mklink /J "C:\Users\Robin\AppData\Roaming\Autodesk\Autodesk Fusion 360\API\Scripts\DecodeSketch\lib" "C:\Users\Robin\source\repos\FusionLib"
# command
f,core,app,ui,design,root = TurtleUtils.initGlobals()

class DecodeSketch(TurtleCommand):
    def __init__(self):
        cmdId = 'DecodeSketchId'
        cmdName = 'Dencode Sketch Command'
        cmdDescription = 'Decodes and creates a sketch based on the previously encoded data.'
        super().__init__(cmdId, cmdName, cmdDescription)

    def runCommand(self):
        #JointMaker()
        #SketchEncoder()
        
        #data = self.getSketchData()
        #transform = core.Matrix3D.create()
        #transform.setToRotation(math.pi/3.0, adsk.core.Vector3D.create(0, 0, 1), adsk.core.Point3D.create(0, 0, 0))
        #transform.setCell(0,0, 2.0)
        #transform.setCell(1,1, 0.5)
        #SketchDecoder(data, transform)

        data = self.getSketchData()
        SketchDecoder(data)

    def getSketchData(self):
        result = TurtleUtils.getClipboardText()
        if result == None or not (result.startswith("#Turtle Generated Data")):
            result = SketchData.getTestData()
        else:
            result = eval(result)# json.loads(result[23:])
        #TurtleUtils.clearClipboardText()
        return result

def run(context):
    cmd = DecodeSketch()
