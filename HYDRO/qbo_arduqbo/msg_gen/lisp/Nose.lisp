; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude Nose.msg.html

(cl:defclass <Nose> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (color
    :reader color
    :initarg :color
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Nose (<Nose>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Nose>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Nose)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<Nose> is deprecated: use qbo_arduqbo-msg:Nose instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Nose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'color-val :lambda-list '(m))
(cl:defmethod color-val ((m <Nose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:color-val is deprecated.  Use qbo_arduqbo-msg:color instead.")
  (color m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Nose>) ostream)
  "Serializes a message object of type '<Nose>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'color)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Nose>) istream)
  "Deserializes a message object of type '<Nose>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'color)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Nose>)))
  "Returns string type for a message object of type '<Nose>"
  "qbo_arduqbo/Nose")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Nose)))
  "Returns string type for a message object of type 'Nose"
  "qbo_arduqbo/Nose")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Nose>)))
  "Returns md5sum for a message object of type '<Nose>"
  "36f63d241a341fc5ac60fd9ee64d4836")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Nose)))
  "Returns md5sum for a message object of type 'Nose"
  "36f63d241a341fc5ac60fd9ee64d4836")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Nose>)))
  "Returns full string definition for message of type '<Nose>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint8 color~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Nose)))
  "Returns full string definition for message of type 'Nose"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint8 color~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Nose>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Nose>))
  "Converts a ROS message object to a list"
  (cl:list 'Nose
    (cl:cons ':header (header msg))
    (cl:cons ':color (color msg))
))
