#button flags
IE_GUI_BUTTON_NORMAL     = 0x00000004   #default button, doesn't stick
IE_GUI_BUTTON_NO_IMAGE   = 0x00000001
IE_GUI_BUTTON_PICTURE    = 0x00000002
IE_GUI_BUTTON_SOUND      = 0x00000004
IE_GUI_BUTTON_ALT_SOUND  = 0x00000008
IE_GUI_BUTTON_CHECKBOX   = 0x00000010   #or radio button
IE_GUI_BUTTON_RADIOBUTTON= 0x00000020   #sticks in a state

#events
IE_GUI_BUTTON_ON_PRESS   = 0x00000000
IE_GUI_SLIDER_ON_CHANGE  = 0x02000000

#button states
IE_GUI_BUTTON_ENABLED    = 0x00000000
IE_GUI_BUTTON_UNPRESSED  = 0x00000000
IE_GUI_BUTTON_PRESSED    = 0x00000001
IE_GUI_BUTTON_SELECTED   = 0x00000002
IE_GUI_BUTTON_DISABLED   = 0x00000003
global IE_GUI_BUTTON_ON_PRESS
global IE_GUI_BUTTON_NO_IMAGE
global IE_GUI_BUTTON_IMAGE
global IE_GUI_BUTTON_PICTURE
global IE_GUI_BUTTON_NO_PICTURE
global IE_GUI_BUTTON_NO_SOUND
global IE_GUI_BUTTON_SOUND
global IE_GUI_BUTTON_CHECKBOX
global IE_GUI_BUTTON_PUSHBUTTON
global IE_GUI_BUTTON_ENABLED
global IE_GUI_BUTTON_UNPRESSED
global IE_GUI_BUTTON_PRESSED
global IE_GUI_BUTTON_SELECTED
global IE_GUI_BUTTON_DISABLED
global IE_GUI_SLIDER_ON_CHANGE

OP_SET = 0
OP_OR = 1
OP_NAND = 2
global OP_SET, OP_OR, OP_NAND

GEMRB_VERSION = -1
global GEMRB_VERSION