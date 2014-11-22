FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/qbo_arduqbo/msg"
  "../src/qbo_arduqbo/srv"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/qbo_arduqbo/HeadPose.h"
  "../msg_gen/cpp/include/qbo_arduqbo/motor_state.h"
  "../msg_gen/cpp/include/qbo_arduqbo/BatteryLevel.h"
  "../msg_gen/cpp/include/qbo_arduqbo/Irs.h"
  "../msg_gen/cpp/include/qbo_arduqbo/LCD.h"
  "../msg_gen/cpp/include/qbo_arduqbo/Expression.h"
  "../msg_gen/cpp/include/qbo_arduqbo/NoiseLevels.h"
  "../msg_gen/cpp/include/qbo_arduqbo/Nose.h"
  "../msg_gen/cpp/include/qbo_arduqbo/Mic.h"
  "../msg_gen/cpp/include/qbo_arduqbo/Mouth.h"
  "../msg_gen/cpp/include/qbo_arduqbo/EyesPositions.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
