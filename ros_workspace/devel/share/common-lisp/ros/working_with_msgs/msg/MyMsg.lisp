; Auto-generated. Do not edit!


(cl:in-package working_with_msgs-msg)


;//! \htmlinclude MyMsg.msg.html

(cl:defclass <MyMsg> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:fixnum
    :initform 0)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass MyMsg (<MyMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MyMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MyMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name working_with_msgs-msg:<MyMsg> is deprecated: use working_with_msgs-msg:MyMsg instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <MyMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader working_with_msgs-msg:id-val is deprecated.  Use working_with_msgs-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <MyMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader working_with_msgs-msg:message-val is deprecated.  Use working_with_msgs-msg:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MyMsg>) ostream)
  "Serializes a message object of type '<MyMsg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MyMsg>) istream)
  "Deserializes a message object of type '<MyMsg>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MyMsg>)))
  "Returns string type for a message object of type '<MyMsg>"
  "working_with_msgs/MyMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MyMsg)))
  "Returns string type for a message object of type 'MyMsg"
  "working_with_msgs/MyMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MyMsg>)))
  "Returns md5sum for a message object of type '<MyMsg>"
  "073ce03da3ba6ba2c19723384f1df5d4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MyMsg)))
  "Returns md5sum for a message object of type 'MyMsg"
  "073ce03da3ba6ba2c19723384f1df5d4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MyMsg>)))
  "Returns full string definition for message of type '<MyMsg>"
  (cl:format cl:nil "uint8 id~%string message~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MyMsg)))
  "Returns full string definition for message of type 'MyMsg"
  (cl:format cl:nil "uint8 id~%string message~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MyMsg>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MyMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'MyMsg
    (cl:cons ':id (id msg))
    (cl:cons ':message (message msg))
))
