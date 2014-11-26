FILE(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/qbo_object_recognition/srv"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/qbo_object_recognition/Update.h"
  "../srv_gen/cpp/include/qbo_object_recognition/Teach.h"
  "../srv_gen/cpp/include/qbo_object_recognition/RecognizeObjectInputImage.h"
  "../srv_gen/cpp/include/qbo_object_recognition/LearnNewObject.h"
  "../srv_gen/cpp/include/qbo_object_recognition/RecognizeObject.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
