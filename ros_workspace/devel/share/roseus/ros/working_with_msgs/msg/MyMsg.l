;; Auto-generated. Do not edit!


(when (boundp 'working_with_msgs::MyMsg)
  (if (not (find-package "WORKING_WITH_MSGS"))
    (make-package "WORKING_WITH_MSGS"))
  (shadow 'MyMsg (find-package "WORKING_WITH_MSGS")))
(unless (find-package "WORKING_WITH_MSGS::MYMSG")
  (make-package "WORKING_WITH_MSGS::MYMSG"))

(in-package "ROS")
;;//! \htmlinclude MyMsg.msg.html


(defclass working_with_msgs::MyMsg
  :super ros::object
  :slots (_id _message ))

(defmethod working_with_msgs::MyMsg
  (:init
   (&key
    ((:id __id) 0)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _message (string __message))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; uint8 _id
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _id
       (write-byte _id s)
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _id
     (setq _id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get working_with_msgs::MyMsg :md5sum-) "073ce03da3ba6ba2c19723384f1df5d4")
(setf (get working_with_msgs::MyMsg :datatype-) "working_with_msgs/MyMsg")
(setf (get working_with_msgs::MyMsg :definition-)
      "uint8 id
string message
")



(provide :working_with_msgs/MyMsg "073ce03da3ba6ba2c19723384f1df5d4")


