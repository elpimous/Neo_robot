
(cl:in-package :asdf)

(defsystem "qbo_object_recognition-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "Update" :depends-on ("_package_Update"))
    (:file "_package_Update" :depends-on ("_package"))
    (:file "Teach" :depends-on ("_package_Teach"))
    (:file "_package_Teach" :depends-on ("_package"))
    (:file "RecognizeObjectInputImage" :depends-on ("_package_RecognizeObjectInputImage"))
    (:file "_package_RecognizeObjectInputImage" :depends-on ("_package"))
    (:file "LearnNewObject" :depends-on ("_package_LearnNewObject"))
    (:file "_package_LearnNewObject" :depends-on ("_package"))
    (:file "RecognizeObject" :depends-on ("_package_RecognizeObject"))
    (:file "_package_RecognizeObject" :depends-on ("_package"))
  ))