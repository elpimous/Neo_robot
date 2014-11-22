; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude BatteryLevel.msg.html

(cl:defclass <BatteryLevel> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (level
    :reader level
    :initarg :level
    :type cl:float
    :initform 0.0)
   (stat
    :reader stat
    :initarg :stat
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BatteryLevel (<BatteryLevel>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BatteryLevel>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BatteryLevel)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<BatteryLevel> is deprecated: use qbo_arduqbo-msg:BatteryLevel instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <BatteryLevel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'level-val :lambda-list '(m))
(cl:defmethod level-val ((m <BatteryLevel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:level-val is deprecated.  Use qbo_arduqbo-msg:level instead.")
  (level m))

(cl:ensure-generic-function 'stat-val :lambda-list '(m))
(cl:defmethod stat-val ((m <BatteryLevel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:stat-val is deprecated.  Use qbo_arduqbo-msg:stat instead.")
  (stat m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BatteryLevel>) ostream)
  "Serializes a message object of type '<BatteryLevel>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'level))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'stat)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BatteryLevel>) istream)
  "Deserializes a message object of type '<BatteryLevel>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'level) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'stat)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BatteryLevel>)))
  "Returns string type for a message object of type '<BatteryLevel>"
  "qbo_arduqbo/BatteryLevel")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BatteryLevel)))
  "Returns string type for a message object of type 'BatteryLevel"
  "qbo_arduqbo/BatteryLevel")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BatteryLevel>)))
  "Returns md5sum for a message object of type '<BatteryLevel>"
  "4f662380ef802191974fae59ab2731d1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BatteryLevel)))
  "Returns md5sum for a message object of type 'BatteryLevel"
  "4f662380ef802191974fae59ab2731d1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BatteryLevel>)))
  "Returns full string definition for message of type '<BatteryLevel>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%float32 level~%uint8 stat~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BatteryLevel)))
  "Returns full string definition for message of type 'BatteryLevel"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%float32 level~%uint8 stat~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BatteryLevel>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BatteryLevel>))
  "Converts a ROS message object to a list"
  (cl:list 'BatteryLevel
    (cl:cons ':header (header msg))
    (cl:cons ':level (level msg))
    (cl:cons ':stat (stat msg))
))
