# Copyright 2000 Harmonix Music Systems.  All rights reserved.
#
# $Header: j:\\cvs/Freq/run/Levels/curve/curve.py,v 1.33 2001/10/10 02:06:21 anon Exp $
#

# sections:
#
# 0 8 bar intro
# 1 8 bar verse 1 
# 2 8 bar verse 1
# 3 8 bar bridge
# 4 8 bar chorus
# 5 8 bar chorus tag
# 6 12 bar verse 2 
# 7 8 bar bridge
# 8 8 bar chorus
# 9 8 bar chorus tag 
# 10 8 bar inst verse 3
# 11 8 bar bridge
# 12 8 bar chorus
# 13 8 bar chorus tag 

class curveLevel (Level):
    def __init__ (self):
        Level.__init__(self)

        self.directory_name = 'curve'
        self.short_name = 'curve'
        self.track_enable_criteria = ('yes', 1, 1, 1, 2, 2, 1, 1)
        self.game_bg_criteria = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.jam_bg_criteria  = ('yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes')
        self.fx_filt_period = (1920, 960, 1920, 480, 1920, 960, 1920, 960)
        self.fx_stt         = (120, 0)
        self.fx_volume      = 50
        self.stage_num      = 3
        self.freestyle_points = [3, 5, 6]
        self.num_laps       = [2, 4, 3, 3]
        self.section_boundaries = [8, 16, 24, 32, 40, 48, 60, 68, 76, 84, 92, 100, 108, 116]
        self.section_instances =  [0, 1, 2, 3, 4, 5, 6, 7, 4, 5, 10, 11, 12, 13, 13]
        self.linked_sections = [[ [0,2], [1,10], [3,7,11], [4,12] ],	  #T1 drums1
                                [ [1,10], [3,7,11] ],               #T2 guitar
                                [ [0,2], [4,12] ],                  #T3 synth
                                [],	                                #T4 vocal
                                [ [1,3], [4,12] ],		        #T5 bass
                                [ [3,7,11], [4,12] ],		        #T6 drums2
                                [],
                                []]
        self.materials = ("drum",
                          "guitar",
                          "synth",
                          "vocal",
                          "bass",
                          "drum",
                          "lead",
                          "lead")

    def get_name (self):        return "Worst Mistake"
    def get_abbrev_name (self): return "Worst Mistake"
    def get_artist (self):      return "Curve"
    def get_genre (self):       return "electronic rock"
    def get_tempo (self):       return "150"
    def get_description (self): return "Curve set the stage in the 90's for female fronted electronic rock and continue to rock hard to this day mixing heavy beats and screaming guitars with sultry vocals.  www.curve.co.uk"
    def get_song_id (self):     return 26   # Return unique id for this song...
    def wacko_panning (self):   return 0
    def use_linear_song_form (self): return 1
    def use_bank_swapping (self): return 1

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
            return 'delay'               # Core 0 uses room
        else:
            return 'room'              # Core 1 uses delay

    # What volumes (left and right) should the effect be at for the given core?
    # Scale is 0-127
    def ps2_hard_effect_volumes (self, core):
        if core == 0:
            return [75, 75]               # Core 0 has delay time of 30
        else:
            return [60, 60]              # Core 1 has delay time of 60

    # What is the delay time for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_delay_time (self, core):
        if core == 0:
            return 76                     # Core 0 has delay time of 60
        else:
            return 20                   # Core 1 has delay time of 70

    # What is the feedback value for the given core?  Only valid for echo and delay.
    # Scale is 0-127
    def ps2_hard_feedback (self, core):
        if core == 0:
            return 40                   # core 0: 40
        else:
            return 7                # core 1: 45

def get_class_name ():
    return curveLevel
