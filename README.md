# TheRoadmanx
STM32连接openmv进行简单的视觉识别
这里以几种简单的水果识别区分为例
这段代码运行在 OpenMV 上，用于图像识别和串口通信。它加载了一个预训练的 TensorFlow Lite 模型（trained.tflite）和标签文件（labels.txt）
通过摄像头捕获图像并进行实时物体检测。检测到的物体被标记在图像上
并根据物体类型通过串口发送对应的数字（如苹果为1，梨为2等）。
同时，使用绿色LED灯闪烁来指示检测到的物体。程序循环运行

//其中的trained.tflite与labels.txt文件可自行前往edge impluse网站进行标注训练

