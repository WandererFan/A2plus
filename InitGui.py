#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2018 kbwbe                                              *
#*                                                                         *
#*   Portions of code based on hamish's assembly 2                         *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

__title__ = 'A2plus assembly Workbench - InitGui file'
__author__ = 'kbwbe'



class a2pWorkbench (Workbench):

    def __init__(self):
        import a2plib
        self.__class__.Icon = a2plib.pathOfModule() + "/icons/a2p_workbench.svg"
        self.__class__.MenuText = 'A2plus'
        self.__class__.ToolTip  = 'An other assembly workbench for FreeCAD'

    def Initialize(self):

        import a2plib #QtCore.QResource.registerResource happens in assembly2lib
        import a2p_importpart
        import a2p_CircularEdgeConnection
        import a2p_planesParallelConstraint
        import a2p_planeConstraint
        import a2p_AxialConnection
        import a2p_angleConnection
        import a2p_pointIdentityConnection
        import a2p_pointOnLineConstraint
        import a2p_pointOnPlaneConstraint
        import a2p_sphericalConnection
        import a2p_solversystem
        import a2p_MuxAssembly

        commandslist = [
            'a2p_ImportPart',
            'a2p_updateImportedParts',
            'a2p_movePart',
            'a2p_duplicatePart',
            'a2p_editImportedPart',
            'a2p_PointIdentityConnectionCommand',
            'a2p_PointOnLineConstraintCommand',
            'a2p_PointOnPlaneConstraintCommand',
            'a2p_CircularEdgeConnection',
            'a2p_PlanesParallelConnectionCommand',
            'a2p_PlaneConnection',
            'a2p_AxialConnection',
            'a2p_AngledPlanesCommand',
            'a2p_SphericalConnection',
            'a2p_SolverCommand',
            'a2p_DeleteConnectionsCommand',
            'a2p_ViewConnectionsCommand',
            'a2p_SimpleAssemblyShapeCommand',
            'a2p_ToggleTransparencyCommand',
            'a2p_isolateCommand',
            'a2p_ToggleAutoSolveCommand',
            'a2p_TogglePartialProcessingCommand',
            'a2p_repairTreeViewCommand'
            ]
        menuEntries = [
            'a2p_repairTreeViewCommand'
            ]
        self.appendToolbar(
               'A2p',
               commandslist
               )
        self.appendMenu(
            'A2p',
            menuEntries
            )
        #FreeCADGui.addPreferencePage( a2plib.pathOfModule() + '/GuiA2p/ui/a2p_prefs.ui','A2plus' )
        FreeCADGui.addPreferencePage(
            a2plib.pathOfModule() +
            '/GuiA2p/Resources/ui/a2p_prefs.ui','A2plus'
            )


    def Activated(self):
        import a2p_observers
        FreeCAD.addDocumentObserver(a2p_observers.redoUndoObserver)

    def Deactivated(self):
        import a2p_observers
        FreeCAD.removeDocumentObserver(a2p_observers.redoUndoObserver)

    def ContextMenu(self, recipient):
        import FreeCAD, FreeCADGui
        selection = [s  for s in FreeCADGui.Selection.getSelection() if s.Document == FreeCAD.ActiveDocument ]
        if len(selection) == 1:
            obj = selection[0]
            if 'sourceFile' in  obj.Content:
                self.appendContextMenu(
                    "A2p",
                    [
                      'a2p_movePart',
                      'a2p_duplicatePart',
                      'a2p_editImportedPart',
                      'a2p_DeleteConnectionsCommand',
                      'a2p_ToggleTransparencyCommand'
                      ]
                    )

Gui.addWorkbench(a2pWorkbench())
