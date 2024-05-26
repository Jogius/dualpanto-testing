# BIS

We use this dualpanto-testing repo for assignment, and uploading dualpanto firmware too.

**Please check and install all requirements at [Readme.md](../Readme.md)**

If you have issue about installing all requirements and this testing tool, **please first ask on discord #general channel.**
Often other students have already solved issue you have. (with 60 students in 2024, there's a good chance they have solved it)



## Assignment Week7: kinematics and rendering wall
Assignment for Week7 is to write code of god object and kinematics partially, and (mainly) get familiar with uploading firmware and this testing work flow since we use the test flow a lot from this week.

We have two coding assignment this week:
### #1 kinematics


1. make sure install ESP32 driver, IDE, and all python library on requirements.txt
2. go to `dualpant-testing/firmware/haptics/BIS week7 Kinematics/firmware/src/hardware/panto.cpp`,find `TODO BIS` and write code
3. `python -m unittest test_firmware.Haptics.test_BIS_week7_kinematics`
4. if you feel the device has issue, follow [test flow (Mechanics and Hardware)](../Readme.md)
5. take the video that linkage is synced when you intearct with ME handle.
6. and upload to dokuwiki project page

### #2 rendering wall
TODO: Given a position of god-object and the position of the handle, calculate rendering force.

1. make sure install ESP32 driver, IDE, and all python library on requirements.txt
2. go to `dualpant-testing/firmware/haptics/BIS week7 God Object/firmware/src/physics/godObject.cpp`,find `TODO BIS` and write code
3. `python -m unittest test_firmware.Haptics.test_BIS_week7_go`
4. if you feel the device has issue, follow [test flow (Mechanics and Hardware)](../Readme.md)
5. take the video that you interacts with rendered wall
6. and upload to dokuwiki project page


## Assignment Week8: 
**WIP**

## Uploading DualpantoFramework
From Week9, we will develop dualpanto app. sometimes you want to upload dualpanto famework again and again when...

1. you update dualpanto framework (e.g. you tune PID)
2. you plug dualpanto device into different PC
    - we observe dualpanto has some wall rendering issue when you connect dualpanto to other PC. e.g, you uplaod firmware from mac and connect to windows pc.
    - this is not always happend. but You need to keep this in mind.
    - We haven't known why so. Welcome you to contribute here!

`python -m unittest test_firmware.UploadDualpantoFrameowrk.test_upload_dp_firmware`
