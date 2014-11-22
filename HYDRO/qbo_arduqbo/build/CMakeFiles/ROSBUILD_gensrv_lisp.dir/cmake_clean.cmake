FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/qbo_arduqbo/msg"
  "../src/qbo_arduqbo/srv"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/BaseStop.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_BaseStop.lisp"
  "../srv_gen/lisp/Test.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_Test.lisp"
  "../srv_gen/lisp/TorqueEnable.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_TorqueEnable.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
