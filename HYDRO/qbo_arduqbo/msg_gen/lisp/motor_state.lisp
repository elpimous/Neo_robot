; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude motor_state.msg.html

(cl:defclass <motor_state> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (goal
    :reader goal
    :initarg :goal
    :type cl:integer
    :initform 0)
   (position
    :reader position
    :initarg :position
    :type cl:integer
    :initform 0)
   (error
    :reader error
    :initarg :error
    :type cl:integer
    :initform 0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:integer
    :initform 0)
   (load
    :reader load
    :initarg :load
    :type cl:float
    :initform 0.0)
   (voltage
    :reader voltage
    :initarg :voltage
    :type cl:float
    :initform 0.0)
   (temperature
    :reader temperature
    :initarg :temperature
    :type cl:integer
    :initform 0)
   (moving
    :reader moving
    :initarg :moving
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass motor_state (<motor_state>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motor_state>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motor_state)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<motor_state> is deprecated: use qbo_arduqbo-msg:motor_state instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:id-val is deprecated.  Use qbo_arduqbo-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:goal-val is deprecated.  Use qbo_arduqbo-msg:goal instead.")
  (goal m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:position-val is deprecated.  Use qbo_arduqbo-msg:position instead.")
  (position m))

(cl:ensure-generic-function 'error-val :lambda-list '(m))
(cl:defmethod error-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:error-val is deprecated.  Use qbo_arduqbo-msg:error instead.")
  (error m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:speed-val is deprecated.  Use qbo_arduqbo-msg:speed instead.")
  (speed m))

(cl:ensure-generic-function 'load-val :lambda-list '(m))
(cl:defmethod load-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:load-val is deprecated.  Use qbo_arduqbo-msg:load instead.")
  (load m))

(cl:ensure-generic-function 'voltage-val :lambda-list '(m))
(cl:defmethod voltage-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:voltage-val is deprecated.  Use qbo_arduqbo-msg:voltage instead.")
  (voltage m))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:temperature-val is deprecated.  Use qbo_arduqbo-msg:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'moving-val :lambda-list '(m))
(cl:defmethod moving-val ((m <motor_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:moving-val is deprecated.  Use qbo_arduqbo-msg:moving instead.")
  (moving m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motor_state>) ostream)
  "Serializes a message object of type '<motor_state>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'goal)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'position)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'error)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'load))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'temperature)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'moving) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motor_state>) istream)
  "Deserializes a message object of type '<motor_state>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'position) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'error) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'load) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'voltage) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'temperature) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:slot-value msg 'moving) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motor_state>)))
  "Returns string type for a message object of type '<motor_state>"
  "qbo_arduqbo/motor_state")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motor_state)))
  "Returns string type for a message object of type 'motor_state"
  "qbo_arduqbo/motor_state")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motor_state>)))
  "Returns md5sum for a message object of type '<motor_state>"
  "7c778bda1190d2be2e7c5f3fad8d4eda")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motor_state)))
  "Returns md5sum for a message object of type 'motor_state"
  "7c778bda1190d2be2e7c5f3fad8d4eda")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motor_state>)))
  "Returns full string definition for message of type '<motor_state>"
  (cl:format cl:nil "Header header~%int32 id            # motor id~%int32 goal          # commanded position (in encoder units)~%int32 position      # current position (in encoder units)~%int32 error         # difference between current and goal positions~%int32 speed         # current speed (0.111 rpm per unit)~%float64 load        # current load - ratio of applied torque over maximum torque~%float64 voltage     # current voltage (V)~%int32 temperature   # current temperature (degrees Celsius)~%bool moving         # whether the motor is currently in motion~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motor_state)))
  "Returns full string definition for message of type 'motor_state"
  (cl:format cl:nil "Header header~%int32 id            # motor id~%int32 goal          # commanded position (in encoder units)~%int32 position      # current position (in encoder units)~%int32 error         # difference between current and goal positions~%int32 speed         # current speed (0.111 rpm per unit)~%float64 load        # current load - ratio of applied torque over maximum torque~%float64 voltage     # current voltage (V)~%int32 temperature   # current temperature (degrees Celsius)~%bool moving         # whether the motor is currently in motion~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motor_state>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     8
     8
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motor_state>))
  "Converts a ROS message object to a list"
  (cl:list 'motor_state
    (cl:cons ':header (header msg))
    (cl:cons ':id (id msg))
    (cl:cons ':goal (goal msg))
    (cl:cons ':position (position msg))
    (cl:cons ':error (error msg))
    (cl:cons ':speed (speed msg))
    (cl:cons ':load (load msg))
    (cl:cons ':voltage (voltage msg))
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':moving (moving msg))
))
