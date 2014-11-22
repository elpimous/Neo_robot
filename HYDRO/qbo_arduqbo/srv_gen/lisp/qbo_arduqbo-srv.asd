
(cl:in-package :asdf)

(defsystem "qbo_arduqbo-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BaseStop" :depends-on ("_package_BaseStop"))
    (:file "_package_BaseStop" :depends-on ("_package"))
    (:file "Test" :depends-on ("_package_Test"))
    (:file "_package_Test" :depends-on ("_package"))
    (:file "TorqueEnable" :depends-on ("_package_TorqueEnable"))
    (:file "_package_TorqueEnable" :depends-on ("_package"))
  ))