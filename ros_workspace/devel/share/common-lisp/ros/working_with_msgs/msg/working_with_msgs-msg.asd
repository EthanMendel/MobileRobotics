
(cl:in-package :asdf)

(defsystem "working_with_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MyMsg" :depends-on ("_package_MyMsg"))
    (:file "_package_MyMsg" :depends-on ("_package"))
  ))