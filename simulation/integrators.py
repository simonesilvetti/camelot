from simulation.node import Node, RandomExamGenerator, Human, CorrectorGenerator
import numpy as np

human=Human(abs(np.random.normal(14.9)), abs(np.random.normal(140)), abs(np.random.normal(4.5)))

exam=Node("Exam", human)

hemo_int=Node("hemo_int",CorrectorGenerator("hemo_int",2))
hemo_inib=Node("hemo_nib",CorrectorGenerator("hemo_nib",20))
sodium_int=Node("sodium_int",CorrectorGenerator("sodium_int",100))
sodium_inib=Node("sodium_inib",CorrectorGenerator("sodium_inib",150))
pot_int=Node("pot_int",CorrectorGenerator("pot_int",1))
pot_inib=Node("pot_inib",CorrectorGenerator("pot_inib",8))


































          )