; Auto-generated. Do not edit!


(cl:in-package qbo_object_recognition-srv)


;//! \htmlinclude RecognizeObjectInputImage-request.msg.html

(cl:defclass <RecognizeObjectInputImage-request> (roslisp-msg-protocol:ros-message)
  ((input_image
    :reader input_image
    :initarg :input_image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass RecognizeObjectInputImage-request (<RecognizeObjectInputImage-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecognizeObjectInputImage-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecognizeObjectInputImage-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<RecognizeObjectInputImage-request> is deprecated: use qbo_object_recognition-srv:RecognizeObjectInputImage-request instead.")))

(cl:ensure-generic-function 'input_image-val :lambda-list '(m))
(cl:defmethod input_image-val ((m <RecognizeObjectInputImage-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:input_image-val is deprecated.  Use qbo_object_recognition-srv:input_image instead.")
  (input_image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecognizeObjectInputImage-request>) ostream)
  "Serializes a message object of type '<RecognizeObjectInputImage-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'input_image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecognizeObjectInputImage-request>) istream)
  "Deserializes a message object of type '<RecognizeObjectInputImage-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'input_image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecognizeObjectInputImage-request>)))
  "Returns string type for a service object of type '<RecognizeObjectInputImage-request>"
  "qbo_object_recognition/RecognizeObjectInputImageRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeObjectInputImage-request)))
  "Returns string type for a service object of type 'RecognizeObjectInputImage-request"
  "qbo_object_recognition/RecognizeObjectInputImageRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecognizeObjectInputImage-request>)))
  "Returns md5sum for a message object of type '<RecognizeObjectInputImage-request>"
  "71f47bcb0df643ea09ed237fc93b7e61")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecognizeObjectInputImage-request)))
  "Returns md5sum for a message object of type 'RecognizeObjectInputImage-request"
  "71f47bcb0df643ea09ed237fc93b7e61")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecognizeObjectInputImage-request>)))
  "Returns full string definition for message of type '<RecognizeObjectInputImage-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%sensor_msgs/Image input_image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecognizeObjectInputImage-request)))
  "Returns full string definition for message of type 'RecognizeObjectInputImage-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%sensor_msgs/Image input_image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecognizeObjectInputImage-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'input_image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecognizeObjectInputImage-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RecognizeObjectInputImage-request
    (cl:cons ':input_image (input_image msg))
))
;//! \htmlinclude RecognizeObjectInputImage-response.msg.html

(cl:defclass <RecognizeObjectInputImage-response> (roslisp-msg-protocol:ros-message)
  ((object_name
    :reader object_name
    :initarg :object_name
    :type cl:string
    :initform "")
   (recognized
    :reader recognized
    :initarg :recognized
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass RecognizeObjectInputImage-response (<RecognizeObjectInputImage-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecognizeObjectInputImage-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecognizeObjectInputImage-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name qbo_object_recognition-srv:<RecognizeObjectInputImage-response> is deprecated: use qbo_object_recognition-srv:RecognizeObjectInputImage-response instead.")))

(cl:ensure-generic-function 'object_name-val :lambda-list '(m))
(cl:defmethod object_name-val ((m <RecognizeObjectInputImage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:object_name-val is deprecated.  Use qbo_object_recognition-srv:object_name instead.")
  (object_name m))

(cl:ensure-generic-function 'recognized-val :lambda-list '(m))
(cl:defmethod recognized-val ((m <RecognizeObjectInputImage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader qbo_object_recognition-srv:recognized-val is deprecated.  Use qbo_object_recognition-srv:recognized instead.")
  (recognized m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecognizeObjectInputImage-response>) ostream)
  "Serializes a message object of type '<RecognizeObjectInputImage-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'object_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'object_name))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'recognized) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecognizeObjectInputImage-response>) istream)
  "Deserializes a message object of type '<RecognizeObjectInputImage-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'object_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'object_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'recognized) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecognizeObjectInputImage-response>)))
  "Returns string type for a service object of type '<RecognizeObjectInputImage-response>"
  "qbo_object_recognition/RecognizeObjectInputImageResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeObjectInputImage-response)))
  "Returns string type for a service object of type 'RecognizeObjectInputImage-response"
  "qbo_object_recognition/RecognizeObjectInputImageResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecognizeObjectInputImage-response>)))
  "Returns md5sum for a message object of type '<RecognizeObjectInputImage-response>"
  "71f47bcb0df643ea09ed237fc93b7e61")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecognizeObjectInputImage-response)))
  "Returns md5sum for a message object of type 'RecognizeObjectInputImage-response"
  "71f47bcb0df643ea09ed237fc93b7e61")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecognizeObjectInputImage-response>)))
  "Returns full string definition for message of type '<RecognizeObjectInputImage-response>"
  (cl:format cl:nil "string object_name~%bool recognized~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecognizeObjectInputImage-response)))
  "Returns full string definition for message of type 'RecognizeObjectInputImage-response"
  (cl:format cl:nil "string object_name~%bool recognized~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecognizeObjectInputImage-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'object_name))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecognizeObjectInputImage-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RecognizeObjectInputImage-response
    (cl:cons ':object_name (object_name msg))
    (cl:cons ':recognized (recognized msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RecognizeObjectInputImage)))
  'RecognizeObjectInputImage-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RecognizeObjectInputImage)))
  'RecognizeObjectInputImage-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeObjectInputImage)))
  "Returns string type for a service object of type '<RecognizeObjectInputImage>"
  "qbo_object_recognition/RecognizeObjectInputImage")