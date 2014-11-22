; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude HeadPose.msg.html

(cl:defclass <HeadPose> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (yaw
    :reader yaw
    :initarg :yaw
    :type cl:float
    :initform 0.0)
   (pitch
    :reader pitch
    :initarg :pitch
    :type cl:float
    :initform 0.0)
   (vel
    :reader vel
    :initarg :vel
    :type cl:fixnum
    :initform 0))
)

(cl:defclass HeadPose (<HeadPose>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HeadPose>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HeadPose)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<HeadPose> is deprecated: use qbo_arduqbo-msg:HeadPose instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <HeadPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <HeadPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:yaw-val is deprecated.  Use qbo_arduqbo-msg:yaw instead.")
  (yaw m))

(cl:ensure-generic-function 'pitch-val :lambda-list '(m))
(cl:defmethod pitch-val ((m <HeadPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:pitch-val is deprecated.  Use qbo_arduqbo-msg:pitch instead.")
  (pitch m))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <HeadPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:vel-val is deprecated.  Use qbo_arduqbo-msg:vel instead.")
  (vel m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HeadPose>) ostream)
  "Serializes a message object of type '<HeadPose>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'yaw))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pitch))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vel)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'vel)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HeadPose>) istream)
  "Deserializes a message object of type '<HeadPose>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pitch) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vel)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'vel)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HeadPose>)))
  "Returns string type for a message object of type '<HeadPose>"
  "qbo_arduqbo/HeadPose")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HeadPose)))
  "Returns string type for a message object of type 'HeadPose"
  "qbo_arduqbo/HeadPose")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HeadPose>)))
  "Returns md5sum for a message object of type '<HeadPose>"
  "fdd46b1f6066f67bbb10e90ea7461cea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HeadPose)))
  "Returns md5sum for a message object of type 'HeadPose"
  "fdd46b1f6066f67bbb10e90ea7461cea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HeadPose>)))
  "Returns full string definition for message of type '<HeadPose>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%float32 yaw~%float32 pitch~%uint16 vel~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HeadPose)))
  "Returns full string definition for message of type 'HeadPose"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%float32 yaw~%float32 pitch~%uint16 vel~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HeadPose>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HeadPose>))
  "Converts a ROS message object to a list"
  (cl:list 'HeadPose
    (cl:cons ':header (header msg))
    (cl:cons ':yaw (yaw msg))
    (cl:cons ':pitch (pitch msg))
    (cl:cons ':vel (vel msg))
))
