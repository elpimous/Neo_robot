; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude Irs.msg.html

(cl:defclass <Irs> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (ir0
    :reader ir0
    :initarg :ir0
    :type cl:fixnum
    :initform 0)
   (ir1
    :reader ir1
    :initarg :ir1
    :type cl:fixnum
    :initform 0)
   (ir2
    :reader ir2
    :initarg :ir2
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Irs (<Irs>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Irs>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Irs)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<Irs> is deprecated: use qbo_arduqbo-msg:Irs instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Irs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'ir0-val :lambda-list '(m))
(cl:defmethod ir0-val ((m <Irs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:ir0-val is deprecated.  Use qbo_arduqbo-msg:ir0 instead.")
  (ir0 m))

(cl:ensure-generic-function 'ir1-val :lambda-list '(m))
(cl:defmethod ir1-val ((m <Irs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:ir1-val is deprecated.  Use qbo_arduqbo-msg:ir1 instead.")
  (ir1 m))

(cl:ensure-generic-function 'ir2-val :lambda-list '(m))
(cl:defmethod ir2-val ((m <Irs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:ir2-val is deprecated.  Use qbo_arduqbo-msg:ir2 instead.")
  (ir2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Irs>) ostream)
  "Serializes a message object of type '<Irs>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ir0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ir1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ir2)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Irs>) istream)
  "Deserializes a message object of type '<Irs>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ir0)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ir1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'ir2)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Irs>)))
  "Returns string type for a message object of type '<Irs>"
  "qbo_arduqbo/Irs")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Irs)))
  "Returns string type for a message object of type 'Irs"
  "qbo_arduqbo/Irs")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Irs>)))
  "Returns md5sum for a message object of type '<Irs>"
  "98d76e6b27680041844888fa67ba28e7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Irs)))
  "Returns md5sum for a message object of type 'Irs"
  "98d76e6b27680041844888fa67ba28e7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Irs>)))
  "Returns full string definition for message of type '<Irs>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint8 ir0~%uint8 ir1~%uint8 ir2~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Irs)))
  "Returns full string definition for message of type 'Irs"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%uint8 ir0~%uint8 ir1~%uint8 ir2~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Irs>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Irs>))
  "Converts a ROS message object to a list"
  (cl:list 'Irs
    (cl:cons ':header (header msg))
    (cl:cons ':ir0 (ir0 msg))
    (cl:cons ':ir1 (ir1 msg))
    (cl:cons ':ir2 (ir2 msg))
))
