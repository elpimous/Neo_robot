; Auto-generated. Do not edit!


(cl:in-package qbo_object_recognition-srv)


;//! \htmlinclude LearnNewObject-request.msg.html

(cl:defclass <LearnNewObject-request> (roslisp-msg-protocol:ros-message)
  ((object_name
    :reader object_name
    :initarg :object_name
    :type cl:string
    :initform ""))
)

(cl:defclass LearnNewObject-request (<LearnNewObject-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LearnNewObject-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LearnNewObject-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<LearnNewObject-request> is deprecated: use qbo_object_recognition-srv:LearnNewObject-request instead.")))

(cl:ensure-generic-function 'object_name-val :lambda-list '(m))
(cl:defmethod object_name-val ((m <LearnNewObject-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:object_name-val is deprecated.  Use qbo_object_recognition-srv:object_name instead.")
  (object_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LearnNewObject-request>) ostream)
  "Serializes a message object of type '<LearnNewObject-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'object_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'object_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LearnNewObject-request>) istream)
  "Deserializes a message object of type '<LearnNewObject-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'object_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'object_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LearnNewObject-request>)))
  "Returns string type for a service object of type '<LearnNewObject-request>"
  "qbo_object_recognition/LearnNewObjectRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LearnNewObject-request)))
  "Returns string type for a service object of type 'LearnNewObject-request"
  "qbo_object_recognition/LearnNewObjectRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LearnNewObject-request>)))
  "Returns md5sum for a message object of type '<LearnNewObject-request>"
  "806e4614bcce891ffdc0106c00889221")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LearnNewObject-request)))
  "Returns md5sum for a message object of type 'LearnNewObject-request"
  "806e4614bcce891ffdc0106c00889221")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LearnNewObject-request>)))
  "Returns full string definition for message of type '<LearnNewObject-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%string object_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LearnNewObject-request)))
  "Returns full string definition for message of type 'LearnNewObject-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%string object_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LearnNewObject-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'object_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LearnNewObject-request>))
  "Converts a ROS message object to a list"
  (cl:list 'LearnNewObject-request
    (cl:cons ':object_name (object_name msg))
))
;//! \htmlinclude LearnNewObject-response.msg.html

(cl:defclass <LearnNewObject-response> (roslisp-msg-protocol:ros-message)
  ((learned
    :reader learned
    :initarg :learned
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass LearnNewObject-response (<LearnNewObject-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LearnNewObject-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LearnNewObject-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<LearnNewObject-response> is deprecated: use qbo_object_recognition-srv:LearnNewObject-response instead.")))

(cl:ensure-generic-function 'learned-val :lambda-list '(m))
(cl:defmethod learned-val ((m <LearnNewObject-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:learned-val is deprecated.  Use qbo_object_recognition-srv:learned instead.")
  (learned m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LearnNewObject-response>) ostream)
  "Serializes a message object of type '<LearnNewObject-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'learned) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LearnNewObject-response>) istream)
  "Deserializes a message object of type '<LearnNewObject-response>"
    (cl:setf (cl:slot-value msg 'learned) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LearnNewObject-response>)))
  "Returns string type for a service object of type '<LearnNewObject-response>"
  "qbo_object_recognition/LearnNewObjectResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LearnNewObject-response)))
  "Returns string type for a service object of type 'LearnNewObject-response"
  "qbo_object_recognition/LearnNewObjectResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LearnNewObject-response>)))
  "Returns md5sum for a message object of type '<LearnNewObject-response>"
  "806e4614bcce891ffdc0106c00889221")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LearnNewObject-response)))
  "Returns md5sum for a message object of type 'LearnNewObject-response"
  "806e4614bcce891ffdc0106c00889221")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LearnNewObject-response>)))
  "Returns full string definition for message of type '<LearnNewObject-response>"
  (cl:format cl:nil "bool learned~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LearnNewObject-response)))
  "Returns full string definition for message of type 'LearnNewObject-response"
  (cl:format cl:nil "bool learned~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LearnNewObject-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LearnNewObject-response>))
  "Converts a ROS message object to a list"
  (cl:list 'LearnNewObject-response
    (cl:cons ':learned (learned msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'LearnNewObject)))
  'LearnNewObject-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'LearnNewObject)))
  'LearnNewObject-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LearnNewObject)))
  "Returns string type for a service object of type '<LearnNewObject>"
  "qbo_object_recognition/LearnNewObject")