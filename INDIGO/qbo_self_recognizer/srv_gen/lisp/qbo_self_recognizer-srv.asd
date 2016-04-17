
(cl:in-package :asdf)

(defsystem "qbo_self_recognizer-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "QboRecognize" :depends-on ("_package_QboRecognize"))
    (:file "_package_QboRecognize" :depends-on ("_package"))
  ))