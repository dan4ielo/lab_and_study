# This chapter describes the process that one needs to
# go through when creating an object oriented program

# The 'recommended' steps:
# NOTE: These steps are not mandatory, but are a good
# starting point for many programing problems

# 1. Write or draw about the problem.
# 2. Extract key concepts from #1 and research them.
# 3. Create a class hierarchy and object map for the
# concepts
# 4. Code the classes and a test to run them
# 5. Repeat and refine.

# From here on out we are going to be building the basis
# for a game engine following these principles

# First we begin with a list of the nouns that we extract
# from the first 2 steps.

# Alien
# Player
# Ship
# Maze
# Room 
# Scene
# Gothon
# Escape Pod
# Planet
# Map 
# Engine
# Death
# Central Corridor
# Laser Weapon Armory
# The bridge

# After analyzing we create a class hierarchy like so

# Map
# Engine
# Scene
#   |- Death
#   |- Central Corridor
#   |- Laser Weapon Armory
#   |- The Bridge
#   |- Escape Pod

# Now we add different methods based on the verbs we
# have laid out for ourselves

# Map
# +- next_scene
# +- opening_scene
# Engine
# +- play
# Scene
# +- enter
#   |- Death
#   |- Central Corridor
#   |- Laser Weapon Armory
#   |- The Bridge
#   |- Escape Pod

#=======================================================#
# Now the coding part

class Scene ():

    def enter(self):
        pass


class Engine():

    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):
    
    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map():
    
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
