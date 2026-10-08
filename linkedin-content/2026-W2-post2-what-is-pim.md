# Phase 1 · W2 · Bài 2 — What is PIM?

## Bản tiếng Việt (bài chính, 2968 ký tự)

```text
Trong một chip AI, phép tính gần như là phần rẻ nhất.
Phần đắt nhất là quãng đường dữ liệu phải đi.

Đọc một giá trị 32-bit từ DRAM tốn năng lượng gấp khoảng 170 lần một phép nhân 32-bit trên chính giá trị đó (Horowitz, ISSCC 2014).

Phần lớn điện năng của hệ thống AI không dành cho việc "tính", mà cho việc "chở" dữ liệu.

Đó là lý do Processing-in-Memory (PIM) đang được cả ngành bán dẫn đặt cược.

—

1/ Nút thắt thật sự: "bức tường bộ nhớ"

Trong kiến trúc truyền thống, bộ nhớ và bộ xử lý tách rời. Năng lực tính toán tăng rất nhanh qua từng thế hệ chip, nhưng băng thông bộ nhớ không theo kịp. Với nhiều workload AI, bộ xử lý chờ dữ liệu lâu hơn thời gian thực sự tính.

Thêm TOPS cũng vô ích nếu dữ liệu không đến kịp.

2/ PIM: đưa phép tính về nơi dữ liệu đang nằm

PIM đặt một phần khả năng xử lý vào trong hoặc sát cạnh bộ nhớ. Ba hướng chính:
• Near-memory: logic đặt sát bộ nhớ, rút ngắn quãng đường dữ liệu.
• Digital PIM: mạch số tích hợp trong mảng nhớ, chính xác và linh hoạt.
• Analog PIM: dùng chính các ô nhớ để thực hiện phép nhân–cộng (MAC) theo định luật Ohm và Kirchhoff: cực kỳ tiết kiệm năng lượng, nhưng khó hơn về độ chính xác.

3/ Ngành đang đi đến đâu?

Samsung đã giới thiệu HBM-PIM và LPDDR5-PIM. SK hynix có GDDR6-AiM. PIM đã bước ra khỏi phòng thí nghiệm.

Pebble Square, công ty công nghệ đứng sau Pebble Vina, theo đuổi cả Analog-PIM và Digital-PIM. Các chip MINT, PAPAYA, PAPAYA FLEX và ESPRESSO được thiết kế cho AI tại thiết bị, nơi từng milliwatt đều có giá.

4/ Góc nhìn thẳng thắn: PIM không phải phép màu

• Hiệu quả nhất với workload memory-bound, như inference mạng nơ-ron.
• Analog PIM phải giải bài toán nhiễu, độ chính xác và chi phí chuyển đổi ADC/DAC.
• Giá trị thực phụ thuộc vào compiler, SDK và khả năng đưa mô hình có sẵn lên chip.

Chip tốt mà thiếu phần mềm thì vẫn chỉ là silicon.

5/ Ý nghĩa với doanh nghiệp

Với camera AI, robot hay cảm biến nhà máy, câu hỏi không chỉ là "bao nhiêu TOPS", mà là:
• Bao nhiêu TOPS trên mỗi watt?
• Chạy pin được bao lâu, tản nhiệt ra sao?
• Có thực sự cần gửi dữ liệu về Cloud?

Hiệu quả năng lượng ở tầng chip quyết định chi phí vận hành AI ở tầng sản phẩm.

—

Với đội ngũ đang triển khai AI: nút thắt lớn nhất hiện nay của bạn là năng lực tính toán, băng thông bộ nhớ hay ngân sách năng lượng?

#PIM #EdgeAI #Semiconductor #AIChip #PebbleVina
```

## English version (đăng riêng, 2544 ký tự)

```text
In an AI chip, the math is almost the cheapest part.
The expensive part is how far the data has to travel.

Reading one 32-bit value from DRAM costs roughly 170x more energy than a 32-bit multiply on that same value (Horowitz, ISSCC 2014).

In other words: most of the power in an AI system isn't spent "thinking". It's spent hauling data back and forth.

That is why the semiconductor industry is betting on Processing-in-Memory (PIM).

—

1/ The real bottleneck: the memory wall

In conventional architectures, memory and compute are separate. Every operation needs data shipped from memory to the processor and back.

Compute has scaled fast with each chip generation. Memory bandwidth hasn't kept up. In many AI workloads, the processor spends more time waiting for data than actually computing.

Adding more TOPS doesn't help if the data can't arrive in time.

2/ PIM: bring compute to where the data lives

PIM places part of the processing inside or right next to memory. Three main approaches:
• Near-memory: logic placed beside memory to shorten the data path.
• Digital PIM: digital circuits inside the memory array; precise and flexible.
• Analog PIM: the memory cells themselves perform multiply-accumulate (MAC) via Ohm's and Kirchhoff's laws; extremely energy-efficient, but harder on precision.

3/ Where is the industry?

Samsung has introduced HBM-PIM and LPDDR5-PIM. SK hynix has GDDR6-AiM. PIM has left the lab.

Pebble Square, the technology company behind Pebble Vina, pursues both Analog-PIM and Digital-PIM. Its MINT, PAPAYA, PAPAYA FLEX and ESPRESSO chip lines are built for on-device AI, where every milliwatt counts.

4/ An honest take: PIM is not magic

• It shines on memory-bound workloads such as neural network inference.
• Analog PIM must handle noise, precision and ADC/DAC conversion overhead.
• Real-world value depends heavily on the compiler, the SDK and how easily existing models can be deployed.

A great chip without great software is still just silicon.

5/ What it means for businesses

For AI cameras, robots, medical devices or factory sensors, the question isn't just "how many TOPS?" It's:
• How many TOPS per watt?
• How long does it run on battery, and how is heat managed?
• Does the data really need to go to the Cloud?

Energy efficiency at the chip level directly drives the cost of running AI at the product level.

—

For teams deploying AI: is your biggest bottleneck today compute, memory bandwidth or power budget?

#PIM #EdgeAI #Semiconductor #AIChip #PebbleVina
```
