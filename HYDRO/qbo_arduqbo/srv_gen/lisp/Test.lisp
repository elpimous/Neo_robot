; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-srv)


;//! \htmlinclude Test-request.msg.html

(cl:defclass <Test-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Test-request (<Test-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Test-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Test-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-srv:<Test-request> is deprecated: use qbo_arduqbo-srv:Test-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Test-request>) ostream)
  "Serializes a message object of type '<Test-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Test-request>) istream)
  "Deserializes a message object of type '<Test-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Test-request>)))
  "Returns string type for a service object of type '<Test-request>"
  "qbo_arduqbo/TestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Test-request)))
  "Returns string type for a service object of type 'Test-request"
  "qbo_arduqbo/TestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Test-request>)))
  "Returns md5sum for a message object of type '<Test-request>"
  "6f8d7da5192e662dd9f7974027b7e5ee")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Test-request)))
  "Returns md5sum for a message object of type 'Test-request"
  "6f8d7da5192e662dd9f7974027b7e5ee")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Test-request>)))
  "Returns full string definition for message of type '<Test-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Test-request)))
  "Returns full string definition for message of type 'Test-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Test-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Test-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Test-request
))
;//! \htmlinclude Test-response.msg.html

(cl:defclass <Test-response> (roslisp-msg-protocol:ros-message)
  ((SRFcount
    :reader SRFcount
    :initarg :SRFcount
    :type cl:fixnum
    :initform 0)
   (SRFAddress
    :reader SRFAddress
    :initarg :SRFAddress
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (SRFNotFound
    :reader SRFNotFound
    :initarg :SRFNotFound
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (Gyroscope
    :reader Gyroscope
    :initarg :Gyroscope
    :type cl:boolean
    :initform cl:nil)
   (Accelerometer
    :reader Accelerometer
    :initarg :Accelerometer
    :type cl:boolean
    :initform cl:nil)
   (LCD
    :reader LCD
    :initarg :LCD
    :type cl:boolean
    :initform cl:nil)
   (Qboard3
    :reader Qboard3
    :initarg :Qboard3
    :type cl:boolean
    :initform cl:nil)
   (Qboard1
    :reader Qboard1
    :initarg :Qboard1
    :type cl:boolean
    :initform cl:nil)
   (Qboard2
    :reader Qboard2
    :initarg :Qboard2
    :type cl:boolean
    :initform cl:nil)
   (rightMotor
    :reader rightMotor
    :initarg :rightMotor
    :type cl:boolean
    :initform cl:nil)
   (leftMotor
    :reader leftMotor
    :initarg :leftMotor
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Test-response (<Test-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Test-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Test-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-srv:<Test-response> is deprecated: use qbo_arduqbo-srv:Test-response instead.")))

(cl:ensure-generic-function 'SRFcount-val :lambda-list '(m))
(cl:defmethod SRFcount-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:SRFcount-val is deprecated.  Use qbo_arduqbo-srv:SRFcount instead.")
  (SRFcount m))

(cl:ensure-generic-function 'SRFAddress-val :lambda-list '(m))
(cl:defmethod SRFAddress-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:SRFAddress-val is deprecated.  Use qbo_arduqbo-srv:SRFAddress instead.")
  (SRFAddress m))

(cl:ensure-generic-function 'SRFNotFound-val :lambda-list '(m))
(cl:defmethod SRFNotFound-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:SRFNotFound-val is deprecated.  Use qbo_arduqbo-srv:SRFNotFound instead.")
  (SRFNotFound m))

(cl:ensure-generic-function 'Gyroscope-val :lambda-list '(m))
(cl:defmethod Gyroscope-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:Gyroscope-val is deprecated.  Use qbo_arduqbo-srv:Gyroscope instead.")
  (Gyroscope m))

(cl:ensure-generic-function 'Accelerometer-val :lambda-list '(m))
(cl:defmethod Accelerometer-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:Accelerometer-val is deprecated.  Use qbo_arduqbo-srv:Accelerometer instead.")
  (Accelerometer m))

(cl:ensure-generic-function 'LCD-val :lambda-list '(m))
(cl:defmethod LCD-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:LCD-val is deprecated.  Use qbo_arduqbo-srv:LCD instead.")
  (LCD m))

(cl:ensure-generic-function 'Qboard3-val :lambda-list '(m))
(cl:defmethod Qboard3-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:Qboard3-val is deprecated.  Use qbo_arduqbo-srv:Qboard3 instead.")
  (Qboard3 m))

(cl:ensure-generic-function 'Qboard1-val :lambda-list '(m))
(cl:defmethod Qboard1-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:Qboard1-val is deprecated.  Use qbo_arduqbo-srv:Qboard1 instead.")
  (Qboard1 m))

(cl:ensure-generic-function 'Qboard2-val :lambda-list '(m))
(cl:defmethod Qboard2-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:Qboard2-val is deprecated.  Use qbo_arduqbo-srv:Qboard2 instead.")
  (Qboard2 m))

(cl:ensure-generic-function 'rightMotor-val :lambda-list '(m))
(cl:defmethod rightMotor-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:rightMotor-val is deprecated.  Use qbo_arduqbo-srv:rightMotor instead.")
  (rightMotor m))

(cl:ensure-generic-function 'leftMotor-val :lambda-list '(m))
(cl:defmethod leftMotor-val ((m <Test-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-srv:leftMotor-val is deprecated.  Use qbo_arduqbo-srv:leftMotor instead.")
  (leftMotor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Test-response>) ostream)
  "Serializes a message object of type '<Test-response>"
  (cl:let* ((signed (cl:slot-value msg 'SRFcount)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'SRFAddress))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'SRFAddress))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'SRFNotFound))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'SRFNotFound))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Gyroscope) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Accelerometer) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'LCD) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Qboard3) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Qboard1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Qboard2) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'rightMotor) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'leftMotor) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Test-response>) istream)
  "Deserializes a message object of type '<Test-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'SRFcount) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'SRFAddress) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'SRFAddress)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'SRFNotFound) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'SRFNotFound)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
    (cl:setf (cl:slot-value msg 'Gyroscope) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Accelerometer) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'LCD) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Qboard3) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Qboard1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'Qboard2) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'rightMotor) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'leftMotor) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Test-response>)))
  "Returns string type for a service object of type '<Test-response>"
  "qbo_arduqbo/TestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Test-response)))
  "Returns string type for a service object of type 'Test-response"
  "qbo_arduqbo/TestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Test-response>)))
  "Returns md5sum for a message object of type '<Test-response>"
  "6f8d7da5192e662dd9f7974027b7e5ee")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Test-response)))
  "Returns md5sum for a message object of type 'Test-response"
  "6f8d7da5192e662dd9f7974027b7e5ee")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Test-response>)))
  "Returns full string definition for message of type '<Test-response>"
  (cl:format cl:nil "int8 SRFcount~%int16[] SRFAddress~%int16[] SRFNotFound~%bool Gyroscope~%bool Accelerometer~%bool LCD~%bool Qboard3~%bool Qboard1~%bool Qboard2~%bool rightMotor~%bool leftMotor~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Test-response)))
  "Returns full string definition for message of type 'Test-response"
  (cl:format cl:nil "int8 SRFcount~%int16[] SRFAddress~%int16[] SRFNotFound~%bool Gyroscope~%bool Accelerometer~%bool LCD~%bool Qboard3~%bool Qboard1~%bool Qboard2~%bool rightMotor~%bool leftMotor~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Test-response>))
  (cl:+ 0
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'SRFAddress) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'SRFNotFound) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Test-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Test-response
    (cl:cons ':SRFcount (SRFcount msg))
    (cl:cons ':SRFAddress (SRFAddress msg))
    (cl:cons ':SRFNotFound (SRFNotFound msg))
    (cl:cons ':Gyroscope (Gyroscope msg))
    (cl:cons ':Accelerometer (Accelerometer msg))
    (cl:cons ':LCD (LCD msg))
    (cl:cons ':Qboard3 (Qboard3 msg))
    (cl:cons ':Qboard1 (Qboard1 msg))
    (cl:cons ':Qboard2 (Qboard2 msg))
    (cl:cons ':rightMotor (rightMotor msg))
    (cl:cons ':leftMotor (leftMotor msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Test)))
  'Test-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Test)))
  'Test-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Test)))
  "Returns string type for a service object of type '<Test>"
  "qbo_arduqbo/Test")