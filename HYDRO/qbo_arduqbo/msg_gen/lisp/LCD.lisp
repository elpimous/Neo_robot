; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude LCD.msg.html

(cl:defclass <LCD> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (msg
    :reader msg
    :initarg :msg
    :type cl:string
    :initform ""))
)

(cl:defclass LCD (<LCD>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LCD>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LCD)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<LCD> is deprecated: use qbo_arduqbo-msg:LCD instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <LCD>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'msg-val :lambda-list '(m))
(cl:defmethod msg-val ((m <LCD>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:msg-val is deprecated.  Use qbo_arduqbo-msg:msg instead.")
  (msg m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LCD>) ostream)
  "Serializes a message object of type '<LCD>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'msg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'msg))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LCD>) istream)
  "Deserializes a message object of type '<LCD>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'msg) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'msg) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LCD>)))
  "Returns string type for a message object of type '<LCD>"
  "qbo_arduqbo/LCD")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LCD)))
  "Returns string type for a message object of type 'LCD"
  "qbo_arduqbo/LCD")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LCD>)))
  "Returns md5sum for a message object of type '<LCD>"
  "b5ddb29fb9a84da18523c89dfbb75dba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LCD)))
  "Returns md5sum for a message object of type 'LCD"
  "b5ddb29fb9a84da18523c89dfbb75dba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LCD>)))
  "Returns full string definition for message of type '<LCD>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%string msg~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LCD)))
  "Returns full string definition for message of type 'LCD"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%string msg~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LCD>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'msg))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LCD>))
  "Converts a ROS message object to a list"
  (cl:list 'LCD
    (cl:cons ':header (header msg))
    (cl:cons ':msg (msg msg))
))
