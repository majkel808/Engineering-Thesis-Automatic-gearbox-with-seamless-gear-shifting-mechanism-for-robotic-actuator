# Engineering Thesis: Automatic gearbox based on cycloidal drive for robotic actuator

Engineering Thesis at the Warsaw University of Technology, 

Field of Study: Mechatronics

Specialization: Micromechanics

Academic Advisor: Marcin Michalowski PhD 

An actuator for a robotic arm was designed, based on a variable transmission gearbox utilizing a cycloidal drive. The diploma thesis included a review of existing solutions, calculations related to the design of the cycloidal gearbox, and the development of a 3D model of the device.

## Table of Contents
- [Detailed Description](#detailed-description)
- [Project Stages](#project-stages)
  - [Research](#research)
  - [Concept Development](#concept-development)
  - [Calculation of Design Parameters](#calculation-of-design-parameters)
  - [3D Model Development](#3d-model-development)
  - [Making of the Prototype](#making-of-the-prototype)
- [Technologies Used](#technologies-used)
- [Documentation](#documentation)
- [Future Work](#future-work)
- [Bibliography](#bibliography)

## Detailed Description
The aim of this thesis is to design a mechatronic system tasked with driving a robotic arm, whose work cycle will consist of frequent changes of the required torque. The gearbox being designed will allow achieving two distinct, independent operating modes, which provide an ability to quickly switch between themselves without stopping the device. This will, in turn, allow the robot to choose the optimal operating mode, enabling either a higher load-bearing capacity or a higher angular velocity of the robotic arm. The project in question has been specifically designed for use in affordable automation and in education. The design of the robotic arm allows it to achieve high angular velocity while also being highly precise due to minimal play. To provide such functionality, two custom cycloidal drives have been designed, one of which is used as a differential. Such a mechanism can rapidly and automatically alter the gear ratio of the gearbox.

#### The 3D render of the designed gearbox:

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/b131ab3c-a6f9-4a0b-ade7-f672599779ae" alt="New_automatic_cycklo_assembly_1" width="700" style="border-radius: 200px;" />


## Project Stages
### Research
During the research process, I gained a better understanding of the construction of automatic transmissions, the design of drives used in robotics, and, most importantly, knowledge in the field of designing cycloidal drives. Before my thesis, I have designed many different kinds of cycloidal drives (Files provided in my 3D_models repository). My biggest inspiration for the project was "A two-speed actuator for robotics with fast seamless gear shifting" [1], which was based on the planetary gearbox. I wanted to improve on this idea and use the cycloidal disk to provide more precise movement and high gear ratio in a compact design. The most important and challenging part of my thesis was the optimization of the device efficiency based on the tribological research of cycloidal drives, such as "A COMPARATIVE CALCULATION OF CYCLOID DRIVE EFFICIENCY” [2].

### Concept Development
The next stage was the development of the device's design based on previous research and comparison of possible solutions. I have developed the following operation diagram of the device. 

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/4ef46058-4046-4ab5-bbd3-063aa6f04634" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

An illustrative depiction featuring labeled components of the designed device.

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/c44094ac-eafc-453b-a403-88f1ee0dbb6f" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

1. Motor 1
2. Shaft locking mechanism
3. Motor 2
4. Low ratio cycloidal reducer
5. Belt-driven reducer
6. Output shaft
7. High ratio cycloidal reducer

### Calculation of Design Parameters
1. After specifying the device requirements, calculations were conducted to determine the necessary gear ratios for both transmissions.
2. Knowing the gear ratios, a model was selected to generate the epicycloidal curve. A Python script was employed to present various geometric configuration parameters of the transmission to find the optimal device design.

   <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/83e1a713-7f1c-44d3-bbc4-3dafc844dbde" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

4. An analytical analysis of the transmission efficiency was conducted, necessary for the correct selection of the motor to ensure the system operates in accordance with the specified requirements.
5. For efficiency optimization, a Python program was written to allow testing of various transmission parameters and selecting the best configuration of these parameters.

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/74db0190-bc7f-4ef1-8df9-deb88d459676" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

### 3D Model Development
The 3D model of the device was created using the Autodesk Inventor software. The device has been divided into several subcomponents. For every assembly, the 3D render of the side view and the cross-section has been provided.

- The high-speed gearbox drive shaft assembly
  
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/1046461a-4af5-411a-ab54-a70797168f7b" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />

- The high-torque gearbox drive shaft assembly
  
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/c64957c0-b5ec-4293-b673-f8f5a3926526" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />

- Automatic transmission assembly
  
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/d941ebfb-a180-4160-a2a0-b2f98a9ad7e3" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />
  
    <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/62c8507e-ec45-4b93-8a2a-1485059a9fd0" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />

### Making of the Prototype
The prototype of the device has been constructed to confirm the required functionality and for establishing the possible use of the cycloidal drive in the automatic transmission. The components were manufactured in the most parts with my own FDM 3D printer. The commercial components required for this project include bearings, shafts, mounting elements, and clutches. 
The prototype was controlled by 2 stepper motor drivers with custom Arduino code. The building process and the final version of the prototype have been presented in the pictures below. 

- Compact cycloidal drive before assembly
  
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/e057688e-1bf3-4fd6-a928-28bf45267a13" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />
  
- The fully assembled actuator
  
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/84212a52-0caa-4b5e-8a8f-1c4f844fd8ba" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />
 
## Technologies Used

During the work on this engineering thesis, it was necessary to use various engineering software, including:

- Autodesk Inventor - for developing the 3D model
- AutoCAD - for developing technical documentation
- Ansys Mechanical - for mass optimization of the cycloidal disk
- Python - for calculations related to epicycloid geometry and transmission efficiency optimization

## Documentation

The technical drawing required for manufacturing part has been made in Autodesk AutoCAD. Part would be manufactured via CNC machining, laser cutting, and 3D printing. Whole documentation has been provided in the sub-folder of this repository.

## Future Work

This project requires further optimization, particularly in correcting the epicycloidal gearing. Subsequently, further prototype testing would be required, which could be constructed in smaller parts using 3D printing to ensure greater structural rigidity.

## Bibliography

[1]: A. Girard and H. Asada, A two-speed actuator for robotics with fast seamless gear shifting. 2015, p. 4711. doi: 10.1109/IROS.2015.7354047.

[2] M. Vasić, “A COMPARATIVE CALCULATION OF CYCLOID DRIVE EFFICIENCY,” Mach. Des., Jan. 2020, Accessed: Jul. 10, 2023. [Online]. Available: https://www.academia.edu/79815900/A_COMPARATIVE_CALCULATION_OF_CYCLOID_DRIVE_EFFICIENCY
