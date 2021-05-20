import seaborn as sn
from matplotlib.colors import ListedColormap
import csv
import os

class _cm:
    """Parent colormap class. Default is new Tableau 10 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/Tab10') ):
        with open(path,newline='') as f:
            reader = csv.reader(f)
            self.colors=next(reader)

    def to_mpl_cmap(self):
        """Returns matplotlib ListedColormap of the selected palette."""
        return ListedColormap(sn.color_palette(self.colors))

    def to_sn_palette(self):
        """Returns seaborn palette of the selected palette."""
        return sn.color_palette(self.colors)

class tab10(_cm):
    """New tableau 10 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/Tab10') ):
        super().__init__(path)

class tab20(_cm):
    """New tableau 20 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/Tab20') ):
        super().__init__(path)

class color_blind(_cm):
    """New tableau color blind palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/CB') ):
        super().__init__(path)

class seattle_grays(_cm):
    """New tableau grays palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/seattle_grays') ):
        super().__init__(path)

class traffic(_cm):
    """New tableau traffic palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/traffic') ):
        super().__init__(path)

class miller_stone(_cm):
    """New tableau miller stone palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/miller_stone') ):
        super().__init__(path)

class superfishel_stone(_cm):
    """New tableau superfishel stone palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/superfishel_stone') ):
        super().__init__(path)

class nuriel_stone(_cm):
    """New tableau nuriel palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/nuriel_stone') ):
        super().__init__(path)

class jewel_bright(_cm):
    """New jewel bright palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/jewel_bright') ):
        super().__init__(path)

class summer(_cm):
    """New tableau summer palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/summer') ):
        super().__init__(path)

class gn_or_tl(_cm):
    """New tableau green-orange-teal palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/green_orange_teal') ):
        super().__init__(path)

class rd_bl_br(_cm):
    """New tableau red-blue-brown palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/red_blue_brown') ):
        super().__init__(path)

class pu_pi_gr(_cm):
    """New tableau purple-pink-gray palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/purple_pink_gray') ):
        super().__init__(path)

class hue_circle(_cm):
    """New tableau hue circle palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/hue_circle') ):
        super().__init__(path)

class classic_tab10(_cm):
    """Classic tableau 10 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/Tab10_classic') ):
        super().__init__(path)

class classic_tab10_medium(_cm):
    """Classic tableau 10 medium palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/Tab10_classic_medium') ):
        super().__init__(path)

class classic_tab10_light(_cm):
    """Classic tableau 10 light palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/Tab10_classic_light') ):
        super().__init__(path)

class classic_tab20(_cm):
    """Classic tableau 20 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/Tab20_classic') ):
        super().__init__(path)

class classic_gray5(_cm):
    """Classic tableau gray 5 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_gray5') ):
        super().__init__(path)

class classic_color_blind(_cm):
    """Classic tableau color blind palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_CB') ):
        super().__init__(path)

class classic_traffic(_cm):
    """Classic tableau traffic light palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_traffic') ):
        super().__init__(path)

class classic_pu_gr6(_cm):
    """Classic tableau purple-gray 6 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_purple_gray6') ):
        super().__init__(path)

class classic_pu_gr12(_cm):
    """Classic tableau purple-gray 12 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_purple_gray12') ):
        super().__init__(path)

class classic_gn_or6(_cm):
    """Classic tableau green-orange 6 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_green_orange6') ):
        super().__init__(path)

class classic_gn_or12(_cm):
    """Classic tableau green-orange 12 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_green_orange12') ):
        super().__init__(path)

class classic_bu_rd6(_cm):
    """Classic tableau blue-red 6 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_blue_red6') ):
        super().__init__(path)

class classic_bu_rd12(_cm):
    """Classic tableau blue-red 12 palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_blue_red12') ):
        super().__init__(path)

class classic_cyclic(_cm):
    """Classic tableau cyclic palette."""
    def __init__( self, path=os.path.join(os.path.dirname(__file__),'color_data/classic_cyclic') ):
        super().__init__(path)