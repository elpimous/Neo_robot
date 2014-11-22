FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/qbo_arduqbo/msg"
  "../src/qbo_arduqbo/srv"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/qbo_arduqbo/BaseStop.h"
  "../srv_gen/cpp/include/qbo_arduqbo/Test.h"
  "../srv_gen/cpp/include/qbo_arduqbo/TorqueEnable.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
