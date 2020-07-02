import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import patsy
import re
from bs4 import BeautifulSoup
import requests

shows = ('1-Extreme_Prejudice', '2-Recovery', '3-Phoenix', '4-Lost_at_Sea', '5-The_Namesake',
         '6-Shell_Shock:_Part_I', '7-Shell_Shock:_Part_II', '8-Gone', '9-Devils_Trifecta', '11-Shabbat_Shalom',
         '12-Shiva', '13-Hit_and_Run', '14-Canary', '15-Hereafter', '16-Detour', '17-Prime_Suspect', '18-Seek',
         '19-Squall', '20-Chasing_Ghosts', '21-Berlin', '22-Revenge', '23-Double_Blind', '24-Damned_If_You_Do')


def ncis_data(shows):
    url = 'https://subslikescript.com/series/NCIS-364845/season-10/episode-{}'
    ncis_df = []

    for show in shows:
        response = requests.get(url.format(show))
        page = response.text
        soup = BeautifulSoup(page, "lxml")
        script = soup.find(class_='full-script')
        words = pd.read_html(str(script))
        #         df = pd.concat(df)

        ncis_df.append(words)
    return pd.DataFrame(ncis_df)


full_eps_list = ("series/NCIS-364845/season-1/episode-1-Yankee_White'
                 ,/ series / NCIS - 364845 / season - 1 / episode - 2 - Hung_Out_to_Dry \
                 / series / NCIS - 364845 / season - 1 / episode - 3 - Seadog\
                 / series / NCIS - 364845 / season - 1 / episode - 4 - The_Immortals\
                 / series / NCIS - 364845 / season - 1 / episode - 5 - The_Curse\
                 / series / NCIS - 364845 / season - 1 / episode - 6 - High_Seas\
                 / series / NCIS - 364845 / season - 1 / episode - 7 - Sub_Rosa\
                 / series / NCIS - 364845 / season - 1 / episode - 8 - Minimum_Security
                 / series / NCIS - 364845 / season - 1 / episode - 9 - Marine_Down
                 / series / NCIS - 364845 / season - 1 / episode - 10 - Left_for_Dead
                 / series / NCIS - 364845 / season - 1 / episode - 11 - Eye_Spy
                 / series / NCIS - 364845 / season - 1 / episode - 12 - My_Other_Left_Foot
                 / series / NCIS - 364845 / season - 1 / episode - 13 - One_Shot_One_Kill
                 / series / NCIS - 364845 / season - 1 / episode - 14 - The_Good_Samaritan
                 / series / NCIS - 364845 / season - 1 / episode - 15 - Enigma
                 / series / NCIS - 364845 / season - 1 / episode - 16 - Bte_Noire
                 / series / NCIS - 364845 / season - 1 / episode - 17 - The_Truth_Is_Out_There
                 / series / NCIS - 364845 / season - 1 / episode - 18 - UnSEALeD
                 / series / NCIS - 364845 / season - 1 / episode - 19 - Dead_Man_Talking
                 / series / NCIS - 364845 / season - 1 / episode - 20 - Missing
                 / series / NCIS - 364845 / season - 1 / episode - 21 - Split_Decision
                 / series / NCIS - 364845 / season - 1 / episode - 22 - A_Weak_Link
                 / series / NCIS - 364845 / season - 1 / episode - 23 - Reveille
                 / series / NCIS - 364845 / season - 2 / episode - 1 - See_No_Evil
                 / series / NCIS - 364845 / season - 2 / episode - 2 - The_Good_Wives_Club
                 / series / NCIS - 364845 / season - 2 / episode - 3 - Vanished
                 / series / NCIS - 364845 / season - 2 / episode - 4 - Lt_Jane_Doe
                 / series / NCIS - 364845 / season - 2 / episode - 5 - The_Bone_Yard
                 / series / NCIS - 364845 / season - 2 / episode - 6 - Terminal_Leave
                 / series / NCIS - 364845 / season - 2 / episode - 7 - Call_of_Silence
                 / series / NCIS - 364845 / season - 2 / episode - 8 - Heart_Break
                 / series / NCIS - 364845 / season - 2 / episode - 9 - Forced_Entry
                 / series / NCIS - 364845 / season - 2 / episode - 10 - Chained
                 / series / NCIS - 364845 / season - 2 / episode - 11 - Black_Water
                 / series / NCIS - 364845 / season - 2 / episode - 12 - Doppelgnger
                 / series / NCIS - 364845 / season - 2 / episode - 13 - The_Meat_Puzzle
                 / series / NCIS - 364845 / season - 2 / episode - 14 - Witness
                 / series / NCIS - 364845 / season - 2 / episode - 15 - Caught_on_Tape
                 / series / NCIS - 364845 / season - 2 / episode - 16 - Pop_Life
                 / series / NCIS - 364845 / season - 2 / episode - 17 - An_Eye_for_an_Eye
                 / series / NCIS - 364845 / season - 2 / episode - 18 - Bikini_Wax
                 / series / NCIS - 364845 / season - 2 / episode - 19 - Conspiracy_Theory
                 / series / NCIS - 364845 / season - 2 / episode - 20 - Red_Cell
                 / series / NCIS - 364845 / season - 2 / episode - 21 - Hometown_Hero
                 / series / NCIS - 364845 / season - 2 / episode - 22 - SWAK
                 / series / NCIS - 364845 / season - 2 / episode - 23 - Twilight
                 / series / NCIS - 364845 / season - 3 / episode - 1 - Kill_Ari_Part_I
                 / series / NCIS - 364845 / season - 3 / episode - 2 - Kill_Ari_Part_2
                 / series / NCIS - 364845 / season - 3 / episode - 3 - Mind_Games
                 / series / NCIS - 364845 / season - 3 / episode - 4 - Silver_War
                 / series / NCIS - 364845 / season - 3 / episode - 5 - Switch
                 / series / NCIS - 364845 / season - 3 / episode - 6 - The_Voyeurs_Web
                 / series / NCIS - 364845 / season - 3 / episode - 7 - Honor_Code
                 / series / NCIS - 364845 / season - 3 / episode - 8 - Under_Covers
                 / series / NCIS - 364845 / season - 3 / episode - 10 - Probie
                 / series / NCIS - 364845 / season - 3 / episode - 11 - Model_Behavior
                 / series / NCIS - 364845 / season - 3 / episode - 12 - Boxed_In
                 / series / NCIS - 364845 / season - 3 / episode - 13 - Deception
                 / series / NCIS - 364845 / season - 3 / episode - 15 - Head_Case
                 / series / NCIS - 364845 / season - 3 / episode - 16 - Family_Secret
                 / series / NCIS - 364845 / season - 3 / episode - 17 - Ravenous
                 / series / NCIS - 364845 / season - 3 / episode - 18 - Bait
                 / series / NCIS - 364845 / season - 3 / episode - 19 - Iced
                 / series / NCIS - 364845 / season - 3 / episode - 20 - Untouchable
                 / series / NCIS - 364845 / season - 3 / episode - 21 - Bloodbath
                 / series / NCIS - 364845 / season - 3 / episode - 22 - Jeopardy
                 / series / NCIS - 364845 / season - 3 / episode - 23 - Hiatus_Part_1
                 / series / NCIS - 364845 / season - 3 / episode - 24 - Hiatus_Part_2
                 / series / NCIS - 364845 / season - 4 / episode - 1 - Shalom
                 / series / NCIS - 364845 / season - 4 / episode - 2 - Escaped
                 / series / NCIS - 364845 / season - 4 / episode - 3 - Singled_Out
                 / series / NCIS - 364845 / season - 4 / episode - 4 - Faking_It
                 / series / NCIS - 364845 / season - 4 / episode - 5 - Dead_and_Unburied
                 / series / NCIS - 364845 / season - 4 / episode - 6 - Witch_Hunt
                 / series / NCIS - 364845 / season - 4 / episode - 7 - Sandblast
                 / series / NCIS - 364845 / season - 4 / episode - 8 - Once_a_Hero
                 / series / NCIS - 364845 / season - 4 / episode - 9 - Twisted_Sister
                 / series / NCIS - 364845 / season - 4 / episode - 10 - Smoked
                 / series / NCIS - 364845 / season - 4 / episode - 11 - Driven
                 / series / NCIS - 364845 / season - 4 / episode - 12 - Suspicion
                 / series / NCIS - 364845 / season - 4 / episode - 13 - Sharif_Returns
                 / series / NCIS - 364845 / season - 4 / episode - 14 - Blowback
                 / series / NCIS - 364845 / season - 4 / episode - 15 - Friends__Lovers
                 / series / NCIS - 364845 / season - 4 / episode - 16 - Dead_Man_Walking
                 / series / NCIS - 364845 / season - 4 / episode - 17 - Skeletons
                 / series / NCIS - 364845 / season - 4 / episode - 18 - Iceman
                 / series / NCIS - 364845 / season - 4 / episode - 19 - Grace_Period
                 / series / NCIS - 364845 / season - 4 / episode - 20 - Cover_Story
                 / series / NCIS - 364845 / season - 4 / episode - 21 - Brothers_in_Arms
                 / series / NCIS - 364845 / season - 4 / episode - 22 - In_the_Dark
                 / series / NCIS - 364845 / season - 4 / episode - 23 - Trojan_Horse
                 / series / NCIS - 364845 / season - 4 / episode - 24 - Angel_of_Death
                 / series / NCIS - 364845 / season - 5 / episode - 1 - Bury_Your_Dead
                 / series / NCIS - 364845 / season - 5 / episode - 2 - Family
                 / series / NCIS - 364845 / season - 5 / episode - 3 - Ex - File
                 / series / NCIS - 364845 / season - 5 / episode - 4 - Identity_Crisis
                 / series / NCIS - 364845 / season - 5 / episode - 5 - Leap_of_Faith
                 / series / NCIS - 364845 / season - 5 / episode - 6 - Chimera
                 / series / NCIS - 364845 / season - 5 / episode - 7 - Requiem
                 / series / NCIS - 364845 / season - 5 / episode - 8 - Designated_Target
                 / series / NCIS - 364845 / season - 5 / episode - 9 - Lost__Found
                 / series / NCIS - 364845 / season - 5 / episode - 10 - Corporal_Punishment
                 / series / NCIS - 364845 / season - 5 / episode - 11 - Tribes
                 / series / NCIS - 364845 / season - 5 / episode - 12 - Stakeout
                 / series / NCIS - 364845 / season - 5 / episode - 13 - Dog_Tags
                 / series / NCIS - 364845 / season - 5 / episode - 14 - Internal_Affairs
                 / series / NCIS - 364845 / season - 5 / episode - 15 - In_the_Zone
                 / series / NCIS - 364845 / season - 5 / episode - 16 - Recoil
                 / series / NCIS - 364845 / season - 5 / episode - 17 - About_Face
                 / series / NCIS - 364845 / season - 5 / episode - 18 - Judgment_Day
                 / series / NCIS - 364845 / season - 6 / episode - 1 - Last_Man_Standing
                 / series / NCIS - 364845 / season - 6 / episode - 2 - Agent_Afloat
                 / series / NCIS - 364845 / season - 6 / episode - 3 - Capitol_Offense
                 / series / NCIS - 364845 / season - 6 / episode - 4 - Heartland
                 / series / NCIS - 364845 / season - 6 / episode - 5 - Nine_Lives
                 / series / NCIS - 364845 / season - 6 / episode - 6 - Murder_20
                 / series / NCIS - 364845 / season - 6 / episode - 7 - Collateral_Damage
                 / series / NCIS - 364845 / season - 6 / episode - 8 - Cloak
                 / series / NCIS - 364845 / season - 6 / episode - 9 - Dagger
                 / series / NCIS - 364845 / season - 6 / episode - 10 - Road_Kill
                 / series / NCIS - 364845 / season - 6 / episode - 11 - Silent_Night
                 / series / NCIS - 364845 / season - 6 / episode - 12 - Caged
                 / series / NCIS - 364845 / season - 6 / episode - 13 - Broken_Bird
                 / series / NCIS - 364845 / season - 6 / episode - 14 - Love__War
                 / series / NCIS - 364845 / season - 6 / episode - 15 - Deliverance
                 / series / NCIS - 364845 / season - 6 / episode - 16 - Bounce
                 / series / NCIS - 364845 / season - 6 / episode - 17 - South_by_Southwest
                 / series / NCIS - 364845 / season - 6 / episode - 18 - Knockout
                 / series / NCIS - 364845 / season - 6 / episode - 19 - Hide_and_Seek
                 / series / NCIS - 364845 / season - 6 / episode - 20 - Dead_Reckoning
                 / series / NCIS - 364845 / season - 6 / episode - 21 - Toxic
                 / series / NCIS - 364845 / season - 6 / episode - 22 - Legend
                 / series / NCIS - 364845 / season - 6 / episode - 23 - Legend_Part_2
                 / series / NCIS - 364845 / season - 6 / episode - 24 - Semper_Fidelis
                 / series / NCIS - 364845 / season - 6 / episode - 25 - Aliyah
                 / series / NCIS - 364845 / season - 7 / episode - 1 - Truth_or_Consequences
                 / series / NCIS - 364845 / season - 7 / episode - 2 - Reunion
                 / series / NCIS - 364845 / season - 7 / episode - 3 - The_Inside_Man
                 / series / NCIS - 364845 / season - 7 / episode - 4 - Good_Cop_Bad_Cop
                 / series / NCIS - 364845 / season - 7 / episode - 5 - Code_of_Conduct
                 / series / NCIS - 364845 / season - 7 / episode - 6 - Outlaws_and_In - Laws
                 / series / NCIS - 364845 / season - 7 / episode - 7 - Endgame
                 / series / NCIS - 364845 / season - 7 / episode - 8 - Power_Down
                 / series / NCIS - 364845 / season - 7 / episode - 9 - Childs_Play
                 / series / NCIS - 364845 / season - 7 / episode - 10 - Faith
                 / series / NCIS - 364845 / season - 7 / episode - 11 - Ignition
                 / series / NCIS - 364845 / season - 7 / episode - 12 - Flesh_and_Blood
                 / series / NCIS - 364845 / season - 7 / episode - 13 - Jet_Lag
                 / series / NCIS - 364845 / season - 7 / episode - 14 - Masquerade
                 / series / NCIS - 364845 / season - 7 / episode - 15 - Jack - Knife
                 / series / NCIS - 364845 / season - 7 / episode - 16 - Mothers_Day
                 / series / NCIS - 364845 / season - 7 / episode - 17 - Double_Identity
                 / series / NCIS - 364845 / season - 7 / episode - 18 - Jurisdiction
                 / series / NCIS - 364845 / season - 7 / episode - 19 - Guilty_Pleasure
                 / series / NCIS - 364845 / season - 7 / episode - 20 - Moonlighting
                 / series / NCIS - 364845 / season - 7 / episode - 21 - Obsession
                 / series / NCIS - 364845 / season - 7 / episode - 22 - Borderland
                 / series / NCIS - 364845 / season - 7 / episode - 23 - Patriot_Down
                 / series / NCIS - 364845 / season - 7 / episode - 24 - Rule_Fifty - One
                 / series / NCIS - 364845 / season - 8 / episode - 1 - Spider_and_the_Fly
                 / series / NCIS - 364845 / season - 8 / episode - 2 - Worst_Nightmare
                 / series / NCIS - 364845 / season - 8 / episode - 3 - Short_Fuse
                 / series / NCIS - 364845 / season - 8 / episode - 4 - Royals__Loyals
                 / series / NCIS - 364845 / season - 8 / episode - 5 - Dead_Air
                 / series / NCIS - 364845 / season - 8 / episode - 6 - Cracked
                 / series / NCIS - 364845 / season - 8 / episode - 7 - Broken_Arrow
                 / series / NCIS - 364845 / season - 8 / episode - 8 - Enemies_Foreign
                 / series / NCIS - 364845 / season - 8 / episode - 9 - Enemies_Domestic
                 / series / NCIS - 364845 / season - 8 / episode - 10 - False_Witness
                 / series / NCIS - 364845 / season - 8 / episode - 11 - Ships_in_the_Night
                 / series / NCIS - 364845 / season - 8 / episode - 12 - Recruited
                 / series / NCIS - 364845 / season - 8 / episode - 13 - Freedom
                 / series / NCIS - 364845 / season - 8 / episode - 14 - A_Man_Walks_Into_a_Bar
                 / series / NCIS - 364845 / season - 8 / episode - 15 - Defiance
                 / series / NCIS - 364845 / season - 8 / episode - 16 - Kill_Screen
                 / series / NCIS - 364845 / season - 8 / episode - 17 - One_Last_Score
                 / series / NCIS - 364845 / season - 8 / episode - 18 - Out_of_the_Frying_Pan
                 / series / NCIS - 364845 / season - 8 / episode - 19 - Tell - All
                 / series / NCIS - 364845 / season - 8 / episode - 20 - Two - Faced
                 / series / NCIS - 364845 / season - 8 / episode - 21 - Dead_Reflection
                 / series / NCIS - 364845 / season - 8 / episode - 22 - Baltimore
                 / series / NCIS - 364845 / season - 8 / episode - 23 - Swan_Song
                 / series / NCIS - 364845 / season - 8 / episode - 24 - Pyramid
                 / series / NCIS - 364845 / season - 9 / episode - 1 - Nature_of_the_Beast
                 / series / NCIS - 364845 / season - 9 / episode - 2 - Restless
                 / series / NCIS - 364845 / season - 9 / episode - 3 - The_Penelope_Papers
                 / series / NCIS - 364845 / season - 9 / episode - 4 - Enemy_on_the_Hill
                 / series / NCIS - 364845 / season - 9 / episode - 5 - Safe_Harbor
                 / series / NCIS - 364845 / season - 9 / episode - 6 - Thirst
                 / series / NCIS - 364845 / season - 9 / episode - 7 - Devils_Triangle
                 / series / NCIS - 364845 / season - 9 / episode - 8 - Engaged_Part_I
                 / series / NCIS - 364845 / season - 9 / episode - 9 - Engaged_Part_II
                 / series / NCIS - 364845 / season - 9 / episode - 10 - Sins_of_the_Father
                 / series / NCIS - 364845 / season - 9 / episode - 11 - Newborn_King
                 / series / NCIS - 364845 / season - 9 / episode - 12 - Housekeeping
                 / series / NCIS - 364845 / season - 9 / episode - 13 - A_Desperate_Man
                 / series / NCIS - 364845 / season - 9 / episode - 14 - Life_Before_His_Eyes
                 / series / NCIS - 364845 / season - 9 / episode - 15 - Secrets
                 / series / NCIS - 364845 / season - 9 / episode - 16 - Psych_Out
                 / series / NCIS - 364845 / season - 9 / episode - 17 - Need_to_Know
                 / series / NCIS - 364845 / season - 9 / episode - 18 - The_Tell
                 / series / NCIS - 364845 / season - 9 / episode - 19 - The_Good_Son
                 / series / NCIS - 364845 / season - 9 / episode - 20 - The_Missionary_Position
                 / series / NCIS - 364845 / season - 9 / episode - 21 - Rekindled
                 / series / NCIS - 364845 / season - 9 / episode - 22 - Playing_with_Fire
                 / series / NCIS - 364845 / season - 9 / episode - 23 - Up_in_Smoke
                 / series / NCIS - 364845 / season - 9 / episode - 24 - Till_Death_Do_Us_Part
                 / series / NCIS - 364845 / season - 10 / episode - 1 - Extreme_Prejudice
                 / series / NCIS - 364845 / season - 10 / episode - 2 - Recovery
                 / series / NCIS - 364845 / season - 10 / episode - 3 - Phoenix
                 / series / NCIS - 364845 / season - 10 / episode - 4 - Lost_at_Sea
                 / series / NCIS - 364845 / season - 10 / episode - 5 - The_Namesake
                 / series / NCIS - 364845 / season - 10 / episode - 6 - Shell_Shock_Part_I
                 / series / NCIS - 364845 / season - 10 / episode - 7 - Shell_Shock_Part_II
                 / series / NCIS - 364845 / season - 10 / episode - 8 - Gone
                 / series / NCIS - 364845 / season - 10 / episode - 9 - Devils_Trifecta
                 / series / NCIS - 364845 / season - 10 / episode - 11 - Shabbat_Shalom
                 / series / NCIS - 364845 / season - 10 / episode - 12 - Shiva
                 / series / NCIS - 364845 / season - 10 / episode - 13 - Hit_and_Run
                 / series / NCIS - 364845 / season - 10 / episode - 14 - Canary
                 / series / NCIS - 364845 / season - 10 / episode - 15 - Hereafter
                 / series / NCIS - 364845 / season - 10 / episode - 16 - Detour
                 / series / NCIS - 364845 / season - 10 / episode - 17 - Prime_Suspect
                 / series / NCIS - 364845 / season - 10 / episode - 18 - Seek
                 / series / NCIS - 364845 / season - 10 / episode - 19 - Squall
                 / series / NCIS - 364845 / season - 10 / episode - 20 - Chasing_Ghosts
                 / series / NCIS - 364845 / season - 10 / episode - 21 - Berlin
                 / series / NCIS - 364845 / season - 10 / episode - 22 - Revenge
                 / series / NCIS - 364845 / season - 10 / episode - 23 - Double_Blind
                 / series / NCIS - 364845 / season - 10 / episode - 24 - Damned_If_You_Do
                 / series / NCIS - 364845 / season - 11 / episode - 1 - Whiskey_Tango_Foxtrot
                 / series / NCIS - 364845 / season - 11 / episode - 2 - Past_Present_and_Future
                 / series / NCIS - 364845 / season - 11 / episode - 3 - Under_the_Radar
                 / series / NCIS - 364845 / season - 11 / episode - 4 - Anonymous_Was_a_Woman
                 / series / NCIS - 364845 / season - 11 / episode - 5 - Once_a_Crook
                 / series / NCIS - 364845 / season - 11 / episode - 6 - Oil_and_Water
                 / series / NCIS - 364845 / season - 11 / episode - 7 - Better_Angels
                 / series / NCIS - 364845 / season - 11 / episode - 8 - Alibi
                 / series / NCIS - 364845 / season - 11 / episode - 9 - Gut_Check
                 / series / NCIS - 364845 / season - 11 / episode - 10 - Devils_Triad
                 / series / NCIS - 364845 / season - 11 / episode - 11 - Homesick
                 / series / NCIS - 364845 / season - 11 / episode - 12 - Kill_Chain
                 / series / NCIS - 364845 / season - 11 / episode - 13 - Double_Back
                 / series / NCIS - 364845 / season - 11 / episode - 14 - Monsters_and_Men
                 / series / NCIS - 364845 / season - 11 / episode - 15 - Bulletproof
                 / series / NCIS - 364845 / season - 11 / episode - 16 - Dressed_to_Kill
                 / series / NCIS - 364845 / season - 11 / episode - 17 - Rock_and_a_Hard_Place
                 / series / NCIS - 364845 / season - 11 / episode - 18 - Crescent_City_Part_1
                 / series / NCIS - 364845 / season - 11 / episode - 19 - Crescent_City_Part_2
                 / series / NCIS - 364845 / season - 11 / episode - 20 - Page_Not_Found
                 / series / NCIS - 364845 / season - 11 / episode - 21 - Alleged
                 / series / NCIS - 364845 / season - 11 / episode - 22 - Shooter
                 / series / NCIS - 364845 / season - 11 / episode - 23 - The_Admirals_Daughter
                 / series / NCIS - 364845 / season - 11 / episode - 24 - Honor_Thy_Father
                 / series / NCIS - 364845 / season - 12 / episode - 1 - Twenty_Klicks
                 / series / NCIS - 364845 / season - 12 / episode - 2 - Kill_the_Messenger
                 / series / NCIS - 364845 / season - 12 / episode - 3 - So_It_Goes
                 / series / NCIS - 364845 / season - 12 / episode - 4 - Choke_Hold
                 / series / NCIS - 364845 / season - 12 / episode - 5 - The_San_Dominick
                 / series / NCIS - 364845 / season - 12 / episode - 6 - Parental_Guidance_Suggested
                 / series / NCIS - 364845 / season - 12 / episode - 7 - The_Searchers
                 / series / NCIS - 364845 / season - 12 / episode - 8 - Semper_Fortis
                 / series / NCIS - 364845 / season - 12 / episode - 9 - Grounded
                 / series / NCIS - 364845 / season - 12 / episode - 10 - House_Rules
                 / series / NCIS - 364845 / season - 12 / episode - 11 - Check
                 / series / NCIS - 364845 / season - 12 / episode - 12 - The_Enemy_Within
                 / series / NCIS - 364845 / season - 12 / episode - 13 - We_Build_We_Fight
                 / series / NCIS - 364845 / season - 12 / episode - 14 - Cadence
                 / series / NCIS - 364845 / season - 12 / episode - 15 - Cabin_Fever
                 / series / NCIS - 364845 / season - 12 / episode - 16 - Blast_from_the_Past
                 / series / NCIS - 364845 / season - 12 / episode - 17 - The_Artful_Dodger
                 / series / NCIS - 364845 / season - 12 / episode - 18 - Status_Update
                 / series / NCIS - 364845 / season - 12 / episode - 19 - Patience
                 / series / NCIS - 364845 / season - 12 / episode - 20 - No_Good_Deed
                 / series / NCIS - 364845 / season - 12 / episode - 21 - Lost_in_Translation
                 / series / NCIS - 364845 / season - 12 / episode - 22 - Troll
                 / series / NCIS - 364845 / season - 12 / episode - 23 - The_Lost_Boys
                 / series / NCIS - 364845 / season - 12 / episode - 24 - Neverland
                 / series / NCIS - 364845 / season - 13 / episode - 1 - Stop_the_Bleeding
                 / series / NCIS - 364845 / season - 13 / episode - 2 - Personal_Day
                 / series / NCIS - 364845 / season - 13 / episode - 3 - Incognito
                 / series / NCIS - 364845 / season - 13 / episode - 4 - Double_Trouble
                 / series / NCIS - 364845 / season - 13 / episode - 5 - Lockdown
                 / series / NCIS - 364845 / season - 13 / episode - 6 - Viral
                 / series / NCIS - 364845 / season - 13 / episode - 7 - Sixteen_Years
                 / series / NCIS - 364845 / season - 13 / episode - 8 - Saviors
                 / series / NCIS - 364845 / season - 13 / episode - 9 - Day_in_Court
                 / series / NCIS - 364845 / season - 13 / episode - 10 - Blood_Brothers
                 / series / NCIS - 364845 / season - 13 / episode - 11 - Spinning_Wheel
                 / series / NCIS - 364845 / season - 13 / episode - 12 - Sister_City_Part_1
                 / series / NCIS - 364845 / season - 13 / episode - 13 - Dj_Vu
                 / series / NCIS - 364845 / season - 13 / episode - 14 - Decompressed
                 / series / NCIS - 364845 / season - 13 / episode - 15 - React
                 / series / NCIS - 364845 / season - 13 / episode - 16 - Loose_Cannons
                 / series / NCIS - 364845 / season - 13 / episode - 17 - After_Hours
                 / series / NCIS - 364845 / season - 13 / episode - 18 - Scope
                 / series / NCIS - 364845 / season - 13 / episode - 19 - Reasonable_Doubts
                 / series / NCIS - 364845 / season - 13 / episode - 20 - Episode_1320
                 / series / NCIS - 364845 / season - 13 / episode - 21 - Return_to_Sender
                 / series / NCIS - 364845 / season - 13 / episode - 22 - Homefront
                 / series / NCIS - 364845 / season - 13 / episode - 23 - Dead_Letter
                 / series / NCIS - 364845 / season - 13 / episode - 24 - Family_First
                 / series / NCIS - 364845 / season - 14 / episode - 1 - Rogue
                 / series / NCIS - 364845 / season - 14 / episode - 2 - Being_Bad
                 / series / NCIS - 364845 / season - 14 / episode - 3 - Privileged_Information
                 / series / NCIS - 364845 / season - 14 / episode - 4 - Love_Boat
                 / series / NCIS - 364845 / season - 14 / episode - 5 - Philly
                 / series / NCIS - 364845 / season - 14 / episode - 6 - Shell_Game
                 / series / NCIS - 364845 / season - 14 / episode - 7 - Home_of_the_Brave
                 / series / NCIS - 364845 / season - 14 / episode - 8 - Enemy_Combatant
                 / series / NCIS - 364845 / season - 14 / episode - 9 - Pay_to_Play
                 / series / NCIS - 364845 / season - 14 / episode - 10 - The_Tie_That_Binds
                 / series / NCIS - 364845 / season - 14 / episode - 11 - Willoughby
                 / series / NCIS - 364845 / season - 14 / episode - 12 - Off_the_Grid
                 / series / NCIS - 364845 / season - 14 / episode - 13 - Keep_Going
                 / series / NCIS - 364845 / season - 14 / episode - 14 - Nonstop
                 / series / NCIS - 364845 / season - 14 / episode - 15 - Pandoras_Box_Part_I
                 / series / NCIS - 364845 / season - 14 / episode - 16 - A_Many_Splendored_Thing
                 / series / NCIS - 364845 / season - 14 / episode - 17 - What_Lies_Above
                 / series / NCIS - 364845 / season - 14 / episode - 18 - MIA
                 / series / NCIS - 364845 / season - 14 / episode - 19 - The_Wall
                 / series / NCIS - 364845 / season - 14 / episode - 20 - Episode_1420
                 / series / NCIS - 364845 / season - 14 / episode - 21 - One_Book_Two_Covers
                 / series / NCIS - 364845 / season - 14 / episode - 22 - Beastmaster
                 / series / NCIS - 364845 / season - 14 / episode - 23 - Something_Blue
                 / series / NCIS - 364845 / season - 14 / episode - 24 - Rendezvous
                 / series / NCIS - 364845 / season - 15 / episode - 1 - House_Divided
                 / series / NCIS - 364845 / season - 15 / episode - 2 - Twofer
                 / series / NCIS - 364845 / season - 15 / episode - 3 - Exit_Strategy
                 / series / NCIS - 364845 / season - 15 / episode - 4 - Skeleton_Crew
                 / series / NCIS - 364845 / season - 15 / episode - 5 - Fake_It_Til_You_Make_It
                 / series / NCIS - 364845 / season - 15 / episode - 6 - Episode_dated_31_October_2017
                 / series / NCIS - 364845 / season - 15 / episode - 7 - Burden_of_Proof
                 / series / NCIS - 364845 / season - 15 / episode - 8 - Voices
                 / series / NCIS - 364845 / season - 15 / episode - 9 - Ready_or_Not
                 / series / NCIS - 364845 / season - 15 / episode - 10 - Double_Down
                 / series / NCIS - 364845 / season - 15 / episode - 11 - High_Tide
                 / series / NCIS - 364845 / season - 15 / episode - 12 - Dark_Secrets
                 / series / NCIS - 364845 / season - 15 / episode - 13 - Family_Ties
                 / series / NCIS - 364845 / season - 15 / episode - 14 - Keep_Your_Friends_Close
                 / series / NCIS - 364845 / season - 15 / episode - 15 - Keep_Your_Enemies_Closer
                 / series / NCIS - 364845 / season - 15 / episode - 16 - Handle_with_Care
                 / series / NCIS - 364845 / season - 15 / episode - 17 - One_Mans_Trash
                 / series / NCIS - 364845 / season - 15 / episode - 19 - Episode_1519
                 / series / NCIS - 364845 / season - 15 / episode - 21 - One_Step_Forward
                 / series / NCIS - 364845 / season - 15 / episode - 22 - Two_Steps_Back
                 / series / NCIS - 364845 / season - 15 / episode - 23 - Fallout
                 / series / NCIS - 364845 / season - 15 / episode - 24 - Date_with_Destiny
                 / series / NCIS - 364845 / season - 16 / episode - 1 - Destinys_Child
                 / series / NCIS - 364845 / season - 16 / episode - 2 - Love_Thy_Neighbor
                 / series / NCIS - 364845 / season - 16 / episode - 3 - Boom
                 / series / NCIS - 364845 / season - 16 / episode - 4 - Third_Wheel
                 / series / NCIS - 364845 / season - 16 / episode - 5 - Fragments
                 / series / NCIS - 364845 / season - 16 / episode - 6 - Beneath_the_Surface
                 / series / NCIS - 364845 / season - 16 / episode - 7 - A_Thousand_Words
                 / series / NCIS - 364845 / season - 16 / episode - 8 - Friendly_Fire
                 / series / NCIS - 364845 / season - 16 / episode - 9 - Episode_169
                 / series / NCIS - 364845 / season - 16 / episode - 11 - Toil_and_Trouble
                 / series / NCIS - 364845 / season - 16 / episode - 12 - The_Last_Link
                 / series / NCIS - 364845 / season - 16 / episode - 15 - Episode_1615
                 / series / NCIS - 364845 / season - 16 / episode - 16 - Bears_and_Cubs
                 / series / NCIS - 364845 / season - 16 / episode - 17 - Silent_Service
                 / series / NCIS - 364845 / season - 16 / episode - 19 - Episode_1619
                 / series / NCIS - 364845 / season - 16 / episode - 20 - Hail__Farewell
                 / series / NCIS - 364845 / season - 16 / episode - 21 - Episode_1621
                 / series / NCIS - 364845 / season - 16 / episode - 23 - Lost_Time
                 / series / NCIS - 364845 / season - 17 / episode - 3 - Going_Mobile
                 / series / NCIS - 364845 / season - 17 / episode - 5 - Wide_Awake
                 / series / NCIS - 364845 / season - 17 / episode - 6 - Institutionalized
                 / series / NCIS - 364845 / season - 17 / episode - 8 - No_Vacancy
                 / series / NCIS - 364845 / season - 17 / episode - 9 - IRL
                 / series / NCIS - 364845 / season - 17 / episode - 10 - The_North_Pole
                 / series / NCIS - 364845 / season - 17 / episode - 11 - In_the_Wind
                 / series / NCIS - 364845 / season - 17 / episode - 12 - Flight_Plan
                 / series / NCIS - 364845 / season - 17 / episode - 13 - Sound_Off
                 / series / NCIS - 364845 / season - 17 / episode - 14 - On_Fire
                 / series / NCIS - 364845 / season - 17 / episode - 15 - Lonely_Hearts"])
