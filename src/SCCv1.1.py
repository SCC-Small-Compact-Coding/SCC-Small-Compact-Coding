import sys
import gc

gc.enable()

class SCC():
    def __init__(self):
        self.GVars = {
            "TRUE": True,
            "FALSE": False
        }

    def _get_val(self, token):
        cleaned = str(token).strip()
        if cleaned in self.GVars:
            return str(self.GVars[cleaned])
        return token

    def runline(self, txt):
        if str(txt).strip() == "": 
            return
        cmd_parts = str(txt).strip().split(maxsplit=1)
        sub_parts = []
        try:
            sub_parts = cmd_parts[1].split(",")
        except:
            pass
        cmd_type = cmd_parts[0].lower().strip()

        if cmd_type == "speak":
            txt_arg = sub_parts[0].strip() if len(sub_parts) > 0 else ""
            txt_arg = self._get_val(txt_arg)
            end_arg = sub_parts[1].strip().upper() if len(sub_parts) > 1 else "FALSE"
            end_bool = self.GVars.get(end_arg, False)
            self.Speak(txt_arg, end_bool)
            
        elif cmd_type == "exit":
            self.exit()
            
        elif cmd_type == "$":
            if len(sub_parts) >= 2:
                val_arg = self._get_val(sub_parts[1].strip())
                self.MakeVar(sub_parts[0].strip(), val_arg)
                
        elif cmd_type == "ask":
            txt_arg = sub_parts[0].strip() if len(sub_parts) > 0 else ""
            txt_arg = self._get_val(txt_arg)
            self.Ask(txt_arg)
            
        elif cmd_type == "ask$":
            if len(sub_parts) >= 2:
                txt_arg = self._get_val(sub_parts[0].strip())
                self.AskAndSetVar(txt_arg, sub_parts[1].strip())
                
        elif cmd_type == "memcolect":
            self.MemColect()
            
        elif cmd_type == "memautocolect":
            state_arg = sub_parts[0].strip().upper() if len(sub_parts) > 0 else ""
            self.MemAutoColect(state_arg)
        
    def Speak(self, txt, end):
        if end == self.GVars["TRUE"]:
            print(txt, flush=True, end="")
        else:
            print(txt, flush=True)
    
    def exit(self):
        sys.exit()

    def MakeVar(self, name, Val):
        self.GVars[name] = Val

    def Ask(self, txt):
        input(txt)

    def AskAndSetVar(self, txt, name):
        self.GVars[name] = input(txt)

    def MemColect(self):
        gc.collect()

    def MemAutoColect(self, state):
        if str(state).strip() == "ON":
            gc.enable()
        elif str(state).strip() == "OFF":
            gc.disable()
        else:
            print("Value Error: State must be on or off.")

    def runfile(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    self.runline(line)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            sys.exit()

if __name__ == "__main__":
    comp = SCC()
    if len(sys.argv) > 1:
        comp.runfile(sys.argv[1])
    else:
        print("Error: Use it like this: SCC <filename>")
