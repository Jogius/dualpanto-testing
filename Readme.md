# Dualpanto Testing

The goal of this repository is to provide (semi) automatic testing for the dualpanto platform. This involves basic functionality checks of the hardware, the haptic rendering and the unity integration.

This project is work-in-progress. Welcome you to contribute.
### For BIS participants
Please check [BIS.md](BIS/BIS.md) first.


## Requirements
### Install the ESP32 driver
- [Download](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads) the installer for your OS-Version.
- Run the installer.

### Install IDE
We highly recommend to use PyCharm to run this test flow.
#### PyCharm
1. download [PyCharm](https://www.jetbrains.com/community/education/#students)
2. clone this repo and open it with pycharm
3. [create vertial environment (we use python 3.7)](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)and [install package using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)
4. install [Mermaid](https://plugins.jetbrains.com/plugin/20146-mermaid) plugin for flowchart vis
5. follow Test Flow section

you can run  unittest from Markdown preview (or [execute unittest from scripts](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#create-test))



#### VScode
1. download [VScode](https://code.visualstudio.com/)
2. clone this repo and open it with VScode
3. [set venv and install package using requirements.txt](https://code.visualstudio.com/docs/python/environments)
4. follow Test Flow section

#### Command Line
you can also run all unittest from command line interface if you want.

# Test Flow
Most of the test is not semi-automated since they are related to haptics and mechanical issue. Check `How to test?`.


## Configurate test flow

1. open `config.py` and enter your ESP port.
2. when you upload a firmware, you probably need to push button back of dualpanto (it depends on OS).
![swith](./resources/dualpanto_switch.jpg)
   
## 1. Mechanical and Hardware

0.  [check mechanical configuration](physical_test%2Fmechanical_issue_check_list.md)
1. `python -m unittest test_firmware.Basic`
2. `python -m unittest test_hardware.Linkage.test_encoder`[How to test?]()
3. `python -m unittest test_hardware.Linkage.test_sync`[How to test?]()
4. `python -m unittest test_hardware.EndEffector.test_encoder` **WIP**
5. `python -m unittest test_hardware.EndEffector.test_motor` **WIP**

```mermaid
%%{init: {'theme': 'neutral' } }%%
flowchart TD;
    ST((start)) --> MC[0.mechanical];
    MC -- checked --> FB;
    
    subgraph  test_firmware
    FB[1.Basic];
    FB -- not work --> CH(check USB connection, <br> COM port and <br> platformIO  properly installed)
    CH -- no idea --> TA0((Ask TA))
    end
    
    FB -- work -->  LTE[2.test_Encoder]

    subgraph test_hardware.Linkage
    LTE -- work -->LTS[3.test_sync];
    LTE-- not work -->  MC1[check mechanical again]
    LTS -- not work --> MC1
    MC1 -- no idea --> TA1((Ask TA))
    end
    
    subgraph test_hardware.EndEffector
    LTS -- work --> EETE[4.test_encoder]
    EETE -- work --> EETM[5.test_motor]
    EETM -- not work -->MC2
    EETM -- work --> DONE((done))
    EETE -- not work --> MC2[check mechanical again]
    MC2 -- no idea --> TA2((Ask TA))
    end
    
    style TA0 fill:#FF9B00
    style TA1 fill:#FF9B00
    style TA2 fill:#FF9B00
    style DONE fill:#99CC00
    
    click LE "https://github.com/HassoPlattnerInstituteHCI/unity-dualpanto-toolkit/blob/develop/README.md"
    click TA "https://discord.com"
    click MC "https://discord.com"
```

## 2. Rendering Haptics = DualPanto Firmware

0. [check mechanical configuration](physical_test/mechanical.md)
1. `python -m unittest test_firmware.Haptics.test_line_wall` [How to test?]()
2. `python -m unittest test_firmware.Haptics.test_force_field` **WIP**
3. `python -m unittest test_firmware.Haptics.test_rail` **WIP**
4. `python -m unittest test_firmware.Haptics.test_rectangle_obstacle` **WIP**
5. `python -m unittest test_firmware.Haptics.test_diamond_obstacle` **WIP**
6. `python -m unittest test_firmware.Haptics.test_moving_obstacle` **WIP**
7. `python -m unittest test_firmware.Kinematics.test_forward` **WIP**
8. `python -m unittest test_firmware.Kinematics.test_inverse` **WIP**
9.  (WIP: mathing it and me's rocation for each dualpanto) 


## 3. Communication between DualPanto and PC

**WIP**

## 4. Unity (Communication between DualPanto and Unity)

**WIP**

## Development
This project is currenty under developement. 
For questions, please reach out to martin.taraz@hpi.de, shohei.katakura@hpi.de

For BIS students, please reach out shohei.katakura@hpi.de