; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-srv)


;//! \htmlinclude BaseStop-request.msg.html

(cl:defclass <BaseStop-request> (roslisp-msg-protocol:ros-message)
  ((sender
    :reader sender
    :initarg :sender
    :type cl:string
    :initform "")
   (state
    :reader state
    :initarg :state
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass BaseStop-request (<BaseStop-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BaseStop-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BaseStop-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-srv:<BaseStop-request> is deprecated: use qbo_arduqbo-srv:BaseStop-request instead.")))

(cl:ensure-generic-function 'sender-val :lambda-list '(m))
(cl:defmethod sender-val ((m <BaseStop-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:sender-val is deprecated.  Use qbo_arduqbo-srv:sender instead.")
  (sender m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <BaseStop-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:state-val is deprecated.  Use qbo_arduqbo-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BaseStop-request>) ostream)
  "Serializes a message object of type '<BaseStop-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'sender))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'sender))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'state) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BaseStop-request>) istream)
  "Deserializes a message object of type '<BaseStop-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sender) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'sender) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'state) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BaseStop-request>)))
  "Returns string type for a service object of type '<BaseStop-request>"
  "qbo_arduqbo/BaseStopRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BaseStop-request)))
  "Returns string type for a service object of type 'BaseStop-request"
  "qbo_arduqbo/BaseStopRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BaseStop-request>)))
  "Returns md5sum for a message object of type '<BaseStop-request>"
  "adc1836ec05769e51272f3bf2b237d1d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BaseStop-request)))
  "Returns md5sum for a message object of type 'BaseStop-request"
  "adc1836ec05769e51272f3bf2b237d1d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BaseStop-request>)))
  "Returns full string definition for message of type '<BaseStop-request>"
  (cl:format cl:nil "string sender~%bool state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BaseStop-request)))
  "Returns full string definition for message of type 'BaseStop-request"
  (cl:format cl:nil "string sender~%bool state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BaseStop-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'sender))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BaseStop-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BaseStop-request
    (cl:cons ':sender (sender msg))
    (cl:cons ':state (state msg))
))
;//! \htmlinclude BaseStop-response.msg.html

(cl:defclass <BaseStop-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass BaseStop-response (<BaseStop-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BaseStop-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BaseStop-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-srv:<BaseStop-response> is deprecated: use qbo_arduqbo-srv:BaseStop-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BaseStop-response>) ostream)
  "Serializes a message object of type '<BaseStop-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BaseStop-response>) istream)
  "Deserializes a message object of type '<BaseStop-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BaseStop-response>)))
  "Returns string type for a service object of type '<BaseStop-response>"
  "qbo_arduqbo/BaseStopResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BaseStop-response)))
  "Returns string type for a service object of type 'BaseStop-response"
  "qbo_arduqbo/BaseStopResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BaseStop-response>)))
  "Returns md5sum for a message object of type '<BaseStop-response>"
  "adc1836ec05769e51272f3bf2b237d1d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BaseStop-response)))
  "Returns md5sum for a message object of type 'BaseStop-response"
  "adc1836ec05769e51272f3bf2b237d1d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BaseStop-response>)))
  "Returns full string definition for message of type '<BaseStop-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BaseStop-response)))
  "Returns full string definition for message of type 'BaseStop-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BaseStop-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BaseStop-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BaseStop-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BaseStop)))
  'BaseStop-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BaseStop)))
  'BaseStop-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BaseStop)))
  "Returns string type for a service object of type '<BaseStop>"
  "qbo_arduqbo/BaseStop")