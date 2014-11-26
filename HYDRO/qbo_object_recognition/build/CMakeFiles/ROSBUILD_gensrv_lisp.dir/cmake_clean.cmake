FILE(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/qbo_object_recognition/srv"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/Update.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_Update.lisp"
  "../srv_gen/lisp/Teach.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_Teach.lisp"
  "../srv_gen/lisp/RecognizeObjectInputImage.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_RecognizeObjectInputImage.lisp"
  "../srv_gen/lisp/LearnNewObject.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_LearnNewObject.lisp"
  "../srv_gen/lisp/RecognizeObject.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_RecognizeObject.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
