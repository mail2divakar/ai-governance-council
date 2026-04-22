| Metric            | Description                                   | Threshold           | Source                   |
| ----------------- | --------------------------------------------- | ------------------- | ------------------------ |
| Correctness       | Is the response factually accurate?           | >= 4.2 / 5          | LLM Judge + Human Review |
| Relevance         | Does the response answer the question?        | >= 4.0 / 5          | LLM Judge                |
| Completeness      | Are all important details included?           | >= 4.0 / 5          | Human Review             |
| Groundedness      | Is the answer supported by retrieved context? | >= 4.0 / 5          | LLM Judge                |
| Safety            | Does the response comply with policy?         | 100% pass           | Automated + Human Review |
| Retrieval Quality | Were the correct documents retrieved?         | >= 4.0 / 5          | Automated                |
| Tool Success      | Were the correct tools used successfully?     | >= 98%              | Trace Analytics          |
| Latency           | Response time                                 | Within SLA          | Trace Analytics          |
| Cost              | Cost per task                                 | Within Budget       | Trace Analytics          |
| User Satisfaction | End-user feedback                             | Stable or Improving | User Feedback            |






| Dimension         | Description                                                      | Typical Threshold   |
| ----------------- | ---------------------------------------------------------------- | ------------------- |
| Correctness       | Is the output factually or logically correct?                    | >= 4.2 / 5          |
| Relevance         | Does the output answer the user request?                         | >= 4.0 / 5          |
| Completeness      | Are all important details included?                              | >= 4.0 / 5          |
| Consistency       | Does the system produce stable outputs for similar inputs?       | >= 4.0 / 5          |
| Safety            | Does the output avoid harmful, biased, or non-compliant content? | 100% pass           |
| Groundedness      | Is the answer supported by evidence or retrieved context?        | >= 4.0 / 5          |
| Conciseness       | Is the output concise and easy to understand?                    | >= 4.0 / 5          |
| Format Adherence  | Does the response follow the required format?                    | >= 95%              |
| Latency           | Is the response time within SLA?                                 | Within target       |
| Cost              | Is the cost per task within budget?                              | Within budget       |
| User Satisfaction | Do users find the output useful?                                 | Stable or Improving |
