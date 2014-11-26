; Auto-generated. Do not edit!


(cl:in-package qbo_object_recognition-srv)


;//! \htmlinclude RecognizeObject-request.msg.html

(cl:defclass <RecognizeObject-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass RecognizeObject-request (<RecognizeObject-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecognizeObject-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecognizeObject-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<RecognizeObject-request> is deprecated: use qbo_object_recognition-srv:RecognizeObject-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecognizeObject-request>) ostream)
  "Serializes a message object of type '<RecognizeObject-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecognizeObject-request>) istream)
  "Deserializes a message object of type '<RecognizeObject-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecognizeObject-request>)))
  "Returns string type for a service object of type '<RecognizeObject-request>"
  "qbo_object_recognition/RecognizeObjectRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeObject-request)))
  "Returns string type for a service object of type 'RecognizeObject-request"
  "qbo_object_recognition/RecognizeObjectRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecognizeObject-request>)))
  "Returns md5sum for a message object of type '<RecognizeObject-request>"
  "20fe0fa539e86f0dcf82db65a3df666b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecognizeObject-request)))
  "Returns md5sum for a message object of type 'RecognizeObject-request"
  "20fe0fa539e86f0dcf82db65a3df666b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecognizeObject-request>)))
  "Returns full string definition for message of type '<RecognizeObject-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecognizeObject-request)))
  "Returns full string definition for message of type 'RecognizeObject-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecognizeObject-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecognizeObject-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RecognizeObject-request
))
;//! \htmlinclude RecognizeObject-response.msg.html

(cl:defclass <RecognizeObject-response> (roslisp-msg-protocol:ros-message)
  ((object_name
    :reader object_name
    :initarg :object_name
    :type cl:string
    :initform "")
   (recognized
    :reader recognized
    :initarg :recognized
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass RecognizeObject-response (<RecognizeObject-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecognizeObject-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecognizeObject-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<RecognizeObject-response> is deprecated: use qbo_object_recognition-srv:RecognizeObject-response instead.")))

(cl:ensure-generic-function 'object_name-val :lambda-list '(m))
(cl:defmethod object_name-val ((m <RecognizeObject-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:object_name-val is deprecated.  Use qbo_object_recognition-srv:object_name instead.")
  (object_name m))

(cl:ensure-generic-function 'recognized-val :lambda-list '(m))
(cl:defmethod recognized-val ((m <RecognizeObject-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:recognized-val is deprecated.  Use qbo_object_recognition-srv:recognized instead.")
  (recognized m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecognizeObject-response>) ostream)
  "Serializes a message object of type '<RecognizeObject-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'object_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'object_name))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'recognized) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecognizeObject-response>) istream)
  "Deserializes a message object of type '<RecognizeObject-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'object_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'object_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'recognized) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecognizeObject-response>)))
  "Returns string type for a service object of type '<RecognizeObject-response>"
  "qbo_object_recognition/RecognizeObjectResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeObject-response)))
  "Returns string type for a service object of type 'RecognizeObject-response"
  "qbo_object_recognition/RecognizeObjectResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecognizeObject-response>)))
  "Returns md5sum for a message object of type '<RecognizeObject-response>"
  "20fe0fa539e86f0dcf82db65a3df666b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecognizeObject-response)))
  "Returns md5sum for a message object of type 'RecognizeObject-response"
  "20fe0fa539e86f0dcf82db65a3df666b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecognizeObject-response>)))
  "Returns full string definition for message of type '<RecognizeObject-response>"
  (cl:format cl:nil "string object_name~%bool recognized~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecognizeObject-response)))
  "Returns full string definition for message of type 'RecognizeObject-response"
  (cl:format cl:nil "string object_name~%bool recognized~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecognizeObject-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'object_name))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecognizeObject-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RecognizeObject-response
    (cl:cons ':object_name (object_name msg))
    (cl:cons ':recognized (recognized msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RecognizeObject)))
  'RecognizeObject-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RecognizeObject)))
  'RecognizeObject-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeObject)))
  "Returns string type for a service object of type '<RecognizeObject>"
  "qbo_object_recognition/RecognizeObject")