FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/qbo_arduqbo/msg"
  "../src/qbo_arduqbo/srv"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/qbo_arduqbo/msg/__init__.py"
  "../src/qbo_arduqbo/msg/_HeadPose.py"
  "../src/qbo_arduqbo/msg/_motor_state.py"
  "../src/qbo_arduqbo/msg/_BatteryLevel.py"
  "../src/qbo_arduqbo/msg/_Irs.py"
  "../src/qbo_arduqbo/msg/_LCD.py"
  "../src/qbo_arduqbo/msg/_Expression.py"
  "../src/qbo_arduqbo/msg/_NoiseLevels.py"
  "../src/qbo_arduqbo/msg/_Nose.py"
  "../src/qbo_arduqbo/msg/_Mic.py"
  "../src/qbo_arduqbo/msg/_Mouth.py"
  "../src/qbo_arduqbo/msg/_EyesPositions.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
