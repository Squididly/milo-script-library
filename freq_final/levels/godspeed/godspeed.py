# Copyright 2000 Harmonix Music Systems.  All rights reserved.

class godspeedLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'godspeed'
        self.track_enable_criteria = ('yes', 'yes', 'yes', 3, 3, 'yes', 3, 4)
        self.game_bg_criteria = ('yes','yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes',(1,2,3,4,5,6), (1,2,3,4,5,6), (1), 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960,  1920, 480,  1920, 960,  1920, 960)
        self.fx_stt         = (120, 0)
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 56, 64]
        self.section_instances = [0, 1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]
        self.fx_volume      = 50
        self.materials = ("drum",
                          "vocals",
                          "synth",
                          "bass",
                          "synth",
                          "synth",
                          "synth",
                          "lead")

    def get_name (self):        return "Godspeed"
    def get_abbrev_name (self): return "Godspeed"
    def get_artist (self):      return "BT"
    def get_genre (self):       return "Trance"
    def get_tempo (self):       return "139"
    def get_description (self): return "BT's Movement In Still Life is a perfect hybrid of musical genres, providing the first truly eclectic sound of the new millennium."
    def get_song_id (self):     return 11   # Return unique id for this song...
    def wacko_panning (self):   return 0
    def use_linear_song_form (self):
        return 1

    # for metagame: 1 means yes, 0 means no
    def is_avail_game(self):    return 1
    def is_avail_jam(self):   return 1

    def get_seermusic_bank (self):
        return self.get_seermusic_bank_by_ruleset ()

    # Turn on a hardware effect for the given core?  1 for yes, 0 for no
    def ps2_use_hard_effect (self, core):
        return 1

    # What hardware effect to use on the given core?  Valid values are
    # 'room', 'studio a', 'studio b', 'studio c', 'hall', 'space',
    # 'echo', 'delay', 'pipe'
    def ps2_hard_effect_name (self, core):
        if core == 0:
            return 'delay'               # Core 0 uses delay
        else:
            return 'hall'                # Core 1 uses hall

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [50, 50]               # Core 0 has delay time of 50
        else:
            return [55, 50]               # Core 1 has delay time of 55
        
    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 80                     # Core 0 has delay time of 80
        else:
            return 90                     # Core 1 has delay time of 90

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 40                   # core 0: 40
        else:
            return 15                   # core 1: 15

def get_class_name ():
    return godspeedLevel
