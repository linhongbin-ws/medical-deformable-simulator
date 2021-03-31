from mujoco_py import (load_model_from_xml,
                        load_model_from_path,
                        MjSim,
                        MjViewer)
import numpy as np
from os.path import join, isfile
import time

# MODEL_XML_PATH = join('.','xmls', 'rope.xml')
MODEL_XML_PATH = join('.','xmls', 'cloth.xml')
if not isfile(MODEL_XML_PATH):
    print(f"cannot find {MODEL_XML_PATH}")
model = load_model_from_path(MODEL_XML_PATH)
sim = MjSim(model)

viewer = MjViewer(sim)

while True:
    sim.step()
    viewer.render()
    # time.sleep(1)