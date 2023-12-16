macroPhotosByMacroType = """SELECT * FROM Macrostructure_Data INNER JOIN
                            Macrostructure_Photo ON 
                            Macrostructure_Data.macrostructureID = Macrostructure_Photo.macrostructureID
                            WHERE Macrostructure_Data.macrostructureType = {macroType};"""

mesoPhotosByMesoType = """SELECT * FROM Mesostructure_Data INNER JOIN
                            Mesostructure_Photo ON 
                            Mesostructure_Data.mesostructureID = Mesostructure_Photo.mesostructureID
                            WHERE Mesostructure_Data.mesostructureType = {mesoType};"""

findPhotosByWaypoint = """SELECT * FROM Waypoint_Data 
                        INNER JOIN Macrostructure_Data ON Waypoint_Data.waypointID = Macrostructure_Data.waypointID
                        INNER JOIN Macrostructure_Photo ON Macrostructure_Photo.macrostructureID = Macrostructure_Photo.macrostructureID
                        LEFT JOIN Mesostructure_Data ON Mesostructure_Data.macrostructureID = Macrostructure_Photo.macrostructureID
                        INNER JOIN Mesostructure_Photo.mesostructureID = Mesostructure_Data.mesostructureID
                        LEFT JOIN Thin_Section_Data ON Thin_Section_Data.mesostructureID = Mesostructure_Data.mesostructureID
                        INNER JOIN Thin_Section_Photo ON Thin_Section_Data.thinSectionID = Thin_Section_Photo.thinSectionID
                        WHERE Waypoint_Data.waypointID = {waypointID};"""