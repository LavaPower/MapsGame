from tkinter import Tk, Label, Button

from MapEditor.BlockTypesEditor import BlockTypesEditor
from MapEditor.MapInfosEditor import MapInfosEditor
from MapEditor.BlocksEditor.BlocksEditor import BlocksEditor


class Editor:
    def __init__(self, mapdir):
        self.mapdir = mapdir
        self.fenetre = Tk()
        self.fenetre.title("MapEditor : "+mapdir)
        self.fenetre.resizable(False, False)
        self.fenetre.geometry("300x375")

        fonts = {
            "title": ("Arial", 20, 'bold'),
            "other": ("Arial", 14)
        }

        titre = Label(self.fenetre, text="Map : "+mapdir, font=fonts["title"])
        blockstypesbutton = Button(self.fenetre, text="Editer les BlockTypes", font=fonts["other"],
                                   command=self.editblocktypes)
        mapinfosbutton = Button(self.fenetre, text="Editer les MapInfos", font=fonts["other"],
                                command=self.editmapinfos)
        blocksbutton = Button(self.fenetre, text="Editer les Blocks", font=fonts["other"], command=self.editblocks)
        retourbutton = Button(self.fenetre, text="Retour Menu Principal", font=fonts["other"], command=self.mainmenu)
        quitterbutton = Button(self.fenetre, text="Quitter", font=fonts["other"], command=self.fenetre.destroy)

        titre.pack(padx=10, pady=20)
        blockstypesbutton.pack(padx=10, pady=10)
        mapinfosbutton.pack(padx=10, pady=5)
        blocksbutton.pack(padx=10, pady=10)
        retourbutton.pack(padx=10, pady=5)
        quitterbutton.pack(padx=10, pady=10)

        self.fenetre.mainloop()

    def editblocks(self):
        self.fenetre.destroy()
        BlocksEditor(self.mapdir)

    def editblocktypes(self):
        self.fenetre.destroy()
        BlockTypesEditor(self.mapdir)

    def editmapinfos(self):
        self.fenetre.destroy()
        MapInfosEditor(self.mapdir)

    def mainmenu(self):
        from Core.Game import MainMenu

        self.fenetre.destroy()
        MainMenu()
