; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude NoiseLevels.msg.html

(cl:defclass <NoiseLevels> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (m0
    :reader m0
    :initarg :m0
    :type cl:fixnum
    :initform 0)
   (m1
    :reader m1
    :initarg :m1
    :type cl:fixnum
    :initform 0)
   (m2
    :reader m2
    :initarg :m2
    :type cl:fixnum
    :initform 0))
)

(cl:defclass NoiseLevels (<NoiseLevels>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NoiseLevels>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NoiseLevels)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<NoiseLevels> is deprecated: use qbo_arduqbo-msg:NoiseLevels instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <NoiseLevels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'm0-val :lambda-list '(m))
(cl:defmethod m0-val ((m <NoiseLevels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:m0-val is deprecated.  Use qbo_arduqbo-msg:m0 instead.")
  (m0 m))

(cl:ensure-generic-function 'm1-val :lambda-list '(m))
(cl:defmethod m1-val ((m <NoiseLevels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:m1-val is deprecated.  Use qbo_arduqbo-msg:m1 instead.")
  (m1 m))

(cl:ensure-generic-function 'm2-val :lambda-list '(m))
(cl:defmethod m2-val ((m <NoiseLevels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:m2-val is deprecated.  Use qbo_arduqbo-msg:m2 instead.")
  (m2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NoiseLevels>) ostream)
  "Serializes a message object of type '<NoiseLevels>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'm0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'm0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'm1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'm1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'm2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'm2)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NoiseLevels>) istream)
  "Deserializes a message object of type '<NoiseLevels>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'm0)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'm0)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'm1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'm1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'm2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'm2)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NoiseLevels>)))
  "Returns string type for a message object of type '<NoiseLevels>"
  "qbo_arduqbo/NoiseLevels")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NoiseLevels)))
  "Returns string type for a message object of type 'NoiseLevels"
  "qbo_arduqbo/NoiseLevels")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NoiseLevels>)))
  "Returns md5sum for a message object of type '<NoiseLevels>"
  "e44910923ee5ef3281d32758158e1379")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NoiseLevels)))
  "Returns md5sum for a message object of type 'NoiseLevels"
  "e44910923ee5ef3281d32758158e1379")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NoiseLevels>)))
  "Returns full string definition for message of type '<NoiseLevels>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint16 m0~%uint16 m1~%uint16 m2~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NoiseLevels)))
  "Returns full string definition for message of type 'NoiseLevels"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint16 m0~%uint16 m1~%uint16 m2~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NoiseLevels>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NoiseLevels>))
  "Converts a ROS message object to a list"
  (cl:list 'NoiseLevels
    (cl:cons ':header (header msg))
    (cl:cons ':m0 (m0 msg))
    (cl:cons ':m1 (m1 msg))
    (cl:cons ':m2 (m2 msg))
))
