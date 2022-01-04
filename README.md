# SimulatorX
## About
SimulatorX is a web-application built on top of Django server. The software offers performing epidemiological simulations of infectious disease. It provides a novel approach towards epidemiological simulations. The data is at the core of its functions. The simulations are driven by data related to demography of population. It means biological features such as age, gender, and ethnicity of population are taken into consideration for driving the simulation. Facial recognition technology is embedded with the software to extract biological features (age, gender, and ethnicity) from face visuals. This version only supports images for facial recognition.

The software consists of two applications: COVID-19 Auto Simulation and Manual Simulation

The software mainly uses NetworkX library for graph network operations. Further, it uses VGG16 model architecture for facial recognition system and KNN classifier to predict the probability of catching COVID-19 infection on an individual level.
