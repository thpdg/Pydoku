class LEDColorTable:
    LEDColorTable = {}

    @staticmethod
    def CreateColorTable(graphics_handle = None) -> dict | None:
        if graphics_handle is None:
            print("Error Creating LED Color Table without Graphics Handle")
            return None
        

        LEDColorTable = {
            0: graphics_handle.create_pen(0,0,0),
            "R": graphics_handle.create_pen(255, 0, 0), 
            "Y": graphics_handle.create_pen(255,255,0),
            "V": graphics_handle.create_pen(255,0,255),
            "G": graphics_handle.create_pen(0,255,0),
            "B": graphics_handle.create_pen(0, 0, 255), 
            "Black": graphics_handle.create_pen(0,0,0),
            "White": graphics_handle.create_pen(64, 64, 64),
        }

        return LEDColorTable
    