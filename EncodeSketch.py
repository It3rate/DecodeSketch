
import adsk.core, adsk.fusion, adsk.cam, traceback
from .lib.TurtleUtils import TurtleUtils
from .lib.TurtleCommand import TurtleCommand
from .lib.SketchEncoder import SketchEncoder
from .lib.SketchDecoder import SketchDecoder
from .lib.data.SketchData import SketchData


# link lib
# mklink /J "C:\Users\Robin\AppData\Roaming\Autodesk\Autodesk Fusion 360\API\Scripts\EncodeSketch\lib" "C:\Users\Robin\source\repos\FusionLib"
# command
f,core,app,ui,design,root = TurtleUtils.initGlobals()

class EncodeSketch(TurtleCommand):
    def __init__(self):
        cmdId = 'EncodeSketchId'
        cmdName = 'Encode Sketch Command'
        cmdDescription = 'Encodes a sketch for reuse in script.'
        super().__init__(cmdId, cmdName, cmdDescription)

    def runCommand(self):
        SketchEncoder()

def run(context):
    cmd = EncodeSketch()
