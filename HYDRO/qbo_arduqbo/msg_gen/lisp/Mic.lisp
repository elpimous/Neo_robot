; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude Mic.msg.html

(cl:defclass <Mic> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (mic
    :reader mic
    :initarg :mic
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Mic (<Mic>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Mic>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Mic)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<Mic> is deprecated: use qbo_arduqbo-msg:Mic instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Mic>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'mic-val :lambda-list '(m))
(cl:defmethod mic-val ((m <Mic>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:mic-val is deprecated.  Use qbo_arduqbo-msg:mic instead.")
  (mic m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Mic>) ostream)
  "Serializes a message object of type '<Mic>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mic)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Mic>) istream)
  "Deserializes a message object of type '<Mic>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mic)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Mic>)))
  "Returns string type for a message object of type '<Mic>"
  "qbo_arduqbo/Mic")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Mic)))
  "Returns string type for a message object of type 'Mic"
  "qbo_arduqbo/Mic")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Mic>)))
  "Returns md5sum for a message object of type '<Mic>"
  "53acd43451f96e661169eddc90448bdc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Mic)))
  "Returns md5sum for a message object of type 'Mic"
  "53acd43451f96e661169eddc90448bdc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Mic>)))
  "Returns full string definition for message of type '<Mic>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint8 mic~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Mic)))
  "Returns full string definition for message of type 'Mic"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint8 mic~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Mic>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Mic>))
  "Converts a ROS message object to a list"
  (cl:list 'Mic
    (cl:cons ':header (header msg))
    (cl:cons ':mic (mic msg))
))
