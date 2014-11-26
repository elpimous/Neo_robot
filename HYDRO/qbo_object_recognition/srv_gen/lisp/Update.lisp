; Auto-generated. Do not edit!


(cl:in-package qbo_object_recognition-srv)


;//! \htmlinclude Update-request.msg.html

(cl:defclass <Update-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Update-request (<Update-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Update-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Update-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<Update-request> is deprecated: use qbo_object_recognition-srv:Update-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Update-request>) ostream)
  "Serializes a message object of type '<Update-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Update-request>) istream)
  "Deserializes a message object of type '<Update-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Update-request>)))
  "Returns string type for a service object of type '<Update-request>"
  "qbo_object_recognition/UpdateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Update-request)))
  "Returns string type for a service object of type 'Update-request"
  "qbo_object_recognition/UpdateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Update-request>)))
  "Returns md5sum for a message object of type '<Update-request>"
  "f2df1c820c92c74a7826e781de98894e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Update-request)))
  "Returns md5sum for a message object of type 'Update-request"
  "f2df1c820c92c74a7826e781de98894e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Update-request>)))
  "Returns full string definition for message of type '<Update-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Update-request)))
  "Returns full string definition for message of type 'Update-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Update-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Update-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Update-request
))
;//! \htmlinclude Update-response.msg.html

(cl:defclass <Update-response> (roslisp-msg-protocol:ros-message)
  ((updated
    :reader updated
    :initarg :updated
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Update-response (<Update-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Update-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Update-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<Update-response> is deprecated: use qbo_object_recognition-srv:Update-response instead.")))

(cl:ensure-generic-function 'updated-val :lambda-list '(m))
(cl:defmethod updated-val ((m <Update-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:updated-val is deprecated.  Use qbo_object_recognition-srv:updated instead.")
  (updated m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Update-response>) ostream)
  "Serializes a message object of type '<Update-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'updated) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Update-response>) istream)
  "Deserializes a message object of type '<Update-response>"
    (cl:setf (cl:slot-value msg 'updated) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Update-response>)))
  "Returns string type for a service object of type '<Update-response>"
  "qbo_object_recognition/UpdateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Update-response)))
  "Returns string type for a service object of type 'Update-response"
  "qbo_object_recognition/UpdateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Update-response>)))
  "Returns md5sum for a message object of type '<Update-response>"
  "f2df1c820c92c74a7826e781de98894e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Update-response)))
  "Returns md5sum for a message object of type 'Update-response"
  "f2df1c820c92c74a7826e781de98894e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Update-response>)))
  "Returns full string definition for message of type '<Update-response>"
  (cl:format cl:nil "bool updated~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Update-response)))
  "Returns full string definition for message of type 'Update-response"
  (cl:format cl:nil "bool updated~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Update-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Update-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Update-response
    (cl:cons ':updated (updated msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Update)))
  'Update-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Update)))
  'Update-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Update)))
  "Returns string type for a service object of type '<Update>"
  "qbo_object_recognition/Update")