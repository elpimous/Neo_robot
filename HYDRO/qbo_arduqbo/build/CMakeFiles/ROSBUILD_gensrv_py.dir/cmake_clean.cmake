FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/qbo_arduqbo/msg"
  "../src/qbo_arduqbo/srv"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/qbo_arduqbo/srv/__init__.py"
  "../src/qbo_arduqbo/srv/_BaseStop.py"
  "../src/qbo_arduqbo/srv/_Test.py"
  "../src/qbo_arduqbo/srv/_TorqueEnable.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
