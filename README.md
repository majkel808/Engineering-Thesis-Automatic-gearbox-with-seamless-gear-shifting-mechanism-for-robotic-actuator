# Engineering Thesis Automatic gearbox based on cycloidal drive for robotic actuator

An actuator for a robot arm was designed, based on a variable transmission gearbox utilizing a cycloidal drive. The diploma thesis included a review of existing solutions, calculations related to the design of the cycloidal gearbox, and the development of 3D model of the divice.

## Table of Contents
- [Detailed description](#Detailed-description)
- [Project Stages](#project-stages)
  - [Reasrch](#Reasrch)
  - [Source Research](#source-research)
  - [Concept Development](#concept-development)
  - [Calculation of Design Parameters](#calculation-of-design-parameters)
  - [3D Model Development](#3d-model-development)
  - [Making of the prototype](#Making-of-the-prototype)
- [Technologies used](#technologies-used)
- [Documentation](#Documentation)
- [Future Work](#future-work)
- [Bibliography](#Bibliography)
  
## Detailed description
The aim of this thesis is to design a mechatronic system tasked with driving a robotic arm, whose work cycle will consist of frequent changes of the required torque. The gearbox being designed will allow for achieving two distinct, independent operating modes, which provide an ability to quickly switch between themselves without stopping the device. This will, in turn, allow the robot to choose the optimal operating mode, enabling either a higher load-bearing capacity or a higher angular velocity of the robotic arm. The project in question has been specifically designed for use in affordable automation and in education.
The design of the robotic arm allows it to achieve high angular velocity, while also being highly precise due to minimal play. To provide such functionality, two cus-tom cycloidal drives have been designed, one of which is used as a differential. Such a mechanism can rapidly and automatically alter the gear ratio of the gearbox.

#### The 3D render of the designed gearbox:

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/b131ab3c-a6f9-4a0b-ade7-f672599779ae" alt="New_automatic_cycklo_assembly_1" width="700" style="border-radius: 200px;" />

## Project Stages
### Reasrch
During the research process, I gained a better understanding of the construction of automatic transmissions, the design of drives used in robotics, and, most importantly, knowledge in the field of designing  cycloidal drives. Before my thesis i have designed many diffent kinds of cycloidal drives 
(Files provided in my 3D_modelid/Cyckloidal_drive repository)
My biggest inspiration fo the project was "A two-speed actuator for robotics with fast seamless gear shifting" [1] wich was based on the planetary gearbox, i wanted to improve on this idea and use the cycloidal disk to provide more precise movement and high gear ratio in a compact design. 
The most inporantat and challanging part of my thesis was the optimalisation of the device efficiency based on the tribological reaserch of cyckloidal drives, such as A "COMPARATIVE CALCULATION OF CYCLOID DRIVE EFFICIENCY”[2].

### Concept Development
The next stage was the development of the device's design based on previous research and comparison of possible solutions. I have developed the following operation diagram of the device. 

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/4ef46058-4046-4ab5-bbd3-063aa6f04634" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

An illustrative depiction featuring labeled components of the designed device.

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/c44094ac-eafc-453b-a403-88f1ee0dbb6f" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

<figcaption style="text-align: left;">
  
  1. Motor 1
  2. Shaft locking mechanism
  3. Motor 2
  4. Low ration cyckloidal reducer
  5. Blet driven reducer
  6. Output shaft
  7. High ration cycloidal reducer
</figcaption>

### Calculation of Design Parameters
1. After specifying the device requirements, calculations were conducted to determine the necessary gear ratios for both transmissions.
2. Knowing the gear ratios, a model was selected to generate the epicycloidal curve. A Python script was employed to present various geometric configuration parameters of the transmission to find the optimal device design. In the picture belowe, one of those configuartions has been presented.

<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/83e1a713-7f1c-44d3-bbc4-3dafc844dbde" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

3. An analytical analysis of the transmission efficiency was conducted, necessary for the correct selection of the motor to ensure the system operates in accordance with the specified requirements.
4. For efficiency optimization, a Python program was written to allow testing of various transmission parameters and selecting the best configuration of these parameters. The results of the analysis of the relationship between the eccentricity of the input shaft and the efficiency has been presented in the picture below.
   
<img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/74db0190-bc7f-4ef1-8df9-deb88d459676" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />

5. Finally, the necessary calculations were conducted to select the belt transmission, motors, and electromagnetic brake for locking the position of the low-ratio gearbox input shaft.
   
### 3D Model Development
The 3D model of the device was created using the Autodesk Inventor sofware. The device has been divided into several subcomponents. For every assebly the 3D render of the side view and the crossection has been privided. 
  - The high-speed gearbox drive shaft assembly
    
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/1046461a-4af5-411a-ab54-a70797168f7b" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />

  - The high-torque gearbox drive shaft assembly
    
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/c64957c0-b5ec-4293-b673-f8f5a3926526" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />

  - Automatic transmission assembly
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/d941ebfb-a180-4160-a2a0-b2f98a9ad7e3" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />
    <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/62c8507e-ec45-4b93-8a2a-1485059a9fd0" alt="New_automatic_cycklo_assembly_1" width="550" style="border-radius: 200px;" />

### Making of the prototype
The prototype of the device has been constructed to confirm the required functionality and for establishing the possible use of the cycklidal drive in the automatic transimsion. The components were manufactured in the most parts with my own FDM 3D printer. The commercial components required for this project include bearings, shafts, mounting elements and clutches. 
The prototype was contrlled by 2 stepper motor drivers with custom arduino code. The builing procces and the final version of the prototype has been preseneted in the pictures below. 

- Comapct cycloidal drive before the assebly
  
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/e057688e-1bf3-4fd6-a928-28bf45267a13" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />
  
- The fully assebled actuoator
  
  <img src="https://github.com/majkel808/Engineering_Thesis_Automatic_gearbox_with_seamless_gear_shifting_mechanism_for_robotic_actuator/assets/163661382/84212a52-0caa-4b5e-8a8f-1c4f844fd8ba" alt="New_automatic_cycklo_assembly_1" width="400" style="border-radius: 200px;" />
            


## Technologies 

During the work on this engineering thesis, it was necessary to use various engineering software, including:

- Autodesk Inventor - for developing the 3D model
- AutoCAD - for developing technical documentation
- Ansys Mechanical - for mass optimization of the cycloidal disk
- Python - for calculations related to epicycloid geometry and transmission efficiency optimization

## Documentation

The technical drawing required for manufacturing part has been made in Autodesk AutoCAD. Part would be manufactured via CNC machining, laser cutting and 3D printing. Whole documentation has been providedn in sub-folder of this repository.

## Future Work

This project requires further optimization, particularly in correcting the epicycloidal gearing. Subsequently, further prototype testing would be required, which could be constructed in smaller parts using 3D printing to ensure greater structural rigidity.

## Bibliography
[1]: A. Girard and H. Asada, A two-speed actuator for robotics with fast seamless gear shifting. 2015,
p. 4711. doi: 10.1109/IROS.2015.7354047.
[2] M. Vasić, “A COMPARATIVE CALCULATION OF CYCLOID DRIVE EFFICIENCY,” Mach. Des., Jan.
2020, Accessed: Jul. 10, 2023. [Online]. Available: https://www.academia.edu/79815900/A_COMPARATIVE_CALCULATION_OF_CYCLOID_DRIVE_EFFICIENCY
