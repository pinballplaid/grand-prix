testVers = '00.00.01'

"""SOUTH-LEFT: [0] Solenoid, [1] Incandescent, [2, 3] Switch"""

import rs232Intf

# Config inputs as all state inputs
wingCfg = [ [ rs232Intf.WING_SOL, rs232Intf.WING_INCAND, rs232Intf.WING_INP, rs232Intf.WING_INP ] ]

# Config inputs as all state inputs
inpCfg = [ [ rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, \
             rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE, rs232Intf.CFG_INP_STATE ] ]

# solenoid config (or lack thereof)
solCfg  = [ [   rs232Intf.CFG_SOL_USE_SWITCH, '\x20', '\x00', rs232Intf.CFG_SOL_USE_SWITCH, '\x20', '\x00', \
                rs232Intf.CFG_SOL_USE_SWITCH, '\x20', '\x00', rs232Intf.CFG_SOL_USE_SWITCH, '\x20', '\x00', \
                '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
                '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
                '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
                '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
                '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', \
                '\x00', '\x00', '\x00', '\x00', '\x00', '\x00' ] ]