; Auto-generated. Do not edit!


(cl:in-package qbo_self_recognizer-srv)


;//! \htmlinclude QboRecognize-request.msg.html

(cl:defclass <QboRecognize-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass QboRecognize-request (<QboRecognize-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <QboRecognize-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'QboRecognize-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_self_recognizer-srv:<QboRecognize-request> is deprecated: use qbo_self_recognizer-srv:QboRecognize-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <QboRecognize-request>) ostream)
  "Serializes a message object of type '<QboRecognize-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <QboRecognize-request>) istream)
  "Deserializes a message object of type '<QboRecognize-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<QboRecognize-request>)))
  "Returns string type for a service object of type '<QboRecognize-request>"
  "qbo_self_recognizer/QboRecognizeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QboRecognize-request)))
  "Returns string type for a service object of type 'QboRecognize-request"
  "qbo_self_recognizer/QboRecognizeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<QboRecognize-request>)))
  "Returns md5sum for a message object of type '<QboRecognize-request>"
  "4a7936398cbe09a7d47b0d9fc1e9e7f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'QboRecognize-request)))
  "Returns md5sum for a message object of type 'QboRecognize-request"
  "4a7936398cbe09a7d47b0d9fc1e9e7f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<QboRecognize-request>)))
  "Returns full string definition for message of type '<QboRecognize-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'QboRecognize-request)))
  "Returns full string definition for message of type 'QboRecognize-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <QboRecognize-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <QboRecognize-request>))
  "Converts a ROS message object to a list"
  (cl:list 'QboRecognize-request
))
;//! \htmlinclude QboRecognize-response.msg.html

(cl:defclass <QboRecognize-response> (roslisp-msg-protocol:ros-message)
  ((recognized
    :reader recognized
    :initarg :recognized
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass QboRecognize-response (<QboRecognize-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <QboRecognize-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'QboRecognize-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_self_recognizer-srv:<QboRecognize-response> is deprecated: use qbo_self_recognizer-srv:QboRecognize-response instead.")))

(cl:ensure-generic-function 'recognized-val :lambda-list '(m))
(cl:defmethod recognized-val ((m <QboRecognize-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_self_recognizer-srv:recognized-val is deprecated.  Use qbo_self_recognizer-srv:recognized instead.")
  (recognized m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <QboRecognize-response>) ostream)
  "Serializes a message object of type '<QboRecognize-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'recognized) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <QboRecognize-response>) istream)
  "Deserializes a message object of type '<QboRecognize-response>"
    (cl:setf (cl:slot-value msg 'recognized) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<QboRecognize-response>)))
  "Returns string type for a service object of type '<QboRecognize-response>"
  "qbo_self_recognizer/QboRecognizeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QboRecognize-response)))
  "Returns string type for a service object of type 'QboRecognize-response"
  "qbo_self_recognizer/QboRecognizeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<QboRecognize-response>)))
  "Returns md5sum for a message object of type '<QboRecognize-response>"
  "4a7936398cbe09a7d47b0d9fc1e9e7f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'QboRecognize-response)))
  "Returns md5sum for a message object of type 'QboRecognize-response"
  "4a7936398cbe09a7d47b0d9fc1e9e7f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<QboRecognize-response>)))
  "Returns full string definition for message of type '<QboRecognize-response>"
  (cl:format cl:nil "bool recognized~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'QboRecognize-response)))
  "Returns full string definition for message of type 'QboRecognize-response"
  (cl:format cl:nil "bool recognized~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <QboRecognize-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <QboRecognize-response>))
  "Converts a ROS message object to a list"
  (cl:list 'QboRecognize-response
    (cl:cons ':recognized (recognized msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'QboRecognize)))
  'QboRecognize-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'QboRecognize)))
  'QboRecognize-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QboRecognize)))
  "Returns string type for a service object of type '<QboRecognize>"
  "qbo_self_recognizer/QboRecognize")