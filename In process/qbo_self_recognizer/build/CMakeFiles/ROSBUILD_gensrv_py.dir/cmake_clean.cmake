FILE(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/qbo_self_recognizer/srv"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/qbo_self_recognizer/srv/__init__.py"
  "../src/qbo_self_recognizer/srv/_QboRecognize.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
