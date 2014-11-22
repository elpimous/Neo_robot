; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude EyesPositions.msg.html

(cl:defclass <EyesPositions> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (rightEye
    :reader rightEye
    :initarg :rightEye
    :type cl:fixnum
    :initform 0)
   (leftEye
    :reader leftEye
    :initarg :leftEye
    :type cl:fixnum
    :initform 0))
)

(cl:defclass EyesPositions (<EyesPositions>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EyesPositions>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EyesPositions)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<EyesPositions> is deprecated: use qbo_arduqbo-msg:EyesPositions instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <EyesPositions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'rightEye-val :lambda-list '(m))
(cl:defmethod rightEye-val ((m <EyesPositions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:rightEye-val is deprecated.  Use qbo_arduqbo-msg:rightEye instead.")
  (rightEye m))

(cl:ensure-generic-function 'leftEye-val :lambda-list '(m))
(cl:defmethod leftEye-val ((m <EyesPositions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:leftEye-val is deprecated.  Use qbo_arduqbo-msg:leftEye instead.")
  (leftEye m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EyesPositions>) ostream)
  "Serializes a message object of type '<EyesPositions>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rightEye)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rightEye)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'leftEye)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'leftEye)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EyesPositions>) istream)
  "Deserializes a message object of type '<EyesPositions>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rightEye)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rightEye)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'leftEye)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'leftEye)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EyesPositions>)))
  "Returns string type for a message object of type '<EyesPositions>"
  "qbo_arduqbo/EyesPositions")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EyesPositions)))
  "Returns string type for a message object of type 'EyesPositions"
  "qbo_arduqbo/EyesPositions")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EyesPositions>)))
  "Returns md5sum for a message object of type '<EyesPositions>"
  "509ef4a37cf01ef016e536e2a179623e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EyesPositions)))
  "Returns md5sum for a message object of type 'EyesPositions"
  "509ef4a37cf01ef016e536e2a179623e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EyesPositions>)))
  "Returns full string definition for message of type '<EyesPositions>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint16 rightEye~%uint16 leftEye~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EyesPositions)))
  "Returns full string definition for message of type 'EyesPositions"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint16 rightEye~%uint16 leftEye~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EyesPositions>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EyesPositions>))
  "Converts a ROS message object to a list"
  (cl:list 'EyesPositions
    (cl:cons ':header (header msg))
    (cl:cons ':rightEye (rightEye msg))
    (cl:cons ':leftEye (leftEye msg))
))
