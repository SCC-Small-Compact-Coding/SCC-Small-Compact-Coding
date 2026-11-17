# SCC-Small-Compact-Coding
This is a new coding language that is easier that the others.

# Syntax
``` SCC
$ GREETING, "Hello! Welcome to the system."
$ PROMPT, "Please enter your secret code: "

speak GREETING, FALSE

ask$ PROMPT, USER_CODE

speak "Your code was: ", TRUE
speak USER_CODE, FALSE

memcolect
memautocolect "OFF"

$ SCC, "Well this will work!!!"
speak SCC

memcolect

ask "exit"

ServerP 8000
ServerD 8888

```
       
       
       Copyright 2026 wawa2016-here
