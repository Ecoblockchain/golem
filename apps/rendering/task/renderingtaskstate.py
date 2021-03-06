from os import path

from apps.core.task.coretaskstate import (TaskDefinition,
                                          AdvanceVerificationOptions,
                                          CoreTaskDefaults)


class RendererDefaults(CoreTaskDefaults):
    """ Suggested default values for Rendering tasks"""
    def __init__(self):
        super(RendererDefaults, self).__init__()
        self.resolution = [1920, 1080]


class RenderingTaskDefinition(TaskDefinition):
    def __init__(self):
        TaskDefinition.__init__(self)
        self.resolution = [0, 0]
        self.renderer = None
        self.options = None
        self.main_scene_file = ""
        self.output_format = ""

    def is_valid(self):
        is_valid, err = super(RenderingTaskDefinition, self).is_valid()
        if is_valid and not path.exists(self.main_scene_file):
            return False, u"Main scene file {} is not properly set".format(self.main_scene_file)
        return is_valid, err

    def add_to_resources(self):
        super(RenderingTaskDefinition, self).add_to_resources()
        self.resources.add(path.normpath(self.main_scene_file))


class AdvanceRenderingVerificationOptions(AdvanceVerificationOptions):
    def __init__(self):
        AdvanceVerificationOptions.__init__(self)
        self.box_size = (5, 5)
        self.probability = 0.01
