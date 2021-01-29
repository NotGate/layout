#MaxHotkeysPerInterval 1000
#InstallKeybdHook
RAlt::send % A_priorkey

$Shift::
Input, vText, L1 T1 I
if (ErrorLevel = "Timeout")
	Return
SendInput +{%vText%}
Return