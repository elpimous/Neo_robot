
(cl:in-package :asdf)

(defsystem "qbo_system_info-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AskInfo" :depends-on ("_package_AskInfo"))
    (:file "_package_AskInfo" :depends-on ("_package"))
  ))