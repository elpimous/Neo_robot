FILE(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/qbo_object_recognition/srv"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/qbo_object_recognition/srv/__init__.py"
  "../src/qbo_object_recognition/srv/_Update.py"
  "../src/qbo_object_recognition/srv/_Teach.py"
  "../src/qbo_object_recognition/srv/_RecognizeObjectInputImage.py"
  "../src/qbo_object_recognition/srv/_LearnNewObject.py"
  "../src/qbo_object_recognition/srv/_RecognizeObject.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
