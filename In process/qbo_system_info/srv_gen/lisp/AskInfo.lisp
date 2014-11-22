; Auto-generated. Do not edit!


(cl:in-package qbo_system_info-srv)


;//! \htmlinclude AskInfo-request.msg.html

(cl:defclass <AskInfo-request> (roslisp-msg-protocol:ros-message)
  ((command
    :reader command
    :initarg :command
    :type cl:string
    :initform ""))
)

(cl:defclass AskInfo-request (<AskInfo-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AskInfo-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AskInfo-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_system_info-srv:<AskInfo-request> is deprecated: use qbo_system_info-srv:AskInfo-request instead.")))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <AskInfo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_system_info-srv:command-val is deprecated.  Use qbo_system_info-srv:command instead.")
  (command m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AskInfo-request>) ostream)
  "Serializes a message object of type '<AskInfo-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AskInfo-request>) istream)
  "Deserializes a message object of type '<AskInfo-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AskInfo-request>)))
  "Returns string type for a service object of type '<AskInfo-request>"
  "qbo_system_info/AskInfoRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AskInfo-request)))
  "Returns string type for a service object of type 'AskInfo-request"
  "qbo_system_info/AskInfoRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AskInfo-request>)))
  "Returns md5sum for a message object of type '<AskInfo-request>"
  "2114094fd794b6de43079d7511fd7383")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AskInfo-request)))
  "Returns md5sum for a message object of type 'AskInfo-request"
  "2114094fd794b6de43079d7511fd7383")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AskInfo-request>)))
  "Returns full string definition for message of type '<AskInfo-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AskInfo-request)))
  "Returns full string definition for message of type 'AskInfo-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AskInfo-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'command))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AskInfo-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AskInfo-request
    (cl:cons ':command (command msg))
))
;//! \htmlinclude AskInfo-response.msg.html

(cl:defclass <AskInfo-response> (roslisp-msg-protocol:ros-message)
  ((info
    :reader info
    :initarg :info
    :type cl:string
    :initform ""))
)

(cl:defclass AskInfo-response (<AskInfo-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AskInfo-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AskInfo-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_system_info-srv:<AskInfo-response> is deprecated: use qbo_system_info-srv:AskInfo-response instead.")))

(cl:ensure-generic-function 'info-val :lambda-list '(m))
(cl:defmethod info-val ((m <AskInfo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_system_info-srv:info-val is deprecated.  Use qbo_system_info-srv:info instead.")
  (info m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AskInfo-response>) ostream)
  "Serializes a message object of type '<AskInfo-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'info))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'info))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AskInfo-response>) istream)
  "Deserializes a message object of type '<AskInfo-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'info) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'info) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AskInfo-response>)))
  "Returns string type for a service object of type '<AskInfo-response>"
  "qbo_system_info/AskInfoResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AskInfo-response)))
  "Returns string type for a service object of type 'AskInfo-response"
  "qbo_system_info/AskInfoResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AskInfo-response>)))
  "Returns md5sum for a message object of type '<AskInfo-response>"
  "2114094fd794b6de43079d7511fd7383")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AskInfo-response)))
  "Returns md5sum for a message object of type 'AskInfo-response"
  "2114094fd794b6de43079d7511fd7383")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AskInfo-response>)))
  "Returns full string definition for message of type '<AskInfo-response>"
  (cl:format cl:nil "string info~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AskInfo-response)))
  "Returns full string definition for message of type 'AskInfo-response"
  (cl:format cl:nil "string info~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AskInfo-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'info))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AskInfo-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AskInfo-response
    (cl:cons ':info (info msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AskInfo)))
  'AskInfo-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AskInfo)))
  'AskInfo-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AskInfo)))
  "Returns string type for a service object of type '<AskInfo>"
  "qbo_system_info/AskInfo")