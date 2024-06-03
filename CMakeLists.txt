cmake_minimum_required(VERSION 3.28)
project(dualpanto_testing)

set(CMAKE_CXX_STANDARD 14)

include_directories("firmware/haptics/BIS week7 God Object/firmware/include")
include_directories("firmware/haptics/BIS week7 God Object/firmware/include/config")
include_directories("firmware/haptics/BIS week7 God Object/firmware/include/hardware")
include_directories("firmware/haptics/BIS week7 God Object/firmware/include/physics")
include_directories("firmware/haptics/BIS week7 God Object/firmware/include/tasks")
include_directories("firmware/haptics/BIS week7 God Object/firmware/include/utils")
include_directories("firmware/haptics/BIS week7 God Object/utils/protocol/include")
include_directories("firmware/haptics/BIS week7 God Object/utils/protocol/include/protocol")
include_directories("firmware/haptics/BIS week7 God Object/utils/serial/include")
include_directories("firmware/haptics/BIS week7 Kinematics/firmware/include")
include_directories("firmware/haptics/BIS week7 Kinematics/firmware/include/config")
include_directories("firmware/haptics/BIS week7 Kinematics/firmware/include/hardware")
include_directories("firmware/haptics/BIS week7 Kinematics/firmware/include/physics")
include_directories("firmware/haptics/BIS week7 Kinematics/firmware/include/tasks")
include_directories("firmware/haptics/BIS week7 Kinematics/firmware/include/utils")
include_directories("firmware/haptics/BIS week7 Kinematics/utils/protocol/include")
include_directories("firmware/haptics/BIS week7 Kinematics/utils/protocol/include/protocol")
include_directories("firmware/haptics/BIS week7 Kinematics/utils/serial/include")
include_directories("firmware/haptics/force field/firmware/include")
include_directories("firmware/haptics/force field/firmware/include/config")
include_directories("firmware/haptics/force field/firmware/include/hardware")
include_directories("firmware/haptics/force field/firmware/include/physics")
include_directories("firmware/haptics/force field/firmware/include/tasks")
include_directories("firmware/haptics/force field/firmware/include/utils")
include_directories("firmware/haptics/force field/utils/protocol/include")
include_directories("firmware/haptics/force field/utils/protocol/include/protocol")
include_directories("firmware/haptics/force field/utils/serial/include")
include_directories(firmware/haptics/kinematics/firmware/include)
include_directories(firmware/haptics/kinematics/firmware/include/config)
include_directories(firmware/haptics/kinematics/firmware/include/hardware)
include_directories(firmware/haptics/kinematics/firmware/include/physics)
include_directories(firmware/haptics/kinematics/firmware/include/tasks)
include_directories(firmware/haptics/kinematics/firmware/include/utils)
include_directories(firmware/haptics/kinematics/utils/protocol/include)
include_directories(firmware/haptics/kinematics/utils/protocol/include/protocol)
include_directories(firmware/haptics/kinematics/utils/serial/include)
include_directories("firmware/haptics/line wall/firmware/include")
include_directories("firmware/haptics/line wall/firmware/include/config")
include_directories("firmware/haptics/line wall/firmware/include/hardware")
include_directories("firmware/haptics/line wall/firmware/include/physics")
include_directories("firmware/haptics/line wall/firmware/include/tasks")
include_directories("firmware/haptics/line wall/firmware/include/utils")
include_directories("firmware/haptics/line wall/utils/protocol/include")
include_directories("firmware/haptics/line wall/utils/protocol/include/protocol")
include_directories("firmware/haptics/line wall/utils/serial/include")
include_directories(firmware/haptics/template/firmware/include)
include_directories(firmware/haptics/template/firmware/include/config)
include_directories(firmware/haptics/template/firmware/include/hardware)
include_directories(firmware/haptics/template/firmware/include/physics)
include_directories(firmware/haptics/template/firmware/include/tasks)
include_directories(firmware/haptics/template/firmware/include/utils)
include_directories(firmware/haptics/template/utils/protocol/include)
include_directories(firmware/haptics/template/utils/protocol/include/protocol)
include_directories(firmware/haptics/template/utils/serial/include)
include_directories(venv/lib/python3.11/site-packages/numpy/core/include)
include_directories(venv/lib/python3.11/site-packages/numpy/core/include/numpy)
include_directories(venv/lib/python3.11/site-packages/numpy/core/include/numpy/random)
include_directories(venv/lib/python3.11/site-packages/numpy/f2py/src)
include_directories(venv/lib64/python3.11/site-packages/numpy/core/include)
include_directories(venv/lib64/python3.11/site-packages/numpy/core/include/numpy)
include_directories(venv/lib64/python3.11/site-packages/numpy/core/include/numpy/random)
include_directories(venv/lib64/python3.11/site-packages/numpy/f2py/src)

add_executable(dualpanto_testing
        "firmware/haptics/BIS week7 God Object/firmware/include/config/config.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/hardware/angleAccessor.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/hardware/panto.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/hardware/spiCommands.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/hardware/spiEncoder.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/hardware/spiEncoderChain.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/hardware/spiPacket.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/annotatedEdge.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/collider.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/edge.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/godObject.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/godObjectAction.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/godObjectActionData.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/godObjectActionType.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/hashtable.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/indexedEdge.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/obstacle.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/pantoPhysics.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physics/rail.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/tasks/task.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/tasks/taskFunction.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/tasks/taskRegistry.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/assert.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/crashDump.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/framerateLimiter.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/performanceMonitor.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/receiveHandler.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/receiveState.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/serial.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/utils.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/utils/vector.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/ioMain.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/include/physicsMain.hpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/config/config.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/hardware/panto.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/hardware/spiCommands.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/hardware/spiEncoder.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/hardware/spiEncoderChain.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/hardware/spiPacket.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/annotatedEdge.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/collider.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/godObject.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/hashtable.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/indexedEdge.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/obstacle.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/pantoPhysics.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physics/rail.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/tasks/task.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/tasks/taskRegistry.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/utils/crashDump.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/utils/framerateLimiter.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/utils/performanceMonitor.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/utils/serial.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/utils/vector.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/ioMain.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/main.cpp"
        "firmware/haptics/BIS week7 God Object/firmware/src/physicsMain.cpp"
        "firmware/haptics/BIS week7 God Object/utils/protocol/include/protocol/header.hpp"
        "firmware/haptics/BIS week7 God Object/utils/protocol/include/protocol/messageType.hpp"
        "firmware/haptics/BIS week7 God Object/utils/protocol/include/protocol/protocol.hpp"
        "firmware/haptics/BIS week7 God Object/utils/protocol/src/protocol/messageType.cpp"
        "firmware/haptics/BIS week7 God Object/utils/protocol/src/protocol/protocol.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/include/crashAnalyzer.hpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/include/libInterface.hpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/include/node.hpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/include/packet.hpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/include/serial.hpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/include/serial_export.hpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/include/standalone.hpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/cppLib/lib.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/crashAnalyzer/analyze.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/crashAnalyzer/buffer.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/node/main.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/node/poll.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/node/receiveHelpers.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/node/send.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/node/sendHelpers.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/node/setup.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/serial/packet.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/serial/shared.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/serial/unix.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/serial/win.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/standalone/main.cpp"
        "firmware/haptics/BIS week7 God Object/utils/serial/src/standalone/standalone.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/config/config.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/hardware/angleAccessor.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/hardware/panto.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/hardware/spiCommands.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/hardware/spiEncoder.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/hardware/spiEncoderChain.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/hardware/spiPacket.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/annotatedEdge.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/collider.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/edge.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/godObject.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/godObjectAction.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/godObjectActionData.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/godObjectActionType.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/hashtable.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/indexedEdge.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/obstacle.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/pantoPhysics.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physics/rail.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/tasks/task.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/tasks/taskFunction.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/tasks/taskRegistry.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/assert.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/crashDump.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/framerateLimiter.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/performanceMonitor.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/receiveHandler.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/receiveState.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/serial.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/utils.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/utils/vector.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/ioMain.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/include/physicsMain.hpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/config/config.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/hardware/panto.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/hardware/spiCommands.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/hardware/spiEncoder.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/hardware/spiEncoderChain.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/hardware/spiPacket.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/annotatedEdge.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/collider.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/godObject.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/hashtable.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/indexedEdge.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/obstacle.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/pantoPhysics.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physics/rail.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/tasks/task.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/tasks/taskRegistry.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/utils/crashDump.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/utils/framerateLimiter.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/utils/performanceMonitor.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/utils/serial.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/utils/vector.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/ioMain.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/main.cpp"
        "firmware/haptics/BIS week7 Kinematics/firmware/src/physicsMain.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/protocol/include/protocol/header.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/protocol/include/protocol/messageType.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/protocol/include/protocol/protocol.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/protocol/src/protocol/messageType.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/protocol/src/protocol/protocol.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/include/crashAnalyzer.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/include/libInterface.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/include/node.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/include/packet.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/include/serial.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/include/serial_export.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/include/standalone.hpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/cppLib/lib.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/crashAnalyzer/analyze.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/crashAnalyzer/buffer.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/node/main.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/node/poll.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/node/receiveHelpers.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/node/send.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/node/sendHelpers.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/node/setup.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/serial/packet.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/serial/shared.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/serial/unix.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/serial/win.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/standalone/main.cpp"
        "firmware/haptics/BIS week7 Kinematics/utils/serial/src/standalone/standalone.cpp"
        "firmware/haptics/force field/firmware/include/config/config.hpp"
        "firmware/haptics/force field/firmware/include/hardware/angleAccessor.hpp"
        "firmware/haptics/force field/firmware/include/hardware/panto.hpp"
        "firmware/haptics/force field/firmware/include/hardware/spiCommands.hpp"
        "firmware/haptics/force field/firmware/include/hardware/spiEncoder.hpp"
        "firmware/haptics/force field/firmware/include/hardware/spiEncoderChain.hpp"
        "firmware/haptics/force field/firmware/include/hardware/spiPacket.hpp"
        "firmware/haptics/force field/firmware/include/physics/annotatedEdge.hpp"
        "firmware/haptics/force field/firmware/include/physics/collider.hpp"
        "firmware/haptics/force field/firmware/include/physics/edge.hpp"
        "firmware/haptics/force field/firmware/include/physics/godObject.hpp"
        "firmware/haptics/force field/firmware/include/physics/godObjectAction.hpp"
        "firmware/haptics/force field/firmware/include/physics/godObjectActionData.hpp"
        "firmware/haptics/force field/firmware/include/physics/godObjectActionType.hpp"
        "firmware/haptics/force field/firmware/include/physics/hashtable.hpp"
        "firmware/haptics/force field/firmware/include/physics/indexedEdge.hpp"
        "firmware/haptics/force field/firmware/include/physics/obstacle.hpp"
        "firmware/haptics/force field/firmware/include/physics/pantoPhysics.hpp"
        "firmware/haptics/force field/firmware/include/physics/rail.hpp"
        "firmware/haptics/force field/firmware/include/tasks/task.hpp"
        "firmware/haptics/force field/firmware/include/tasks/taskFunction.hpp"
        "firmware/haptics/force field/firmware/include/tasks/taskRegistry.hpp"
        "firmware/haptics/force field/firmware/include/utils/assert.hpp"
        "firmware/haptics/force field/firmware/include/utils/crashDump.hpp"
        "firmware/haptics/force field/firmware/include/utils/framerateLimiter.hpp"
        "firmware/haptics/force field/firmware/include/utils/performanceMonitor.hpp"
        "firmware/haptics/force field/firmware/include/utils/receiveHandler.hpp"
        "firmware/haptics/force field/firmware/include/utils/receiveState.hpp"
        "firmware/haptics/force field/firmware/include/utils/serial.hpp"
        "firmware/haptics/force field/firmware/include/utils/utils.hpp"
        "firmware/haptics/force field/firmware/include/utils/vector.hpp"
        "firmware/haptics/force field/firmware/include/ioMain.hpp"
        "firmware/haptics/force field/firmware/include/physicsMain.hpp"
        "firmware/haptics/force field/firmware/src/config/config.cpp"
        "firmware/haptics/force field/firmware/src/hardware/panto.cpp"
        "firmware/haptics/force field/firmware/src/hardware/spiCommands.cpp"
        "firmware/haptics/force field/firmware/src/hardware/spiEncoder.cpp"
        "firmware/haptics/force field/firmware/src/hardware/spiEncoderChain.cpp"
        "firmware/haptics/force field/firmware/src/hardware/spiPacket.cpp"
        "firmware/haptics/force field/firmware/src/physics/annotatedEdge.cpp"
        "firmware/haptics/force field/firmware/src/physics/collider.cpp"
        "firmware/haptics/force field/firmware/src/physics/godObject.cpp"
        "firmware/haptics/force field/firmware/src/physics/hashtable.cpp"
        "firmware/haptics/force field/firmware/src/physics/indexedEdge.cpp"
        "firmware/haptics/force field/firmware/src/physics/obstacle.cpp"
        "firmware/haptics/force field/firmware/src/physics/pantoPhysics.cpp"
        "firmware/haptics/force field/firmware/src/physics/rail.cpp"
        "firmware/haptics/force field/firmware/src/tasks/task.cpp"
        "firmware/haptics/force field/firmware/src/tasks/taskRegistry.cpp"
        "firmware/haptics/force field/firmware/src/utils/crashDump.cpp"
        "firmware/haptics/force field/firmware/src/utils/framerateLimiter.cpp"
        "firmware/haptics/force field/firmware/src/utils/performanceMonitor.cpp"
        "firmware/haptics/force field/firmware/src/utils/serial.cpp"
        "firmware/haptics/force field/firmware/src/utils/vector.cpp"
        "firmware/haptics/force field/firmware/src/ioMain.cpp"
        "firmware/haptics/force field/firmware/src/main.cpp"
        "firmware/haptics/force field/firmware/src/physicsMain.cpp"
        "firmware/haptics/force field/utils/protocol/include/protocol/header.hpp"
        "firmware/haptics/force field/utils/protocol/include/protocol/messageType.hpp"
        "firmware/haptics/force field/utils/protocol/include/protocol/protocol.hpp"
        "firmware/haptics/force field/utils/protocol/src/protocol/messageType.cpp"
        "firmware/haptics/force field/utils/protocol/src/protocol/protocol.cpp"
        "firmware/haptics/force field/utils/serial/include/crashAnalyzer.hpp"
        "firmware/haptics/force field/utils/serial/include/libInterface.hpp"
        "firmware/haptics/force field/utils/serial/include/node.hpp"
        "firmware/haptics/force field/utils/serial/include/packet.hpp"
        "firmware/haptics/force field/utils/serial/include/serial.hpp"
        "firmware/haptics/force field/utils/serial/include/serial_export.hpp"
        "firmware/haptics/force field/utils/serial/include/standalone.hpp"
        "firmware/haptics/force field/utils/serial/src/cppLib/lib.cpp"
        "firmware/haptics/force field/utils/serial/src/crashAnalyzer/analyze.cpp"
        "firmware/haptics/force field/utils/serial/src/crashAnalyzer/buffer.cpp"
        "firmware/haptics/force field/utils/serial/src/node/main.cpp"
        "firmware/haptics/force field/utils/serial/src/node/poll.cpp"
        "firmware/haptics/force field/utils/serial/src/node/receiveHelpers.cpp"
        "firmware/haptics/force field/utils/serial/src/node/send.cpp"
        "firmware/haptics/force field/utils/serial/src/node/sendHelpers.cpp"
        "firmware/haptics/force field/utils/serial/src/node/setup.cpp"
        "firmware/haptics/force field/utils/serial/src/serial/packet.cpp"
        "firmware/haptics/force field/utils/serial/src/serial/shared.cpp"
        "firmware/haptics/force field/utils/serial/src/serial/unix.cpp"
        "firmware/haptics/force field/utils/serial/src/serial/win.cpp"
        "firmware/haptics/force field/utils/serial/src/standalone/main.cpp"
        "firmware/haptics/force field/utils/serial/src/standalone/standalone.cpp"
        firmware/haptics/kinematics/firmware/include/config/config.hpp
        firmware/haptics/kinematics/firmware/include/hardware/angleAccessor.hpp
        firmware/haptics/kinematics/firmware/include/hardware/panto.hpp
        firmware/haptics/kinematics/firmware/include/hardware/spiCommands.hpp
        firmware/haptics/kinematics/firmware/include/hardware/spiEncoder.hpp
        firmware/haptics/kinematics/firmware/include/hardware/spiEncoderChain.hpp
        firmware/haptics/kinematics/firmware/include/hardware/spiPacket.hpp
        firmware/haptics/kinematics/firmware/include/physics/annotatedEdge.hpp
        firmware/haptics/kinematics/firmware/include/physics/collider.hpp
        firmware/haptics/kinematics/firmware/include/physics/edge.hpp
        firmware/haptics/kinematics/firmware/include/physics/godObject.hpp
        firmware/haptics/kinematics/firmware/include/physics/godObjectAction.hpp
        firmware/haptics/kinematics/firmware/include/physics/godObjectActionData.hpp
        firmware/haptics/kinematics/firmware/include/physics/godObjectActionType.hpp
        firmware/haptics/kinematics/firmware/include/physics/hashtable.hpp
        firmware/haptics/kinematics/firmware/include/physics/indexedEdge.hpp
        firmware/haptics/kinematics/firmware/include/physics/obstacle.hpp
        firmware/haptics/kinematics/firmware/include/physics/pantoPhysics.hpp
        firmware/haptics/kinematics/firmware/include/physics/rail.hpp
        firmware/haptics/kinematics/firmware/include/tasks/task.hpp
        firmware/haptics/kinematics/firmware/include/tasks/taskFunction.hpp
        firmware/haptics/kinematics/firmware/include/tasks/taskRegistry.hpp
        firmware/haptics/kinematics/firmware/include/utils/assert.hpp
        firmware/haptics/kinematics/firmware/include/utils/crashDump.hpp
        firmware/haptics/kinematics/firmware/include/utils/framerateLimiter.hpp
        firmware/haptics/kinematics/firmware/include/utils/performanceMonitor.hpp
        firmware/haptics/kinematics/firmware/include/utils/receiveHandler.hpp
        firmware/haptics/kinematics/firmware/include/utils/receiveState.hpp
        firmware/haptics/kinematics/firmware/include/utils/serial.hpp
        firmware/haptics/kinematics/firmware/include/utils/utils.hpp
        firmware/haptics/kinematics/firmware/include/utils/vector.hpp
        firmware/haptics/kinematics/firmware/include/ioMain.hpp
        firmware/haptics/kinematics/firmware/include/physicsMain.hpp
        firmware/haptics/kinematics/firmware/src/config/config.cpp
        firmware/haptics/kinematics/firmware/src/hardware/panto.cpp
        firmware/haptics/kinematics/firmware/src/hardware/spiCommands.cpp
        firmware/haptics/kinematics/firmware/src/hardware/spiEncoder.cpp
        firmware/haptics/kinematics/firmware/src/hardware/spiEncoderChain.cpp
        firmware/haptics/kinematics/firmware/src/hardware/spiPacket.cpp
        firmware/haptics/kinematics/firmware/src/physics/annotatedEdge.cpp
        firmware/haptics/kinematics/firmware/src/physics/collider.cpp
        firmware/haptics/kinematics/firmware/src/physics/godObject.cpp
        firmware/haptics/kinematics/firmware/src/physics/hashtable.cpp
        firmware/haptics/kinematics/firmware/src/physics/indexedEdge.cpp
        firmware/haptics/kinematics/firmware/src/physics/obstacle.cpp
        firmware/haptics/kinematics/firmware/src/physics/pantoPhysics.cpp
        firmware/haptics/kinematics/firmware/src/physics/rail.cpp
        firmware/haptics/kinematics/firmware/src/tasks/task.cpp
        firmware/haptics/kinematics/firmware/src/tasks/taskRegistry.cpp
        firmware/haptics/kinematics/firmware/src/utils/crashDump.cpp
        firmware/haptics/kinematics/firmware/src/utils/framerateLimiter.cpp
        firmware/haptics/kinematics/firmware/src/utils/performanceMonitor.cpp
        firmware/haptics/kinematics/firmware/src/utils/serial.cpp
        firmware/haptics/kinematics/firmware/src/utils/vector.cpp
        firmware/haptics/kinematics/firmware/src/ioMain.cpp
        firmware/haptics/kinematics/firmware/src/main.cpp
        firmware/haptics/kinematics/firmware/src/physicsMain.cpp
        firmware/haptics/kinematics/utils/protocol/include/protocol/header.hpp
        firmware/haptics/kinematics/utils/protocol/include/protocol/messageType.hpp
        firmware/haptics/kinematics/utils/protocol/include/protocol/protocol.hpp
        firmware/haptics/kinematics/utils/protocol/src/protocol/messageType.cpp
        firmware/haptics/kinematics/utils/protocol/src/protocol/protocol.cpp
        firmware/haptics/kinematics/utils/serial/include/crashAnalyzer.hpp
        firmware/haptics/kinematics/utils/serial/include/libInterface.hpp
        firmware/haptics/kinematics/utils/serial/include/node.hpp
        firmware/haptics/kinematics/utils/serial/include/packet.hpp
        firmware/haptics/kinematics/utils/serial/include/serial.hpp
        firmware/haptics/kinematics/utils/serial/include/serial_export.hpp
        firmware/haptics/kinematics/utils/serial/include/standalone.hpp
        firmware/haptics/kinematics/utils/serial/src/cppLib/lib.cpp
        firmware/haptics/kinematics/utils/serial/src/crashAnalyzer/analyze.cpp
        firmware/haptics/kinematics/utils/serial/src/crashAnalyzer/buffer.cpp
        firmware/haptics/kinematics/utils/serial/src/node/main.cpp
        firmware/haptics/kinematics/utils/serial/src/node/poll.cpp
        firmware/haptics/kinematics/utils/serial/src/node/receiveHelpers.cpp
        firmware/haptics/kinematics/utils/serial/src/node/send.cpp
        firmware/haptics/kinematics/utils/serial/src/node/sendHelpers.cpp
        firmware/haptics/kinematics/utils/serial/src/node/setup.cpp
        firmware/haptics/kinematics/utils/serial/src/serial/packet.cpp
        firmware/haptics/kinematics/utils/serial/src/serial/shared.cpp
        firmware/haptics/kinematics/utils/serial/src/serial/unix.cpp
        firmware/haptics/kinematics/utils/serial/src/serial/win.cpp
        firmware/haptics/kinematics/utils/serial/src/standalone/main.cpp
        firmware/haptics/kinematics/utils/serial/src/standalone/standalone.cpp
        "firmware/haptics/line wall/firmware/include/config/config.hpp"
        "firmware/haptics/line wall/firmware/include/hardware/angleAccessor.hpp"
        "firmware/haptics/line wall/firmware/include/hardware/panto.hpp"
        "firmware/haptics/line wall/firmware/include/hardware/spiCommands.hpp"
        "firmware/haptics/line wall/firmware/include/hardware/spiEncoder.hpp"
        "firmware/haptics/line wall/firmware/include/hardware/spiEncoderChain.hpp"
        "firmware/haptics/line wall/firmware/include/hardware/spiPacket.hpp"
        "firmware/haptics/line wall/firmware/include/physics/annotatedEdge.hpp"
        "firmware/haptics/line wall/firmware/include/physics/collider.hpp"
        "firmware/haptics/line wall/firmware/include/physics/edge.hpp"
        "firmware/haptics/line wall/firmware/include/physics/godObject.hpp"
        "firmware/haptics/line wall/firmware/include/physics/godObjectAction.hpp"
        "firmware/haptics/line wall/firmware/include/physics/godObjectActionData.hpp"
        "firmware/haptics/line wall/firmware/include/physics/godObjectActionType.hpp"
        "firmware/haptics/line wall/firmware/include/physics/hashtable.hpp"
        "firmware/haptics/line wall/firmware/include/physics/indexedEdge.hpp"
        "firmware/haptics/line wall/firmware/include/physics/obstacle.hpp"
        "firmware/haptics/line wall/firmware/include/physics/pantoPhysics.hpp"
        "firmware/haptics/line wall/firmware/include/physics/rail.hpp"
        "firmware/haptics/line wall/firmware/include/tasks/task.hpp"
        "firmware/haptics/line wall/firmware/include/tasks/taskFunction.hpp"
        "firmware/haptics/line wall/firmware/include/tasks/taskRegistry.hpp"
        "firmware/haptics/line wall/firmware/include/utils/assert.hpp"
        "firmware/haptics/line wall/firmware/include/utils/crashDump.hpp"
        "firmware/haptics/line wall/firmware/include/utils/framerateLimiter.hpp"
        "firmware/haptics/line wall/firmware/include/utils/performanceMonitor.hpp"
        "firmware/haptics/line wall/firmware/include/utils/receiveHandler.hpp"
        "firmware/haptics/line wall/firmware/include/utils/receiveState.hpp"
        "firmware/haptics/line wall/firmware/include/utils/serial.hpp"
        "firmware/haptics/line wall/firmware/include/utils/utils.hpp"
        "firmware/haptics/line wall/firmware/include/utils/vector.hpp"
        "firmware/haptics/line wall/firmware/include/ioMain.hpp"
        "firmware/haptics/line wall/firmware/include/physicsMain.hpp"
        "firmware/haptics/line wall/firmware/src/config/config.cpp"
        "firmware/haptics/line wall/firmware/src/hardware/panto.cpp"
        "firmware/haptics/line wall/firmware/src/hardware/spiCommands.cpp"
        "firmware/haptics/line wall/firmware/src/hardware/spiEncoder.cpp"
        "firmware/haptics/line wall/firmware/src/hardware/spiEncoderChain.cpp"
        "firmware/haptics/line wall/firmware/src/hardware/spiPacket.cpp"
        "firmware/haptics/line wall/firmware/src/physics/annotatedEdge.cpp"
        "firmware/haptics/line wall/firmware/src/physics/collider.cpp"
        "firmware/haptics/line wall/firmware/src/physics/godObject.cpp"
        "firmware/haptics/line wall/firmware/src/physics/hashtable.cpp"
        "firmware/haptics/line wall/firmware/src/physics/indexedEdge.cpp"
        "firmware/haptics/line wall/firmware/src/physics/obstacle.cpp"
        "firmware/haptics/line wall/firmware/src/physics/pantoPhysics.cpp"
        "firmware/haptics/line wall/firmware/src/physics/rail.cpp"
        "firmware/haptics/line wall/firmware/src/tasks/task.cpp"
        "firmware/haptics/line wall/firmware/src/tasks/taskRegistry.cpp"
        "firmware/haptics/line wall/firmware/src/utils/crashDump.cpp"
        "firmware/haptics/line wall/firmware/src/utils/framerateLimiter.cpp"
        "firmware/haptics/line wall/firmware/src/utils/performanceMonitor.cpp"
        "firmware/haptics/line wall/firmware/src/utils/serial.cpp"
        "firmware/haptics/line wall/firmware/src/utils/vector.cpp"
        "firmware/haptics/line wall/firmware/src/ioMain.cpp"
        "firmware/haptics/line wall/firmware/src/main.cpp"
        "firmware/haptics/line wall/firmware/src/physicsMain.cpp"
        "firmware/haptics/line wall/utils/protocol/include/protocol/header.hpp"
        "firmware/haptics/line wall/utils/protocol/include/protocol/messageType.hpp"
        "firmware/haptics/line wall/utils/protocol/include/protocol/protocol.hpp"
        "firmware/haptics/line wall/utils/protocol/src/protocol/messageType.cpp"
        "firmware/haptics/line wall/utils/protocol/src/protocol/protocol.cpp"
        "firmware/haptics/line wall/utils/serial/include/crashAnalyzer.hpp"
        "firmware/haptics/line wall/utils/serial/include/libInterface.hpp"
        "firmware/haptics/line wall/utils/serial/include/node.hpp"
        "firmware/haptics/line wall/utils/serial/include/packet.hpp"
        "firmware/haptics/line wall/utils/serial/include/serial.hpp"
        "firmware/haptics/line wall/utils/serial/include/serial_export.hpp"
        "firmware/haptics/line wall/utils/serial/include/standalone.hpp"
        "firmware/haptics/line wall/utils/serial/src/cppLib/lib.cpp"
        "firmware/haptics/line wall/utils/serial/src/crashAnalyzer/analyze.cpp"
        "firmware/haptics/line wall/utils/serial/src/crashAnalyzer/buffer.cpp"
        "firmware/haptics/line wall/utils/serial/src/node/main.cpp"
        "firmware/haptics/line wall/utils/serial/src/node/poll.cpp"
        "firmware/haptics/line wall/utils/serial/src/node/receiveHelpers.cpp"
        "firmware/haptics/line wall/utils/serial/src/node/send.cpp"
        "firmware/haptics/line wall/utils/serial/src/node/sendHelpers.cpp"
        "firmware/haptics/line wall/utils/serial/src/node/setup.cpp"
        "firmware/haptics/line wall/utils/serial/src/serial/packet.cpp"
        "firmware/haptics/line wall/utils/serial/src/serial/shared.cpp"
        "firmware/haptics/line wall/utils/serial/src/serial/unix.cpp"
        "firmware/haptics/line wall/utils/serial/src/serial/win.cpp"
        "firmware/haptics/line wall/utils/serial/src/standalone/main.cpp"
        "firmware/haptics/line wall/utils/serial/src/standalone/standalone.cpp"
        firmware/haptics/template/firmware/include/config/config.hpp
        firmware/haptics/template/firmware/include/hardware/angleAccessor.hpp
        firmware/haptics/template/firmware/include/hardware/panto.hpp
        firmware/haptics/template/firmware/include/hardware/spiCommands.hpp
        firmware/haptics/template/firmware/include/hardware/spiEncoder.hpp
        firmware/haptics/template/firmware/include/hardware/spiEncoderChain.hpp
        firmware/haptics/template/firmware/include/hardware/spiPacket.hpp
        firmware/haptics/template/firmware/include/physics/annotatedEdge.hpp
        firmware/haptics/template/firmware/include/physics/collider.hpp
        firmware/haptics/template/firmware/include/physics/edge.hpp
        firmware/haptics/template/firmware/include/physics/godObject.hpp
        firmware/haptics/template/firmware/include/physics/godObjectAction.hpp
        firmware/haptics/template/firmware/include/physics/godObjectActionData.hpp
        firmware/haptics/template/firmware/include/physics/godObjectActionType.hpp
        firmware/haptics/template/firmware/include/physics/hashtable.hpp
        firmware/haptics/template/firmware/include/physics/indexedEdge.hpp
        firmware/haptics/template/firmware/include/physics/obstacle.hpp
        firmware/haptics/template/firmware/include/physics/pantoPhysics.hpp
        firmware/haptics/template/firmware/include/physics/rail.hpp
        firmware/haptics/template/firmware/include/tasks/task.hpp
        firmware/haptics/template/firmware/include/tasks/taskFunction.hpp
        firmware/haptics/template/firmware/include/tasks/taskRegistry.hpp
        firmware/haptics/template/firmware/include/utils/assert.hpp
        firmware/haptics/template/firmware/include/utils/crashDump.hpp
        firmware/haptics/template/firmware/include/utils/framerateLimiter.hpp
        firmware/haptics/template/firmware/include/utils/performanceMonitor.hpp
        firmware/haptics/template/firmware/include/utils/receiveHandler.hpp
        firmware/haptics/template/firmware/include/utils/receiveState.hpp
        firmware/haptics/template/firmware/include/utils/serial.hpp
        firmware/haptics/template/firmware/include/utils/utils.hpp
        firmware/haptics/template/firmware/include/utils/vector.hpp
        firmware/haptics/template/firmware/include/ioMain.hpp
        firmware/haptics/template/firmware/include/physicsMain.hpp
        firmware/haptics/template/firmware/src/config/config.cpp
        firmware/haptics/template/firmware/src/hardware/panto.cpp
        firmware/haptics/template/firmware/src/hardware/spiCommands.cpp
        firmware/haptics/template/firmware/src/hardware/spiEncoder.cpp
        firmware/haptics/template/firmware/src/hardware/spiEncoderChain.cpp
        firmware/haptics/template/firmware/src/hardware/spiPacket.cpp
        firmware/haptics/template/firmware/src/physics/annotatedEdge.cpp
        firmware/haptics/template/firmware/src/physics/collider.cpp
        firmware/haptics/template/firmware/src/physics/godObject.cpp
        firmware/haptics/template/firmware/src/physics/hashtable.cpp
        firmware/haptics/template/firmware/src/physics/indexedEdge.cpp
        firmware/haptics/template/firmware/src/physics/obstacle.cpp
        firmware/haptics/template/firmware/src/physics/pantoPhysics.cpp
        firmware/haptics/template/firmware/src/physics/rail.cpp
        firmware/haptics/template/firmware/src/tasks/task.cpp
        firmware/haptics/template/firmware/src/tasks/taskRegistry.cpp
        firmware/haptics/template/firmware/src/utils/crashDump.cpp
        firmware/haptics/template/firmware/src/utils/framerateLimiter.cpp
        firmware/haptics/template/firmware/src/utils/performanceMonitor.cpp
        firmware/haptics/template/firmware/src/utils/serial.cpp
        firmware/haptics/template/firmware/src/utils/vector.cpp
        firmware/haptics/template/firmware/src/ioMain.cpp
        firmware/haptics/template/firmware/src/main.cpp
        firmware/haptics/template/firmware/src/physicsMain.cpp
        firmware/haptics/template/utils/protocol/include/protocol/header.hpp
        firmware/haptics/template/utils/protocol/include/protocol/messageType.hpp
        firmware/haptics/template/utils/protocol/include/protocol/protocol.hpp
        firmware/haptics/template/utils/protocol/src/protocol/messageType.cpp
        firmware/haptics/template/utils/protocol/src/protocol/protocol.cpp
        firmware/haptics/template/utils/serial/include/crashAnalyzer.hpp
        firmware/haptics/template/utils/serial/include/libInterface.hpp
        firmware/haptics/template/utils/serial/include/node.hpp
        firmware/haptics/template/utils/serial/include/packet.hpp
        firmware/haptics/template/utils/serial/include/serial.hpp
        firmware/haptics/template/utils/serial/include/serial_export.hpp
        firmware/haptics/template/utils/serial/include/standalone.hpp
        firmware/haptics/template/utils/serial/src/cppLib/lib.cpp
        firmware/haptics/template/utils/serial/src/crashAnalyzer/analyze.cpp
        firmware/haptics/template/utils/serial/src/crashAnalyzer/buffer.cpp
        firmware/haptics/template/utils/serial/src/node/main.cpp
        firmware/haptics/template/utils/serial/src/node/poll.cpp
        firmware/haptics/template/utils/serial/src/node/receiveHelpers.cpp
        firmware/haptics/template/utils/serial/src/node/send.cpp
        firmware/haptics/template/utils/serial/src/node/sendHelpers.cpp
        firmware/haptics/template/utils/serial/src/node/setup.cpp
        firmware/haptics/template/utils/serial/src/serial/packet.cpp
        firmware/haptics/template/utils/serial/src/serial/shared.cpp
        firmware/haptics/template/utils/serial/src/serial/unix.cpp
        firmware/haptics/template/utils/serial/src/serial/win.cpp
        firmware/haptics/template/utils/serial/src/standalone/main.cpp
        firmware/haptics/template/utils/serial/src/standalone/standalone.cpp
        "firmware/hardware/#example/00 template/src/main.cpp"
        "firmware/hardware/#example/02 echo/src/main.cpp"
        "firmware/hardware/linkage encoder/src/main.cpp"
        "firmware/hardware/linkage motor/src/main.cpp"
        "firmware/hardware/linkage sync/src/main.cpp"
        "firmware/hello world/src/main.cpp"
        venv/lib/python3.11/site-packages/fontTools/cu2qu/cu2qu.c
        venv/lib/python3.11/site-packages/fontTools/feaLib/lexer.c
        venv/lib/python3.11/site-packages/fontTools/misc/bezierTools.c
        venv/lib/python3.11/site-packages/fontTools/pens/momentsPen.c
        venv/lib/python3.11/site-packages/fontTools/qu2cu/qu2cu.c
        venv/lib/python3.11/site-packages/fontTools/varLib/iup.c
        venv/lib/python3.11/site-packages/markupsafe/_speedups.c
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/random/bitgen.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/random/distributions.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/random/libdivide.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/__multiarray_api.c
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/__multiarray_api.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/__ufunc_api.c
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/__ufunc_api.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/_dtype_api.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/_numpyconfig.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/arrayobject.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/arrayscalars.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/experimental_dtype_api.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/halffloat.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/ndarrayobject.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/ndarraytypes.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/noprefix.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_3kcompat.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_common.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_cpu.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_endian.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_interrupt.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_math.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/npy_os.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/numpyconfig.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/old_defines.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/ufuncobject.h
        venv/lib/python3.11/site-packages/numpy/core/include/numpy/utils.h
        venv/lib/python3.11/site-packages/numpy/core/tests/data/generate_umath_validation_data.cpp
        venv/lib/python3.11/site-packages/numpy/core/tests/examples/limited_api/limited_api.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimd.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimddp.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimdfhm.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_asimdhp.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx2.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_clx.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_cnl.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_icl.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_knl.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_knm.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_skx.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_spr.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512cd.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_avx512f.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_f16c.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_fma3.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_fma4.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_neon.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_neon_fp16.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_neon_vfpv4.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_popcnt.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse2.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse3.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse41.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_sse42.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_ssse3.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx2.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx3.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vsx4.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vx.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vxe.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_vxe2.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/cpu_xop.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_avx512bw_mask.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_avx512dq_mask.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_avx512f_reduce.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_vsx3_half_double.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_vsx4_mma.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/extra_vsx_asm.c
        venv/lib/python3.11/site-packages/numpy/distutils/checks/test_flags.c
        venv/lib/python3.11/site-packages/numpy/distutils/mingw/gfortran_vs2003_hack.c
        venv/lib/python3.11/site-packages/numpy/f2py/src/fortranobject.c
        venv/lib/python3.11/site-packages/numpy/f2py/src/fortranobject.h
        venv/lib/python3.11/site-packages/numpy/f2py/tests/src/array_from_pyobj/wrapmodule.c
        venv/lib64/python3.11/site-packages/fontTools/cu2qu/cu2qu.c
        venv/lib64/python3.11/site-packages/fontTools/feaLib/lexer.c
        venv/lib64/python3.11/site-packages/fontTools/misc/bezierTools.c
        venv/lib64/python3.11/site-packages/fontTools/pens/momentsPen.c
        venv/lib64/python3.11/site-packages/fontTools/qu2cu/qu2cu.c
        venv/lib64/python3.11/site-packages/fontTools/varLib/iup.c
        venv/lib64/python3.11/site-packages/markupsafe/_speedups.c
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/random/bitgen.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/random/distributions.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/random/libdivide.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/__multiarray_api.c
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/__multiarray_api.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/__ufunc_api.c
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/__ufunc_api.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/_dtype_api.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/_numpyconfig.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/arrayobject.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/arrayscalars.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/experimental_dtype_api.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/halffloat.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/ndarrayobject.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/ndarraytypes.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/noprefix.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_3kcompat.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_common.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_cpu.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_endian.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_interrupt.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_math.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/npy_os.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/numpyconfig.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/old_defines.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/ufuncobject.h
        venv/lib64/python3.11/site-packages/numpy/core/include/numpy/utils.h
        venv/lib64/python3.11/site-packages/numpy/core/tests/data/generate_umath_validation_data.cpp
        venv/lib64/python3.11/site-packages/numpy/core/tests/examples/limited_api/limited_api.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_asimd.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_asimddp.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_asimdfhm.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_asimdhp.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx2.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_clx.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_cnl.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_icl.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_knl.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_knm.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_skx.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512_spr.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512cd.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_avx512f.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_f16c.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_fma3.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_fma4.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_neon.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_neon_fp16.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_neon_vfpv4.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_popcnt.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_sse.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_sse2.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_sse3.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_sse41.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_sse42.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_ssse3.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_vsx.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_vsx2.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_vsx3.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_vsx4.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_vx.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_vxe.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_vxe2.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/cpu_xop.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/extra_avx512bw_mask.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/extra_avx512dq_mask.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/extra_avx512f_reduce.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/extra_vsx3_half_double.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/extra_vsx4_mma.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/extra_vsx_asm.c
        venv/lib64/python3.11/site-packages/numpy/distutils/checks/test_flags.c
        venv/lib64/python3.11/site-packages/numpy/distutils/mingw/gfortran_vs2003_hack.c
        venv/lib64/python3.11/site-packages/numpy/f2py/src/fortranobject.c
        venv/lib64/python3.11/site-packages/numpy/f2py/src/fortranobject.h
        venv/lib64/python3.11/site-packages/numpy/f2py/tests/src/array_from_pyobj/wrapmodule.c)
