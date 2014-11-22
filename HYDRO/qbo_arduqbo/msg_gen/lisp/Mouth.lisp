; Auto-generated. Do not edit!


(cl:in-package qbo_arduqbo-msg)


;//! \htmlinclude Mouth.msg.html

(cl:defclass <Mouth> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (mouthImage
    :reader mouthImage
    :initarg :mouthImage
    :type (cl:vector cl:boolean)
   :initform (cl:make-array 20 :element-type 'cl:boolean :initial-element cl:nil)))
)

(cl:defclass Mouth (<Mouth>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Mouth>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Mouth)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_arduqbo-msg:<Mouth> is deprecated: use qbo_arduqbo-msg:Mouth instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Mouth>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:header-val is deprecated.  Use qbo_arduqbo-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'mouthImage-val :lambda-list '(m))
(cl:defmethod mouthImage-val ((m <Mouth>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_arduqbo-msg:mouthImage-val is deprecated.  Use qbo_arduqbo-msg:mouthImage instead.")
  (mouthImage m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Mouth>) ostream)
  "Serializes a message object of type '<Mouth>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if ele 1 0)) ostream))
   (cl:slot-value msg 'mouthImage))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Mouth>) istream)
  "Deserializes a message object of type '<Mouth>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:setf (cl:slot-value msg 'mouthImage) (cl:make-array 20))
  (cl:let ((vals (cl:slot-value msg 'mouthImage)))
    (cl:dotimes (i 20)
    (cl:setf (cl:aref vals i) (cl:not (cl:zerop (cl:read-byte istream))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Mouth>)))
  "Returns string type for a message object of type '<Mouth>"
  "qbo_arduqbo/Mouth")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Mouth)))
  "Returns string type for a message object of type 'Mouth"
  "qbo_arduqbo/Mouth")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Mouth>)))
  "Returns md5sum for a message object of type '<Mouth>"
  "52d894e119976923d77120ac6260422a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Mouth)))
  "Returns md5sum for a message object of type 'Mouth"
  "52d894e119976923d77120ac6260422a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Mouth>)))
  "Returns full string definition for message of type '<Mouth>"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%bool[20] mouthImage~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Mouth)))
  "Returns full string definition for message of type 'Mouth"
  (cl:format cl:nil "# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.# Software License Agreement (LGPL v2.1 License)~%#~%# Copyright (c) 2012 Thecorpora, Inc.~%#~%# This library is free software; you can redistribute it and/or modify ~%# it under the terms of the GNU Lesser General Public License as published~%# by the Free Software Foundation; either version 2.1 of the License, ~%# or (at your option) any later version.~%#~%# This library is distributed in the hope that it will be useful, but ~%# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY ~%# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public ~%# License for more details.~%#  ~%# You should have received a copy of the GNU General Public License ~%# along with this program; if not, write to the Free Software ~%# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, ~%# MA 02110-1301, USA.~%~%Header header~%bool[20] mouthImage~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Mouth>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'mouthImage) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Mouth>))
  "Converts a ROS message object to a list"
  (cl:list 'Mouth
    (cl:cons ':header (header msg))
    (cl:cons ':mouthImage (mouthImage msg))
))
