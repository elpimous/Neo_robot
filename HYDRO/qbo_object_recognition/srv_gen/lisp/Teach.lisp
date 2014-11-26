; Auto-generated. Do not edit!


(cl:in-package qbo_object_recognition-srv)


;//! \htmlinclude Teach-request.msg.html

(cl:defclass <Teach-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Teach-request (<Teach-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Teach-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Teach-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<Teach-request> is deprecated: use qbo_object_recognition-srv:Teach-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Teach-request>) ostream)
  "Serializes a message object of type '<Teach-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Teach-request>) istream)
  "Deserializes a message object of type '<Teach-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Teach-request>)))
  "Returns string type for a service object of type '<Teach-request>"
  "qbo_object_recognition/TeachRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Teach-request)))
  "Returns string type for a service object of type 'Teach-request"
  "qbo_object_recognition/TeachRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Teach-request>)))
  "Returns md5sum for a message object of type '<Teach-request>"
  "045e724eaf9efdeff4f56e372f7e1c92")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Teach-request)))
  "Returns md5sum for a message object of type 'Teach-request"
  "045e724eaf9efdeff4f56e372f7e1c92")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Teach-request>)))
  "Returns full string definition for message of type '<Teach-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Teach-request)))
  "Returns full string definition for message of type 'Teach-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Teach-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Teach-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Teach-request
))
;//! \htmlinclude Teach-response.msg.html

(cl:defclass <Teach-response> (roslisp-msg-protocol:ros-message)
  ((taught
    :reader taught
    :initarg :taught
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Teach-response (<Teach-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Teach-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Teach-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<Teach-response> is deprecated: use qbo_object_recognition-srv:Teach-response instead.")))

(cl:ensure-generic-function 'taught-val :lambda-list '(m))
(cl:defmethod taught-val ((m <Teach-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:taught-val is deprecated.  Use qbo_object_recognition-srv:taught instead.")
  (taught m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Teach-response>) ostream)
  "Serializes a message object of type '<Teach-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'taught) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Teach-response>) istream)
  "Deserializes a message object of type '<Teach-response>"
    (cl:setf (cl:slot-value msg 'taught) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Teach-response>)))
  "Returns string type for a service object of type '<Teach-response>"
  "qbo_object_recognition/TeachResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Teach-response)))
  "Returns string type for a service object of type 'Teach-response"
  "qbo_object_recognition/TeachResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Teach-response>)))
  "Returns md5sum for a message object of type '<Teach-response>"
  "045e724eaf9efdeff4f56e372f7e1c92")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Teach-response)))
  "Returns md5sum for a message object of type 'Teach-response"
  "045e724eaf9efdeff4f56e372f7e1c92")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Teach-response>)))
  "Returns full string definition for message of type '<Teach-response>"
  (cl:format cl:nil "bool taught~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Teach-response)))
  "Returns full string definition for message of type 'Teach-response"
  (cl:format cl:nil "bool taught~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Teach-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Teach-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Teach-response
    (cl:cons ':taught (taught msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Teach)))
  'Teach-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Teach)))
  'Teach-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Teach)))
  "Returns string type for a service object of type '<Teach>"
  "qbo_object_recognition/Teach")