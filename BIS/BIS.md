# BIS

We use this dualpanto-testing repo for assignment, and uploading dualpanto firmware too.

**Please check and install all requirements at [Readme.md](../Readme.md)**


## Assignment Week7: rendering wall
Assignment for Week7 is to write code of god objeect partially, and get familiar with uploading firmware and this testing work flow.

1. make sure install ESP32 driver, IDE, and all python library on requirements.txt
2. go to `dualpant-testing/firmware/haptics/BIS week7/src`,find TODO and write code
3. `python -m unittest test_firmware.Haptics.test_BIS_week7`
4. if you feel the device has issue, follow [test flow (Mechanics and Hardware)](../Readme.md)
5. take the video that you interacts with rendered wall

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
