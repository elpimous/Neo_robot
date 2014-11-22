FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/qbo_arduqbo/msg"
  "../src/qbo_arduqbo/srv"
  "CMakeFiles/rospack_gensrv"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/rospack_gensrv.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
